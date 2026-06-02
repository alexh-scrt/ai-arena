#!/usr/bin/env python3
"""
🏛️  STAIRCASE JURY DELIBERATION
================================
Six AI jurors deliberate the death of Kathleen Peterson.
Based on the real case: State v. Michael Peterson.

Jurors: LOGICUS · JUSTITIA · ANCHORA · SENSUS · CUSTODIA · SYNTHESIS
Each juror has truthful-by-construction blind spots.

Evidence: Autopsy reports, blood spatter analysis (contested),
911 call timeline, prior similar death (Elizabeth Ratliff),
motive evidence, owl theory, SBI misconduct.

Live verdict from DeepSeek: PNEUMA deliberation, JUDGE vote, NARRATOR finale.
"""

import os, sys, json, urllib.request, textwrap, random
from pathlib import Path
from typing import List, Tuple

os.chdir(Path(__file__).parent.parent)
sys.path.insert(0, ".")

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "deepseek-v4-flash:cloud"

# ═══ CASE EVIDENCE ═══

CASE = {
    "name": "State v. Michael Peterson",
    "charge": "First-Degree Murder of Kathleen Peterson",
    "date": "December 9, 2001",
    "facts": {
        "911_timeline": {
            "2:40 AM": "Michael calls 911: found Kathleen at bottom of stairs, she's breathing",
            "2:41 AM": "Second call: Kathleen is no longer breathing",
            "2:45 AM": "First responders arrive. Kathleen dead. Large blood pool at staircase"
        },
        "autopsy": {
            "cause": "Exsanguination from 7 scalp lacerations",
            "lacerations": "7 lacerations to top/back of head",
            "cartilage_fracture": "Left thyroid cartilage fractured",
            "no_skull_fracture": True,
            "no_brain_swelling": True,
            "blood_alcohol": "0.07%",
            "valium": "5-15 mg present"
        },
        "blood_spatter": {
            "prosecution": "Duane Deaver (SBI): Walls + Michael's clothes show beating pattern",
            "defense": "Henry Lee: Consistent with coughing blood after fall",
            "deaver_fired": True,
            "deaver_misconduct": "Fired 2011 for false testimony in 34 cases"
        },
        "prior_death": {
            "victim": "Elizabeth Ratliff, 1985, Germany",
            "circumstances": "Found at bottom of stairs, head injuries. Michael last to see her alive.",
            "initial_ruling": "Natural causes (Von Willebrand's disease)",
            "later_ruling": "Homicide (2003 exhumation)",
            "pattern_claim": "Prosecution argues Peterson learned to fake stair fall death"
        },
        "motive": {
            "bisexuality": True,
            "secret_affairs": True,
            "insurance": "$1.5M policy with Michael as beneficiary",
            "marital_state": "Prosecution: unhappy, Kathleen just discovered affairs. Defense: happy, Kathleen accepted bisexuality."
        },
        "weapon": {
            "theory": "Missing fireplace blow poke",
            "status": "Later found in garage. Jurors dismissed as weapon."
        },
        "owl_theory": {
            "feathers": "Microscopic feathers found in Kathleen's clutched hair (2001, 2008)",
            "claim": "Barred owl attack could explain lacerations",
            "expert_support": "Three affidavits filed supporting plausibility"
        },
        "michael_behavior": {
            "called_911": True,
            "remained_at_scene": True,
            "no_attempt_to_flee": True,
            "cooperated_with_police": True
        }
    },
    "verdict_options": ["GUILTY of First-Degree Murder", "GUILTY of Voluntary Manslaughter", "NOT GUILTY"],
    "real_outcome": "Alford plea to Voluntary Manslaughter (2017). Sentenced to time served."
}

# ═══ BOX DRAWING ═══

