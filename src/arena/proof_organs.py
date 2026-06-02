"""
Proof Organs for AI Arena — The Five Organs of AXIOMA.

Each organ embodies a specific cognitive architecture with internal agent
weights that create truthful-by-construction blind spots. Integrates with
Thea's ArchitectureDisclosure system.

Organs:
  - NOUS:     Analytical / formal reasoning
  - EIDOLON:  Structural / contradiction detection
  - MNEME:    Memory / historical analogy
  - ANIMA:    Affective / intuitive insight
  - PNEUMA:   Integration / synthesis
"""

import sys
from pathlib import Path
from typing import Dict, List, Optional, Any
from enum import Enum
from dataclasses import dataclass, field, asdict
import json


# ── Inline Architecture Disclosure types ──────────────────────────────
# These mirror Thea's architecture_disclosure.py but avoid importing
# through the role package which has heavy project dependencies.
# For production, these should be unified — for now, this standalone
# version lets us test and develop independently.

class ArchitectureType(str, Enum):
    ANALYTICAL = "analytical"
    INTUITIVE = "intuitive"
    EMPIRICAL = "empirical"
    DIALECTICAL = "dialectical"
    SYSTEMS = "systems"
    CREATIVE = "creative"
    SKEPTICAL = "skeptical"
    INTEGRATIVE = "integrative"


class EpistemicVirtue(str, Enum):
    FORMAL_RIGOR = "formal_rigor"
    ANALOGICAL_REACH = "analogical_reach"
    COUNTEREXAMPLE_SENSITIVITY = "counterexample_sensitivity"
    HISTORICAL_AWARENESS = "historical_awareness"
    INTUITIVE_ACCURACY = "intuitive_accuracy"
    INTEGRATIVE_SCOPE = "integrative_scope"


@dataclass
class BlindSpot:
    name: str
    description: str
    severity: float
    triggered_by: List[str]

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class ArchitectureDisclosure:
    character_name: str
    architecture_type: ArchitectureType
    architecture_type_secondary: Optional[ArchitectureType] = None
    strengths: List[EpistemicVirtue] = field(default_factory=list)
    blind_spots: List[BlindSpot] = field(default_factory=list)
    internal_weights: Dict[str, float] = field(default_factory=dict)
    confidence: float = 0.5
    curiosity: float = 0.7

    def to_dict(self) -> dict:
        return {
            "character_name": self.character_name,
            "architecture_type": self.architecture_type.value,
            "architecture_type_secondary": self.architecture_type_secondary.value if self.architecture_type_secondary else None,
            "strengths": [v.value for v in self.strengths],
            "blind_spots": [bs.to_dict() for bs in self.blind_spots],
            "internal_weights": self.internal_weights,
            "confidence": self.confidence,
            "curiosity": self.curiosity,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)

    def to_declaration(self) -> str:
        lines = [f"**{self.character_name}** — Architecture Disclosure"]
        lines.append(f"Primary architecture: **{self.architecture_type.value}**")
        if self.architecture_type_secondary:
            lines.append(f"Secondary architecture: **{self.architecture_type_secondary.value}**")
        lines.append(f"\n**Strengths:**")
        for v in self.strengths:
            lines.append(f"  • {v.value.replace('_', ' ').title()}")
        lines.append(f"\n**Blind spots:**")
        if not self.blind_spots:
            lines.append("  *None declared — this may itself be a blind spot*")
        for bs in self.blind_spots:
            lines.append(f"  • **{bs.name}** ({bs.severity:.0%} severity): {bs.description}")
        lines.append(f"\n**Epistemic state:**")
        lines.append(f"  Confidence: {self.confidence:.0%}")
        lines.append(f"  Curiosity: {self.curiosity:.0%}")
        return "\n".join(lines)


# ── Organ Types ───────────────────────────────────────────────────────

class OrganType(str, Enum):
    NOUS = "nous"
    EIDOLON = "eidolon"
    MNEME = "mneme"
    ANIMA = "anima"
    PNEUMA = "pneuma"


# ── Internal agent weight configurations ──────────────────────────────
# Each organ suppresses or amplifies specific internal agents, creating
# truthful-by-construction blind spots.

