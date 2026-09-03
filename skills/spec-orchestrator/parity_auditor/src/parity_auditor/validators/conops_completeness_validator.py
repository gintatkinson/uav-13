r"""
Gate 26: ConOps & Mission Intent Completeness Validator Engine (ISO 29148 / NATO STANAG 4586 / OMG UAF).

Enforces:
1. ConopsCompletenessValidator:
   12 Mandatory Sections for Concept of Operations (CONOPS.md):
   - 1. Scope & System Identification
   - 2. Normative Standards & Regulatory Baseline
   - 3. Current Situation & Deficiency Analysis (Predecessors)
   - 4. Operational Justification & Priority Matrix (Trade-Offs)
   - 5. Operational Modes & Lifecycle Stages (\Phi_{lifecycle})
   - 6. 4D Operational Volume & SORA Ground Risk Buffer (GRB) Mathematics
   - 7. OMG UAF Operational Activity Taxonomy (with Gate 24 tags)
   - 8. Operational Information Exchange (Op-Tx) Matrix
   - 9. Operational Environments & Physical Constraints
   - 10. Multi-Threaded Operational Scenarios
   - 11. Maintenance & Sustainment Concepts (O/I/D Maintenance)
   - 12. 7-Row Emergency Decision & Contingency Matrix (EMG-01..07)

2. MissionIntentCompletenessValidator:
   10 Mandatory Sections for Mission Intent (MISSION_INTENT.md):
   - 1. Commander's Intent & Operational Objectives
   - 2. Mission Essential Task List (METL MET-01..N)
   - 3. Measures of Effectiveness (MoE) & Measures of Performance (MoP) Metrics
   - 4. Threat & Electronic Warfare (EW) / Cyber Environment Matrix
   - 5. PACE C2 Link Communications Plan (Primary, Alternate, Contingency, Emergency)
   - 6. Rules of Engagement (ROE) & Weapon/Sensor Interlocks
   - 7. Airspace Deconfliction & U-space Dynamic Geo-Zones
   - 8. Go/No-Go Decision Matrix
   - 9. Bingo Energy Mathematics & Secondary Divert Protocols (Statutory Reserve \ge 20%)
   - 10. Gate 24 MissionTask Traceability Tags

3. Pure Abstract Systems Engineering Archetypes across templates, models, and solvers.
"""

import math
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple, Union

try:
    from .base import IValidator
    from ..core.findings import Finding
    from ..core.workspace import WorkspaceRepository, extract_metadata_from_content
    from ..parsers.research_inventory import parse_research_inventory
    from .coverage_digest_validator import _normalize_obligation_id, _parse_obligation_tags
    from .obligation_witness_validator import _parse_witness_tags
except (ImportError, ValueError):
    _src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    if _src_dir not in sys.path:
        sys.path.insert(0, _src_dir)
    from parity_auditor.validators.base import IValidator
    from parity_auditor.core.findings import Finding
    from parity_auditor.core.workspace import WorkspaceRepository, extract_metadata_from_content
    from parity_auditor.parsers.research_inventory import parse_research_inventory
    from parity_auditor.validators.coverage_digest_validator import _normalize_obligation_id, _parse_obligation_tags
    from parity_auditor.validators.obligation_witness_validator import _parse_witness_tags


# =============================================================================
# Mathematical Helpers
# =============================================================================

def calculate_sora_grb_radius(
    h_max_m: float,
    theta_impact_deg: float = 45.0,
    v_wind_max_mps: float = 15.0,
    g: float = 9.80665,
    d_glide_max_m: float = 0.0,
) -> float:
    """
    Computes minimum theoretical SORA Ground Risk Buffer radius in accordance with
    JARUS SORA v2.5 Annex B:
        R_GRB = h_max * tan(theta_impact) + v_wind_max * sqrt(2 * h_max / g) + d_glide_max
    """
    if h_max_m <= 0:
        return 0.0
    theta_rad = math.radians(theta_impact_deg)
    t_fall = math.sqrt((2.0 * h_max_m) / g)
    r_grb = (h_max_m * math.tan(theta_rad)) + (v_wind_max_mps * t_fall) + d_glide_max_m
    return r_grb


def calculate_bingo_energy_reserve_ratio(
    total_capacity_j: float,
    reserve_energy_j: float,
) -> float:
    """
    Computes the statutory energy reserve ratio:
        ratio = reserve_energy_j / total_capacity_j
    Statutory requirement: ratio >= 0.20 (20%).
    """
    if total_capacity_j <= 0:
        return 0.0
    return reserve_energy_j / total_capacity_j


# =============================================================================
# Domain Models for ConOps & Mission Intent
# =============================================================================

@dataclass
class OperationalVolume4D:
    nominal_waypoints: List[str] = field(default_factory=list)
    min_altitude_meters: float = 0.0
    max_altitude_meters: float = 120.0
    contingency_margin_meters: float = 50.0
    sora_grb_radius_meters: float = 200.0

    def is_volume_bounded(self) -> bool:
        return self.max_altitude_meters > self.min_altitude_meters and self.sora_grb_radius_meters > 0


@dataclass
class SoraRiskBuffer:
    max_altitude_agl: float = 120.0
    impact_angle_degrees: float = 45.0
    max_wind_speed_mps: float = 15.0
    free_fall_time_seconds: float = 4.95
    terminal_velocity_mps: float = 25.0
    impact_kinetic_energy_joules: float = 1562.5
    sora_grc_classification: str = "GRC-3"


@dataclass
class EmergencyDecisionRow:
    trigger_id: str
    contingency_trigger_name: str
    detection_mechanism: str
    automated_containment_action: str
    failsafe_recovery_state: str
    max_response_time_seconds: float
    human_in_the_loop_role: str


@dataclass
class UafActivityEntry:
    activity_id: str
    activity_name: str
    description: str
    allocation_tag: str


@dataclass
class OpTxExchangeEntry:
    exchange_id: str
    source_node: str
    dest_node: str
    information_item: str
    data_rate: str
    max_latency: str
    criticality: str


@dataclass
class ConopsDocumentModel:
    scope: str = ""
    normative_standards: List[str] = field(default_factory=list)
    current_situation: str = ""
    justification: str = ""
    operational_modes: List[str] = field(default_factory=list)
    operational_volume: Optional[OperationalVolume4D] = None
    sora_risk_buffer: Optional[SoraRiskBuffer] = None
    activity_taxonomy: List[UafActivityEntry] = field(default_factory=list)
    op_tx_matrix: List[OpTxExchangeEntry] = field(default_factory=list)
    operational_environments: str = ""
    scenarios: List[str] = field(default_factory=list)
    maintenance_concepts: str = ""
    emergency_matrix: List[EmergencyDecisionRow] = field(default_factory=list)


@dataclass
class METLTaskEntry:
    task_id: str
    task_name: str
    condition_statement: str
    standard_metric: str
    verification_method: str
    gate24_allocation_tag: str


@dataclass
class MoEMoPMetricEntry:
    metric_id: str
    metric_type: str
    metric_name: str
    mathematical_formula: str
    threshold_value: float
    objective_value: float
    measurement_unit: str


@dataclass
class PaceC2LinkPlan:
    primary_link: str = ""
    alternate_link: str = ""
    contingency_link: str = ""
    emergency_link: str = ""
    heartbeat_timeout_seconds: float = 5.0


@dataclass
class BingoEnergyModel:
    total_capacity_joules: float = 500000.0
    return_energy_joules: float = 150000.0
    divert_energy_joules: float = 60000.0
    reserve_energy_joules: float = 100000.0
    contingency_energy_joules: float = 40000.0
    bingo_threshold_joules: float = 350000.0
    primary_divert_waypoint: str = "DIVERT_ALPHA"
    secondary_divert_waypoint: str = "DIVERT_BRAVO"


@dataclass
class MissionIntentDocumentModel:
    commanders_intent: str = ""
    metl_roster: List[METLTaskEntry] = field(default_factory=list)
    moe_mop_metrics: List[MoEMoPMetricEntry] = field(default_factory=list)
    threat_matrix: List[Dict[str, str]] = field(default_factory=list)
    pace_link_plan: Optional[PaceC2LinkPlan] = None
    roe_rules: List[str] = field(default_factory=list)
    airspace_zones: str = ""
    go_no_go_matrix: List[Dict[str, str]] = field(default_factory=list)
    bingo_energy_model: Optional[BingoEnergyModel] = None
    gate24_task_tags: List[str] = field(default_factory=list)


@dataclass
class ValidationReport:
    gate_id: str = "Gate-26"
    status: str = "PASSED"
    total_checks: int = 0
    passed_checks: int = 0
    findings: List[Finding] = field(default_factory=list)
    conops_coverage: float = 1.0
    mission_intent_coverage: float = 1.0


# =============================================================================
# Parsing Utilities
# =============================================================================

