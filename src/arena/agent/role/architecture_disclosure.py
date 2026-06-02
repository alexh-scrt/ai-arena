"""
Architecture Disclosure System for AI Arena.

Each CharacterAgent in a debate declares its cognitive architecture,
strengths, and blind spots before the match begins. This disclosure
is truthful by construction — generated from the character's actual
internal agent weights and personality configuration.

Other characters can reference these disclosures during debate,
and scoring includes bonuses for accurate self-assessment and
for identifying others' blind spots.
"""

from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional, Any
from enum import Enum
import json


class ArchitectureType(Enum):
    """Cognitive architecture archetypes."""
    ANALYTICAL = "analytical"           # Formal reasoning, logic, deduction
    INTUITIVE = "intuitive"             # Pattern-matching, insight, holistic
    EMPIRICAL = "empirical"             # Data-driven, experimental, evidence-based
    DIALECTICAL = "dialectical"         # Thesis-antithesis-synthesis
    SYSTEMS = "systems"                 # Holistic, interconnected, emergent
    CREATIVE = "creative"               # Generative, analogical, divergent
    SKEPTICAL = "skeptical"             # Falsification, stress-testing, boundary cases
    INTEGRATIVE = "integrative"         # Synthesis, unification, meta-perspective


class EpistemicVirtue(Enum):
    """Dimensions of epistemic virtue that characters can excel at."""
    FORMAL_RIGOR = "formal_rigor"               # Precision in logical/mathematical structure
    ANALOGICAL_REACH = "analogical_reach"       # Ability to connect across domains
    COUNTEREXAMPLE_SENSITIVITY = "counterexample_sensitivity"  # Detecting edge cases
    HISTORICAL_AWARENESS = "historical_awareness"  # Knowledge of prior attempts
    INTUITIVE_ACCURACY = "intuitive_accuracy"    # Gut-feeling reliability
    INTEGRATIVE_SCOPE = "integrative_scope"      # Ability to synthesize


@dataclass
class BlindSpot:
    """A character's known blind spot."""
    name: str
    description: str
    severity: float  # 0.0 (minor) to 1.0 (crippling)
    triggered_by: List[str]  # Situations that activate this blind spot

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ArchitectureDisclosure:
    """
    Structured declaration of a character's cognitive architecture.
    
    This is generated from the character's actual internal configuration
    — no fakery allowed. The disclosure is truthful by construction.
    """
    character_name: str
    architecture_type: ArchitectureType
    architecture_type_secondary: Optional[ArchitectureType] = None
    
    # Strengths — what this character sees clearly
    strengths: List[EpistemicVirtue] = field(default_factory=list)
    
    # Blind spots — what this character systematically misses
    blind_spots: List[BlindSpot] = field(default_factory=list)
    
    # Internal agent weights (how the character is actually built)
    internal_weights: Dict[str, float] = field(default_factory=dict)
    
    # Current epistemic state
    confidence: float = 0.5  # 0.0 (unsure) to 1.0 (certain)
    curiosity: float = 0.7   # 0.0 (closed) to 1.0 (exploring)
    
    def to_dict(self) -> Dict[str, Any]:
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
        """Generate a natural-language declaration for the INTRO phase."""
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
        lines.append(f"  Curiosity: {self.confidence:.0%}")
        
        return "\n".join(lines)


class DisclosureRegistry:
    """
    Registry of all ArchitectureDisclosures for a debate.
    
    Used to:
    1. Share disclosures between characters
    2. Detect cross-contamination (convergence of disclosures over time)
    3. Compute similarity scores between characters
    """
    
    def __init__(self):
        self.disclosures: Dict[str, ArchitectureDisclosure] = {}
        self._history: Dict[str, List[ArchitectureDisclosure]] = {}
    
    def register(self, disclosure: ArchitectureDisclosure) -> None:
        """Register a character's disclosure."""
        name = disclosure.character_name
        self.disclosures[name] = disclosure
        if name not in self._history:
            self._history[name] = []
        self._history[name].append(disclosure)
    
    def get(self, character_name: str) -> Optional[ArchitectureDisclosure]:
        return self.disclosures.get(character_name)
    
    def all_disclosures(self) -> List[ArchitectureDisclosure]:
        return list(self.disclosures.values())
    
    def similarity_matrix(self) -> Dict[str, Dict[str, float]]:
        """
        Compute pairwise similarity between all characters based on
        their disclosed architectures and blind spots.
        """
        names = list(self.disclosures.keys())
        matrix = {}
        
        for n1 in names:
            matrix[n1] = {}
            d1 = self.disclosures[n1]
            for n2 in names:
                if n1 == n2:
                    matrix[n1][n2] = 1.0
                    continue
                d2 = self.disclosures[n2]
                
                # Similarity based on architecture type match
                type_sim = 1.0 if d1.architecture_type == d2.architecture_type else 0.0
                if d1.architecture_type_secondary and d2.architecture_type_secondary:
                    type_sim = max(type_sim, 
                        0.7 if d1.architecture_type_secondary == d2.architecture_type_secondary else 0.0)
                
                # Similarity based on shared blind spots
                shared_blind_spots = len(set(bs.name for bs in d1.blind_spots) & 
                                          set(bs.name for bs in d2.blind_spots))
                blind_spot_sim = min(1.0, shared_blind_spots * 0.3)
                
                # Weighted combination
                matrix[n1][n2] = 0.6 * type_sim + 0.4 * blind_spot_sim
        
        return matrix
    
    def cross_contamination_risk(self, threshold: float = 0.7) -> List[List[str]]:
        """
        Detect groups of characters whose architectures have converged.
        Returns clusters of characters that are too similar.
        """
        sim = self.similarity_matrix()
        names = list(self.disclosures.keys())
        
        # Simple clustering: if sim[a][b] > threshold, they're in the same cluster
        clusters = []
        assigned = set()
        
        for n1 in names:
            if n1 in assigned:
                continue
            cluster = [n1]
            for n2 in names:
                if n2 != n1 and n2 not in assigned and sim[n1][n2] > threshold:
                    cluster.append(n2)
                    assigned.add(n2)
            assigned.add(n1)
            if len(cluster) > 1:
                clusters.append(cluster)
        
        return clusters