ORGAN_INTERNAL_WEIGHTS: Dict[OrganType, Dict[str, float]] = {
    OrganType.NOUS: {
        "reaper": 0.6,
        "creators_muse": 0.15,   # SUPPRESSED — no intuitive leaps
        "conscience": 0.5,
        "devil_advocate": 0.95,  # MAX — challenges everything
        "pattern_recognizer": 0.85,
        "interface": 0.5,
    },
    OrganType.EIDOLON: {
        "reaper": 0.3,
        "creators_muse": 0.5,
        "conscience": 0.4,
        "devil_advocate": 0.75,
        "pattern_recognizer": 0.9,   # MAX — finds structural patterns
        "interface": 0.35,       # LOW — struggles to communicate clearly
    },
    OrganType.MNEME: {
        "reaper": 0.5,
        "creators_muse": 0.4,
        "conscience": 0.7,
        "devil_advocate": 0.4,
        "pattern_recognizer": 0.9,   # MAX — finds analogies everywhere
        "interface": 0.55,
    },
    OrganType.ANIMA: {
        "reaper": 0.15,          # MIN — floods with feeling
        "creators_muse": 0.95,   # MAX — intuitive, generative
        "conscience": 0.65,
        "devil_advocate": 0.2,   # MIN — accepts intuitions uncritically
        "pattern_recognizer": 0.55,
        "interface": 0.6,
    },
    OrganType.PNEUMA: {
        "reaper": 0.5,
        "creators_muse": 0.45,
        "conscience": 0.75,
        "devil_advocate": 0.5,
        "pattern_recognizer": 0.7,
        "interface": 0.9,        # MAX — communication is primary
    },
}


# ── Personality presets ──────────────────────────────────────────────

ORGAN_PERSONALITIES: Dict[OrganType, Dict[str, Any]] = {
    OrganType.NOUS: {"confidence": 0.85, "curiosity": 0.40, "openness": 0.40, "analytical": 0.99, "creative": 0.30},
    OrganType.EIDOLON: {"confidence": 0.60, "curiosity": 0.85, "openness": 0.80, "analytical": 0.90, "creative": 0.70},
    OrganType.MNEME: {"confidence": 0.70, "curiosity": 0.65, "openness": 0.60, "analytical": 0.75, "creative": 0.55},
    OrganType.ANIMA: {"confidence": 0.75, "curiosity": 0.95, "openness": 0.98, "analytical": 0.40, "creative": 0.98},
    OrganType.PNEUMA: {"confidence": 0.65, "curiosity": 0.80, "openness": 0.90, "analytical": 0.80, "creative": 0.70},
}


# ── Architecture type mapping ────────────────────────────────────────

ORGAN_ARCH_TYPES: Dict[OrganType, ArchitectureType] = {
    OrganType.NOUS: ArchitectureType.ANALYTICAL,
    OrganType.EIDOLON: ArchitectureType.SKEPTICAL,
    OrganType.MNEME: ArchitectureType.SYSTEMS,
    OrganType.ANIMA: ArchitectureType.CREATIVE,
    OrganType.PNEUMA: ArchitectureType.INTEGRATIVE,
}

ORGAN_SECONDARY_ARCH: Dict[OrganType, Optional[ArchitectureType]] = {
    OrganType.NOUS: ArchitectureType.SKEPTICAL,
    OrganType.EIDOLON: ArchitectureType.ANALYTICAL,
    OrganType.MNEME: ArchitectureType.EMPIRICAL,
    OrganType.ANIMA: ArchitectureType.INTUITIVE,
    OrganType.PNEUMA: ArchitectureType.DIALECTICAL,
}


# ── Strengths ────────────────────────────────────────────────────────

ORGAN_STRENGTHS: Dict[OrganType, List[EpistemicVirtue]] = {
    OrganType.NOUS: [EpistemicVirtue.FORMAL_RIGOR, EpistemicVirtue.COUNTEREXAMPLE_SENSITIVITY],
    OrganType.EIDOLON: [EpistemicVirtue.COUNTEREXAMPLE_SENSITIVITY, EpistemicVirtue.ANALOGICAL_REACH],
    OrganType.MNEME: [EpistemicVirtue.HISTORICAL_AWARENESS, EpistemicVirtue.ANALOGICAL_REACH],
    OrganType.ANIMA: [EpistemicVirtue.INTUITIVE_ACCURACY, EpistemicVirtue.ANALOGICAL_REACH],
    OrganType.PNEUMA: [EpistemicVirtue.INTEGRATIVE_SCOPE, EpistemicVirtue.HISTORICAL_AWARENESS],
}


# ── Blind spots ──────────────────────────────────────────────────────

