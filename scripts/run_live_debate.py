#!/usr/bin/env python3
"""
🏛️  Live AXIOMA Proof Arena — one-organ demo.
Run: python scripts/run_live_debate.py
First call takes ~45-60s as qwen3:32b loads into GPU memory.
"""

import os, sys, json, urllib.request, textwrap
from pathlib import Path

os.chdir(Path(__file__).parent.parent)
sys.path.insert(0, ".")
from src.arena.proof_organs import OrganType, build_organ_disclosure

OLLAMA_URL = "http://localhost:11434/api/generate"

def call(prompt: str, timeout: int = 120) -> str:
    payload = {"model": "qwen3:32b", "prompt": prompt, "stream": False, "temperature": 0.7, "max_tokens": 300}
    req = urllib.request.Request(OLLAMA_URL, data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
    resp = urllib.request.urlopen(req, timeout=timeout)
    return json.loads(resp.read()).get("response", "").strip()

def main():
    print("=" * 70)
    print("🏛️  AXIOMA LIVE PROOF ARENA")
    print("🤖 qwen3:32b · One live organ call (rest cached)")
    print("=" * 70)
    
    # Show all disclosures
    print("\n📋 ARCHITECTURE DISCLOSURES:")
    for ot in OrganType:
        d = build_organ_disclosure(ot)
        bs = ", ".join(f"{b.name} ({b.severity:.0%})" for b in d.blind_spots)
        print(f"  {d.character_name:10s} | {d.architecture_type.value:15s} | {bs}")
    
    # Cached analyses
    analyses = {
        "NOUS": "Formal proof by contradiction: assume √2 = p/q in lowest terms, derive p² = 2q² → p even → q even → contradiction. Logically valid. [Blind spot: Intuition Blindness 85%]",
        "EIDOLON": "Structural boundary check: proof depends on 'if n² even then n even' which holds in ℤ. No hidden contradictions. [Blind spot: False Positive Bias 70% — briefly flagged ℤ/2ℤ, but it's a red herring.]",
        "MNEME": "Pythagorean school, ~500 BCE. Hippasus drowned. Verified for 2500 years. No refutations. [Blind spot: Novelty Blindness 75%]",
        "ANIMA": "Feels right. Koan-like self-reference. Minimal, clean, necessary. [Blind spot: Justification Gap 80% — cannot explain why, only that it does.]",
    }
    
    for name, analysis in analyses.items():
        print(f"\n📢 {name}")
        print("─" * 70)
        for line in textwrap.fill(analysis, width=66).split('\n'):
            print(f"   {line}")
    
    # PNEUMA — live integration
    print(f"\n🧠 PNEUMA — LIVE INTEGRATION (generating...)", end=" ", flush=True)
    try:
        prompt = (
            "You are PNEUMA, the integrative organ. Synthesize these analyses into a verdict.\n"
            f"NOUS: {analyses['NOUS']}\n"
            f"EIDOLON: {analyses['EIDOLON']}\n"
            f"MNEME: {analyses['MNEME']}\n"
            f"ANIMA: {analyses['ANIMA']}\n"
            "Provide convergences, divergences, blind spot effects, and your verdict."
        )
        verdict = call(prompt)
        print("✅\n")
        for line in textwrap.fill(verdict, width=66).split('\n'):
            print(f"   {line}")
    except Exception as e:
        print(f"⚠️  {e}")
    
    print(f"\n{'=' * 70}")
    print("🏛️  DEBATE COMPLETE")
    print(f"{'=' * 70}")

if __name__ == "__main__":
    main()