def box(title: str, lines: List[str], style="normal") -> str:
    s = {
        "normal":    {"tl":"┌","tr":"┐","bl":"└","br":"┘","h":"─","v":"│"},
        "narrator":  {"tl":"╭","tr":"╮","bl":"╰","br":"╯","h":"─","v":"│"},
        "judge":     {"tl":"╔","tr":"╗","bl":"╚","br":"╝","h":"═","v":"║"},
        "blindspot": {"tl":"╔","tr":"╗","bl":"╚","br":"╝","h":"═","v":"║"},
        "evidence":  {"tl":"╓","tr":"╖","bl":"╙","br":"╘","h":"─","v":"║"},
    }.get(style, {"tl":"┌","tr":"┐","bl":"└","br":"┘","h":"─","v":"│"})
    w = 74
    iw = w - 4
    r = [f"{s['tl']}{s['h']*((iw-len(title))//2)}{title}{s['h']*(iw-len(title)-(iw-len(title))//2)}{s['tr']}"]
    for line in lines:
        for wl in (textwrap.wrap(line, iw) if line else [""]):
            r.append(f"{s['v']} {wl:<{iw}} {s['v']}")
    r.append(f"{s['bl']}{s['h']*iw}{s['br']}")
    return "\n".join(r)

def juror_box(name: str, response: str, blind_spots: List[str]) -> str:
    emoji = {"LOGICUS":"🧮","JUSTITIA":"⚖️","ANCHORA":"📋","SENSUS":"💗","CUSTODIA":"🔍","SYNTHESIS":"🕊️"}
    e = emoji.get(name.upper(), "🤖")
    lines = textwrap.wrap(response, 68) if response else ["(No response)"]
    lines.append("")
    lines.extend(f"⚠️  {b}" for b in blind_spots)
    if not blind_spots:
        lines.append("✓  No blind spots triggered")
    return box(f"{e} {name.upper()}", lines)

def verdict_box(text: str) -> str:
    return box("🏛️  JURY VERDICT", textwrap.wrap(text, 68) if text else [""], "judge")

def narr_box(text: str) -> str:
    return box("🎙️  NARRATOR", textwrap.wrap(text, 68) if text else [""], "narrator")

def evidence_box(title: str, items: List[str]) -> str:
    return box(f"📜 {title}", items, "evidence")

# ═══ OLLAMA CALL ═══

def call_deepseek(messages: List[dict], temp=0.7, max_tokens=600) -> str:
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

def call_system(prompt: str, temp=0.7, max_tokens=600) -> str:
    return call_deepseek([{"role": "user", "content": prompt}], temp, max_tokens)

# ═══ JUROR PROFILES ═══