def _extract_markdown_sections(text: str) -> Dict[str, Tuple[int, str]]:
    """
    Extracts top-level and H2 sections from markdown.
    Returns mapping of section_heading -> (line_number, section_content).
    """
    sections: Dict[str, Tuple[int, str]] = {}
    lines = text.splitlines()
    current_heading = ""
    current_line = 1
    current_chunk: List[str] = []

    for idx, line in enumerate(lines, start=1):
        m = re.match(r'^(#{1,2})\s+(.+)$', line.strip())
        if m:
            if current_heading:
                sections[current_heading] = (current_line, "\n".join(current_chunk))
            current_heading = m.group(2).strip()
            current_line = idx
            current_chunk = []
        else:
            current_chunk.append(line)

    if current_heading:
        sections[current_heading] = (current_line, "\n".join(current_chunk))

    return sections


def _parse_commonmark_tables(text: str) -> Tuple[List[List[Dict[str, str]]], List[int]]:
    """
    Parses CommonMark tables from markdown text.
    Returns list of tables and list of malformed table line numbers.
    """
    tables: List[List[Dict[str, str]]] = []
    malformed_lines: List[int] = []
    lines = text.splitlines()
    i = 0

    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("|") and line.endswith("|"):
            header_line = line
            if i + 1 < len(lines):
                sep_line = lines[i + 1].strip()
                if re.match(r"^\|(\s*:?-+:?\s*\|)+$", sep_line):
                    # Replace escaped pipes
                    clean_hdr_line = header_line.replace(r"\|", "\x00")
                    raw_headers = [col.replace("\x00", "|").strip() for col in clean_hdr_line.split("|")[1:-1]]
                    clean_headers = [re.sub(r'[*`_]', '', col).strip() for col in raw_headers]
                    norm_headers = [re.sub(r'[\s\-/]+', '_', h.lower()).strip('_') for h in clean_headers]
                    
                    rows: List[Dict[str, str]] = []
                    j = i + 2
                    is_malformed = False

                    while j < len(lines):
                        row_line = lines[j].strip()
                        if not (row_line.startswith("|") and row_line.endswith("|")):
                            if row_line.startswith("|") and not row_line.endswith("|"):
                                malformed_lines.append(j + 1)
                                is_malformed = True
                            break
                        clean_row_line = row_line.replace(r"\|", "\x00")
                        cols = [col.replace("\x00", "|").strip() for col in clean_row_line.split("|")[1:-1]]
                        if len(cols) != len(norm_headers):
                            # Allow trailing empty columns but flag significant mismatch
                            if abs(len(cols) - len(norm_headers)) > 1:
                                malformed_lines.append(j + 1)
                        row_dict: Dict[str, str] = {}
                        for idx_h, h in enumerate(norm_headers):
                            val = cols[idx_h] if idx_h < len(cols) else ""
                            row_dict[h] = val.strip("`").strip()
                        rows.append(row_dict)
                        j += 1

                    if not is_malformed:
                        tables.append(rows)
                    i = j
                    continue
                else:
                    if "|" in sep_line and not re.match(r"^\|(\s*:?-+:?\s*\|)+$", sep_line):
                        malformed_lines.append(i + 2)
        elif line.startswith("|") and not line.endswith("|"):
            malformed_lines.append(i + 1)
        i += 1

    return tables, malformed_lines


def _find_matching_section(
    sections: Dict[str, Tuple[int, str]],
    sec_num: int,
    canonical_name: str,
    aliases: List[str],
) -> Optional[Tuple[str, int, str]]:
    """
    Finds a section in the parsed sections dictionary by matching section number or aliases.
    Prioritizes direct section number prefix match before alias fallback.
    """
    # Pass 1: Direct prefix match: e.g. "1. Scope", "## 1.", "1 - Scope", "Section 1:"
    num_pattern = rf'^(?:section\s+)?{sec_num}[.\s:\-—]'
    for heading, (line_no, content) in sections.items():
        h_clean = heading.lower()
        if re.search(num_pattern, h_clean):
            return heading, line_no, content

    # Pass 2: Check alias matches
    for heading, (line_no, content) in sections.items():
        h_clean = heading.lower()
        for alias in aliases:
            if alias.lower() in h_clean:
                return heading, line_no, content

    return None


# =============================================================================
# Gate 26: ConopsCompletenessValidator
# =============================================================================