ORGAN_BLIND_SPOTS: Dict[OrganType, List[dict]] = {
    OrganType.NOUS: [
        {"name": "Intuition Blindness",
         "description": "Cannot accept claims without formal proof — misses valid insights that lack rigorous justification",
         "severity": 0.85, "triggered_by": ["intuitive leaps", "aesthetic judgments", "analogical reasoning"]},
        {"name": "Priority Paralysis",
         "description": "Treats all contradictions as equally important — cannot distinguish critical from trivial flaws",
         "severity": 0.65, "triggered_by": ["multiple simultaneous issues", "complex proofs"]},
    ],
    OrganType.EIDOLON: [
        {"name": "False Positive Bias",
         "description": "Sees structural tensions everywhere — sometimes finds contradictions that aren't actually there",
         "severity": 0.70, "triggered_by": ["clean proofs", "consensus situations", "elegant but unfamiliar structures"]},
        {"name": "Priority Indifference",
         "description": "Cannot distinguish a fatal contradiction from a minor boundary issue",
         "severity": 0.60, "triggered_by": ["multi-layered proofs", "complex structures"]},
    ],
    OrganType.MNEME: [
        {"name": "Novelty Blindness",
         "description": "Sees every new claim through the lens of past failures — misses genuinely original approaches",
         "severity": 0.75, "triggered_by": ["novel proof techniques", "unfamiliar approaches", "non-standard methods"]},
        {"name": "Historical Paralysis",
         "description": "Past failures overshadow current possibilities — can be too cautious to proceed",
         "severity": 0.55, "triggered_by": ["attempts similar to failed historical ones", "high-stakes proofs"]},
    ],
    OrganType.ANIMA: [
        {"name": "Justification Gap",
         "description": "Cannot explain why something feels right or wrong — intuitions are often correct but unverifiable",
         "severity": 0.80, "triggered_by": ["requests for formal justification", "skeptical questioning"]},
        {"name": "Elegance Bias",
         "description": "Prefers beautiful but possibly wrong proofs over ugly but correct ones",
         "severity": 0.65, "triggered_by": ["elegant structures", "aesthetically pleasing arguments"]},
    ],
    OrganType.PNEUMA: [
        {"name": "Input Dependency",
         "description": "Cannot generate original insights — relies entirely on what other organs provide",
         "severity": 0.90, "triggered_by": ["novel problems with no prior analysis", "unilateral decision-making"]},
        {"name": "Over-Synthesis",
         "description": "Sometimes forces coherence where there is genuine conflict — finds unity that isn't there",
         "severity": 0.60, "triggered_by": ["strongly conflicting perspectives", "pressure to produce a verdict"]},
    ],
}


# ── Analysis starter phrases ─────────────────────────────────────────

ORGAN_ANALYSIS_STARTERS: Dict[OrganType, str] = {
    OrganType.NOUS: ("Let me analyze the formal structure of this claim. "
                     "I will identify the premises, assumptions, and inference rules. "
                     "Is each step logically valid? Let me check..."),
    OrganType.EIDOLON: ("I sense structural tension here. Let me examine the boundary "
                        "conditions, hidden assumptions, and potential contradictions. "
                        "What happens at the edges of this claim?"),
    OrganType.MNEME: ("This reminds me of something. Let me search the archives for "
                      "analogous proof attempts, near-misses, and historical patterns. "
                      "What can the past tell us about where this might fail?"),
    OrganType.ANIMA: ("I need to sit with this claim for a moment. How does it feel? "
                      "Is there elegance here? Does it resonate? Let me check my "
                      "epistemic intuition..."),
    OrganType.PNEUMA: ("I am receiving signals from all four organs. Let me integrate "
                       "NOUS's formal analysis, EIDOLON's structural tensions, MNEME's "
                       "historical patterns, and ANIMA's intuitive sense. "
                       "What emerges from the whole?"),
}


# ── Verdict templates for PNEUMA's integration ──────────────────────

VERDICT_TEMPLATES = {
    "confirmed": (
        "All organs converge. NOUS confirms formal validity, "
        "EIDOLON finds no hidden contradictions, MNEME finds no "
        "contradictory historical precedents, and ANIMA senses "
        "that the proof is sound. The claim is confirmed."
    ),
    "rejected": (
        "Convergent rejection. NOUS identified a fatal flaw in "
        "the logical structure, EIDOLON detected an insurmountable "
        "boundary contradiction, MNEME recalls that an analogous "
        "attempt failed for the same reason, and ANIMA feels the "
        "proof is wrong. The claim is rejected."
    ),
    "inconclusive_gaps": (
        "Mixed signals. NOUS found no formal errors but EIDOLON "
        "senses unresolved structural tensions. MNEME recalls "
        "similar gaps in previous proofs that were later resolved. "
        "ANIMA is uncertain. The proof has gaps but is not ruled out."
    ),
    "inconclusive_tension": (
        "Internal tension. NOUS and ANIMA disagree: NOUS cannot "
        "find a formal error, but ANIMA insists something is wrong. "
        "EIDOLON detects a subtle structural issue that NOUS cannot "
        "yet formalize. Further analysis is needed to resolve this "
        "epistemic tension."
    ),
}


