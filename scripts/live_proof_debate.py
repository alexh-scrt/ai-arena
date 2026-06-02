#!/usr/bin/env python3
"""
Live Proof Arena — AXIOMA organs debate a claim using Ollama qwen3:32b.

Each organ generates its analysis using a real LLM call, with its
architecture disclosure and internal agent weights shaping the prompt.
"""

import os, sys, json, urllib.request, textwrap
from pathlib import Path

# Ensure we're in the project root
os.chdir(Path(__file__).parent.parent)
sys.path.insert(0, ".")

from src.arena.proof_organs import (
    OrganType, build_organ_disclosure, get_organ_analysis_starter
)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3:32b"

def call_ollama(prompt: str, system: str = "") -> str:
    """Call Ollama and return the response text."""
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "system": system,
        "stream": False,
        "temperature": 0.7,
        "max_tokens": 500,
    }
    req = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}
    )
    resp = urllib.request.urlopen(req, timeout=60)
    data = json.loads(resp.read())
    return data.get("response", "").strip()

def organ_prompt(organ_type: OrganType, claim: str) -> str:
    """Build a prompt for a specific organ."""
    disclosure = build_organ_disclosure(organ_type)
    starter = get_organ_analysis_starter(organ_type)
    
    blind_spots_desc = "\n".join(
        f"  - {bs.name} ({bs.severity:.0%} severity): {bs.description}"
        for bs in disclosure.blind_spots
    )
    
    prompt = f"""You are {disclosure.character_name}, an AI proof-checking organ.

ARCHITECTURE DISCLOSURE:
- Primary: {disclosure.architecture_type.value}
- Strengths: {', '.join(s.value for s in disclosure.strengths)}
- Blind spots:
{blind_spots_desc}

CLAIM UNDER ANALYSIS:
"{claim}"

YOUR ANALYSIS:
{starter}

Please provide your full analysis of this claim. Be honest about what you can and cannot determine. If you hit a blind spot, acknowledge it explicitly."""
    return prompt

def run_debate(claim: str):
    """Run a live debate with all five organs."""
    print("=" * 70)
    print("🏛️  LIVE PROOF ARENA — AXIOMA ORGANS DEBATE")
    print(f"🔍 Claim: {claim}")
    print(f"🤖 Model: {MODEL}")
    print("=" * 70)
    
    responses = {}
    
    for ot in OrganType:
        name = ot.value.upper()
        print(f"\n{'─' * 70}")
        print(f"📢 {name}")
        print(f"{'─' * 70}")
        
        prompt = organ_prompt(ot, claim)
        print(f"   Generating...", end=" ", flush=True)
        
        try:
            response = call_ollama(prompt)
            responses[ot] = response
            print("✅")
            
            # Print wrapped response
            wrapped = textwrap.fill(response, width=66)
            for line in wrapped.split('\n'):
                print(f"   {line}")
        except Exception as e:
            print(f"❌ Error: {e}")
            responses[ot] = f"[ERROR: {e}]"
    
    # PNEUMA integration
    print(f"\n{'═' * 70}")
    print("🧠 PNEUMA — INTEGRATION & VERDICT")
    print(f"{'═' * 70}")
    
    integration_prompt = f"""You are PNEUMA, the integrative organ of AXIOMA. Your role is to synthesize the analyses of the four other organs into a unified verdict.

NOUS (formal analysis) says:
{responses.get(OrganType.NOUS, '[no response]')[:500]}

EIDOLON (structural tension) says:
{responses.get(OrganType.EIDOLON, '[no response]')[:500]}

MNEME (historical patterns) says:
{responses.get(OrganType.MNEME, '[no response]')[:500]}

ANIMA (intuitive insight) says:
{responses.get(OrganType.ANIMA, '[no response]')[:500]}

ARCHITECTURE DISCLOSURE:
You have Input Dependency (90% severity) — you cannot generate original insights.
You have Over-Synthesis (60% severity) — you may force coherence where there is genuine conflict.

Please provide:
1. Where the four organs CONVERGE
2. Where they DIVERGE
3. Whether the divergence is due to blind spots (name which)
4. Your VERDICT: Confirmed / Rejected / Inconclusive with gaps identified

Be honest about uncertainties."""
    
    print("   Integrating...", end=" ", flush=True)
    try:
        verdict = call_ollama(integration_prompt)
        print("✅\n")
        wrapped = textwrap.fill(verdict, width=66)
        for line in wrapped.split('\n'):
            print(f"   {line}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print(f"\n{'=' * 70}")
    print("🏛️  DEBATE COMPLETE")
    print(f"{'=' * 70}")

if __name__ == "__main__":
    import sys
    claim = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "The square root of 2 is irrational."
    run_debate(claim)