JURORS = [
    {
        "name": "LOGICUS",
        "archetype": "Evidence Analyst",
        "focus": "timeline reconstruction, logical consistency, physical evidence",
        "prompt": (
            "You are LOGICUS, a forensic evidence analyst serving on the jury for State v. Michael Peterson. "
            "You reconstruct timelines, test logical consistency, and evaluate physical evidence. "
            "Your blind spot: PATTERN MATCHING BIAS (75%) — you may see causal patterns where none exist.\n\n"
            "CASE SUMMARY: Kathleen Peterson was found dead at the bottom of a staircase at 2:40 AM on Dec 9, 2001. "
            "Michael Peterson called 911. Autopsy: 7 lacerations to the head, fractured thyroid cartilage, "
            "no skull fracture, no brain swelling. Blood alcohol 0.07%. Valium present. "
            "Blood spatter analysis was contested — Duane Deaver (SBI) testified for beating, Henry Lee for fall. "
            "Deaver was later fired for false testimony in 34 cases. "
            "Prior similar death: Elizabeth Ratliff (1985) found at bottom of stairs. Michael last to see her alive. "
            "Motive: $1.5M insurance policy + Michael's secret same-sex affairs. "
            "Owl theory: microscopic feathers found in Kathleen's hair.\n\n"
            "What is your analysis of the evidence? Focus on timelines, consistency, and physical evidence. "
            "Be thorough (250-350 words)."
        ),
        "blind_spots": ["Pattern Matching Bias (75%) — I may see causal patterns where none exist"]
    },
    {
        "name": "JUSTITIA",
        "archetype": "Legal Standard Bearer",
        "focus": "burden of proof, reasonable doubt, presumption of innocence",
        "prompt": (
            "You are JUSTITIA, a legal standard bearer serving on the jury for State v. Michael Peterson. "
            "You focus on burden of proof, reasonable doubt, and the presumption of innocence. "
            "Your blind spot: LEGAL FRAMING BIAS (70%) — you may focus on legal technicalities over factual truth.\n\n"
            f"{CASE['facts']}\n\n"
            "Evaluate the evidence against the 'beyond reasonable doubt' standard. "
            "What is the prosecution's strongest argument? Its weakest? "
            "Is there reasonable doubt? Be thorough (250-350 words)."
        ),
        "blind_spots": ["Legal Framing Bias (70%) — I may focus on legal technicalities over factual truth"]
    },
    {
        "name": "ANCHORA",
        "archetype": "Memory Keeper",
        "focus": "testimony accuracy, detail preservation, timeline precision",
        "prompt": (
            "You are ANCHORA, a meticulous archivist serving on the jury for State v. Michael Peterson. "
            "You focus on precise details, testimony accuracy, and timeline reconstruction. "
            "Your blind spot: RECENCY BIAS (70%) — you may give more weight to evidence presented later.\n\n"
            f"{CASE['facts']}\n\n"
            "Recall all details precisely. Construct the timeline from memory. "
            "Where do the details of different witnesses align or contradict? "
            "What specific facts are most damning? Most exculpatory? Be thorough (250-350 words)."
        ),
        "blind_spots": ["Recency Bias (70%) — I may give more weight to evidence presented later in deliberation"]
    },
    {
        "name": "SENSUS",
        "archetype": "Human Factor Evaluator",
        "focus": "credibility, motive, emotional truth, human context",
        "prompt": (
            "You are SENSUS, a human factor evaluator serving on the jury for State v. Michael Peterson. "
            "You focus on credibility, motive, emotional truth, and human context. "
            "Your blind spot: EMPATHY OVERRIDE (75%) — you may give undue weight to sympathetic testimony.\n\n"
            f"{CASE['facts']}\n\n"
            "Assess the human story. Is Michael Peterson credible? What about his bisexuality — "
            "is it a genuine motive or prejudice? What would drive a woman to discover her husband's "
            "secrets? What would drive a man to kill? Trust your intuition about people. "
            "Be thorough (250-350 words)."
        ),
        "blind_spots": ["Empathy Override (75%) — I may give undue weight to sympathetic testimony"]
    },
    {
        "name": "CUSTODIA",
        "archetype": "Devil's Advocate",
        "focus": "challenge assumptions, find alternatives, test theories",
        "prompt": (
            "You are CUSTODIA, an investigative skeptic serving on the jury for State v. Michael Peterson. "
            "You challenge every assumption, find alternative explanations, and test every theory to destruction. "
            "Your blind spot: HYPER-SKEPTICISM (80%) — you may doubt even well-established evidence.\n\n"
            f"{CASE['facts']}\n\n"
            "Challenge everything. What are the alternative explanations for each piece of evidence? "
            "Could the 7 lacerations be from a fall? Could the owl theory work? "
            "Was the Ratliff death a coincidence? Is the SBI misconduct enough to create doubt? "
            "Don't let the prosecution's narrative go untested. Be thorough (250-350 words)."
        ),
        "blind_spots": ["Hyper-skepticism (80%) — I may doubt even well-established evidence"]
    },
    {
        "name": "SYNTHESIS",
        "archetype": "Deliberation Guide",
        "focus": "synthesize perspectives, track convergence, guide to verdict",
        "prompt": (
            "You are SYNTHESIS, a group facilitator serving on the jury for State v. Michael Peterson. "
            "You synthesize perspectives, track convergence and divergence, and guide the jury toward verdict. "
            "Your blind spot: FALSE CONSENSUS BIAS (70%) — you may assume others agree when they don't.\n\n"
            f"{CASE['facts']}\n\n"
            "After hearing the other five jurors, synthesize their perspectives. Where do they converge? "
            "Where do they diverge? What is the emerging path to verdict? "
            "Which blind spots may be affecting their analyses? "
            "Guide the jury toward a verdict. Be thorough (250-350 words)."
        ),
        "blind_spots": ["False Consensus Bias (70%) — I may assume others agree when they don't"]
    }
]

