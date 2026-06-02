#!/usr/bin/env python3
"""
Quick Live Proof Arena Demo — one live Ollama call + cached responses for speed.
Run with: python scripts/live_debate_quick.py
"""

import os, sys, json, urllib.request, textwrap
from pathlib import Path

os.chdir(Path(__file__).parent.parent)
sys.path.insert(0, ".")
from src.arena.proof_organs import OrganType, build_organ_disclosure

OLLAMA_URL = "http://localhost:11434/api/generate"

# Cached responses from a previous live run (to keep demo fast)
CACHED = {
    OrganType.NOUS: (
        "I examine the formal structure. Assume √2 = p/q in lowest terms (p,q ∈ ℤ, gcd(p,q)=1). "
        "Squaring: 2 = p²/q² → p² = 2q². Thus p is even, let p = 2k. Then (2k)² = 2q² → 4k² = 2q² → q² = 2k². "
        "Thus q is also even, contradicting lowest terms. The inference is valid in ℤ. "
        "I find no logical gaps. [Blind spot: Intuition Blindness at 85% — I cannot assess whether this proof is 'beautiful' or 'elegant', only whether it is formally sound.]"
    ),
    OrganType.EIDOLON: (
        "I sense structural tension at the boundary. The proof depends on the property: if n² is even then n is even. "
        "This holds in ℤ but NOT in all rings — e.g. in ℤ/2ℤ, 1²=1 which is 'even' (0 mod 2) but 1 is odd. "
        "However, the claim is about ℚ and ℤ, so the domain is correct. No fatal contradictions found. "
        "[Blind spot: False Positive Bias at 70% — I initially flagged the modular arithmetic edge case, but it's a red herring, not a real flaw.]"
    ),
    OrganType.MNEME: (
        "This proof is attributed to the Pythagorean school, circa 500 BCE. Legend holds that Hippasus was drowned for discovering it. "
        "The proof has been verified by every major mathematician for 2500 years. No successful refutation exists. "
        "Attempts to circumvent it (constructive mathematics, non-Euclidean frameworks) have yielded alternative geometries but not refutations. "
        "[Blind spot: Novelty Blindness at 75% — I default to 'this is settled history' and may underestimate genuinely novel reinterpretations.]"
    ),
    OrganType.ANIMA: (
        "This proof feels *right*. There is a koan-like quality to it — the way it turns in on itself, the contradiction emerging from the very assumption of rationality. "
        "It has aesthetic completeness: the argument is minimal, every premise is necessary, the contradiction is clean. "
        "My epistemic intuition is calm. [Blind spot: Justification Gap at 80% — I cannot explain WHY it feels right, only THAT it does.]"
    ),
}

def call_ollama_live(prompt: str, timeout: int = 120) -> str:
    """Make a live Ollama call."""
    payload = {
        "model": "qwen3:32b",
        "prompt": prompt,
        "stream": False,
        "temperature": 0.7,
        "max_tokens": 300,
    }
    req = urllib.request.Request(
        OLLAMA_URL, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}
    )
    resp = urllib.request.urlopen(req, timeout=timeout)
    return json.loads(resp.read()).get("response", "").strip()

def demonstrate():
    claim = "The square root of 2 is irrational."
    
    print("=" * 70)
    print("🏛️  AXIOMA LIVE PROOF ARENA — DEMO")
    print(f"🤖 Model: qwen3:32b")
    print(f"🔍 Claim: {claim}")
    print("=" * 70)
    
    # Architecture Disclosures
    print("\n📋 ARCHITECTURE DISCLOSURES")
    print("─" * 70)
    for ot in OrganType:
        disc = build_organ_disclosure(ot)
        name = disc.character_name
        bs = ", ".join(f"{b.name} ({b.severity:.0%})" for b in disc.blind_spots)
        print(f"  {name:10s} | {disc.architecture_type.value:15s} | Blind spots: {bs}")
    print()
    
    # Organ analyses (cached for speed)
    for ot in OrganType:
        if ot == OrganType.PNEUMA:
            continue  # PNEUMA comes last
        name = ot.value.upper()
        print(f"\n📢 {name}")
        print("─" * 70)
        response = CACHED[ot]
        wrapped = textwrap.fill(response, width=66)
        for line in wrapped.split('\n'):
            print(f"   {line}")
    
    # PNEUMA Integration — live call
    print(f"\n🧠 PNEUMA — INTEGRATION (LIVE)")
    print("─" * 70)
    
    integration_prompt = (
        f"You are PNEUMA, the integrative organ of AXIOMA. Synthesize these four analyses.\n\n"
        f"NOUS: {CACHED[OrganType.NOUS][:400]}\n\n"
        f"EIDOLON: {CACHED[OrganType.EIDOLON][:400]}\n\n"
        f"MNEME: {CACHED[OrganType.MNEME][:400]}\n\n"
        f"ANIMA: {CACHED[OrganType.ANIMA][:400]}\n\n"
        f"Provide: where they CONVERGE, where they DIVERGE, whether blind spots explain any divergence, and your VERDICT."
    )
    
    print("   Calling qwen3:32b...", end=" ", flush=True)
    try:
        verdict = call_ollama_live(integration_prompt)
        print("✅\n")
        wrapped = textwrap.fill(verdict, width=66)
        for line in wrapped.split('\n'):
            print(f"   {line}")
    except Exception as e:
        print(f"❌ Error: {e}")
        verdict = (
            "Integration complete. All four organs converge: NOUS confirms formal validity, "
            "EIDOLON finds no structural contradictions within the domain, MNEME attests to 2500 years of verification, "
            "and ANIMA senses the proof is sound. "
            "Divergence is minimal — EIDOLON's initial concern about modular arithmetic was a false positive (its blind spot). "
            "VERDICT: Confirmed. √2 is irrational."
        )
        print(f"\n   {textwrap.fill(verdict, width=66)}")
    
    print(f"\n{'=' * 70}")
    print("🏛️  DEBATE COMPLETE")
    print(f"{'=' * 70}")
    print("\nTo run with full live LLM calls: python scripts/live_proof_debate.py")

if __name__ == "__main__":
    demonstrate()