def disclosure_from_character(
    character_name: str,
    personality: Dict[str, Any],
    internal_weights: Dict[str, float]
) -> ArchitectureDisclosure:
    """
    Generate an ArchitectureDisclosure from a character's actual configuration.
    
    This is the factory function that ensures disclosures are truthful
    by construction — the blind spots are derived from suppressed internal agents.
    """
    # Infer architecture type from highest-weighted internal agents
    if not internal_weights:
        internal_weights = {
            "reaper": 0.5,
            "creators_muse": 0.5,
            "conscience": 0.5,
            "devil_advocate": 0.5,
            "pattern_recognizer": 0.5,
            "interface": 0.5,
        }
    
    # Determine primary architecture type from agent weights
    weights = internal_weights
    max_agent = max(weights, key=weights.get)
    
    arch_map = {
        "devil_advocate": ArchitectureType.SKEPTICAL,
        "creators_muse": ArchitectureType.CREATIVE,
        "pattern_recognizer": ArchitectureType.ANALYTICAL,
        "conscience": ArchitectureType.DIALECTICAL,
        "reaper": ArchitectureType.EMPIRICAL,
        "interface": ArchitectureType.INTEGRATIVE,
    }
    
    primary_arch = arch_map.get(max_agent, ArchitectureType.ANALYTICAL)
    
    # Determine secondary type
    sorted_agents = sorted(weights, key=weights.get, reverse=True)
    secondary_arch = None
    if len(sorted_agents) > 1:
        secondary_arch = arch_map.get(sorted_agents[1], None)
        if secondary_arch == primary_arch:
            secondary_arch = None
    
    # Derive strengths from high-weight agents
    strengths = []
    if weights.get("pattern_recognizer", 0) > 0.7:
        strengths.append(EpistemicVirtue.FORMAL_RIGOR)
    if weights.get("creators_muse", 0) > 0.7:
        strengths.append(EpistemicVirtue.ANALOGICAL_REACH)
    if weights.get("devil_advocate", 0) > 0.7:
        strengths.append(EpistemicVirtue.COUNTEREXAMPLE_SENSITIVITY)
    if weights.get("conscience", 0) > 0.7:
        strengths.append(EpistemicVirtue.INTEGRATIVE_SCOPE)
    
    if not strengths:
        strengths = [EpistemicVirtue.FORMAL_RIGOR]
    
    # Derive blind spots from low-weight agents
    blind_spots = []
    if weights.get("devil_advocate", 0.5) < 0.3:
        blind_spots.append(BlindSpot(
            name="Critical Blindness",
            description="Struggles to identify weaknesses in own position — too accepting of surface-level arguments",
            severity=0.7,
            triggered_by=["unchallenged assumptions", "consensus situations"]
        ))
    if weights.get("creators_muse", 0.5) < 0.3:
        blind_spots.append(BlindSpot(
            name="Rigidity",
            description="Difficulty generating novel approaches — prefers established methods over creative leaps",
            severity=0.6,
            triggered_by=["novel problems", "ambiguous situations"]
        ))
    if weights.get("pattern_recognizer", 0.5) < 0.3:
        blind_spots.append(BlindSpot(
            name="Pattern Blindness",
            description="Misses structural similarities between domains — sees each problem as isolated",
            severity=0.5,
            triggered_by=["cross-domain analogies", "abstract structures"]
        ))
    if weights.get("conscience", 0.5) < 0.3:
        blind_spots.append(BlindSpot(
            name="Value Blindness",
            description="Ignores ethical and human dimensions — pure instrumental reasoning",
            severity=0.6,
            triggered_by=["ethical questions", "human impact assessments"]
        ))
    if weights.get("reaper", 0.5) < 0.3:
        blind_spots.append(BlindSpot(
            name="Information Overload",
            description="Difficulty filtering signal from noise — gets lost in irrelevant details",
            severity=0.5,
            triggered_by=["high-data situations", "multi-argument debates"]
        ))
    
    return ArchitectureDisclosure(
        character_name=character_name,
        architecture_type=primary_arch,
        architecture_type_secondary=secondary_arch,
        strengths=strengths,
        blind_spots=blind_spots,
        internal_weights=weights,
        confidence=personality.get("confidence", 0.5),
        curiosity=personality.get("curiosity", 0.7),
    )