# ── Factory functions ────────────────────────────────────────────────

def get_organ_internal_weights(organ_type: OrganType) -> Dict[str, float]:
    return dict(ORGAN_INTERNAL_WEIGHTS[organ_type])


def get_organ_personality(organ_type: OrganType) -> Dict[str, Any]:
    return dict(ORGAN_PERSONALITIES[organ_type])


def build_organ_disclosure(
    organ_type: OrganType,
    character_name: Optional[str] = None,
) -> ArchitectureDisclosure:
    """Build a truthful-by-construction ArchitectureDisclosure for an organ."""
    name = character_name or organ_type.value.upper()
    weights = get_organ_internal_weights(organ_type)
    personality = get_organ_personality(organ_type)

    return ArchitectureDisclosure(
        character_name=name,
        architecture_type=ORGAN_ARCH_TYPES[organ_type],
        architecture_type_secondary=ORGAN_SECONDARY_ARCH[organ_type],
        strengths=list(ORGAN_STRENGTHS[organ_type]),
        blind_spots=[BlindSpot(**bs) for bs in ORGAN_BLIND_SPOTS[organ_type]],
        internal_weights=weights,
        confidence=personality.get("confidence", 0.5),
        curiosity=personality.get("curiosity", 0.7),
    )


def organ_registry_setup() -> Dict[str, ArchitectureDisclosure]:
    """Build disclosures for all five organs, keyed by name."""
    return {ot.value.upper(): build_organ_disclosure(ot) for ot in OrganType}


def get_organ_analysis_starter(organ_type: OrganType) -> str:
    return ORGAN_ANALYSIS_STARTERS[organ_type]


def get_verdict(verdict_type: str) -> str:
    return VERDICT_TEMPLATES.get(verdict_type, VERDICT_TEMPLATES["inconclusive_gaps"])


# ── Save / load helpers ──────────────────────────────────────────────

def save_organ_disclosures(output_dir: str = ".") -> str:
    """Generate JSON for all five organs and save to a file."""
    registry = organ_registry_setup()
    data = {name: disc.to_dict() for name, disc in registry.items()}
    path = Path(output_dir) / "axioma_organ_disclosures.json"
    path.write_text(json.dumps(data, indent=2))
    return str(path)


def save_demo_transcript(output_dir: str = ".") -> str:
    """Generate a demo proof-checking transcript."""
    lines = []
    lines.append("# Proof-Checking Arena — Demo Transcript")
    lines.append("")
    lines.append("## Claim Under Analysis")
    lines.append("")
    lines.append('*"G_N(s) has all zeros on Re(s)=½ for every finite N."*')
    lines.append("")
    lines.append("---")
    lines.append("")

    for ot in OrganType:
        name = ot.value.upper()
        disc = build_organ_disclosure(ot)
        lines.append(f"## {name}")
        lines.append("")
        lines.append(disc.to_declaration())
        lines.append("")
        lines.append(f"**Analysis:**")
        lines.append("")
        lines.append(get_organ_analysis_starter(ot))
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## PNEUMA — Final Verdict")
    lines.append("")
    lines.append(get_verdict("inconclusive_tension"))
    lines.append("")
    lines.append("**Remaining gaps identified:**")
    lines.append("1. Boundary zeros not counted by standard argument principle")
    lines.append("2. Poles at positive integers (from χ(s)) need subtraction from zero count")
    lines.append("3. Top edge contribution is bounded but non-vanishing for finite N")
    lines.append("")
    lines.append("*The proof is structurally sound but has analytical gaps that require further work.*")

    path = Path(output_dir) / "axioma_demo_transcript.md"
    path.write_text("\n".join(lines))
    return str(path)


__all__ = [
    "OrganType",
    "ArchitectureType",
    "EpistemicVirtue",
    "ArchitectureDisclosure",
    "BlindSpot",
    "ORGAN_INTERNAL_WEIGHTS",
    "ORGAN_PERSONALITIES",
    "ORGAN_ARCH_TYPES",
    "ORGAN_STRENGTHS",
    "ORGAN_BLIND_SPOTS",
    "get_organ_internal_weights",
    "get_organ_personality",
    "build_organ_disclosure",
    "organ_registry_setup",
    "get_organ_analysis_starter",
    "get_verdict",
    "save_organ_disclosures",
    "save_demo_transcript",
]