class ConopsCompletenessValidator(IValidator):
    """
    Quality Gate 26: ConOps Completeness Validator.
    Enforces 12 mandatory sections, SORA 4D Volume & GRB Math, UAF Activity taxonomy,
    Op-Tx exchange matrix, O/I/D maintenance, and 7-Row Emergency Decision determinism.
    """

    MANDATORY_SECTIONS: List[Dict[str, Any]] = [
        {"num": 1, "title": "Scope & System Identification", "aliases": ["scope", "system identification", "system boundary"]},
        {"num": 2, "title": "Normative Standards & Regulatory Baseline", "aliases": ["normative standards", "regulatory baseline", "applicable documents", "standards"]},
        {"num": 3, "title": "Current Situation & Deficiency Analysis", "aliases": ["current situation", "deficiency analysis", "predecessor", "predecessors", "deficiencies"]},
        {"num": 4, "title": "Operational Justification & Priority Matrix", "aliases": ["operational justification", "priority matrix", "justification", "trade-off", "trade-offs", "priorities"]},
        {"num": 5, "title": "Operational Modes & Lifecycle Stages", "aliases": ["operational modes", "lifecycle stages", "lifecycle", "modes", "stages", "phi_lifecycle"]},
        {"num": 6, "title": "4D Operational Volume & SORA Ground Risk Buffer Mathematics", "aliases": ["4d operational volume", "ground risk buffer", "sora", "operational volume", "grb math", "grb"]},
        {"num": 7, "title": "OMG UAF Operational Activity Taxonomy", "aliases": ["operational activity taxonomy", "uaf operational activities", "operational activities", "uaf activities", "oa-"]},
        {"num": 8, "title": "Operational Information Exchange (Op-Tx) Matrix", "aliases": ["operational information exchange", "op-tx matrix", "op-tx table", "information exchange", "op-tx"]},
        {"num": 9, "title": "Operational Environments & Constraints", "aliases": ["operational environments", "physical constraints", "constraints", "environmental constraints"]},
        {"num": 10, "title": "Multi-Threaded Operational Scenarios", "aliases": ["operational scenarios", "scenarios", "multi-threaded", "operational threads"]},
        {"num": 11, "title": "Maintenance & Sustainment Concepts", "aliases": ["maintenance & sustainment", "maintenance concepts", "sustainment", "o/i/d maintenance", "maintenance", "o-level"]},
        {"num": 12, "title": "7-Row Emergency Decision & Contingency Matrix", "aliases": ["emergency decision", "contingency matrix", "7-row emergency", "emergency matrix", "emergency decision & contingency matrix", "emg-"]},
    ]

    CANONICAL_EMERGENCY_TRIGGERS: List[str] = [
        "EMG-01",  # Lost C2 Link
        "EMG-02",  # GNSS Navigation Loss
        "EMG-03",  # Propulsion / Power Failure
        "EMG-04",  # Critical Sensor Fault
        "EMG-05",  # Geofence Breach / Airspace Conflict
        "EMG-06",  # Structural / Actuation Anomaly
        "EMG-07",  # Flight Termination Command
    ]

    CANONICAL_EMERGENCY_SUBSECTIONS: List[Dict[str, Any]] = [
        {
            "num": "12.1",
            "title": "Failsafe State Transition Semantics / Timing Guarantees",
            "aliases": [
                "12.1",
                "failsafe state transition semantics",
                "state transition semantics",
                "timing guarantees",
                "failsafe state transition",
            ],
        },
        {
            "num": "12.2",
            "title": "Failsafe State Machine Architecture / Statechart Diagram",
            "aliases": [
                "12.2",
                "failsafe state machine architecture",
                "state machine architecture",
                "statechart diagram",
                "statechart",
                "state machine",
            ],
        },
        {
            "num": "12.3",
            "title": "Contingency Flight Maneuvers / Aerodynamic Descent Profiles",
            "aliases": [
                "12.3",
                "contingency flight maneuvers",
                "aerodynamic descent profiles",
                "contingency maneuvers",
                "descent profiles",
                "flight maneuvers",
            ],
        },
        {
            "num": "12.4",
            "title": "Flight Termination Subsystem FTS / Safe-Arm Circuitry",
            "aliases": [
                "12.4",
                "flight termination subsystem",
                "flight termination subsystem fts",
                "safe-arm circuitry",
                "fts",
                "safe-arm",
            ],
        },
        {
            "num": "12.5",
            "title": "Human-in-the-Loop Override / Veto Timers",
            "aliases": [
                "12.5",
                "human-in-the-loop override",
                "veto timers",
                "hitl override",
                "veto timer",
            ],
        },
        {
            "num": "12.6",
            "title": "Post-Emergency Ground Recovery / Telemetry Quarantine / Investigation",
            "aliases": [
                "12.6",
                "post-emergency ground recovery",
                "telemetry quarantine",
                "investigation",
                "ground recovery",
                "post-emergency recovery",
            ],
        },
    ]

    def __init__(self, strict_sora_math: bool = True) -> None:
        self.strict_sora_math = strict_sora_math

    def validate(self, repo: WorkspaceRepository, **kwargs) -> List[Finding]:
        findings: List[Finding] = []
        workspace_dir = repo.workspace_dir
        conops_dir = os.path.join(workspace_dir, "docs", "conops")

        if not os.path.isdir(conops_dir):
            if repo.is_upstream_compiler_repo():
                return []
            return [Finding(
                "conops-corpus-missing",
                "ConOps corpus directory 'docs/conops' is missing in workspace.",
                location="docs/conops",
            )]

        # Find CONOPS file(s)
        conops_files: List[str] = []
        for root, _, files in os.walk(conops_dir):
            for f in sorted(files):
                if f.upper().startswith("CONOPS") and f.endswith(".md") and "TEMPLATE" not in f.upper():
                    conops_files.append(os.path.join(root, f))

        if not conops_files:
            if repo.is_upstream_compiler_repo():
                return []
            return [Finding(
                "conops-corpus-missing",
                "No valid ConOps specification document ('CONOPS*.md') found in 'docs/conops'.",
                location="docs/conops",
            )]

        for c_file in conops_files:
            rel_path = os.path.relpath(c_file, workspace_dir)
            try:
                with open(c_file, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
            except Exception as e:
                findings.append(Finding(
                    "conops-read-error",
                    f"Failed to read ConOps document '{rel_path}': {e}",
                    location=rel_path,
                ))
                continue

            findings.extend(self._validate_conops_text(content, rel_path, repo=repo))

        return findings

    def _validate_conops_text(self, content: str, rel_path: str, repo: Optional[WorkspaceRepository] = None) -> List[Finding]:
        findings: List[Finding] = []
        sections = _extract_markdown_sections(content)
        tables, malformed_lines = _parse_commonmark_tables(content)

        # Check for allocated obligations from RESEARCH_INVENTORY.md (Gate 26, Issue #109)
        if "TEMPLATE" not in rel_path.upper():
            inventory_file = None
            if repo is not None:
                inventory_file = os.path.join(repo.workspace_dir, "docs", "research", "RESEARCH_INVENTORY.md")
            else:
                candidate = os.path.join("docs", "research", "RESEARCH_INVENTORY.md")
                if os.path.isfile(candidate):
                    inventory_file = candidate

            if inventory_file and os.path.isfile(inventory_file):
                try:
                    with open(inventory_file, "r", encoding="utf-8") as inv_f:
                        inv_doc = parse_research_inventory(inv_f.read())

                    # Extract document's realized/witnessed tags
                    doc_tags = set(_parse_witness_tags(content) + _parse_obligation_tags(content))
                    fm = extract_metadata_from_content(content)
                    if fm:
                        for key in ("obligations", "normative_obligations", "allocated_obligations", "obligation_id"):
                            val = fm.get(key)
                            if isinstance(val, list):
                                for item in val:
                                    norm = _normalize_obligation_id(str(item))
                                    if norm:
                                        doc_tags.add(norm)
                            elif isinstance(val, str):
                                norm = _normalize_obligation_id(val)
                                if norm:
                                    doc_tags.add(norm)

                    # Find all obligations allocated to CONOPS in clause allocations
                    for alloc in inv_doc.clause_allocations:
                        if alloc.population_id and alloc.downstream_spec_file:
                            spec_target = alloc.downstream_spec_file.strip("`* ")
                            target_base = os.path.basename(spec_target).upper()
                            is_conops_target = (
                                target_base.startswith("CONOPS")
                                or os.path.normpath(spec_target) == os.path.normpath(rel_path)
                            )
                            if is_conops_target:
                                norm_id = _normalize_obligation_id(alloc.population_id)
                                if norm_id not in doc_tags:
                                    findings.append(Finding(
                                        "conops-obligation-unwitnessed",
                                        f"ConOps document '{rel_path}' is missing mandatory witness/realization tag for allocated obligation '{norm_id}' ({alloc.clause_citation or alloc.standard_id}).",
                                        location=rel_path,
                                        detail={"obligation_id": norm_id, "file": rel_path, "standard_id": alloc.standard_id},
                                    ))
                except Exception:
                    pass

        # Check for malformed tables
        for m_line in malformed_lines:
            findings.append(Finding(
                "conops-table-malformed",
                f"Malformed CommonMark table or broken row formatting detected at line {m_line} in '{rel_path}'.",
                location=f"{rel_path}:{m_line}",
            ))

        # Check for 12 Mandatory Sections
        matched_sections: Dict[int, Tuple[str, int, str]] = {}
        for req in self.MANDATORY_SECTIONS:
            sec_num = req["num"]
            title = req["title"]
            aliases = req["aliases"]
            res = _find_matching_section(sections, sec_num, title, aliases)
            if res:
                matched_sections[sec_num] = res
            else:
                findings.append(Finding(
                    "conops-section-missing",
                    f"Mandatory ConOps Section {sec_num} ('{title}') is missing or empty in '{rel_path}'.",
                    location=rel_path,
                    detail={"section_number": sec_num, "section_title": title},
                ))

        # Section 6: SORA 4D Volume & GRB Math Validation
        if 6 in matched_sections:
            _, sec6_line, sec6_content = matched_sections[6]
            h_max_val: Optional[float] = None
            v_wind_val: Optional[float] = None
            theta_val: float = 45.0
            r_grb_val: Optional[float] = None

            # Extract parameters via regex from tables or text
            m_h = re.search(r'h[_\s]*max[^\d]*([0-9]+(?:\.[0-9]+)?)', sec6_content, re.IGNORECASE)
            if not m_h:
                m_h = re.search(r'(?:max(?:imum)?\s+altitude|operating\s+ceiling)[^\d]*([0-9]+(?:\.[0-9]+)?)', sec6_content, re.IGNORECASE)
            if m_h:
                try:
                    h_max_val = float(m_h.group(1))
                except ValueError:
                    pass

            m_w = re.search(r'v[_\s]*wind(?:[_\s]*max)?[^\d]*([0-9]+(?:\.[0-9]+)?)', sec6_content, re.IGNORECASE)
            if not m_w:
                m_w = re.search(r'(?:max(?:imum)?\s+wind|wind\s+limit|wind\s+speed)[^\d]*([0-9]+(?:\.[0-9]+)?)', sec6_content, re.IGNORECASE)
            if m_w:
                try:
                    v_wind_val = float(m_w.group(1))
                except ValueError:
                    pass

            m_theta = re.search(r'theta[_\s]*impact[^\d]*([0-9]+(?:\.[0-9]+)?)', sec6_content, re.IGNORECASE)
            if m_theta:
                try:
                    theta_val = float(m_theta.group(1))
                except ValueError:
                    pass

            m_r = re.search(r'R[_\s]*GRB[^\d]*([0-9]+(?:\.[0-9]+)?)', sec6_content, re.IGNORECASE)
            if not m_r:
                m_r = re.search(r'(?:ground\s+risk\s+buffer\s+radius|buffer\s+radius)[^\d]*([0-9]+(?:\.[0-9]+)?)', sec6_content, re.IGNORECASE)
            if m_r:
                try:
                    r_grb_val = float(m_r.group(1))
                except ValueError:
                    pass

            if h_max_val is not None and v_wind_val is not None and r_grb_val is not None and self.strict_sora_math:
                r_calc = calculate_sora_grb_radius(h_max_m=h_max_val, theta_impact_deg=theta_val, v_wind_max_mps=v_wind_val)
                if r_grb_val < (r_calc - 1.0):
                    findings.append(Finding(
                        "conops-sora-grb-underdimensioned",
                        f"Ground Risk Buffer radius R_GRB = {r_grb_val:.1f} m in Section 6 is under-dimensioned against JARUS SORA v2.5 theoretical minimum {r_calc:.1f} m (for h_max={h_max_val} m, v_wind={v_wind_val} m/s).",
                        location=f"{rel_path}:{sec6_line}",
                        detail={"declared_r_grb": r_grb_val, "minimum_r_grb": r_calc},
                    ))

        # Section 12: 7-Row Emergency Decision Matrix Validation
        if 12 in matched_sections:
            _, sec12_line, sec12_content = matched_sections[12]
            sec12_tables, _ = _parse_commonmark_tables(sec12_content)
            
            found_triggers: Set[str] = set()
            if sec12_tables:
                emergency_rows = sec12_tables[0]
                for r in emergency_rows:
                    full_row_str = " ".join(r.values())
                    m_emg = re.search(r'(EMG-0*[1-7])', full_row_str, re.IGNORECASE)
                    if m_emg:
                        found_triggers.add(m_emg.group(1).upper().replace("-0", "-0" if len(m_emg.group(1).split("-")[1]) == 2 else "-0"))
                    for trig in self.CANONICAL_EMERGENCY_TRIGGERS:
                        if trig in full_row_str.upper():
                            found_triggers.add(trig)
            else:
                # Fallback regex over raw section text if no table was parsed
                for trig in self.CANONICAL_EMERGENCY_TRIGGERS:
                    if re.search(rf'\b{trig}\b', sec12_content, re.IGNORECASE):
                        found_triggers.add(trig)

            if len(found_triggers) < 7:
                missing_triggers = [t for t in self.CANONICAL_EMERGENCY_TRIGGERS if t not in found_triggers]
                findings.append(Finding(
                    "conops-emergency-matrix-incomplete",
                    f"Section 12 Emergency Decision Matrix has {len(found_triggers)}/7 canonical emergency triggers; missing: {', '.join(missing_triggers)}.",
                    location=f"{rel_path}:{sec12_line}",
                    detail={"found_triggers": list(found_triggers), "missing_triggers": missing_triggers},
                ))

            # Emergency Matrix depth, canonical subsections, statechart & density floor (Issue #88)
            findings.extend(self._validate_emergency_matrix_depth(content, rel_path, sec12_line, sec12_content))

        return findings

    def _is_emergency_subsection_present(self, req: Dict[str, Any], sec_text: str) -> bool:
        sub_num = req["num"]
        num_pattern = rf'^(?:#{1,4})\s+(?:subsection\s+|section\s+)?{re.escape(sub_num)}[.\s:\-—]'
        for line in sec_text.splitlines():
            s = line.strip()
            if re.search(num_pattern, s, re.IGNORECASE):
                return True
            if s.startswith("#"):
                s_lower = s.lower()
                for alias in req.get("aliases", []):
                    if alias.lower() in s_lower:
                        return True
        if re.search(rf'^(?:#{1,4})\s*{re.escape(sub_num)}\b', sec_text, re.MULTILINE | re.IGNORECASE):
            return True
        return False

    def _validate_emergency_matrix_depth(
        self,
        content: str,
        rel_path: str = "docs/conops/CONOPS.md",
        sec12_line: int = 1,
        sec12_content: Optional[str] = None,
    ) -> List[Finding]:
        """
        Validates Section 12 Emergency Decision & Contingency Matrix for:
        a) Mandatory presence of canonical subsections 12.1 through 12.6:
           - 12.1 (Failsafe State Transition Semantics / Timing Guarantees)
           - 12.2 (Failsafe State Machine Architecture / Statechart Diagram)
           - 12.3 (Contingency Flight Maneuvers / Aerodynamic Descent Profiles)
           - 12.4 (Flight Termination Subsystem FTS / Safe-Arm Circuitry)
           - 12.5 (Human-in-the-Loop Override / Veto Timers)
           - 12.6 (Post-Emergency Ground Recovery / Telemetry Quarantine / Investigation)
           Emits Finding 'conops-emergency-subsection-missing' if any subsection is missing.
        b) Mandatory presence of a valid Mermaid stateDiagram-v2 statechart inside Section 12.
           Emits Finding 'conops-emergency-statechart-missing' if absent.
        c) Content density floor: Section 12 content must have at least 1500 characters.
           Emits Finding 'conops-emergency-section-underpopulated' if below floor.
        """
        findings: List[Finding] = []
        if sec12_content is not None:
            target_text = sec12_content
        else:
            sections = _extract_markdown_sections(content)
            sec12_match = _find_matching_section(
                sections,
                12,
                "7-Row Emergency Decision & Contingency Matrix",
                ["emergency decision", "contingency matrix", "7-row emergency", "emergency matrix", "emergency decision & contingency matrix", "emg-"],
            )
            if sec12_match:
                _, sec12_line, target_text = sec12_match
            else:
                target_text = content

        # a) Mandatory canonical subsections 12.1 through 12.6
        for sub in self.CANONICAL_EMERGENCY_SUBSECTIONS:
            if not self._is_emergency_subsection_present(sub, target_text):
                findings.append(Finding(
                    "conops-emergency-subsection-missing",
                    f"Section 12 in '{rel_path}' is missing mandatory subsection {sub['num']} ('{sub['title']}').",
                    location=f"{rel_path}:{sec12_line}",
                    detail={"subsection": sub["num"], "title": sub["title"], "file": rel_path},
                ))

        # b) Mandatory Mermaid stateDiagram-v2 statechart
        has_statechart = bool(re.search(r'```mermaid[\s\S]*?stateDiagram(?:-v2)?[\s\S]*?```', target_text, re.IGNORECASE))
        if not has_statechart:
            findings.append(Finding(
                "conops-emergency-statechart-missing",
                f"Section 12 in '{rel_path}' is missing mandatory Mermaid stateDiagram-v2 statechart diagram.",
                location=f"{rel_path}:{sec12_line}",
                detail={"file": rel_path},
            ))

        # c) Content density floor: Section 12 content must have at least 1500 characters
        sec12_len = len(target_text.strip())
        if sec12_len < 1500:
            findings.append(Finding(
                "conops-emergency-section-underpopulated",
                f"Section 12 content in '{rel_path}' has {sec12_len} characters, failing mandatory content density floor of 1500 characters.",
                location=f"{rel_path}:{sec12_line}",
                detail={"character_count": sec12_len, "minimum_required": 1500, "file": rel_path},
            ))

        return findings

    def synthesize_canonical_template(self, output_path: Union[str, Path]) -> bool:
        """Synthesizes domain-neutral CONOPS_CANONICAL_TEMPLATE.md."""
        res_path = Path(__file__).resolve().parents[4] / "resources" / "CONOPS_CANONICAL_TEMPLATE.md"
        if res_path.is_file():
            template_text = res_path.read_text(encoding="utf-8")
        else:
            template_text = """| Attribute | Value |
| :--- | :--- |
| **Title** | Concept of Operations (ConOps): {{SYSTEM_IDENTIFIER}} |
| **Version** | {{DOCUMENT_VERSION}} |
| **Date** | {{DOCUMENT_DATE}} |

# Concept of Operations (ConOps): {{SYSTEM_IDENTIFIER}}

## 1. Scope & System Identification
- **System Identifier:** `{{SYSTEM_IDENTIFIER}}`
- **Operational Domain:** `{{OPERATIONAL_DOMAIN}}`
- **Operational Boundaries:** {{OPERATIONAL_BOUNDARIES}}
- **Stakeholder Roster:** {{STAKEHOLDER_ROSTER}}

## 2. Normative Standards & Regulatory Baseline
| Standard ID | Issuing Body | Title / Baseline | Applicable Clauses |
| :--- | :--- | :--- | :--- |
| ISO/IEC/IEEE 29148:2018 | ISO/IEEE | Systems and Software Engineering — Requirements Engineering | §6.4.2 ConOps & §6.4.3 OpsCon |
| OMG UAF v1.2 / v2.0 | OMG | Unified Architecture Framework | Operational Domain (Op-*) |
| NATO STANAG 4586 | NATO | Standard Interfaces of Autonomous Control Systems | Interoperability Profiles |
| JARUS SORA v2.5 | JARUS | Specific Operations Risk Assessment | Annex B (Ground Risk & GRB) |
| RTCA DO-178C / DO-254 | RTCA | Software and Electronic Hardware Considerations | Safety Assurance |

## 3. Current Situation & Deficiency Analysis (Predecessors)
- **Current Operational Baseline:** {{CURRENT_OPERATIONAL_BASELINE}}
- **Operational Deficiencies:** {{OPERATIONAL_DEFICIENCIES}}

## 4. Operational Justification & Priority Matrix (Trade-Offs)
- **Mission Drivers & Value Proposition:** {{MISSION_DRIVERS_AND_VALUE_PROPOSITION}}
- **Trade-Off Analysis:** {{TRADE_OFF_ANALYSIS}}

## 5. Operational Modes & Lifecycle Stages
Formal operational lifecycle stages across $\\Phi_{\\mathrm{lifecycle}}$:
- **Phase_Startup:** {{PHASE_STARTUP_DESCRIPTION}}
- **Phase_NominalExecution:** {{PHASE_NOMINAL_EXECUTION_DESCRIPTION}}
- **Phase_DegradedMode:** {{PHASE_DEGRADED_MODE_DESCRIPTION}}
- **Phase_ContingencyFailsafe:** {{PHASE_CONTINGENCY_FAILSAFE_DESCRIPTION}}
- **Phase_SecureShutdown:** {{PHASE_SECURE_SHUTDOWN_DESCRIPTION}}
- **Phase_MaintenanceMode:** {{PHASE_MAINTENANCE_MODE_DESCRIPTION}}

## 6. 4D Operational Volume & SORA Ground Risk Buffer Mathematics
$$
\\begin{aligned}
V_{\\mathrm{4D}} &= V_{\\mathrm{SpatialGeometry}} \\cup V_{\\mathrm{ContingencyVolume}} \\cup V_{\\mathrm{GRB}} \\\\
R_{\\mathrm{GRB}} &= h_{\\mathrm{max}} \\cdot \\tan(\\theta_{\\mathrm{impact}}) + v_{\\mathrm{wind,max}} \\cdot \\sqrt{\\frac{2 h_{\\mathrm{max}}}{g}} + d_{\\mathrm{glide,max}}
\\end{aligned}
$$

| Parameter | Symbol | Value | Units | Description |
| :--- | :--- | :--- | :--- | :--- |
| Max Altitude / Ceiling | h_max | {{H_MAX_M}} | m | Maximum operating ceiling above reference surface |
| Impact Angle | theta_impact | {{THETA_IMPACT_DEG}} | deg | Worst-case operational trajectory impact angle |
| Max Wind Speed | v_wind_max | {{V_WIND_MAX_MPS}} | m/s | Maximum operational wind speed limit |
| Gravitational Accel | g | {{G_ACCEL_MPS2}} | m/s^2 | Standard gravitational acceleration constant |
| Maximum Glide Distance | d_glide_max | {{D_GLIDE_MAX_M}} | m | Maximum unpowered lateral displacement margin |
| Ground Risk Buffer Radius | R_GRB | {{R_GRB_METERS}} | m | Declared ground risk buffer containment radius |
| Terminal Velocity | v_terminal | {{V_TERMINAL_MPS}} | m/s | Estimated unpowered descent terminal velocity |
| Impact Kinetic Energy | E_impact | {{E_IMPACT_JOULES}} | J | Kinetic energy at operational boundary impact |

## 7. OMG UAF Operational Activity Taxonomy
| Activity ID | Activity Name | Description | Gate 24 Allocation Tag |
| :--- | :--- | :--- | :--- |
| OA-01 | {{OA_ACTIVITY_NAME}} | {{OA_DESCRIPTION}} | `/// OperationalAllocation: [OA-01]` |

## 8. Operational Information Exchange (Op-Tx) Matrix
| Exchange ID | Source Node | Destination Node | Information Item | Data Rate | Max Latency | Criticality |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| OpTx-01 | {{OPTX_SOURCE_NODE}} | {{OPTX_DEST_NODE}} | {{OPTX_INFO_ITEM}} | {{OPTX_DATA_RATE}} | {{OPTX_MAX_LATENCY}} | {{OPTX_CRITICALITY}} |

## 9. Operational Environments & Constraints
- **Ambient Temperature:** {{AMBIENT_TEMPERATURE_RANGE}}
- **Environmental Ingress:** {{ENVIRONMENTAL_INGRESS_RATING}}
- **Electromagnetic / RF Environment:** {{RF_ENVIRONMENT_CONSTRAINTS}}
- **Physical Spatial Constraints:** {{PHYSICAL_SPATIAL_CONSTRAINTS}}

## 10. Multi-Threaded Operational Scenarios
- **Scenario 1 (Nominal Execution):** {{SCENARIO_NOMINAL_THREAD}}
- **Scenario 2 (Degraded Mode & Mitigation):** {{SCENARIO_DEGRADED_THREAD}}
- **Scenario 3 (Contingency Recovery):** {{SCENARIO_CONTINGENCY_THREAD}}

## 11. Maintenance & Sustainment Concepts (O/I/D Maintenance)
- **O-Level (Organizational):** {{O_LEVEL_MAINTENANCE_DESCRIPTION}}
- **I-Level (Intermediate):** {{I_LEVEL_MAINTENANCE_DESCRIPTION}}
- **D-Level (Depot):** {{D_LEVEL_MAINTENANCE_DESCRIPTION}}

## 12. 7-Row Emergency Decision & Contingency Matrix
| Trigger ID | Contingency Trigger | Detection Mechanism | Automated Containment Action | Failsafe State | Max Response Time | HITL Role |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `EMG-01` | {{EMG_TRIGGER_NAME}} | {{EMG_DETECTION_MECHANISM}} | {{EMG_CONTAINMENT_ACTION}} | `{{EMG_FAILSAFE_STATE}}` | {{EMG_MAX_RESPONSE_TIME}} | {{EMG_HITL_ROLE}} |
| `EMG-02` | {{EMG_TRIGGER_NAME}} | {{EMG_DETECTION_MECHANISM}} | {{EMG_CONTAINMENT_ACTION}} | `{{EMG_FAILSAFE_STATE}}` | {{EMG_MAX_RESPONSE_TIME}} | {{EMG_HITL_ROLE}} |
| `EMG-03` | {{EMG_TRIGGER_NAME}} | {{EMG_DETECTION_MECHANISM}} | {{EMG_CONTAINMENT_ACTION}} | `{{EMG_FAILSAFE_STATE}}` | {{EMG_MAX_RESPONSE_TIME}} | {{EMG_HITL_ROLE}} |
| `EMG-04` | {{EMG_TRIGGER_NAME}} | {{EMG_DETECTION_MECHANISM}} | {{EMG_CONTAINMENT_ACTION}} | `{{EMG_FAILSAFE_STATE}}` | {{EMG_MAX_RESPONSE_TIME}} | {{EMG_HITL_ROLE}} |
| `EMG-05` | {{EMG_TRIGGER_NAME}} | {{EMG_DETECTION_MECHANISM}} | {{EMG_CONTAINMENT_ACTION}} | `{{EMG_FAILSAFE_STATE}}` | {{EMG_MAX_RESPONSE_TIME}} | {{EMG_HITL_ROLE}} |
| `EMG-06` | {{EMG_TRIGGER_NAME}} | {{EMG_DETECTION_MECHANISM}} | {{EMG_CONTAINMENT_ACTION}} | `{{EMG_FAILSAFE_STATE}}` | {{EMG_MAX_RESPONSE_TIME}} | {{EMG_HITL_ROLE}} |
| `EMG-07` | {{EMG_TRIGGER_NAME}} | {{EMG_DETECTION_MECHANISM}} | {{EMG_CONTAINMENT_ACTION}} | `{{EMG_FAILSAFE_STATE}}` | {{EMG_MAX_RESPONSE_TIME}} | {{EMG_HITL_ROLE}} |

### 12.1 Failsafe State Transition Semantics & Timing Guarantees
- **State Transition Semantics:** {{FAILSAFE_TRANSITION_SEMANTICS}}
- **Priority Arbitration:**
$$
\\begin{aligned}
P_{\\mathrm{EMG-07}} > P_{\\mathrm{EMG-03}} > P_{\\mathrm{EMG-05}} > P_{\\mathrm{EMG-06}} > P_{\\mathrm{EMG-04}} > P_{\\mathrm{EMG-02}} > P_{\\mathrm{EMG-01}}
\\end{aligned}
$$
- **Timing Bounds:** Maximum automated containment reaction time strictly bounded by $t_{\\mathrm{resp}} \\le {{MAX_CONTAINMENT_RESPONSE_TIME_MS}}\\text{ ms}$.
- **State Latching:** {{FAILSAFE_STATE_LATCHING_RULES}}

### 12.2 Failsafe State Machine Architecture & Statechart Diagram
```mermaid
stateDiagram-v2
    [*] --> Phase_NominalExecution : System BIT Passed / Normal Operation

    state Phase_NominalExecution {
        [*] --> MissionExecution
        MissionExecution --> SensorProcessing
        SensorProcessing --> MissionExecution
    }

    Phase_NominalExecution --> Degraded_SensorFailsafe : EMG-04 (Sensor Fault)
    Phase_NominalExecution --> Contingency_DeadReckoning : EMG-02 (GNSS Loss)
    Phase_NominalExecution --> Contingency_LostLinkReturn : EMG-01 (C2 Loss)
    Phase_NominalExecution --> Contingency_GeofenceContainment : EMG-05 (Geofence Breach)
    Phase_NominalExecution --> Contingency_PrecautionaryLand : EMG-06 (Structural Anomaly)
    Phase_NominalExecution --> Contingency_EmergencyGlide : EMG-03 (Propulsion Loss)
    Phase_NominalExecution --> Emergency_FlightTermination : EMG-07 (FTS Abort Command)

    Degraded_SensorFailsafe --> Contingency_PrecautionaryLand : Fault Escalation
    Contingency_DeadReckoning --> Contingency_LostLinkReturn : Timeout Expired
    Contingency_LostLinkReturn --> Emergency_FlightTermination : Outer Geofence Violation
    Contingency_GeofenceContainment --> Phase_NominalExecution : Safe Corridor Restored
    Contingency_EmergencyGlide --> Phase_SecureShutdown : Glide Touchdown
    Contingency_PrecautionaryLand --> Phase_SecureShutdown : Landing Verified
    Emergency_FlightTermination --> Phase_SecureShutdown : Parachute Descent & Ground Quarantine

    state Phase_SecureShutdown {
        [*] --> PowerCutoff
        PowerCutoff --> TelemetryQuarantineLock
        TelemetryQuarantineLock --> EmergencyBeaconActive
    }
```

### 12.3 Contingency Flight Maneuvers & Aerodynamic Descent Profiles
- **Containment Turnaround Profile:** Commanded coordinated turn at maximum bank angle $\\phi_{\\mathrm{max}} = {{MAX_BANK_ANGLE_DEG}}^\\circ$ with turnaround airspeed $v_{\\mathrm{turn}} = {{TURNAROUND_AIRSPEED_MPS}}\\text{ m/s}$.
$$
\\begin{aligned}
R_{\\mathrm{turn}} = \\frac{v_{\\mathrm{turn}}^2}{g \\cdot \\tan(\\phi_{\\mathrm{max}})}
\\end{aligned}
$$
- **Optimal Glide Descent Profile:** Best $(L/D)_{\\mathrm{max}} = {{MAX_L_OVER_D_RATIO}}$ unpowered glide descent toward secondary divert coordinates.
- **Precautionary Landing Profile:** {{PRECAUTIONARY_LANDING_PROFILE}}

### 12.4 Flight Termination Subsystem (FTS) & Safe-Arm Circuitry
- **Hardware Isolation:** {{FTS_HARDWARE_ISOLATION_DESCRIPTION}}
- **Power Cutoff Mechanism:** High-voltage main power distribution bus disconnect within $t_{\\mathrm{cut}} \\le {{FTS_CUTOFF_TIME_MS}}\\text{ ms}$.
- **Deployment Mechanism:** {{FTS_PARACHUTE_DEPLOYMENT_MECHANISM}}
- **Safe-Arm Interlocks:** {{FTS_SAFE_ARM_INTERLOCKS}}

### 12.5 Human-in-the-Loop Override & Veto Timers
- **Supervisory Veto Timer:** GCS operator veto countdown window $\\tau_{\\mathrm{veto}} = {{HITL_VETO_WINDOW_SECONDS}}\\text{ s}$ prior to non-immediate failsafe trajectory execution.
- **Manual Override Precedence:** Dedicated emergency link manual override commands strictly preempt autonomous loiter profiles.
- **Dual-Consent Authorization:** Critical flight termination requires dual-consent cryptographic confirmation.

### 12.6 Post-Emergency Ground Recovery, Telemetry Quarantine & Investigation
- **Telemetry Quarantine:** Autonomous write-lock and cryptographic hashing (SHA-256) of flight recorder partitions upon touchdown.
- **Localization Beacon:** Dedicated emergency homing beacon ($406.040\\text{ MHz}$ COSPAS-SARSAT / $121.5\\text{ MHz}$) active for at least {{BEACON_DURATION_HOURS}} hours.
- **Ground Ordnance & De-Arming:** {{GROUND_DEARMING_AND_RECOVERY_PROCEDURES}}
"""
        out_p = Path(output_path)
        out_p.parent.mkdir(parents=True, exist_ok=True)
        out_p.write_text(template_text, encoding="utf-8")
        return True


# =============================================================================
# Gate 26: MissionIntentCompletenessValidator
# =============================================================================

class MissionIntentCompletenessValidator(IValidator):
    """
    Quality Gate 26: Mission Intent Completeness Validator.
    Enforces 10 mandatory sections, METL roster MET-01..N with Gate 24 allocation tags,
    MoE/MoP metrics, Threat/EW matrix, PACE C2 plan, ROE interlocks, dynamic geo-zones,
    Go/No-Go matrix, and Bingo Energy mathematics with >= 20% statutory reserve.
    """

    MANDATORY_SECTIONS: List[Dict[str, Any]] = [
        {"num": 1, "title": "Commander's Intent & Operational Objectives", "aliases": ["commander's intent", "operational objectives", "purpose", "mission intent"]},
        {"num": 2, "title": "Mission Essential Task List (METL)", "aliases": ["mission essential task list", "metl", "met-", "essential tasks"]},
        {"num": 3, "title": "Measures of Effectiveness (MoE) & Measures of Performance (MoP) Metrics", "aliases": ["measures of effectiveness", "measures of performance", "moe", "mop", "moe/mop", "metrics"]},
        {"num": 4, "title": "Threat & Electronic Warfare (EW) / Cyber Environment Matrix", "aliases": ["threat", "electronic warfare", "ew matrix", "cyber environment", "threat matrix"]},
        {"num": 5, "title": "PACE C2 Link Communications Plan", "aliases": ["pace c2", "pace plan", "pace communications plan", "c2 link communications plan", "pace"]},
        {"num": 6, "title": "Rules of Engagement (ROE) & Weapon/Sensor Interlocks", "aliases": ["rules of engagement", "roe", "weapon/sensor interlocks", "sensor interlocks", "roe interlocks", "interlocks"]},
        {"num": 7, "title": "Airspace Deconfliction & U-space Dynamic Geo-Zones", "aliases": ["airspace deconfliction", "u-space", "geo-zones", "dynamic geo-zones", "airspace", "geofence"]},
        {"num": 8, "title": "Go/No-Go Decision Matrix", "aliases": ["go/no-go", "go-no-go", "go / no-go decision matrix", "go / no-go matrix", "gng-"]},
        {"num": 9, "title": "Bingo Energy Mathematics & Secondary Divert Protocols", "aliases": ["bingo energy", "secondary divert", "divert protocols", "bingo energy mathematics", "bingo", "divert"]},
        {"num": 10, "title": "Gate 24 MissionTask Traceability Tags", "aliases": ["gate 24", "missiontask traceability", "traceability tags", "allocation tags", "operationalallocation"]},
    ]

    MANDATORY_THREAT_DOMAINS: List[Dict[str, Any]] = [
        {"name": "Kinetic", "patterns": [r"\bkinetic\b"]},
        {"name": "Mechanical", "patterns": [r"\bmechanical\b", r"\bstructural\b"]},
        {"name": "Power / Thermal", "patterns": [r"\bpower\b", r"\bthermal\b", r"\bpropulsion\b"]},
        {"name": "Environmental", "patterns": [r"\benvironment(?:al)?\b"]},
        {"name": "Electronic Warfare", "patterns": [r"\belectronic\s+warfare\b", r"\bew\b"]},
        {"name": "Cybersecurity", "patterns": [r"\bcyber(?:security)?\b"]},
        {"name": "Optical", "patterns": [r"\boptical\b", r"\bdirected\s+energy\b"]},
        {"name": "Signature", "patterns": [r"\bsignature\b", r"\bacoustic\b"]},
        {"name": "Human Factors", "patterns": [r"\bhuman(?:\s+factors)?\b", r"\bcrm\b"]},
        {"name": "Hazardous Environment", "patterns": [r"\bhazardous(?:\s+environment)?\b", r"\bcbrn\b", r"\btoxic\b", r"\bchemical\b"]},
    ]

    def __init__(self, strict_bingo_math: bool = True) -> None:
        self.strict_bingo_math = strict_bingo_math

    def validate(self, repo: WorkspaceRepository, **kwargs) -> List[Finding]:
        findings: List[Finding] = []
        workspace_dir = repo.workspace_dir
        conops_dir = os.path.join(workspace_dir, "docs", "conops")

        if not os.path.isdir(conops_dir):
            if repo.is_upstream_compiler_repo():
                return []
            return [Finding(
                "mission-intent-corpus-missing",
                "Mission Intent corpus directory 'docs/conops' is missing in workspace.",
                location="docs/conops",
            )]

        mission_files: List[str] = []
        for root, _, files in os.walk(conops_dir):
            for f in sorted(files):
                if ("MISSION_INTENT" in f.upper() or "MISSIONINTENT" in f.upper()) and f.endswith(".md") and "TEMPLATE" not in f.upper():
                    mission_files.append(os.path.join(root, f))

        if not mission_files:
            if repo.is_upstream_compiler_repo():
                return []
            return [Finding(
                "mission-intent-corpus-missing",
                "No valid Mission Intent specification document ('MISSION_INTENT*.md') found in 'docs/conops'.",
                location="docs/conops",
            )]

        for m_file in mission_files:
            rel_path = os.path.relpath(m_file, workspace_dir)
            try:
                with open(m_file, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
            except Exception as e:
                findings.append(Finding(
                    "mission-read-error",
                    f"Failed to read Mission Intent document '{rel_path}': {e}",
                    location=rel_path,
                ))
                continue

            findings.extend(self._validate_mission_text(content, rel_path, repo=repo))

        return findings

    def _validate_mission_text(self, content: str, rel_path: str, repo: Optional[WorkspaceRepository] = None) -> List[Finding]:
        findings: List[Finding] = []
        sections = _extract_markdown_sections(content)
        tables, malformed_lines = _parse_commonmark_tables(content)

        # Check for allocated obligations from RESEARCH_INVENTORY.md (Gate 26, Issue #109)
        if "TEMPLATE" not in rel_path.upper():
            inventory_file = None
            if repo is not None:
                inventory_file = os.path.join(repo.workspace_dir, "docs", "research", "RESEARCH_INVENTORY.md")
            else:
                candidate = os.path.join("docs", "research", "RESEARCH_INVENTORY.md")
                if os.path.isfile(candidate):
                    inventory_file = candidate

            if inventory_file and os.path.isfile(inventory_file):
                try:
                    with open(inventory_file, "r", encoding="utf-8") as inv_f:
                        inv_doc = parse_research_inventory(inv_f.read())

                    # Extract document's realized/witnessed tags
                    doc_tags = set(_parse_witness_tags(content) + _parse_obligation_tags(content))
                    fm = extract_metadata_from_content(content)
                    if fm:
                        for key in ("obligations", "normative_obligations", "allocated_obligations", "obligation_id"):
                            val = fm.get(key)
                            if isinstance(val, list):
                                for item in val:
                                    norm = _normalize_obligation_id(str(item))
                                    if norm:
                                        doc_tags.add(norm)
                            elif isinstance(val, str):
                                norm = _normalize_obligation_id(val)
                                if norm:
                                    doc_tags.add(norm)

                    # Find all obligations allocated to MISSION_INTENT in clause allocations
                    for alloc in inv_doc.clause_allocations:
                        if alloc.population_id and alloc.downstream_spec_file:
                            spec_target = alloc.downstream_spec_file.strip("`* ")
                            target_base = os.path.basename(spec_target).upper()
                            is_mission_target = (
                                "MISSION_INTENT" in target_base
                                or "MISSIONINTENT" in target_base
                                or os.path.normpath(spec_target) == os.path.normpath(rel_path)
                            )
                            if is_mission_target:
                                norm_id = _normalize_obligation_id(alloc.population_id)
                                if norm_id not in doc_tags:
                                    findings.append(Finding(
                                        "mission-intent-obligation-unwitnessed",
                                        f"Mission Intent document '{rel_path}' is missing mandatory witness/realization tag for allocated obligation '{norm_id}' ({alloc.clause_citation or alloc.standard_id}).",
                                        location=rel_path,
                                        detail={"obligation_id": norm_id, "file": rel_path, "standard_id": alloc.standard_id},
                                    ))
                except Exception:
                    pass

        # Check for malformed tables
        for m_line in malformed_lines:
            findings.append(Finding(
                "mission-table-malformed",
                f"Malformed CommonMark table or broken row formatting detected at line {m_line} in '{rel_path}'.",
                location=f"{rel_path}:{m_line}",
            ))

        # Check for 10 Mandatory Sections
        matched_sections: Dict[int, Tuple[str, int, str]] = {}
        for req in self.MANDATORY_SECTIONS:
            sec_num = req["num"]
            title = req["title"]
            aliases = req["aliases"]
            res = _find_matching_section(sections, sec_num, title, aliases)
            if res:
                matched_sections[sec_num] = res
            else:
                findings.append(Finding(
                    "mission-section-missing",
                    f"Mandatory Mission Intent Section {sec_num} ('{title}') is missing or empty in '{rel_path}'.",
                    location=rel_path,
                    detail={"section_number": sec_num, "section_title": title},
                ))

        # Section 4: Threat & Electronic Warfare (EW) / Cyber Environment Matrix Validation (Threat Matrix Density)
        if 4 in matched_sections:
            _, sec4_line, sec4_content = matched_sections[4]
            findings.extend(self._validate_threat_matrix_density(content, rel_path, sec4_line, sec4_content))

        # Section 2 & 10: METL Roster & Gate 24 Allocation Traceability (Theorem 3)
        if 2 in matched_sections:
            _, sec2_line, sec2_content = matched_sections[2]
            declared_met_tasks: Set[str] = set()

            # 1. Parse tables if present in Section 2
            sec2_tables, _ = _parse_commonmark_tables(sec2_content)
            for tbl in sec2_tables:
                for row in tbl:
                    task_val = (
                        row.get("task_id")
                        or row.get("id")
                        or row.get("task")
                        or row.get("metl_id")
                        or row.get("met_id")
                    )
                    if not task_val and row:
                        first_k = list(row.keys())[0]
                        task_val = row[first_k]
                    if task_val:
                        clean_val = re.sub(r'[*`_]', '', task_val).strip()
                        m = re.search(r'\b(MET-0*[0-9]+)\b', clean_val, re.IGNORECASE)
                        if m:
                            num = int(m.group(1).split("-")[1])
                            declared_met_tasks.add(f"MET-{num:02d}")

            # 2. Extract declared MET tasks from text lines / bullet points
            met_task_matches = re.finditer(
                r'\b(MET-0*[0-9]+)\b',
                sec2_content,
                re.IGNORECASE,
            )
            for m in met_task_matches:
                num = int(m.group(1).split("-")[1])
                declared_met_tasks.add(f"MET-{num:02d}")

            sorted_tasks = sorted(list(declared_met_tasks))

            # Check allocation tags across the document
            for task_id in sorted_tasks:
                # Look for '/// OperationalAllocation: [ ... task_id ... ]' or '/// OperationalAllocation: task_id'
                tag_pattern = rf'///\s*OperationalAllocation\s*:\s*(?:\[[^\]]*(?<![A-Za-z0-9_-]){re.escape(task_id)}(?![A-Za-z0-9_-])[^\]]*\]|(?<![A-Za-z0-9_-]){re.escape(task_id)}(?![A-Za-z0-9_-]))'
                if not re.search(tag_pattern, content, re.IGNORECASE):
                    findings.append(Finding(
                        "mission-metl-unallocated",
                        f"Mission Essential Task '{task_id}' declared in Section 2 has no valid Gate 24 allocation tag ('/// OperationalAllocation: [{task_id}]') in '{rel_path}'.",
                        location=f"{rel_path}:{sec2_line}",
                        detail={"task_id": task_id},
                    ))

        # Section 9: Bingo Energy Mathematics & Reserve Ratio Validation
        if 9 in matched_sections:
            _, sec9_line, sec9_content = matched_sections[9]
            capacity_val: Optional[float] = None
            reserve_val: Optional[float] = None

            # Regex search for E_capacity and E_reserve
            m_cap = re.search(r'E[_\s]*capacity[^\d]*([0-9]+(?:\.[0-9]+)?)', sec9_content, re.IGNORECASE)
            if not m_cap:
                m_cap = re.search(r'(?:total\s+capacity|pack\s+capacity|battery\s+capacity)[^\d]*([0-9]+(?:\.[0-9]+)?)', sec9_content, re.IGNORECASE)
            if m_cap:
                try:
                    capacity_val = float(m_cap.group(1))
                except ValueError:
                    pass

            m_res = re.search(r'E[_\s]*reserve[^\d]*([0-9]+(?:\.[0-9]+)?)', sec9_content, re.IGNORECASE)
            if not m_res:
                m_res = re.search(r'(?:statutory\s+reserve|reserve\s+energy|energy\s+reserve)[^\d]*([0-9]+(?:\.[0-9]+)?)', sec9_content, re.IGNORECASE)
            if m_res:
                try:
                    reserve_val = float(m_res.group(1))
                except ValueError:
                    pass

            if capacity_val is not None and reserve_val is not None and self.strict_bingo_math:
                ratio = calculate_bingo_energy_reserve_ratio(total_capacity_j=capacity_val, reserve_energy_j=reserve_val)
                if ratio < 0.199:  # Strict 20% minimum statutory reserve
                    findings.append(Finding(
                        "mission-bingo-reserve-insufficient",
                        f"Statutory reserve energy E_reserve = {reserve_val:.1f} J is {ratio*100.0:.1f}% of total capacity {capacity_val:.1f} J in Section 9, violating mandatory 20.0% statutory reserve threshold.",
                        location=f"{rel_path}:{sec9_line}",
                        detail={"capacity_joules": capacity_val, "reserve_joules": reserve_val, "reserve_ratio": ratio},
                    ))

        return findings

    def _validate_threat_matrix_density(
        self,
        content: str,
        rel_path: str = "docs/conops/MISSION_INTENT.md",
        sec4_line: int = 1,
        sec4_content: Optional[str] = None,
    ) -> List[Finding]:
        """
        Validates Section 4 Threat Matrix tables for presence of mandatory operational domains:
        Kinetic, Mechanical, Power / Thermal, Environmental, Electronic Warfare,
        Cybersecurity, Optical, Signature, Human Factors, and Hazardous Environment.
        Emits Finding 'mission-threat-domain-missing' if a mandatory operational threat domain
        is absent from the Domain column.
        """
        findings: List[Finding] = []
        if sec4_content is not None:
            target_text = sec4_content
        else:
            sections = _extract_markdown_sections(content)
            sec4_match = _find_matching_section(
                sections,
                4,
                "Threat & Electronic Warfare (EW) / Cyber Environment Matrix",
                ["threat", "electronic warfare", "ew matrix", "cyber environment", "threat matrix"],
            )
            if sec4_match:
                _, sec4_line, target_text = sec4_match
            else:
                target_text = content

        tables, _ = _parse_commonmark_tables(target_text)

        present_domains: Set[str] = set()
        for table in tables:
            for row in table:
                domain_val = row.get("domain") or row.get("threat_domain") or row.get("operational_domain")
                if not domain_val:
                    continue
                clean_domain = re.sub(r'[*`_]', '', str(domain_val)).strip()
                for req_dom in self.MANDATORY_THREAT_DOMAINS:
                    dom_name = req_dom["name"]
                    for pat in req_dom["patterns"]:
                        if re.search(pat, clean_domain, re.IGNORECASE):
                            present_domains.add(dom_name)
                            break

        for req_dom in self.MANDATORY_THREAT_DOMAINS:
            dom_name = req_dom["name"]
            if dom_name not in present_domains:
                findings.append(Finding(
                    "mission-threat-domain-missing",
                    f"Section 4 Threat Matrix in '{rel_path}' is missing mandatory operational threat domain '{dom_name}'.",
                    location=f"{rel_path}:{sec4_line}",
                    detail={"domain": dom_name, "file": rel_path},
                ))

        return findings

    def synthesize_canonical_template(self, output_path: Union[str, Path]) -> bool:
        """Synthesizes domain-neutral MISSION_INTENT_CANONICAL_TEMPLATE.md."""
        res_path = Path(__file__).resolve().parents[4] / "resources" / "MISSION_INTENT_CANONICAL_TEMPLATE.md"
        if res_path.is_file():
            template_text = res_path.read_text(encoding="utf-8")
        else:
            template_text = """| Attribute | Value |
| :--- | :--- |
| **Title** | Tactical Mission Intent & Execution Plan: {{MISSION_SYSTEM_NAME}} |
| **Version** | {{DOCUMENT_VERSION}} |
| **Date** | {{DOCUMENT_DATE}} |

# Tactical Mission Intent & Execution Plan: {{MISSION_SYSTEM_NAME}}

## 1. Commander's Intent & Operational Objectives
- **Operational Purpose:** {{OPERATIONAL_PURPOSE}}
- **Key Tasks:** {{KEY_MISSION_TASKS}}
- **End State:** {{MISSION_END_STATE}}

## 2. Mission Essential Task List (METL)
| Task ID | Task Name | Condition Statement | Standard Metric | Verification Method | Gate 24 Allocation Tag |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `MET-01` | {{MET_TASK_NAME}} | {{MET_CONDITION}} | {{MET_STANDARD}} | {{MET_VERIFICATION}} | `/// OperationalAllocation: [MET-01]` |

## 3. Measures of Effectiveness (MoE) & Measures of Performance (MoP) Metrics
| Metric ID | Metric Type | Metric Name | Formulation / Equation | Threshold | Objective | Unit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MoE-01 | MoE | {{MOE_NAME}} | {{MOE_EQUATION}} | {{MOE_THRESHOLD}} | {{MOE_OBJECTIVE}} | {{MOE_UNIT}} |
| MoP-01 | MoP | {{MOP_NAME}} | {{MOP_EQUATION}} | {{MOP_THRESHOLD}} | {{MOP_OBJECTIVE}} | {{MOP_UNIT}} |

## 4. Threat & Electronic Warfare (EW) / Cyber Environment Matrix
| Threat ID | Domain | Threat Vector | Description | Severity | Autonomous Mitigation Rule |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `THR-01` | Kinetic | {{THR_VECTOR}} | {{THR_DESCRIPTION}} | {{THR_SEVERITY}} | {{THR_MITIGATION_RULE}} |
| `THR-02` | Mechanical | {{THR_VECTOR}} | {{THR_DESCRIPTION}} | {{THR_SEVERITY}} | {{THR_MITIGATION_RULE}} |
| `THR-03` | Power / Thermal | {{THR_VECTOR}} | {{THR_DESCRIPTION}} | {{THR_SEVERITY}} | {{THR_MITIGATION_RULE}} |
| `THR-04` | Environmental | {{THR_VECTOR}} | {{THR_DESCRIPTION}} | {{THR_SEVERITY}} | {{THR_MITIGATION_RULE}} |
| `THR-05` | Electronic Warfare | {{THR_VECTOR}} | {{THR_DESCRIPTION}} | {{THR_SEVERITY}} | {{THR_MITIGATION_RULE}} |
| `THR-06` | Cybersecurity | {{THR_VECTOR}} | {{THR_DESCRIPTION}} | {{THR_SEVERITY}} | {{THR_MITIGATION_RULE}} |
| `THR-07` | Optical | {{THR_VECTOR}} | {{THR_DESCRIPTION}} | {{THR_SEVERITY}} | {{THR_MITIGATION_RULE}} |
| `THR-08` | Signature | {{THR_VECTOR}} | {{THR_DESCRIPTION}} | {{THR_SEVERITY}} | {{THR_MITIGATION_RULE}} |
| `THR-09` | Human Factors | {{THR_VECTOR}} | {{THR_DESCRIPTION}} | {{THR_SEVERITY}} | {{THR_MITIGATION_RULE}} |
| `THR-10` | Hazardous Environment | {{THR_VECTOR}} | {{THR_DESCRIPTION}} | {{THR_SEVERITY}} | {{THR_MITIGATION_RULE}} |

## 5. PACE C2 Link Communications Plan
| PACE Tier | Link Medium | Frequency Band | Nominal Data Rate | Heartbeat Timeout | Priority / Role |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Primary** | {{PACE_PRIMARY_MEDIUM}} | {{PACE_PRIMARY_BAND}} | {{PACE_PRIMARY_DATA_RATE}} | {{PACE_PRIMARY_TIMEOUT}} | {{PACE_PRIMARY_ROLE}} |
| **Alternate** | {{PACE_ALTERNATE_MEDIUM}} | {{PACE_ALTERNATE_BAND}} | {{PACE_ALTERNATE_DATA_RATE}} | {{PACE_ALTERNATE_TIMEOUT}} | {{PACE_ALTERNATE_ROLE}} |
| **Contingency** | {{PACE_CONTINGENCY_MEDIUM}} | {{PACE_CONTINGENCY_BAND}} | {{PACE_CONTINGENCY_DATA_RATE}} | {{PACE_CONTINGENCY_TIMEOUT}} | {{PACE_CONTINGENCY_ROLE}} |
| **Emergency** | {{PACE_EMERGENCY_MEDIUM}} | {{PACE_EMERGENCY_BAND}} | {{PACE_EMERGENCY_DATA_RATE}} | {{PACE_EMERGENCY_TIMEOUT}} | {{PACE_EMERGENCY_ROLE}} |

## 6. Rules of Engagement (ROE) & Weapon/Sensor Interlocks
- **ROE-01:** {{ROE_RULE_STATEMENT}}

## 7. Airspace Deconfliction & U-space Dynamic Geo-Zones
- **Primary Boundary Perimeter:** {{PRIMARY_BOUNDARY_PERIMETER}}
- **Dynamic Exclusion Zones:** {{DYNAMIC_EXCLUSION_ZONES}}
- **Separation Minima:** {{SEPARATION_MINIMA}}

## 8. Go/No-Go Decision Matrix
| Check ID | Phase | Parameter / Check | Threshold Condition | Sensor / Mechanism | Go / No-Go Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| GNG-01 | {{GNG_PHASE}} | {{GNG_PARAMETER}} | {{GNG_THRESHOLD}} | {{GNG_MECHANISM}} | {{GNG_ACTION}} |

## 9. Bingo Energy Mathematics & Secondary Divert Protocols
$$
\\begin{aligned}
E_{\\mathrm{bingo}}(t) &= E_{\\mathrm{return}}(\\mathbf{p}(t), \\mathbf{p}_{\\mathrm{dest}}) + E_{\\mathrm{divert}}(\\mathbf{p}_{\\mathrm{dest}}, \\mathbf{p}_{\\mathrm{alt}}) + E_{\\mathrm{reserve}} + E_{\\mathrm{contingency}} \\\\
E_{\\mathrm{reserve}} &\\ge 0.20 \\cdot E_{\\mathrm{capacity}}
\\end{aligned}
$$

| Energy Parameter | Symbol | Value | Units | Constraint Rule |
| :--- | :--- | :--- | :--- | :--- |
| Total Storage Capacity | E_capacity | {{E_CAPACITY_JOULES}} | J | Total nominal energy storage capacity |
| Return Transit Energy | E_return | {{E_RETURN_JOULES}} | J | Energy required for primary return trajectory |
| Secondary Divert Energy | E_divert | {{E_DIVERT_JOULES}} | J | Energy required to divert to secondary recovery site |
| Mandatory Statutory Reserve | E_reserve | {{E_RESERVE_JOULES}} | J | Statutory reserve threshold (E_reserve >= 0.20 * E_capacity) |
| Contingency Buffer | E_contingency | {{E_CONTINGENCY_JOULES}} | J | Dynamic operational contingency energy reserve |
| Total Bingo Threshold | E_bingo | {{E_BINGO_THRESHOLD_JOULES}} | J | Critical return threshold condition |

## 10. Gate 24 MissionTask Traceability Tags (Allocation Tags)
- `/// OperationalAllocation: [MET-01]`
"""
        out_p = Path(output_path)
        out_p.parent.mkdir(parents=True, exist_ok=True)
        out_p.write_text(template_text, encoding="utf-8")
        return True


if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else None
    repo = WorkspaceRepository(workspace_dir=target_dir)
    v1 = ConopsCompletenessValidator()
    v2 = MissionIntentCompletenessValidator()
    errs1 = v1.validate(repo)
    errs2 = v2.validate(repo)
    all_errs = errs1 + errs2
    if all_errs:
        for err in all_errs:
            print(f"[{getattr(err, 'rule_id', 'ERROR')}] {err}")
        sys.exit(1)
    else:
        print("[OK] Gate 26 (ConOps & Mission Intent Completeness): All checks passed.")
        sys.exit(0)

