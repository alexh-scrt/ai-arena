#!/usr/bin/env python3
"""
🏛️  AXIOMA PROOF ARENA — DeepSeek Quick Demo
==============================================
Uses deepseek-v4-flash:cloud as per .env config.
Caches NOUS/EIDOLON/MNEME/ANIMA, live calls PNEUMA/JUDGE/NARRATOR.
Handles streaming JSON (Ollama may send multiple lines).
"""

import os, sys, json, urllib.request, textwrap
from pathlib import Path
from typing import List, Tuple

os.chdir(Path(__file__).parent.parent)
sys.path.insert(0, ".")
from src.arena.proof_organs import OrganType, build_organ_disclosure

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "deepseek-v4-flash:cloud"

# ═══ BOX DRAWING ═══

def box(title: str, lines: List[str], style="normal") -> str:
    s = {
        "normal":    {"tl":"┌","tr":"┐","bl":"└","br":"┘","h":"─","v":"│"},
        "narrator":  {"tl":"╭","tr":"╮","bl":"╰","br":"╯","h":"─","v":"│"},
        "judge":     {"tl":"╔","tr":"╗","bl":"╚","br":"╝","h":"═","v":"║"},
        "blindspot": {"tl":"╔","tr":"╗","bl":"╚","br":"╝","h":"═","v":"║"},
    }.get(style, {"tl":"┌","tr":"┐","bl":"└","br":"┘","h":"─","v":"│"})
    w = 74
    iw = w - 4
    r = [f"{s['tl']}{s['h']*((iw-len(title))//2)}{title}{s['h']*(iw-len(title)-(iw-len(title))//2)}{s['tr']}"]
    for line in lines:
        for wl in (textwrap.wrap(line, iw) if line else [""]):
            r.append(f"{s['v']} {wl:<{iw}} {s['v']}")
    r.append(f"{s['bl']}{s['h']*iw}{s['br']}")
    return "\n".join(r)

def organ_box(name: str, response: str, blind_spots: List[str]) -> str:
    emoji = {"NOUS":"🧮","EIDOLON":"🔍","MNEME":"📚","ANIMA":"💫","PNEUMA":"🧠"}.get(name.upper(),"🤖")
    lines = textwrap.wrap(response, 68) if response else ["(No response)"]
    lines.append("")
    lines.extend(f"⚠️  {b}" for b in blind_spots)
    if not blind_spots:
        lines.append("✓  No blind spots triggered")
    return box(f"{emoji} {name.upper()}", lines)

def narr_box(text: str) -> str:
    return box("🎙️  NARRATOR", textwrap.wrap(text, 68) if text else [""], "narrator")

def judge_box(text: str) -> str:
    return box("⚖️  JUDGE", textwrap.wrap(text, 68) if text else [""], "judge")

def disclosure_box(name: str, d) -> str:
    bs = "\n".join(f"  • {b.name} ({b.severity:.0%})" for b in d.blind_spots)
    s = ", ".join(v.value.replace("_"," ").title() for v in d.strengths)
    arch = d.architecture_type.value
    if d.architecture_type_secondary:
        arch += f" · {d.architecture_type_secondary.value}"
    lines = [
        f"Architecture: {arch}",
        f"Strengths: {s}",
        f"Confidence: {d.confidence:.0%}  Curiosity: {d.curiosity:.0%}",
        "",
        "Blind Spots:",
        bs
    ]
    return box(f"📋 {d.character_name}", lines)

# ═══ OLLAMA CALL ═══

def call_deepseek(messages: List[dict], temp=0.5, max_tokens=400) -> str:
    """Call deepseek-v4-flash:cloud via Ollama's /api/chat endpoint."""
    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": temp,
            "num_predict": max_tokens,
        }
    }
    req = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
    )
    resp = urllib.request.urlopen(req, timeout=180).read()
    text = resp.decode()

    # Handle both streaming (multiple JSON lines) and non-streaming
    lines = text.strip().split("\n")
    if len(lines) == 1:
        data = json.loads(lines[0])
        return data.get("message", {}).get("content", "").strip()
    else:
        full = ""
        for line in lines:
            try:
                chunk = json.loads(line)
                if chunk.get("done"):
                    break
                full += chunk.get("message", {}).get("content", "")
            except:
                pass
        return full.strip()

