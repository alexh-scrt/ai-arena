#!/usr/bin/env python3
"""
Proof Arena Demo — Standalone Demo Script

Generates a synthetic transcript of the five AXIOMA proof organs
debating a mathematical claim. Zero external dependencies beyond
the Python standard library and the Arena's core modules.

Usage:
    python scripts/proof_arena_demo.py

Output:
    outputs/proof_arena_demo_transcript.md
"""

import sys
from pathlib import Path
from datetime import datetime

# Ensure we can import from the Arena
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.arena.proof_organs import (
    OrganType,
    build_organ_disclosure,
    get_organ_analysis_starter,
    get_verdict,
    organ_registry_setup,
)


# ── Demo claim ───────────────────────────────────────────────────────

CLAIM = '"The square root of 2 is irrational."'


# ── Simulated organ responses ───────────────────────────────────────

ORGAN_RESPONSES = {
    OrganType.NOUS: (
        "I begin by examining the formal structure of the claim. "
        "Assume for contradiction that √2 = p/q in lowest terms. "
        "Then 2 = p²/q², so p² = 2q². Thus p is even — let p = 2k. "
        "Then (2k)² = 2q² → 4k² = 2q² → q² = 2k². Thus q is also even, "
        "contradicting the assumption that p/q was in lowest terms. "
        "The formal structure is sound. I find no gaps in the logical chain."
    ),
    OrganType.EIDOLON: (
        "I sense structural tension at the boundary of this proof. "
        "The contradiction method is classic — but what if p/q = 0? "
        "No, √2 > 0, so that's fine. What if we're working in a ring "
        "where 2 is not prime? The proof depends on the property that "
        "if p² is even then p is even, which holds in ℤ but not in all "
        "integral domains. Within ℤ, the structure is sound. The only "
        "hidden assumption is that we're working in the integers — which "
        "is the intended domain. I find no fatal structural contradictions."
    ),
    OrganType.MNEME: (
        "This proof has a deep history. It is attributed to the "
        "Pythagorean school, circa 5th century BCE. Legend holds that "
        "Hippasus of Metapontum was drowned at sea for discovering it — "
        "the existence of irrational numbers threatened the Pythagorean "
        "doctrine that 'all is number.' The proof itself is structurally "
        "identical to the one presented here. It has been verified "
        "countless times across 2500 years. No historical counterexample "
        "or successful refutation exists. The weight of history confirms it."
    ),
    OrganType.ANIMA: (
        "This proof feels *right*. There is an elegance to it — "
        "the way it turns in on itself, the way the contradiction "
        "emerges from the very assumption of rationality. It has the "
        "quality of a zen koan: 'If √2 were rational, it would force "
        "both p and q to be even, which is impossible because they were "
        "already reduced.' The beauty is in the self-referential structure. "
        "I sense no epistemic tension. This proof is true."
    ),
    OrganType.PNEUMA: (
        "I integrate the signals from all four organs. NOUS confirms "
        "the formal validity of the proof by contradiction. EIDOLON "
        "finds no hidden structural contradictions within the intended "
        "domain (ℤ). MNEME attests to 2500 years of uninterrupted "
        "verification. ANIMA senses the aesthetic rightness of the "
        "self-referential structure. All four signals converge. "
        "The claim is confirmed: √2 is irrational."
    ),
}


# ── Demo runner ─────────────────────────────────────────────────────

def generate_demo_transcript(output_dir: str = "outputs") -> str:
    """Generate a full demo transcript and save to file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    lines = []
    lines.append("# 🏛️  Proof Arena — AXIOMA Demo Transcript")
    lines.append("")
    lines.append(f"*Generated: {timestamp}*")
    lines.append(f"*Claim under analysis: {CLAIM}*")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Phase 1: Architecture Disclosure")
    lines.append("")
    lines.append("Before the debate begins, each organ discloses its cognitive")
    lines.append("architecture — strengths, blind spots, and internal configuration.")
    lines.append("These disclosures are **truthful by construction**, derived from")
    lines.append("the organ's actual internal agent weights.")
    lines.append("")
    
    # Build disclosure registry
    registry = organ_registry_setup()
    
    for organ_type in OrganType:
        disclosure = build_organ_disclosure(organ_type)
        lines.append(f"### {disclosure.character_name}")
        lines.append("")
        lines.append(disclosure.to_declaration())
        lines.append("")
    
    lines.append("---")
    lines.append("")
    lines.append("## Phase 2: Claim Statement")
    lines.append("")
    lines.append(f"The claim under analysis is presented to the panel:")
    lines.append("")
    lines.append(f"> {CLAIM}")
    lines.append("")
    lines.append("Each organ now applies its cognitive lens to the claim.")
    lines.append("")
    
    # Organ analyses
    for organ_type in OrganType:
        name = organ_type.value.upper()
        lines.append(f"### {name}")
        lines.append("")
        lines.append(f"**Analysis starter:**")
        lines.append("")
        lines.append(f"> {get_organ_analysis_starter(organ_type)}")
        lines.append("")
        lines.append(f"**Response:**")
        lines.append("")
        lines.append(f"> {ORGAN_RESPONSES[organ_type]}")
        lines.append("")
    
    lines.append("---")
    lines.append("")
    lines.append("## Phase 3: Integration & Verdict")
    lines.append("")
    lines.append(f"### PNEUMA — Final Synthesis")
    lines.append("")
    lines.append(f"> {ORGAN_RESPONSES[OrganType.PNEUMA]}")
    lines.append("")
    lines.append(f"**Official verdict:**")
    lines.append("")
    lines.append(f"> {get_verdict('confirmed')}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*Demo complete. To run a live LangGraph debate with actual")
    lines.append("LLM responses, use:*")
    lines.append("")
    lines.append("```bash")
    lines.append('python main.py --panel math_proof --topic "Prove √2 is irrational"')
    lines.append("```")
    
    # Write output
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    transcript_path = output_path / "proof_arena_demo_transcript.md"
    transcript_path.write_text("\n".join(lines))
    
    return str(transcript_path)


# ── Main ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("🏛️  Proof Arena — AXIOMA Demo")
    print("=" * 50)
    print(f"Claim: {CLAIM}")
    print()
    
    path = generate_demo_transcript()
    
    print(f"✅ Demo transcript generated!")
    print(f"📄 {path}")
    print()
    print("Transcript includes:")
    print("  • Architecture Disclosure for all 5 organs")
    print("  • Analysis from NOUS, EIDOLON, MNEME, ANIMA, PNEUMA")
    print("  • Integrated verdict from PNEUMA")
    print()
    print("To view:")
    print(f"  cat {path}")
    print()
    print("For a LIVE LangGraph debate (requires Ollama + qwen3:32b):")
    print('  python main.py --panel math_proof --topic "Prove √2 is irrational"')