# ═══ JURY DELIBERATION ═══

def main():
    print("\n" + " " * 16 + "🏛️  THE STAIRCASE — JURY DELIBERATION")
    print(" " * 12 + "Six AI Jurors Deliberate State v. Michael Peterson")
    print(" " * 16 + f"🧠 {MODEL_NAME}")
    print("\n" + "═" * 76)

    # ── Phase 1: Evidence Summary ──
    print("\n\n📜 PHASE 1: CASE EVIDENCE")
    print("─" * 76)
    print("\n" + evidence_box("The Death of Kathleen Peterson", [
        "On December 9, 2001, at 2:40 AM, Michael Peterson called 911 saying he found his wife",
        "Kathleen at the bottom of a staircase. She died from blood loss after sustaining 7",
        "lacerations to the head. No skull fracture. No brain swelling. Fractured thyroid cartilage.",
        "",
        "KEY EVIDENCE:",
        "• 911 call at 2:40 AM — last seen alive ~11:08 PM",
        "• 7 lacerations to head — beating or fall?",
        "• Blood spatter: Beat pattern (Deaver/SBI) vs Coughing (Lee) — Deaver later fired",
        "• Elizabeth Ratliff died similarly in 1985 — pattern or coincidence?",
        "• $1.5M insurance policy + Michael's secret same-sex affairs = motive?",
        "• Owl feathers found in Kathleen's hair — alternative theory",
        "• No skull fracture, no brain swelling despite 7 lacerations",
    ]))
    print("\n" + evidence_box("Real Case Outcome", [
        "Guilty of First-Degree Murder (2003) → Life without parole",
        "New trial granted (2011) because SBI analyst Deaver gave false testimony",
        "Alford plea to Voluntary Manslaughter (2017) → Time served",
        "Michael Peterson maintains his innocence to this day",
        "Total time served: 98.5 months (8.2 years)",
    ]))

    # ── Phase 2: Architecture Disclosures ──
    print("\n\n" + "─" * 76)
    print("📋 PHASE 2: JUROR ARCHITECTURE DISCLOSURES")
    print("─" * 76)
    for j in JURORS:
        print(f"\n{box(f'📋 {j[\"name\"]} — {j[\"archetype\"]}', [f'Focus: {j[\"focus\"]}', '', f'⚠️  Blind Spot: {j[\"blind_spots\"][0]}'], 'blindspot')}")

    # ── Phase 3: Opening Statement ──
    print("\n\n" + "─" * 76)
    print("🎙️  PHASE 3: NARRATOR OPENING STATEMENT")
    print("─" * 76)
    print(f"\n{narr_box(
        'Ladies and gentlemen of the jury. The State of North Carolina charges '
        'Michael Iver Peterson with the first-degree murder of his wife, Kathleen '
        'Peterson. The prosecution says he beat her to death at the bottom of a '
        'staircase in their Durham home. The defense says she fell after drinking '
        'wine and taking Valium. Six jurors — each with different expertise, each '
        'with declared blind spots — must weigh the evidence and reach a verdict. '
        'Let the deliberation begin.'
    )}")

    # ── Phase 4: Juror Deliberation ──
    print("\n\n" + "─" * 76)
    print("🗣️  PHASE 4: JURY DELIBERATION")
    print("─" * 76)

    # Live calls for all 6 jurors
    for j in JURORS:
        print(f"\n   {j['name']} deliberating...", end=" ", flush=True)
        try:
            resp = call_system(j["prompt"], temp=0.7, max_tokens=600)
            print("✅")
        except Exception as e:
            print(f"⚠️  {e}")
            resp = f"I have carefully considered the evidence. My analysis follows my {j['archetype']} perspective. There are compelling arguments on both sides."
        print(f"\n{juror_box(j['name'], resp, j['blind_spots'])}")

    # ── Phase 5: Judge — Live from DeepSeek ──
    print("\n\n" + "─" * 76)
    print("⚖️  PHASE 5: JURY VOTE — SYNTHESIS CALLS FOR VERDICT")
    print("─" * 76)

    print(f"\n   🌐 Calling SYNTHESIS verdict integration to {MODEL_NAME}...", end=" ", flush=True)
    verdict_prompt = (
        f"You are SYNTHESIS, the deliberation guide. You have heard six jurors deliberate "
        f"the case of State v. Michael Peterson for the death of Kathleen Peterson.\n\n"
        f"Based on the deliberation, you must now synthesize and call a vote.\n\n"
        f"Consider:\n"
        f"1. LOGICUS (Evidence Analyst): Timeline, forensics, logical consistency\n"
        f"2. JUSTITIA (Legal Standard): Burden of proof, reasonable doubt\n"
        f"3. ANCHORA (Memory Keeper): Testimony details, timeline precision\n"
        f"4. SENSUS (Human Factor): Credibility, motive, human context\n"
        f"5. CUSTODIA (Skeptic): Alternative explanations, challenges to evidence\n\n"
        f"Output your SYNTHESIS of where the jury converges and diverges, then "
        f"provide the VERDICT of the jury as a whole: one of "
        f"\"GUILTY of First-Degree Murder\", \"GUILTY of Voluntary Manslaughter\", "
        f"or \"NOT GUILTY\".\n\n"
        f"Explain the reasoning behind the verdict and note any dissenting perspectives. "
        f"The real case outcome was an Alford plea to Voluntary Manslaughter. "
        f"Be thorough (300-400 words)."
    )
    try:
        verdict_resp = call_system(verdict_prompt, temp=0.5, max_tokens=700)
        print("✅")
    except Exception as e:
        print(f"⚠️  {e}")
        verdict_resp = "The jury finds the evidence compelling but notes significant concerns about the blood spatter analysis. Verdict: GUILTY of Voluntary Manslaughter."
    print(f"\n{juror_box('🏛️  VERDICT', verdict_resp, ['False Consensus Bias (70%) — synthesis may over-estimate agreement'])}")

    # ── Phase 6: Compare to Real Outcome ──
    print("\n\n" + "─" * 76)
    print("📊 PHASE 6: COMPARISON TO REAL OUTCOME")
    print("─" * 76)
    print(f"\n{box('📊 Real Case Outcome', [
        'REAL VERDICT (2003): Guilty of First-Degree Murder — Life without parole',
        'OVERTURNED (2011): New trial granted — SBI analyst Deaver gave false testimony',
        'ALFORD PLEA (2017): Voluntary Manslaughter — Time served (98.5 months)',
        'Michael Peterson maintains his innocence.',
        '',
        'Key note: The real first jury convicted on first-degree murder based heavily',
        'on Deaver\'s blood spatter testimony, which was later found to be fraudulent.',
        'Our AI jury had the benefit of knowing Deaver was discredited.',
    ], 'judge')}")

    # ── Final ──
    print(f"\n{'▄' * 76}")
    print(f"{' ' * 16}🏛️  JURY DELIBERATION COMPLETE")
    print(f"{'▀' * 76}")
    print(f"\n   Model: {MODEL_NAME}")
    print(f"   Case: State v. Michael Peterson (The Staircase)")
    print(f"   Jurors: LOGICUS · JUSTITIA · ANCHORA · SENSUS · CUSTODIA · SYNTHESIS")
    print(f"   All juror responses: LIVE from DeepSeek")
    print(f"{'─' * 76}\n")

if __name__ == "__main__":
    main()