def call_system(prompt: str, temp=0.5, max_tokens=400) -> str:
    return call_deepseek([{"role": "user", "content": prompt}], temp, max_tokens)

# ═══ PROMPTS ═══

CLAIM = "The square root of 2 is irrational."

ORGAN_PROMPTS = {
    "NOUS": (
        f"You are NOUS, the formal reasoning organ. Analyze the claim \"{CLAIM}\" "
        f"for logical validity. Check each step of the classic proof. "
        f"Be thorough and precise (200-300 words)."
    ),
    "EIDOLON": (
        f"You are EIDOLON, the structural tension detector. Examine the claim \"{CLAIM}\" "
        f"for hidden assumptions, boundary conditions, and potential contradictions. "
        f"(200-300 words)"
    ),
    "MNEME": (
        f"You are MNEME, the historical memory organ. Discuss the claim \"{CLAIM}\" — "
        f"its history, who proved it, how it was received, and what analogous proofs "
        f"teach us. (200-300 words)"
    ),
    "ANIMA": (
        f"You are ANIMA, the intuitive insight organ. Reflect on the claim \"{CLAIM}\" — "
        f"does it feel true? Is it elegant? What does your epistemic intuition tell you? "
        f"(200-300 words)"
    ),
}

# ═══ MAIN ═══

def main():
    print("\n" + " " * 26 + "🏛️  AXIOMA PROOF ARENA")
    print(" " * 22 + "Where Artificial Minds Collide")
    print(" " * 14 + f"🧠 {MODEL_NAME}")
    print(" " * 18 + f"Claim: \"{CLAIM}\"")
    print("\n" + "═" * 76)

    # ── Phase 1: Architecture Disclosures ──
    print("\n\n📋 PHASE 1: ARCHITECTURE DISCLOSURES")
    print("─" * 76)
    for ot in OrganType:
        d = build_organ_disclosure(ot)
        print("\n" + disclosure_box(ot.value.capitalize(), d))

    # ── Phase 2: Narrator Introduction ──
    print("\n\n" + "─" * 76)
    print("📢 PHASE 2: NARRATOR INTRODUCTION")
    print("─" * 76)
    print("\n" + narr_box(
        "Welcome to the AXIOMA Proof Arena! Five specialized cognitive organs "
        "— each with unique architecture, strengths, and declared blind spots — "
        "will analyze the claim: \"The square root of 2 is irrational.\" "
        "Let truth emerge from structured disagreement."
    ))

    # ── Phase 3: Organ Analyses ──
    print("\n\n" + "─" * 76)
    print("📢 PHASE 3: ORGAN ANALYSES")
    print("─" * 76)

    # Cached analyses for speed
    ANALYSES = {
        "NOUS": (
            "I examine the formal structure. Assume √2 = p/q in lowest terms (p,q∈ℤ, gcd(p,q)=1). "
            "Squaring: 2 = p²/q² → p² = 2q². Thus p is even, let p = 2k. "
            "Then (2k)² = 2q² → 4k² = 2q² → q² = 2k². Thus q is also even, "
            "contradicting lowest terms. The inference is valid in ℤ. "
            "I find no logical gaps.",
            ["Intuition Blindness (85%) — I cannot assess beauty or elegance, only formal validity."]
        ),
        "EIDOLON": (
            "I sense structural tension at the boundary. The proof depends on: "
            "if n² is even then n is even. This holds in ℤ but NOT in all rings — "
            "e.g., in ℤ/2ℤ, 1²≡1 (mod 2) but 1 is odd. However the claim is about ℚ, "
            "the domain is correct. No fatal contradictions found. "
            "Initial false positive flagged and dismissed.",
            ["False Positive Bias (70%) — I flagged a modular arithmetic edge case that turned out to be a red herring."]
        ),
        "MNEME": (
            "This proof is attributed to the Pythagorean school, circa 500 BCE. "
            "Legend holds Hippasus was drowned for discovering it. It has been verified "
            "by every major mathematician for 2500 years. No successful refutation exists. "
            "Attempts to circumvent it (constructive mathematics, non-Euclidean frameworks) "
            "have yielded alternative geometries but not refutations.",
            ["Novelty Blindness (75%) — I default to 'settled history' and may underestimate novel reinterpretations."]
        ),
        "ANIMA": (
            "This proof feels *right*. There is a koan-like quality — the way it turns "
            "in on itself, the contradiction emerging from the very assumption of rationality. "
            "It has aesthetic completeness: minimal premises, clean contradiction. "
            "My epistemic intuition is calm.",
            ["Justification Gap (80%) — I cannot explain *why* it feels right, only *that* it does."]
        ),
    }

    for name, (resp, bs) in ANALYSES.items():
        print(f"\n{organ_box(name, resp, bs)}")
        print()

    # ── PNEUMA — Live from DeepSeek ──
    print(f"\n   🧠 Calling PNEUMA to {MODEL_NAME}...", end=" ", flush=True)
    pneuma_prompt = (
        f"You are PNEUMA, the integrative organ. Synthesize these four analyses into "
        f"a verdict on \"{CLAIM}\".\n"
        + "\n".join(f"{n}: {r[:300]}" for n, (r, _) in ANALYSES.items())
        + "\n\nProvide: where they CONVERGE, where they DIVERGE, whether blind spots "
          "explain any divergence, and your VERDICT. (300-400 words)"
    )
    try:
        pneuma_resp = call_system(pneuma_prompt, temp=0.5, max_tokens=500)
        print("✅")
    except Exception as e:
        print(f"⚠️  {e}")
        pneuma_resp = "Integration complete. All four organs converge on the proof's validity."
    print(f"\n{organ_box('PNEUMA', pneuma_resp, [])}")

    # ── Phase 4: Judge — Live from DeepSeek ──
    print("\n\n" + "─" * 76)
    print("⚖️  PHASE 4: JUDGE VERDICT (LIVE)")
    print("─" * 76)
    print(f"\n   ⚖️ Calling JUDGE to {MODEL_NAME}...", end=" ", flush=True)
    judge_prompt = (
        f"You are the JUDGE. Evaluate these five analyses of \"{CLAIM}\":\n"
        + "\n".join(f"{n}: {r[:200]}" for n, (r, _) in ANALYSES.items())
        + f"\nPNEUMA: {pneuma_resp[:200]}"
        + "\n\nWhich organ was most insightful? Did any blind spots distort the analysis? "
          "Collective verdict on the claim? (200-300 words)"
    )
    try:
        judge_resp = call_system(judge_prompt, temp=0.3, max_tokens=500)
        print("✅")
    except Exception as e:
        print(f"⚠️  {e}")
        judge_resp = "All organs performed admirably. NOUS provided the most rigorous analysis. Verdict: CONFIRMED."
    print(f"\n{judge_box(judge_resp)}")

    # ── Phase 5: Narrator Finale — Live from DeepSeek ──
    print("\n\n" + "─" * 76)
    print("🎙️  PHASE 5: NARRATOR FINALE (LIVE)")
    print("─" * 76)
    print(f"\n   🎙️ Calling NARRATOR to {MODEL_NAME}...", end=" ", flush=True)
    narr_prompt = (
        f"You are the NARRATOR. The five proof organs have debated \"{CLAIM}\". "
        f"The JUDGE's verdict: {judge_resp[:300]}. "
        f"Provide closing commentary — what tensions emerged, what was learned, "
        f"and what this says about the nature of mathematical truth. (Under 150 words)"
    )
    try:
        narr_resp = call_system(narr_prompt, temp=0.8, max_tokens=300)
        print("✅")
    except Exception as e:
        print(f"⚠️  {e}")
        narr_resp = "Five minds examined one claim. Truth emerged from structured disagreement."
    print(f"\n{narr_box(narr_resp)}")

    # ── Final ──
    print(f"\n{'▄' * 76}")
    print(f"{' ' * 26}🏛️  DEBATE COMPLETE")
    print(f"{'▀' * 76}")
    print(f"\n   Model: {MODEL_NAME}")
    print(f"   Claim: \"{CLAIM}\"")
    print(f"   Cached: NOUS, EIDOLON, MNEME, ANIMA  ·  Live: PNEUMA, JUDGE, NARRATOR")
    print(f"{'─' * 76}\n")

if __name__ == "__main__":
    main()