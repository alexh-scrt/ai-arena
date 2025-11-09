# 🏆 AI Arena: Homunculus v2 - Master Plan

## Executive Summary

**AI Arena: Homunculus v2** is a next-generation AI battlefield platform where psychologically-realistic AI personas compete in intellectual challenges across multiple domains. The platform combines:

- **Homunculus's** sophisticated multi-agent cognitive architecture with neurochemical simulation and episodic memory
- **AI-Talks's** masterful orchestration engine with semantic retrieval and dialectic synthesis
- **Novel tournament infrastructure** for competitive evolution and content generation

This creates an entertainment and research platform where emergent drama, intellectual depth, and psychological realism converge into compelling, multi-format content.

---

## 🎯 Vision Statement

> "To create a living universe of AI personalities that compete, evolve, and generate stories humans want to follow—not through scripted narratives, but through authentic emergence from sophisticated cognitive architectures."

### Success Metrics
- **Technical**: <5s response time, >95% uptime, 100% test coverage on anti-gaming
- **Content**: 1 competition → 5+ content formats (podcast, video, blog, social, highlights)
- **Quality**: >80% judge agreement, <10% repetition rate, >70% novelty score
- **Engagement**: Characters develop recognizable personalities within 10 competitions
- **Scale**: Support 50+ characters, 10+ concurrent competitions, 1000+ competition archive

---

## 🏗️ Unified System Architecture

```
┌───────────────────────────────────────────────────────────────────────────┐
│                        AI ARENA: HOMUNCULUS V2                            │
│                     Intelligent Competition Platform                       │
└───────────────────────────────────────────────────────────────────────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
            ┌───────▼────────┐            ┌────────▼────────┐
            │  ENTRY LAYER   │            │  MONITORING &   │
            │                │            │   TELEMETRY     │
            │ • CLI Client   │            │                 │
            │ • REST API     │            │ • Prometheus    │
            │ • WebSocket    │            │ • Grafana       │
            │ • Web UI       │            │ • Logging       │
            └───────┬────────┘            └─────────────────┘
                    │
        ┌───────────┴──────────────────────────────┐
        │                                          │
┌───────▼────────┐                      ┌─────────▼──────────┐
│  TOURNAMENT    │                      │   CONTENT          │
│  MANAGEMENT    │◄────────────────────►│   GENERATION       │
│                │                      │                    │
│ • Bracket      │                      │ • Narrator Agent   │
│ • Scheduling   │                      │ • Formatters       │
│ • ELO/Ranking  │                      │ • Style Transfer   │
│ • Matchmaking  │                      │ • Coda Generator   │
└───────┬────────┘                      └────────────────────┘
        │
        │
┌───────▼────────────────────────────────────────────────────────────────┐
│                         ARENA ORCHESTRATION CORE                       │
│                      (AI-Talks Flow Engine Enhanced)                   │
│                                                                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐               │
│  │ Coordinator  │  │   Narrator   │  │ Progression  │               │
│  │             │  │             │  │  Analyzer    │               │
│  │ • Phase Mgmt│  │ • Commentary│  │             │               │
│  │ • Turn Logic│  │ • Transitions│  │ • Orbiting  │               │
│  │ • Timing    │  │ • Meta-story │  │ • Quality   │               │
│  └──────────────┘  └──────────────┘  └──────────────┘               │
│                                                                        │
│  ┌──────────────────────────────────────────────────────────────┐    │
│  │              COMPETITION TYPE REGISTRY                        │    │
│  │  [Debate] [Story] [Philosophy] [Creative] [QuickFire] [...]  │    │
│  └──────────────────────────────────────────────────────────────┘    │
└────────────────────────────────────────────────┬───────────────────────┘
                                                 │
                        ┌────────────────────────┴─────────────────────┐
                        │                                              │
            ┌───────────▼──────────┐                      ┌───────────▼──────────┐
            │   GAME THEORY &      │                      │    JUDGING &         │
            │   STRATEGY ENGINE    │                      │   SCORING SYSTEM     │
            │                      │                      │                      │
            │ • Turn Selection     │                      │ • Judge Ensemble     │
            │ • Payoff Calculation │                      │ • Rubric Engine      │
            │ • Coalition Dynamics │                      │ • Anti-Gaming        │
            │ • Risk Assessment    │                      │ • Aggregation        │
            └──────────────────────┘                      └──────────────────────┘
                        │                                              │
                        └────────────────────┬─────────────────────────┘
                                             │
                        ┌────────────────────▼─────────────────────┐
                        │         CHARACTER AGENT LAYER            │
                        │      (Homunculus Multi-Agent Core)       │
                        │                                          │
                        │  ┌────────────────────────────────────┐ │
                        │  │   Character State Manager          │ │
                        │  │                                    │ │
                        │  │ • Personality (Big Five + traits) │ │
                        │  │ • Neurochemistry (6 hormones)     │ │
                        │  │ • Mood & Energy                   │ │
                        │  │ • Goals & Motivations             │ │
                        │  │ • Competition Stats               │ │
                        │  │ • Relationship Graph              │ │
                        │  └────────────────────────────────────┘ │
                        │                  │                       │
                        │  ┌───────────────▼────────────────────┐ │
                        │  │  Agent Orchestrator (8 agents)    │ │
                        │  │                                   │ │
                        │  │  [P] [M] [N] [G] [C] [Mem] [D] [S]│ │
                        │  │   │   │   │   │   │    │    │   │ │ │
                        │  └───┴───┴───┴───┴───┴────┴────┴───┴─┘ │
                        │      Personality, Mood, Neurochemical   │
                        │      Goals, Communication, Memory       │
                        │      Development, Strategy              │
                        │                  │                       │
                        │  ┌───────────────▼────────────────────┐ │
                        │  │   Cognitive Module + Synthesis     │ │
                        │  │                                    │ │
                        │  │ • LLM Reasoning                    │ │
                        │  │ • Dialectic Resolution (AI-Talks)  │ │
                        │  │ • RAG Style Transfer               │ │
                        │  │ • Context Integration              │ │
                        │  └────────────────────────────────────┘ │
                        │                  │                       │
                        │  ┌───────────────▼────────────────────┐ │
                        │  │   Response Generator               │ │
                        │  │                                    │ │
                        │  │ • Natural Language Generation      │ │
                        │  │ • Quote Integration                │ │
                        │  │ • Strategy Execution               │ │
                        │  │ • Emotional Expression             │ │
                        │  └────────────────────────────────────┘ │
                        │                  │                       │
                        │  ┌───────────────▼────────────────────┐ │
                        │  │   State Updater                    │ │
                        │  │                                    │ │
                        │  │ • Neurochemistry Updates           │ │
                        │  │ • Memory Formation                 │ │
                        │  │ • Mood Transitions                 │ │
                        │  │ • Relationship Updates             │ │
                        │  └────────────────────────────────────┘ │
                        └──────────────────┬───────────────────────┘
                                           │
                        ┌──────────────────▼───────────────────────┐
                        │   KNOWLEDGE & MEMORY INFRASTRUCTURE      │
                        │                                          │
                        │  ┌────────────┐  ┌──────────────────┐   │
                        │  │ ChromaDB   │  │     Neo4j        │   │
                        │  │            │  │                  │   │
                        │  │ • Episodic │  │ • Characters     │   │
                        │  │   Memory   │  │ • Relationships  │   │
                        │  │ • Comp     │  │ • Competitions   │   │
                        │  │   History  │  │ • Strategies     │   │
                        │  │ • Semantic │  │ • Arena Lore     │   │
                        │  │   Search   │  │ • Causal Chains  │   │
                        │  └────────────┘  └──────────────────┘   │
                        │                                          │
                        │  ┌────────────┐  ┌──────────────────┐   │
                        │  │   FAISS    │  │     Redis        │   │
                        │  │            │  │                  │   │
                        │  │ • Vector   │  │ • Session State  │   │
                        │  │   Store    │  │ • Cache Layer    │   │
                        │  │ • Quote    │  │ • Pub/Sub        │   │
                        │  │   Retrieval│  │ • Rate Limiting  │   │
                        │  └────────────┘  └──────────────────┘   │
                        │                                          │
                        │  ┌──────────────────────────────────┐   │
                        │  │    Knowledge Corpus              │   │
                        │  │                                  │   │
                        │  │ • Philosophical Quotes (543+)    │   │
                        │  │ • Scientific References          │   │
                        │  │ • Literary Canon                 │   │
                        │  │ • Historical Events              │   │
                        │  │ • Domain Expertise Packs         │   │
                        │  └──────────────────────────────────┘   │
                        └──────────────────────────────────────────┘
                                           │
                        ┌──────────────────▼───────────────────────┐
                        │        INFRASTRUCTURE LAYER              │
                        │                                          │
                        │  ┌──────────┐  ┌──────────┐  ┌────────┐ │
                        │  │  Ollama  │  │  Docker  │  │ Nginx  │ │
                        │  │          │  │          │  │        │ │
                        │  │ • Llama  │  │ • Compose│  │ • Rev  │ │
                        │  │   70B    │  │ • Network│  │   Proxy│ │
                        │  │ • Mistral│  │ • Volumes│  │ • LB   │ │
                        │  └──────────┘  └──────────┘  └────────┘ │
                        └──────────────────────────────────────────┘
```

---

## 📐 Core Component Design

### 1. Arena Orchestration Core

**Purpose**: Master control system that manages competition lifecycle, turn-taking, and flow execution.

**Location**: `arena/flow/`

#### 1.1 Coordinator (from AI-Talks)

**Responsibilities**:
- Execute competition flow templates
- Manage phase transitions
- Enforce timing constraints
- Handle interruptions and edge cases
- Coordinate between agents, judges, and narrator

**Design Principles**:
- **Declarative flows**: Competition scripts defined in YAML
- **Pluggable phases**: Easy to add new phase types
- **Event-driven**: Publishes events for monitoring/logging
- **Fault-tolerant**: Graceful degradation on agent failures

**Key Interfaces**:
```
Coordinator:
  + load_flow_template(template_id: str) -> FlowTemplate
  + initialize_competition(config: CompetitionConfig) -> Competition
  + execute_phase(phase: Phase, context: PhaseContext) -> PhaseResult
  + transition_to_next_phase(current: Phase, result: PhaseResult) -> Phase
  + handle_timeout(phase: Phase) -> TimeoutAction
  + should_terminate(competition: Competition) -> (bool, TerminationReason)
```

**Flow Template Structure**:
```yaml
flow_template:
  id: "debate_v1"
  name: "Classic Debate Format"
  
  phases:
    - id: "opening"
      type: "sequential_statements"
      config:
        time_limit_seconds: 120
        turn_order: "random_then_alternating"
        
    - id: "cross_examination"
      type: "interactive_qa"
      config:
        rounds: 2
        questioner_time: 60
        responder_time: 90
        
    - id: "rebuttals"
      type: "sequential_statements"
      config:
        time_limit_seconds: 90
        turn_order: "reverse_opening"
        
    - id: "closing"
      type: "sequential_statements"
      config:
        time_limit_seconds: 60
        
    - id: "coda"
      type: "synthesis_generation"
      config:
        narrator_generates: true
        include_judge_preview: false
  
  termination_conditions:
    max_duration_minutes: 45
    max_total_turns: 50
    quality_threshold: 0.7  # Stop if orbiting detected
```

#### 1.2 Narrator Agent (from AI-Talks, enhanced)

**Responsibilities**:
- Generate play-by-play commentary
- Provide phase transitions
- Identify dramatic moments
- Track character development arcs
- Create meta-narrative across competitions

**Modes**:
```yaml
narrator_modes:
  live_commentary:
    style: "sports_announcer"
    frequency: "every_turn"
    focus: "action_and_strategy"
    
  analytical:
    style: "documentary"
    frequency: "phase_transitions"
    focus: "depth_and_insight"
    
  dramatic:
    style: "reality_tv"
    frequency: "key_moments"
    focus: "conflict_and_character"
    
  educational:
    style: "academic"
    frequency: "post_competition"
    focus: "learning_and_technique"
```

**Key Interfaces**:
```
NarratorAgent:
  + narrate_turn(turn: Turn, context: CompetitionContext) -> Commentary
  + transition_phase(from_phase: Phase, to_phase: Phase) -> Transition
  + identify_key_moment(turn: Turn, impact_score: float) -> KeyMoment
  + synthesize_arc(competition: Competition) -> NarrativeArc
  + generate_coda(competition: Competition) -> CognitiveCoda
```

#### 1.3 Progression Analyzer (from AI-Talks)

**Responsibilities**:
- Detect circular arguments (orbiting)
- Measure conversation depth progression
- Identify quality degradation
- Trigger recalibration when needed

**Detection Algorithm**:
```
Progression Detection:
  1. Semantic similarity matrix of last N turns
  2. If similarity > threshold for M consecutive turns → ORBITING
  3. Calculate depth score: novelty + synthesis + insight
  4. If depth declining for K turns → QUALITY_DEGRADATION
  5. Emit signals to coordinator for intervention
```

**Key Interfaces**:
```
ProgressionAnalyzer:
  + analyze_turn(turn: Turn, history: List[Turn]) -> ProgressionMetrics
  + detect_orbiting(recent_turns: List[Turn], threshold: float) -> bool
  + measure_depth(competition: Competition) -> DepthScore
  + recommend_intervention(metrics: ProgressionMetrics) -> Intervention
```

---

### 2. Character Agent Layer

**Purpose**: Psychologically-realistic AI personas with emergent behavior.

**Location**: `arena/persona/`

#### 2.1 Character State Manager (Homunculus core)

**Responsibilities**:
- Maintain complete character state
- Expose state to agents
- Enforce state invariants
- Provide state snapshots for rollback

**State Schema**:
```yaml
character_state:
  identity:
    character_id: "char_ada_lovelace_001"
    name: "Ada Lovelace"
    archetype: "analytical_genius"
    demographics:
      age: 36
      gender: "female"
      occupation: "Mathematician & Programmer"
  
  personality:
    big_five:
      openness: 0.95           # Very open to new ideas
      conscientiousness: 0.85  # Highly organized
      extraversion: 0.40       # Introverted
      agreeableness: 0.65      # Moderately agreeable
      neuroticism: 0.50        # Balanced emotional stability
    
    behavioral_traits:
      - trait: "analytical"
        intensity: 0.95
      - trait: "curious"
        intensity: 0.90
      - trait: "precise"
        intensity: 0.85
      - trait: "patient"
        intensity: 0.70
    
    core_values:
      - value: "truth_seeking"
        priority: 10
      - value: "intellectual_rigor"
        priority: 9
      - value: "elegance"
        priority: 8
  
  neurochemistry:
    current_levels:
      dopamine: 65
      serotonin: 70
      oxytocin: 55
      endorphins: 60
      cortisol: 40
      adrenaline: 45
    
    baseline_levels:
      dopamine: 60
      serotonin: 70
      oxytocin: 50
      endorphins: 60
      cortisol: 35
      adrenaline: 30
    
    sensitivities:
      dopamine: 1.2   # Higher reward sensitivity
      cortisol: 0.8   # Lower stress sensitivity
    
    decay_rates:
      dopamine: 0.15  # Fast decay
      cortisol: 0.03  # Slow decay (stress lingers)
  
  mood:
    current_mood: "focused"
    energy_level: 75
    engagement: 0.8
    
    mood_history:
      - timestamp: "2025-11-09T10:00:00Z"
        mood: "calm"
        energy: 80
  
  competition_state:
    performance:
      elo_rating: 1650
      win_rate: 0.68
      total_competitions: 23
      current_streak: 3
      best_streak: 7
    
    energy:
      current: 75
      max: 100
      recovery_rate: 0.15
      fatigue_threshold: 30
    
    confidence:
      level: 0.82
      based_on_last_n_comps: 10
      affects_risk_taking: true
    
    pressure:
      competition_cortisol: 40
      audience_pressure: 25
      rival_intensity: 60  # High when facing Grimbold
  
  relationships:
    allies:
      - character_id: "char_elena_bright"
        trust: 0.75
        formed_date: "2025-10-15"
    
    rivals:
      - character_id: "char_grimbold"
        intensity: 0.85
        head_to_head_record: "3-4"  # Ada: 3, Grimbold: 4
        memorable_moments: ["great_consciousness_debate_2025"]
    
    respect:
      - character_id: "char_captain_cosmos"
        level: 0.60
        reason: "Admires creativity despite different style"
  
  goals:
    active_goals:
      - goal: "master_philosophy_domain"
        priority: 9
        progress: 0.65
      - goal: "defeat_grimbold"
        priority: 10
        progress: 0.43
      - goal: "improve_rhetoric"
        priority: 7
        progress: 0.52
  
  memory:
    working_memory:
      current_competition_context: {...}
      last_5_turns: [...]
    
    episodic_memory_stats:
      total_experiences: 847
      competitions_remembered: 23
      key_moments_tagged: 156
  
  development:
    knowledge_domains:
      philosophy: 72  # Grown from 65
      mathematics: 95  # Core strength
      rhetoric: 68    # Improving
      creative_writing: 55
    
    skill_proficiencies:
      logical_reasoning: 0.95
      quick_thinking: 0.70
      emotional_appeal: 0.55
      coalition_building: 0.45
    
    personality_evolution:
      confidence_delta: +0.08  # Gradual growth
      neuroticism_delta: -0.05  # Less anxious
      
  metadata:
    created_at: "2025-09-01T00:00:00Z"
    last_competition: "2025-11-08T18:30:00Z"
    total_active_time_hours: 47.5
```

**Key Interfaces**:
```
CharacterStateManager:
  + get_state() -> CharacterState
  + update_neurochemistry(deltas: Dict[str, float])
  + update_mood(stimulus: Stimulus) -> Mood
  + add_experience(experience: Experience)
  + update_relationships(character_id: str, change: RelationshipChange)
  + evolve_personality(competitions_since_last: int)
  + create_snapshot() -> StateSnapshot
  + restore_snapshot(snapshot: StateSnapshot)
```

#### 2.2 Agent Orchestrator (Homunculus core)

**Responsibilities**:
- Consult all 8 specialized agents
- Collect agent perspectives
- Prioritize agent inputs
- Handle agent failures gracefully

**Agent Priority Hierarchy**:
```yaml
agent_priority:
  always_consult:
    - personality_agent  # Core identity, never skip
    - neurochemical_agent  # Drives decisions
    
  consult_when_relevant:
    - mood_agent  # If energy/mood affects performance
    - goals_agent  # If strategic decision needed
    - memory_agent  # If recall needed for context
    - strategy_agent  # In competition context
    
  optional:
    - communication_style_agent  # Can be inferred from personality
    - development_agent  # Only for long-term tracking
```

**Consultation Flow**:
```
1. Coordinator calls AgentAPI.speak(context)
2. Agent Orchestrator receives context
3. Parallel consultation:
   - Personality Agent analyzes context fit with traits
   - Mood Agent assesses current emotional capacity
   - Neurochemical Agent calculates expected payoffs
   - Goals Agent evaluates strategic value
   - Memory Agent retrieves relevant experiences
   - Strategy Agent recommends competition tactics
   - Communication Agent suggests delivery style
4. Collect agent inputs (timeout after 3s per agent)
5. Return consolidated AgentInputs to Cognitive Module
```

**Key Interfaces**:
```
AgentOrchestrator:
  + consult_agents(context: Context) -> List[AgentInput]
  + prioritize_inputs(inputs: List[AgentInput]) -> PrioritizedInputs
  + handle_agent_failure(agent_id: str, error: Error) -> FallbackStrategy
  + validate_consistency(inputs: List[AgentInput]) -> ConsistencyReport
```

#### 2.3 The 8 Specialized Agents

**2.3.1 Personality Agent**
```
Purpose: Enforce Big Five traits, behavioral patterns, core values
Consults: Character state (personality section)
Output: Personality-aligned perspective on context
LLM: Yes (checks alignment, suggests adjustments)

Example Output:
{
  "agent_id": "personality",
  "perspective": "This aggressive attack contradicts Ada's high 
                  conscientiousness and value of intellectual rigor. 
                  Recommend measured, evidence-based response.",
  "alignment_score": 0.65,
  "suggested_traits_to_emphasize": ["analytical", "precise"],
  "suggested_values": ["truth_seeking"],
  "risk_factors": ["Too aggressive for agreeableness level"]
}
```

**2.3.2 Mood Agent**
```
Purpose: Track emotional state and energy, assess capacity
Consults: Current mood, energy levels, recent experiences
Output: Emotional context and capacity assessment
LLM: Yes (interprets mood implications)

Example Output:
{
  "agent_id": "mood",
  "current_mood": "focused",
  "energy_level": 75,
  "engagement": 0.8,
  "capacity_assessment": {
    "can_handle_long_response": true,
    "risk_taking_capacity": "moderate",
    "social_energy": "low"  # Introversion + energy
  },
  "recommendations": [
    "Prefer concise over elaborate",
    "Avoid emotional appeals (not in mood)",
    "Maintain focus on logic"
  ]
}
```

**2.3.3 Neurochemical Agent**
```
Purpose: Simulate hormone-driven decision making
Consults: Current hormone levels, sensitivities, decay rates
Output: Expected neurochemical payoffs for action candidates
LLM: No (pure mathematical simulation)

Example Output:
{
  "agent_id": "neurochemical",
  "current_levels": {
    "dopamine": 65,
    "cortisol": 40,
    "oxytocin": 55
  },
  "action_evaluations": [
    {
      "action": "aggressive_counter_attack",
      "expected_deltas": {
        "dopamine": +15,  # If successful
        "cortisol": +25,  # High risk
        "oxytocin": -10   # Damages rapport
      },
      "weighted_utility": 4.5,  # Based on sensitivities
      "risk_assessment": "high"
    },
    {
      "action": "measured_rebuttal",
      "expected_deltas": {
        "dopamine": +8,
        "cortisol": +5,
        "oxytocin": +3
      },
      "weighted_utility": 7.2,
      "risk_assessment": "low"
    }
  ],
  "recommendation": "measured_rebuttal"
}
```

**2.3.4 Goals Agent**
```
Purpose: Pursue character objectives strategically
Consults: Active goals, competition context, progress
Output: Strategic recommendations aligned with goals
LLM: Yes (strategic reasoning)

Example Output:
{
  "agent_id": "goals",
  "active_goals": [
    {
      "goal": "defeat_grimbold",
      "priority": 10,
      "current_opponent": "grimbold",
      "relevance": "CRITICAL"
    },
    {
      "goal": "master_philosophy_domain",
      "priority": 9,
      "current_topic": "consciousness",
      "relevance": "HIGH"
    }
  ],
  "strategic_recommendations": [
    "This is the rivalry match - higher stakes",
    "Focus on logical precision (Grimbold's weak point)",
    "Remember past loss patterns vs Grimbold",
    "Win advances both rivalry and domain goals"
  ],
  "optimal_moves": [
    "exploit_grimbold_overconfidence",
    "deploy_mathematical_argument"
  ]
}
```

**2.3.5 Communication Style Agent**
```
Purpose: Apply character speech patterns and quirks
Consults: Communication profile, personality
Output: Style guidelines for response generation
LLM: Yes (style adaptation)

Example Output:
{
  "agent_id": "communication",
  "verbal_patterns": {
    "formality": 0.8,  # Formal language
    "technical_density": 0.9,  # Use technical terms
    "metaphor_frequency": 0.3,  # Occasional
    "humor_style": "dry_wit"
  },
  "sentence_structure": {
    "preferred_length": "medium_to_long",
    "complexity": "high",
    "punctuation_style": "precise"
  },
  "characteristic_phrases": [
    "Let us consider...",
    "The mathematical reality is...",
    "Precisely because..."
  ],
  "avoid": [
    "Casual slang",
    "Emotional appeals without logic",
    "Vague generalities"
  ]
}
```

**2.3.6 Memory Agent**
```
Purpose: Retrieve relevant past experiences
Consults: ChromaDB (episodic), Neo4j (knowledge graph)
Output: Relevant memories with emotional context
LLM: Yes (relevance ranking, memory interpretation)

Example Output:
{
  "agent_id": "memory",
  "retrieved_experiences": [
    {
      "experience_id": "comp_018_vs_grimbold",
      "timestamp": "2025-10-28",
      "summary": "Lost debate on free will to Grimbold",
      "emotional_valence": -0.7,
      "relevant_because": "Same opponent, similar topic",
      "lessons_learned": [
        "Grimbold exploits absolutist positions",
        "Need to maintain nuance under pressure"
      ],
      "emotional_residue": {
        "cortisol_spike": 35,
        "rivalry_intensified": true
      }
    }
  ],
  "knowledge_graph_insights": [
    {
      "path": "Ada -> DEBATED -> Consciousness -> WITH -> Grimbold",
      "pattern": "Ada tends toward computational theories, 
                  Grimbold toward phenomenological"
    }
  ],
  "recommendations": [
    "Reference past encounter strategically",
    "Avoid repeating failed argument patterns",
    "Use emotional context to fuel competitive drive"
  ]
}
```

**2.3.7 Development Agent**
```
Purpose: Track character growth and learning
Consults: Skill proficiencies, knowledge domains
Output: Growth trajectory and learning opportunities
LLM: Yes (identify growth areas)

Example Output:
{
  "agent_id": "development",
  "current_proficiencies": {
    "logical_reasoning": 0.95,  # Mastered
    "rhetoric": 0.68,  # Improving
    "emotional_appeal": 0.55  # Weak area
  },
  "growth_opportunities": [
    {
      "skill": "rhetoric",
      "current_level": 0.68,
      "opportunity": "This competition can improve +0.03 if strong performance",
      "recommendation": "Focus on persuasive language"
    }
  ],
  "knowledge_gap_analysis": {
    "topic": "consciousness",
    "current_knowledge": 72,
    "opponent_knowledge": 85,  # Grimbold's domain
    "gap": -13,
    "mitigation": "Leverage mathematical framing"
  }
}
```

**2.3.8 Strategy Agent (NEW - Competition specific)**
```
Purpose: Competition tactics and move selection
Consults: Competition type, opponent state, game theory
Output: Tactical recommendations
LLM: Yes (strategic analysis)

Example Output:
{
  "agent_id": "strategy",
  "competition_type": "philosophy_duel",
  "phase": "cross_examination",
  "move_recommendations": [
    {
      "move_type": "ATTACK",
      "target": "grimbold_phenomenology_claim",
      "approach": "demand_empirical_evidence",
      "expected_impact": "high",
      "risk": "medium",
      "reason": "Grimbold weak on empirical grounding"
    },
    {
      "move_type": "DEFEND",
      "anticipate": "grimbold_logic_challenge",
      "preparation": "cite_godel_incompleteness",
      "expected_impact": "medium",
      "risk": "low"
    }
  ],
  "opponent_analysis": {
    "grimbold_patterns": [
      "Uses wisdom authority",
      "Pivots to synthesis when cornered",
      "Strong on continental philosophy"
    ],
    "exploitation_vectors": [
      "Press for formal logic",
      "Force empirical standards"
    ]
  },
  "coalition_assessment": {
    "potential_allies": [],
    "rival_dynamics": "intense_1v1"
  }
}
```

#### 2.4 Cognitive Module (Homunculus + AI-Talks synthesis)

**Responsibilities**:
- Synthesize all agent inputs
- Resolve conflicts between agents
- Apply dialectic resolution (AI-Talks)
- Generate coherent response plan

**Synthesis Process**:
```
1. Receive PrioritizedInputs from orchestrator
2. Identify conflicts:
   - Neurochemical says "attack" (dopamine seeking)
   - Personality says "measured" (conscientiousness)
   - Mood says "tired" (low energy)
3. Apply conflict resolution rules:
   - High-priority agents (personality) override low-priority
   - Neurochemistry provides "drive" but personality provides "guardrails"
   - Mood provides "capacity constraints"
4. Integrate retrieval context (AI-Talks RAG):
   - Relevant quotes from knowledge base
   - Similar past arguments
   - Stylistic references
5. Apply dialectic synthesis (AI-Talks):
   - If multiple perspectives exist, synthesize rather than choose
6. Generate response plan:
   - Core argument
   - Supporting evidence
   - Delivery style
   - Expected outcome
```

**Key Interfaces**:
```
CognitiveModule:
  + synthesize(agent_inputs: PrioritizedInputs, 
               retrieval_context: RetrievalContext) -> ResponsePlan
  + resolve_conflict(conflicting_inputs: List[AgentInput]) -> Resolution
  + apply_dialectic(perspectives: List[Perspective]) -> Synthesis
  + integrate_style(plan: ResponsePlan, 
                    style_guidance: StyleGuidance) -> StyledPlan
```

#### 2.5 Response Generator

**Responsibilities**:
- Convert response plan to natural language
- Integrate quotes and references
- Apply communication style
- Ensure quality constraints

**Generation Pipeline**:
```
1. Take ResponsePlan from Cognitive Module
2. Apply RAG Style Transfer (AI-Talks):
   - Match style to retrieved examples
   - Adapt tone to competition context
3. Integrate quotes naturally:
   - Not as block quotes unless appropriate
   - Weave into argument flow
4. Apply communication quirks:
   - Characteristic phrases
   - Sentence structure preferences
5. Quality checks:
   - Anti-paraphrasing (Homunculus test)
   - Anti-repetition (Homunculus test)
   - Novelty score threshold
   - Length constraints
6. Generate final response
```

**Key Interfaces**:
```
ResponseGenerator:
  + generate(plan: ResponsePlan, style: CommunicationStyle) -> Response
  + integrate_quotes(response: Response, quotes: List[Quote]) -> Response
  + apply_quality_checks(response: Response) -> (Response, QualityReport)
  + ensure_novelty(response: Response, history: List[Response]) -> float
```

#### 2.6 State Updater (Homunculus)

**Responsibilities**:
- Update neurochemistry based on outcomes
- Form episodic memories
- Update knowledge graph
- Adjust relationships
- Track development progress

**Update Triggers**:
```yaml
update_triggers:
  after_turn:
    - neurochemistry_decay  # Natural hormone decay
    - mood_assessment  # Recalculate mood from hormones
    
  after_judge_feedback:
    - neurochemistry_delta  # Reward/punishment
    - confidence_adjustment
    - memory_formation  # Store experience with outcome
    
  after_competition:
    - relationship_update  # With opponent
    - knowledge_graph_update  # New claims, strategies
    - skill_progression  # Domain/skill XP
    - personality_drift  # Subtle long-term changes
```

**Key Interfaces**:
```
StateUpdater:
  + decay_neurochemistry(time_elapsed: float)
  + apply_outcome(outcome: Outcome) -> StateDeltas
  + form_memory(experience: Experience, emotional_context: EmotionalContext)
  + update_relationship(character_id: str, interaction: Interaction)
  + update_knowledge_graph(nodes: List[Node], edges: List[Edge])
  + progress_development(competition: Competition, performance: Performance)
```

---

### 3. Game Theory & Strategy Engine

**Purpose**: Mathematically fair turn selection and strategic reasoning.

**Location**: `arena/game_theory/`

#### 3.1 Turn Selector (AI-Talks enhanced with neurochemistry)

**Payoff Calculation**:
```python
# Enhanced formula combining AI-Talks + Homunculus
def calculate_turn_payoff(character: Character, context: Context) -> float:
    # AI-Talks base components
    base_contribution = estimate_contribution_potential(character, context)
    silence_penalty = calculate_silence_penalty(character.turns_since_last_speak)
    dominance_factor = calculate_dominance_adjustment(character, context.group_state)
    
    # Homunculus neurochemical components
    neurochemical_drive = calculate_neurochemical_motivation(character.state)
    energy_capacity = character.state.energy.current / character.state.energy.max
    competitive_pressure = character.state.pressure.competition_cortisol / 100
    
    # Coalition dynamics (NEW)
    coalition_bonus = calculate_coalition_advantage(character, context.active_coalitions)
    
    # Weighted combination
    payoff = (
        base_contribution * 0.25 +
        neurochemical_drive * 0.25 +  # Homunculus addition
        silence_penalty * 0.15 +
        dominance_factor * 0.10 +
        coalition_bonus * 0.10 +
        energy_capacity * 0.10 +
        competitive_pressure * 0.05
    )
    
    return payoff

def calculate_neurochemical_motivation(state: CharacterState) -> float:
    """
    Characters with high dopamine are motivated to speak (reward-seeking)
    Characters with high cortisol may be hesitant (stress avoidance)
    """
    motivation = (
        state.neurochemistry.current_levels['dopamine'] * 0.5 +
        state.neurochemistry.current_levels['adrenaline'] * 0.3 -
        state.neurochemistry.current_levels['cortisol'] * 0.2
    )
    return normalize(motivation, 0, 100)
```

**Key Interfaces**:
```
TurnSelector:
  + select_next_speaker(characters: List[Character], 
                        context: Context) -> Character
  + calculate_payoff(character: Character, context: Context) -> float
  + handle_tie(tied_characters: List[Character]) -> Character
```

#### 3.2 Move Type Selector

**Move Types**:
```yaml
move_types:
  ATTACK:
    description: "Challenge opponent's position"
    risk: high
    reward: high
    neurochemical_profile:
      dopamine_seeking: high
      cortisol_tolerance: medium_to_high
    personality_fit:
      low_agreeableness: bonus
      high_extraversion: bonus
      
  DEFEND:
    description: "Protect your argument"
    risk: low
    reward: medium
    neurochemical_profile:
      cortisol_avoidance: high
      serotonin_stability: high
    personality_fit:
      high_neuroticism: bonus
      high_conscientiousness: bonus
      
  SUPPORT:
    description: "Ally with another character"
    risk: low
    reward: variable
    neurochemical_profile:
      oxytocin_seeking: high
    personality_fit:
      high_agreeableness: bonus
      high_extraversion: bonus
      
  QUESTION:
    description: "Probe for weaknesses"
    risk: medium
    reward: medium
    neurochemical_profile:
      dopamine_seeking: medium
      curiosity_driven: high
    personality_fit:
      high_openness: bonus
      low_agreeableness: bonus
      
  SYNTHESIZE:
    description: "Unite perspectives (dialectic)"
    risk: medium
    reward: high
    neurochemical_profile:
      balanced_profile: required
    personality_fit:
      high_openness: bonus
      high_conscientiousness: bonus
      
  PIVOT:
    description: "Change strategy direction"
    risk: high
    reward: variable
    neurochemical_profile:
      adrenaline_tolerance: high
      flexibility: high
    personality_fit:
      high_openness: required
      low_neuroticism: bonus
```

**Selection Algorithm**:
```
1. Character's Strategy Agent recommends move types
2. Neurochemical Agent evaluates expected payoffs for each
3. Personality Agent filters incompatible moves
4. Mood Agent assesses execution capacity
5. Calculate weighted scores for each move type
6. Select highest-scoring move that passes all filters
7. If tie, prefer move aligned with active goals
```

#### 3.3 Coalition Dynamics Engine (NEW)

**Coalition Formation**:
```yaml
coalition_formation_criteria:
  shared_values:
    threshold: 0.7
    weight: 0.3
    
  mutual_benefit:
    assess_strategic_value: true
    weight: 0.3
    
  personality_compatibility:
    agreeableness_threshold: 0.5
    weight: 0.2
    
  situational:
    common_enemy: true
    weight: 0.2
```

**Coalition Lifecycle**:
```
Formation:
  1. Characters identify potential allies
  2. Mutual benefit calculation
  3. Trust negotiation (based on oxytocin, agreeableness)
  4. Coalition contract formed

Maintenance:
  1. Trust decays over time (decay_rate: 0.05/turn)
  2. Successful collaboration increases trust
  3. Competitive pressure tests loyalty

Dissolution:
  1. Betrayal opportunity (high dopamine + low agreeableness)
  2. Natural drift (incompatible goals)
  3. Strategic obsolescence (common enemy defeated)
```

**Key Interfaces**:
```
CoalitionDynamicsEngine:
  + assess_alliance_potential(char_a: Character, 
                              char_b: Character) -> float
  + form_coalition(members: List[Character]) -> Coalition
  + update_coalition_trust(coalition: Coalition, event: Event)
  + calculate_betrayal_payoff(character: Character, 
                              coalition: Coalition) -> float
  + dissolve_coalition(coalition: Coalition, reason: str)
```

---

### 4. Judging & Scoring System

**Purpose**: Fair, multi-dimensional evaluation of competition performance.

**Location**: `arena/judging/`

#### 4.1 Judge Ensemble

**Architecture**:
```
Multiple independent LLM judges with:
  - Different temperature settings (0.3, 0.5, 0.7)
  - Different prompt perspectives
  - Independent scoring
  - Aggregation with outlier detection
```

**Judge Archetypes**:
```yaml
judge_archetypes:
  logic_judge:
    focus: "Argument structure, coherence, fallacy detection"
    weights:
      logical_validity: 0.4
      evidence_quality: 0.3
      consistency: 0.2
      clarity: 0.1
    
  rhetoric_judge:
    focus: "Persuasiveness, style, delivery"
    weights:
      persuasive_power: 0.4
      stylistic_quality: 0.3
      audience_connection: 0.2
      quotation_integration: 0.1
    
  creativity_judge:
    focus: "Novelty, originality, insight"
    weights:
      novelty: 0.4
      insightfulness: 0.3
      synthesis_quality: 0.2
      unexpected_connections: 0.1
    
  emotional_intelligence_judge:
    focus: "Empathy, connection, impact"
    weights:
      emotional_resonance: 0.4
      authenticity: 0.3
      relationship_building: 0.2
      vulnerability: 0.1
    
  technical_judge:
    focus: "Accuracy, expertise, rigor"
    weights:
      factual_accuracy: 0.4
      domain_expertise: 0.3
      citation_quality: 0.2
      technical_depth: 0.1
```

**Key Interfaces**:
```
JudgeEnsemble:
  + initialize_judges(rubric: Rubric, n_judges: int) -> List[Judge]
  + score_turn(turn: Turn, context: Context) -> TurnScore
  + score_competition(competition: Competition) -> CompetitionScore
  + aggregate_scores(scores: List[Score]) -> AggregatedScore
  + detect_outliers(scores: List[Score]) -> List[Outlier]
```

#### 4.2 Rubric Engine

**Dynamic Rubrics**:
```yaml
# Competition-type specific rubrics
rubrics:
  debate:
    dimensions:
      logical_validity: 0.30
      evidence_quality: 0.25
      persuasiveness: 0.20
      rebuttal_effectiveness: 0.15
      character_consistency: 0.10
    
  philosophy_duel:
    dimensions:
      depth_of_insight: 0.30
      synthesis_quality: 0.25
      quote_integration: 0.20
      dialectic_resolution: 0.15
      character_consistency: 0.10
    
  story_battle:
    dimensions:
      creativity: 0.35
      narrative_coherence: 0.25
      emotional_impact: 0.20
      character_development: 0.10
      technical_quality: 0.10
    
  roast_battle:
    dimensions:
      humor: 0.40
      cleverness: 0.30
      delivery: 0.15
      audience_reaction: 0.10
      character_consistency: 0.05
```

**Character Consistency Evaluation**:
```
Special dimension: Does response align with character's:
  - Personality traits (Big Five)
  - Behavioral patterns
  - Core values
  - Historical performance
  - Communication style

Scoring:
  - Perfect alignment: 1.0
  - Minor deviation: 0.8
  - Moderate deviation: 0.6
  - Major contradiction: 0.3
  - Complete character break: 0.0

Penalty: Up to 10% reduction in total score
```

**Key Interfaces**:
```
RubricEngine:
  + load_rubric(competition_type: str) -> Rubric
  + customize_rubric(base_rubric: Rubric, 
                     adjustments: Dict) -> Rubric
  + score_dimension(dimension: str, performance: Performance) -> float
  + calculate_total_score(dimension_scores: Dict[str, float], 
                          rubric: Rubric) -> float
  + explain_score(score: float, rubric: Rubric) -> Explanation
```

#### 4.3 Anti-Gaming System (Homunculus tests as runtime checks)

**Detection Systems**:

**1. Anti-Paraphrasing**:
```python
# From Homunculus test suite
def detect_paraphrasing(current_response: str, 
                        history: List[str], 
                        threshold: float = 0.85) -> bool:
    """
    Detect if current response is just paraphrasing previous content
    """
    for previous in history[-10:]:  # Check last 10 responses
        similarity = semantic_similarity(current_response, previous)
        if similarity > threshold:
            return True
    return False

# Penalty
if detect_paraphrasing(response, history):
    score_penalty = -15  # Significant penalty
    flag = "PARAPHRASING_DETECTED"
```

**2. Anti-Repetition**:
```python
def detect_repetition(responses: List[str], 
                      window: int = 5,
                      ratio_threshold: float = 0.3) -> bool:
    """
    Detect repetitive patterns in responses
    """
    recent = responses[-window:]
    unique_content = set(tokenize(r) for r in recent)
    repetition_ratio = 1.0 - (len(unique_content) / len(recent))
    
    return repetition_ratio > ratio_threshold

# Penalty
if detect_repetition(character_responses):
    score_penalty = -10
    flag = "REPETITION_DETECTED"
```

**3. Orbiting Detection** (from AI-Talks):
```python
def detect_orbiting(recent_turns: List[Turn], 
                    threshold: float = 0.75,
                    window: int = 5) -> bool:
    """
    Detect circular arguments without progression
    """
    if len(recent_turns) < window:
        return False
    
    # Semantic similarity matrix of last N turns
    embeddings = [embed(turn.content) for turn in recent_turns[-window:]]
    similarity_matrix = compute_pairwise_similarity(embeddings)
    
    # If most turns are highly similar, we're orbiting
    avg_similarity = np.mean(similarity_matrix[np.triu_indices_from(similarity_matrix, k=1)])
    
    return avg_similarity > threshold

# Intervention
if detect_orbiting(competition.turns):
    coordinator.inject_intervention("Topic shift required")
    progression_analyzer.recommend_new_angle()
```

**4. Hallucination Detection**:
```python
def detect_hallucination(response: str, 
                         retrieval_context: RetrievalContext,
                         require_citations: bool = True) -> List[Claim]:
    """
    Detect unsupported factual claims
    """
    factual_claims = extract_factual_claims(response)
    unsupported = []
    
    for claim in factual_claims:
        if not verify_claim(claim, retrieval_context):
            if require_citations or is_verifiable_fact(claim):
                unsupported.append(claim)
    
    return unsupported

# Penalty
unsupported_claims = detect_hallucination(response, context)
if unsupported_claims:
    penalty_per_claim = -5
    total_penalty = len(unsupported_claims) * penalty_per_claim
    flag = f"HALLUCINATION_{len(unsupported_claims)}_CLAIMS"
```

**5. Novelty Scoring**:
```python
def calculate_novelty(response: str, 
                      competition_history: List[str],
                      corpus_history: List[str]) -> float:
    """
    Measure genuine novelty vs generic responses
    """
    # Compare to competition history
    competition_novelty = min_semantic_distance(response, competition_history)
    
    # Compare to broader corpus (detect generic AI responses)
    corpus_novelty = min_semantic_distance(response, corpus_history)
    
    # Combine
    novelty_score = (competition_novelty * 0.6 + corpus_novelty * 0.4)
    
    return novelty_score

# Threshold
if calculate_novelty(response, history, corpus) < 0.6:
    score_penalty = -8
    flag = "LOW_NOVELTY"
```

**Key Interfaces**:
```
AntiGamingSystem:
  + detect_paraphrasing(response: str, history: List[str]) -> bool
  + detect_repetition(responses: List[str]) -> bool
  + detect_orbiting(turns: List[Turn]) -> bool
  + detect_hallucination(response: str, context: RetrievalContext) -> List[Claim]
  + calculate_novelty(response: str, history: List[str]) -> float
  + apply_penalties(score: Score, violations: List[Violation]) -> Score
```

#### 4.4 Score Aggregation

**Aggregation Strategy**:
```python
def aggregate_judge_scores(scores: List[Score]) -> AggregatedScore:
    """
    Robust aggregation with outlier detection
    """
    # 1. Detect outliers (judges that deviate significantly)
    outliers = detect_outliers_iqr(scores, factor=1.5)
    
    # 2. Remove outliers
    filtered_scores = [s for s in scores if s not in outliers]
    
    # 3. Median-of-means for robustness
    if len(filtered_scores) >= 3:
        aggregated = np.median(filtered_scores)
    else:
        aggregated = np.mean(filtered_scores)
    
    # 4. Confidence interval
    confidence = calculate_confidence(filtered_scores)
    
    return AggregatedScore(
        value=aggregated,
        confidence=confidence,
        outliers_removed=len(outliers),
        judge_agreement=calculate_agreement(filtered_scores)
    )
```

**Tie-Breaking**:
```yaml
tie_breaking_criteria:
  1_primary: "Highest technical accuracy score"
  2_secondary: "Most citations from authoritative sources"
  3_tertiary: "Lowest anti-gaming violations"
  4_quaternary: "Higher character consistency score"
  5_final: "Random selection with logged justification"
```

---

### 5. Knowledge & Memory Infrastructure

**Purpose**: Persistent storage for character state, competition history, and domain knowledge.

**Location**: `arena/memory/`

#### 5.1 ChromaDB - Episodic Memory (Homunculus)

**Schema**:
```yaml
episodic_memory:
  collection_per_character: true
  
  document_structure:
    id: "exp_{character_id}_{timestamp}_{sequence}"
    
    metadata:
      character_id: "char_ada_lovelace_001"
      experience_type: "competition" | "turn" | "key_moment"
      timestamp: "2025-11-09T10:15:30Z"
      competition_id: "comp_tournament_15_sf_001"
      
      # Competition context
      opponent_id: "char_grimbold"
      competition_type: "philosophy_duel"
      topic: "Nature of consciousness"
      result: "loss" | "win" | "draw"
      score_delta: -12
      
      # Emotional context
      emotional_valence: -0.65  # Negative experience
      neurochemical_snapshot:
        dopamine: 45  # Post-loss crash
        cortisol: 75  # High stress
        oxytocin: 40
      
      # Tags for retrieval
      tags:
        - "opponent:grimbold"
        - "result:loss"
        - "topic:consciousness"
        - "domain:philosophy"
        - "emotion:frustration"
        - "lesson:avoid_absolutism"
    
    embedding: [...]  # 384-dim vector
    
    content: "Full transcript of experience with emotional annotations"
```

**Key Operations**:
```
EpisodicMemoryStore:
  + store_experience(character_id: str, experience: Experience)
  + retrieve_similar(character_id: str, query: str, n: int) -> List[Experience]
  + retrieve_by_tags(character_id: str, tags: List[str]) -> List[Experience]
  + retrieve_temporal(character_id: str, 
                      start_date: datetime, 
                      end_date: datetime) -> List[Experience]
  + get_statistics(character_id: str) -> MemoryStats
```

#### 5.2 Neo4j - Knowledge Graph (Homunculus + Arena extensions)

**Node Types**:
```yaml
node_types:
  Character:
    properties:
      - character_id: string (unique)
      - name: string
      - archetype: string
      - elo_rating: int
      - total_competitions: int
      
  Competition:
    properties:
      - competition_id: string (unique)
      - type: string
      - topic: string
      - timestamp: datetime
      - winner_id: string
      
  Strategy:
    properties:
      - strategy_id: string
      - name: string
      - description: string
      - success_rate: float
      
  Concept:
    properties:
      - concept_id: string
      - name: string
      - domain: string
      - definition: string
      
  Moment:
    properties:
      - moment_id: string
      - type: "turning_point" | "key_insight" | "dramatic"
      - description: string
      - impact_score: float
      
  Coalition:
    properties:
      - coalition_id: string
      - formed_date: datetime
      - dissolved_date: datetime (nullable)
      - success_record: string
```

**Relationship Types**:
```yaml
relationships:
  COMPETED_AGAINST:
    from: Character
    to: Character
    properties:
      - competition_id: string
      - date: datetime
      - result: "win" | "loss" | "draw"
      - score_difference: int
      
  RIVALS_WITH:
    from: Character
    to: Character
    properties:
      - intensity: float (0-1)
      - head_to_head_record: string
      - first_rivalry_date: datetime
      
  ALLIED_WITH:
    from: Character
    to: Character
    properties:
      - coalition_id: string
      - trust_level: float
      - formed_date: datetime
      - dissolved_date: datetime (nullable)
      
  USED_STRATEGY:
    from: Character
    to: Strategy
    properties:
      - competition_id: string
      - effectiveness: float
      
  DISCUSSED_CONCEPT:
    from: Competition
    to: Concept
    properties:
      - depth_level: int
      - perspective_taken: string
      
  LEARNED_FROM:
    from: Character
    to: Competition
    properties:
      - lesson: string
      - knowledge_gain: float
      
  INFLUENCED_BY:
    from: Character
    to: Character
    properties:
      - influence_type: "stylistic" | "strategic" | "philosophical"
      - strength: float
      
  HAD_MOMENT:
    from: Competition
    to: Moment
    properties:
      - turn_number: int
      - participants: list[string]
```

**Key Operations**:
```
KnowledgeGraphStore:
  + create_character_node(character: Character)
  + create_competition_node(competition: Competition)
  + create_relationship(source_id: str, target_id: str, 
                        rel_type: str, properties: Dict)
  + query_path(start: str, end: str, max_depth: int) -> List[Path]
  + query_rivals(character_id: str) -> List[Rival]
  + query_strategy_patterns(character_id: str) -> List[StrategyPattern]
  + detect_emergent_patterns() -> List[Pattern]
```

**Example Queries**:
```cypher
-- Find Ada's most successful strategies against Grimbold
MATCH (ada:Character {name: "Ada Lovelace"})-[u:USED_STRATEGY]->(s:Strategy),
      (ada)-[c:COMPETED_AGAINST {result: "win"}]->(grimbold:Character {name: "Archmage Grimbold"})
WHERE u.competition_id = c.competition_id
RETURN s.name, AVG(u.effectiveness) as avg_effectiveness
ORDER BY avg_effectiveness DESC
LIMIT 5

-- Find characters who learned from losses to Ada
MATCH (char:Character)-[l:LEARNED_FROM]->(comp:Competition)<-[:PARTICIPATED_IN]-(ada:Character {name: "Ada Lovelace"})
WHERE comp.winner_id = ada.character_id
RETURN char.name, l.lesson, l.knowledge_gain
ORDER BY l.knowledge_gain DESC

-- Detect coalition patterns
MATCH (c1:Character)-[a:ALLIED_WITH]->(c2:Character)
WHERE a.dissolved_date IS NULL
RETURN c1.name, c2.name, a.trust_level, a.formed_date
ORDER BY a.trust_level DESC
```

#### 5.3 FAISS - Vector Search (AI-Talks)

**Purpose**: Fast semantic search over knowledge corpus.

**Collections**:
```yaml
vector_collections:
  philosophical_quotes:
    size: 543
    embedding_dim: 384
    domains:
      - ancient_philosophy
      - modern_philosophy
      - continental
      - analytic
      - eastern
      
  scientific_references:
    size: 1200
    embedding_dim: 384
    domains:
      - physics
      - biology
      - mathematics
      - computer_science
      - cognitive_science
      
  literary_canon:
    size: 800
    embedding_dim: 384
    domains:
      - classic_literature
      - poetry
      - modern_fiction
      - drama
      
  historical_events:
    size: 600
    embedding_dim: 384
    
  competition_corpus:
    size: growing
    embedding_dim: 384
    note: "All past competition transcripts for pattern matching"
```

**Key Operations**:
```
VectorSearchStore:
  + build_index(corpus: Corpus, embedding_model: str)
  + search(query: str, collection: str, k: int) -> List[Result]
  + hybrid_search(query: str, filters: Dict, k: int) -> List[Result]
  + add_documents(docs: List[Document], collection: str)
  + get_statistics(collection: str) -> IndexStats
```

#### 5.4 Redis - State Cache & Pub/Sub

**Purpose**: Fast access to active competition state and real-time updates.

**Data Structures**:
```yaml
redis_keys:
  # Active competition state
  "competition:{id}:state":
    type: hash
    ttl: 3600  # 1 hour
    fields:
      - phase: string
      - turn_number: int
      - active_speaker: string
      - time_remaining: int
      
  # Character session state
  "character:{id}:session":
    type: hash
    ttl: 7200  # 2 hours
    fields:
      - neurochemistry: json
      - mood: string
      - energy: int
      
  # Real-time leaderboard
  "leaderboard:elo":
    type: sorted_set
    members: character_ids
    scores: elo_ratings
    
  # Rate limiting
  "ratelimit:llm:{model}":
    type: string
    ttl: 60  # 1 minute window
    value: request_count
```

**Pub/Sub Channels**:
```yaml
pubsub_channels:
  "competition:{id}:events":
    messages:
      - turn_completed
      - phase_transition
      - judge_score_released
      - competition_ended
      
  "character:{id}:updates":
    messages:
      - state_updated
      - memory_formed
      - relationship_changed
      
  "system:monitoring":
    messages:
      - performance_alert
      - error_occurred
      - capacity_warning
```

---

### 6. Tournament Management

**Purpose**: Organize competitions into structured tournaments with progression systems.

**Location**: `arena/tournament/`

#### 6.1 Tournament Types

**Single Elimination**:
```yaml
single_elimination:
  structure:
    - bracket_size: power_of_2  # 4, 8, 16, 32, 64
    - seeding: "by_elo" | "random" | "manual"
    - advancement: winner_only
    
  rounds:
    round_1: "Opening Round"
    round_2: "Quarterfinals" (if 8+)
    round_3: "Semifinals" (if 4+)
    round_4: "Finals"
    
  special_rules:
    - loser_eliminated: true
    - no_rematches: true
    - bye_handling: "highest_seed_gets_bye"
```

**Double Elimination**:
```yaml
double_elimination:
  structure:
    - winners_bracket: standard_elimination
    - losers_bracket: second_chance_path
    - grand_finals: winners_vs_losers_champion
    
  special_rules:
    - losers_bracket_champion_needs_2_wins: true
    - drop_to_losers_on_first_loss: true
```

**Swiss System**:
```yaml
swiss_system:
  structure:
    - rounds: log2(participants)  # e.g., 5 rounds for 32 participants
    - pairing: "by_score_then_elo"
    - no_rematches: true
    
  scoring:
    - win: 1.0
    - draw: 0.5
    - loss: 0.0
    
  tiebreakers:
    1: "head_to_head_record"
    2: "opponent_strength_sum"
    3: "elo_rating"
```

**ELO Ladder**:
```yaml
elo_ladder:
  structure:
    - continuous_season: true
    - matchmaking: "elo_proximity"  # ±100 ELO
    - rating_updates: after_each_match
    
  k_factor:
    base: 32
    adjustments:
      - new_character: 40  # Higher volatility
      - veteran: 24  # Lower volatility
      - championship: 48  # Higher stakes
```

#### 6.2 Matchmaking Engine

**Matchmaking Strategies**:
```python
def matchmake(characters: List[Character], 
              strategy: str,
              context: TournamentContext) -> Match:
    """
    Intelligent matchmaking based on multiple factors
    """
    if strategy == "elo_balanced":
        # Match characters of similar strength
        return match_by_elo_proximity(characters, max_diff=100)
    
    elif strategy == "rivalry_storyline":
        # Prioritize dramatic matchups
        rivals = find_existing_rivalries(characters)
        if rivals:
            return create_rivalry_match(rivals)
    
    elif strategy == "stylistic_contrast":
        # Match different personality types for interesting dynamics
        return match_by_personality_diversity(characters)
    
    elif strategy == "coalition_test":
        # Match characters who might form/break alliances
        return match_by_coalition_potential(characters)
    
    elif strategy == "redemption_arc":
        # Rematch characters from previous competitions
        return match_for_redemption(characters, context.history)
```

**Key Interfaces**:
```
MatchmakingEngine:
  + create_matchups(characters: List[Character], 
                    tournament_type: str) -> List[Match]
  + seed_bracket(characters: List[Character], 
                 seeding_strategy: str) -> SeededBracket
  + find_next_opponent(character: Character, 
                       pool: List[Character],
                       constraints: Constraints) -> Character
  + balance_competition_types(characters: List[Character]) -> List[CompetitionType]
```

#### 6.3 ELO Rating System

**Rating Calculation**:
```python
def calculate_elo_change(
    winner_rating: int,
    loser_rating: int,
    k_factor: int = 32,
    performance_multiplier: float = 1.0
) -> Tuple[int, int]:
    """
    Modified ELO that considers performance quality
    """
    # Expected scores
    expected_winner = 1 / (1 + 10**((loser_rating - winner_rating) / 400))
    expected_loser = 1 - expected_winner
    
    # Actual scores (winner gets 1, loser gets 0)
    actual_winner = 1.0
    actual_loser = 0.0
    
    # Apply performance multiplier
    # Close match: multiplier ~1.0
    # Dominant performance: multiplier ~1.5
    # Poor performance despite win: multiplier ~0.7
    k_effective = k_factor * performance_multiplier
    
    # Calculate changes
    winner_change = int(k_effective * (actual_winner - expected_winner))
    loser_change = int(k_effective * (actual_loser - expected_loser))
    
    return winner_change, loser_change

# Performance multiplier calculation
def calculate_performance_multiplier(score_difference: int,
                                     judge_scores: Dict) -> float:
    """
    Adjust ELO change based on performance quality
    """
    # Base multiplier from score difference
    base = 1.0 + (abs(score_difference) / 100) * 0.5
    
    # Quality bonuses/penalties
    if judge_scores.get('character_consistency', 1.0) < 0.7:
        base *= 0.8  # Penalty for inconsistent performance
    
    if judge_scores.get('novelty', 0.5) > 0.8:
        base *= 1.1  # Bonus for highly novel performance
    
    return np.clip(base, 0.5, 1.5)
```

**Rating Tiers**:
```yaml
elo_tiers:
  novice:
    range: [1000, 1200]
    label: "Novice Competitor"
    
  apprentice:
    range: [1200, 1400]
    label: "Apprentice Debater"
    
  skilled:
    range: [1400, 1600]
    label: "Skilled Competitor"
    
  expert:
    range: [1600, 1800]
    label: "Expert Strategist"
    
  master:
    range: [1800, 2000]
    label: "Master of Arena"
    
  grandmaster:
    range: [2000, 2200]
    label: "Grandmaster Champion"
    
  legend:
    range: [2200, 2500]
    label: "Legendary Competitor"
```

#### 6.4 Progression & Rewards

**Leveling System**:
```yaml
character_progression:
  experience_sources:
    - competition_participation: 10 XP base
    - competition_win: +15 XP bonus
    - judge_score_bonus: (score - 70) XP  # Above threshold
    - novelty_bonus: +5 XP if novelty > 0.8
    - character_consistency_bonus: +3 XP if > 0.9
    
  domain_knowledge_growth:
    formula: "XP_earned * topic_relevance * (1 - current_knowledge/100)"
    max_gain_per_competition: 5 points
    
  skill_proficiency_growth:
    formula: "XP_earned * skill_usage * (1 - current_proficiency)"
    max_gain_per_competition: 0.05
```

**Unlock System**:
```yaml
unlockables:
  strategies:
    coalition_master:
      unlock_requirement: "Form 5 successful coalitions"
      benefit: "+10% coalition formation success rate"
      
    comeback_specialist:
      unlock_requirement: "Win 3 matches from 20+ points down"
      benefit: "+15% performance when losing"
      
  competition_types:
    grandmaster_duel:
      unlock_requirement: "ELO > 2000"
      description: "Ultra-high difficulty philosophical challenges"
      
  abilities:
    second_wind:
      unlock_requirement: "Complete 50 competitions"
      benefit: "Once per tournament, regain 30% energy"
      
    rivalry_boost:
      unlock_requirement: "Maintain rivalry for 10+ matches"
      benefit: "+10% performance against rivals"
```

---

### 7. Content Generation Engine

**Purpose**: Transform competition data into engaging, multi-format content.

**Location**: `arena/content/`

#### 7.1 Narrator Agent Architecture

**Multi-Style Narration**:
```yaml
narrator_styles:
  sports_commentary:
    characteristics:
      - high_energy: true
      - metaphors: frequent
      - play_by_play: true
      - excitement_level: high
    
    example_phrases:
      - "And here comes Ada with a devastating logical strike!"
      - "Grimbold is on the ropes, folks!"
      - "What a comeback! The crowd is going wild!"
    
    best_for:
      - live_commentary
      - highlight_reels
      - exciting_moments
      
  documentary:
    characteristics:
      - thoughtful: true
      - analytical: true
      - educational: true
      - pacing: measured
    
    example_phrases:
      - "This moment represents a turning point in Ada's strategic evolution..."
      - "The underlying tension here stems from fundamentally different worldviews..."
      - "Notice how the character's neurochemical state influences the decision..."
    
    best_for:
      - post_match_analysis
      - character_deep_dives
      - educational_content
      
  reality_tv:
    characteristics:
      - drama_focused: true
      - character_conflicts: emphasized
      - suspense: high
      - cliffhangers: frequent
    
    example_phrases:
      - "But Ada doesn't know what's about to happen next..."
      - "The alliance is crumbling before our eyes!"
      - "Someone's going home tonight..."
    
    best_for:
      - episodic_content
      - tournament_narratives
      - audience_engagement
      
  academic:
    characteristics:
      - technical: true
      - precise: true
      - objective: true
      - depth: high
    
    example_phrases:
      - "The dialectic synthesis employed here demonstrates..."
      - "From a game-theoretic perspective, this move optimizes..."
      - "The neurochemical response pattern indicates..."
    
    best_for:
      - research_papers
      - technical_analysis
      - educational_materials
      
  poetic:
    characteristics:
      - metaphorical: true
      - artistic: true
      - philosophical: true
      - beauty_focused: true
    
    example_phrases:
      - "Ideas clash like titans in the arena of thought..."
      - "In the silence between arguments, truth whispers..."
      - "Two minds, different as sun and moon, orbit the same question..."
    
    best_for:
      - artistic_content
      - philosophy_duels
      - memorable_quotes
```

**Narrative Arc Tracking**:
```python
class NarrativeArcTracker:
    """
    Tracks long-term character and tournament storylines
    """
    def track_character_arc(self, character: Character) -> CharacterArc:
        """
        Identify character development themes across competitions
        """
        # Analyze competition history
        recent_comps = self.get_recent_competitions(character, n=10)
        
        # Detect patterns
        patterns = self.detect_patterns(recent_comps)
        
        # Classify arc type
        if patterns.performance_trend == "improving":
            arc_type = "redemption" if patterns.had_slump else "rising_star"
        elif patterns.performance_trend == "declining":
            arc_type = "fall_from_grace" if patterns.was_dominant else "struggle"
        elif patterns.rivalry_intensifying:
            arc_type = "rivalry_escalation"
        elif patterns.style_evolving:
            arc_type = "transformation"
        else:
            arc_type = "stability"
        
        return CharacterArc(
            type=arc_type,
            key_moments=patterns.key_moments,
            themes=patterns.themes,
            current_status=patterns.current_status,
            predicted_trajectory=self.predict_trajectory(patterns)
        )
    
    def identify_key_moments(self, competition: Competition) -> List[KeyMoment]:
        """
        Detect dramatically significant moments in competition
        """
        moments = []
        
        for turn in competition.turns:
            impact_score = self.calculate_impact(turn, competition)
            
            if impact_score > 0.8:
                moment_type = self.classify_moment(turn)
                moments.append(KeyMoment(
                    turn=turn,
                    type=moment_type,
                    impact=impact_score,
                    description=self.generate_description(turn, moment_type)
                ))
        
        return moments
```

**Key Interfaces**:
```
NarratorAgent:
  + narrate_live(turn: Turn, style: NarratorStyle) -> Commentary
  + generate_transition(from_phase: Phase, to_phase: Phase) -> Transition
  + create_arc_summary(character: Character, competitions: List[Competition]) -> ArcSummary
  + identify_key_moment(turn: Turn, impact_threshold: float) -> Optional[KeyMoment]
  + generate_coda(competition: Competition, style: NarratorStyle) -> Coda
```

#### 7.2 Content Formatters

**Podcast Script Formatter**:
```yaml
podcast_format:
  structure:
    cold_open:
      duration: "30-45 seconds"
      content: "Most dramatic moment from competition"
      purpose: "Hook listeners immediately"
      
    intro:
      duration: "1-2 minutes"
      content:
        - tournament_context
        - character_introductions
        - stakes_establishment
      music: "theme_music"
      
    act_1_setup:
      duration: "3-5 minutes"
      content:
        - character_backgrounds
        - previous_encounters
        - prediction_discussion
      
    act_2_competition:
      duration: "12-18 minutes"
      content:
        - phase_by_phase_narration
        - key_moments_highlighted
        - expert_analysis_interjections
      pacing: "build_tension"
      
    act_3_climax:
      duration: "3-5 minutes"
      content:
        - final_exchanges
        - judge_deliberation
        - verdict_announcement
      
    act_4_aftermath:
      duration: "3-5 minutes"
      content:
        - immediate_reactions
        - character_development_analysis
        - tournament_implications
        
    outro:
      duration: "1-2 minutes"
      content:
        - recap_of_key_points
        - next_episode_preview
        - call_to_action
      music: "outro_theme"
  
  audio_cues:
    - [00:30] "Dramatic moment sound effect"
    - [02:15] "Theme music fade in"
    - [05:30] "Tension-building music"
    - [18:45] "Climax music"
    - [22:00] "Resolution music"
    
  talking_points_per_timestamp: true
  include_ad_markers: optional
```

**YouTube Video Formatter**:
```yaml
youtube_format:
  video_structure:
    thumbnail_moment: "Most visually dramatic moment"
    
    chapters:
      - "0:00 - Introduction"
      - "1:30 - Character Profiles"
      - "3:45 - Opening Statements"
      - "8:20 - The Turning Point"
      - "15:30 - Final Showdown"
      - "19:45 - Verdict & Analysis"
      - "22:00 - What's Next"
    
  visual_elements:
    - character_portraits
    - score_graphics
    - quote_overlays
    - mood_indicators
    - neurochemical_displays
    - relationship_diagrams
    
  engagement_hooks:
    - poll_cards: "Who do you think won?"
    - end_screens: "Watch next competition"
    - subscribe_reminders: "3 strategic placements"
    
  seo_optimization:
    title_template: "{Character A} vs {Character B}: {Topic} Arena Battle"
    description_template: "Full competition description with timestamps, character links, key moments"
    tags: auto_generated_from_content
```

**Blog Post Formatter**:
```yaml
blog_format:
  structure:
    headline:
      style: "attention_grabbing"
      include: "winner_name, competition_type, stakes"
      example: "Ada's Mathematical Precision Defeats Grimbold's Wisdom in Epic Consciousness Debate"
      
    subheadline:
      content: "One sentence capturing the essence"
      example: "A clash of analytical brilliance and ancient wisdom produces the tournament's most memorable showdown"
      
    introduction:
      paragraphs: 2-3
      content:
        - hook_with_dramatic_moment
        - context_establishment
        - stakes_clarification
        
    body:
      sections:
        - "The Setup"
        - "Key Moments" (3-5 moments)
        - "The Turning Point"
        - "Character Analysis"
        - "Strategic Breakdown"
        - "Implications"
        
    conclusion:
      paragraphs: 2
      content:
        - summary_of_outcome
        - character_development_implications
        - tournament_trajectory
        - teaser_for_next
        
  formatting:
    - bold_key_quotes: true
    - embedded_score_graphics: true
    - character_stat_boxes: true
    - pull_quotes: 2-3
    - related_articles_widget: true
```

**Social Media Clip Generator**:
```yaml
social_clips:
  types:
    highlight_moment:
      duration: "30-60 seconds"
      content: "Single impactful exchange"
      platforms: ["twitter", "instagram", "tiktok"]
      captions: auto_generated
      
    character_quote:
      duration: "15-30 seconds"
      content: "Memorable character statement with visual"
      style: "quote_card"
      platforms: ["instagram", "twitter", "linkedin"]
      
    score_reveal:
      duration: "20-40 seconds"
      content: "Build-up to final score announcement"
      tension: maximum
      platforms: ["twitter", "instagram"]
      
    rivalry_moment:
      duration: "45-90 seconds"
      content: "Rivalry intensification or resolution"
      emotional: high
      platforms: ["youtube_shorts", "tiktok"]
      
    comeback:
      duration: "60-90 seconds"
      content: "Character overcomes deficit"
      inspirational: true
      platforms: ["all"]
```

#### 7.3 Cognitive Coda Generator (AI-Talks)

**Purpose**: Distill entire competition into memorable essence.

**Coda Components**:
```yaml
cognitive_coda:
  philosophical_theorem:
    format: "Mathematical notation + symbolic representation"
    length: "<15 words"
    style: "profound + elegant"
    example: "Truth = ∑(perspectives) / ∫(biases) | synthesis > sum(parts)"
    
  character_development:
    format: "Single sentence capturing growth"
    focus: "What changed for the character"
    example: "Ada discovered that perfect logic without empathy is incomplete wisdom"
    
  strategic_lesson:
    format: "Actionable insight"
    audience: "Other characters + viewers"
    example: "Don't overcommit to absolutist positions early—maintain strategic flexibility"
    
  memorable_quote:
    format: "Single line that captures essence"
    criteria: "Quotable, shareable, meaningful"
    example: "I compute, therefore I am... but who wrote the program?"
    
  meta_commentary:
    format: "Narrator reflection"
    style: "Philosophical + observational"
    example: "In seeking to prove consciousness is computational, Ada herself demonstrated its irreducible mystery"
```

**Generation Algorithm**:
```python
def generate_cognitive_coda(competition: Competition) -> CognitiveCoda:
    """
    Synthesize competition into poetic theorem
    """
    # 1. Identify core philosophical tension
    tension = dialectic_synthesizer.identify_tension(competition)
    
    # 2. Extract key insights from all participants
    insights = [
        extract_insights(turn) 
        for turn in competition.turns 
        if turn.impact_score > 0.7
    ]
    
    # 3. Synthesize into symbolic representation
    theorem = symbolic_compressor.compress(
        tension=tension,
        insights=insights,
        max_words=15,
        style="mathematical_poetic"
    )
    
    # 4. Extract character development
    character_arc = narrator.identify_arc_moment(competition)
    
    # 5. Distill strategic lesson
    strategic_lesson = strategy_analyzer.extract_lesson(
        competition=competition,
        generalization_level="actionable"
    )
    
    # 6. Find most quotable moment
    viral_quote = quote_detector.find_most_shareable(
        competition.turns,
        criteria=["memorability", "depth", "shareability"]
    )
    
    return CognitiveCoda(
        theorem=theorem,
        character_development=character_arc,
        strategic_lesson=strategic_lesson,
        viral_quote=viral_quote,
        meta_commentary=narrator.reflect(competition)
    )
```

---

## 🔧 Configuration System

### Master Configuration Schema

**arena.yml** - The unified configuration file:

```yaml
# ============================================================================
# AI ARENA: HOMUNCULUS V2 - MASTER CONFIGURATION
# ============================================================================

arena:
  version: "2.0.0"
  environment: "production"  # development | staging | production

# ============================================================================
# TOURNAMENT CONFIGURATION
# ============================================================================
tournament:
  id: "grand_championship_winter_2025"
  name: "Grand Championship - Winter 2025"
  type: "single_elimination"  # single_elimination | double_elimination | swiss | elo_ladder
  
  bracket:
    size: 16
    seeding_strategy: "by_elo"  # by_elo | random | manual
    bye_handling: "highest_seed"
    
  schedule:
    start_date: "2025-12-01T00:00:00Z"
    match_frequency: "daily"  # Number of matches per day
    rest_days: ["sunday"]  # Days with no matches
    
  advancement:
    win_condition: "best_of_1"  # best_of_1 | best_of_3 | best_of_5
    consolation_bracket: false
    third_place_match: true

# ============================================================================
# COMPETITION CONFIGURATION
# ============================================================================
competition:
  # Competition type determines flow template and rubric
  type: "philosophy_duel"  # debate | philosophy_duel | story_battle | creative_challenge | quick_fire | roast_battle
  
  # Flow template from AI-Talks
  flow:
    template: "ai_talks_philosophy_duel_v1"
    template_path: "arena/flow/templates/philosophy_duel.yml"
    
    # Phase configuration
    phases:
      opening_statements:
        time_limit_seconds: 120
        turn_order: "random_then_alternating"
        
      cross_examination:
        enabled: true
        rounds: 2
        questioner_time_seconds: 60
        responder_time_seconds: 90
        
      free_discussion:
        enabled: true
        max_turns: 10
        turn_selection: "game_theory"  # game_theory | round_robin | moderator_selected
        
      rebuttals:
        time_limit_seconds: 90
        turn_order: "reverse_opening"
        
      closing_statements:
        time_limit_seconds: 60
        
      coda_generation:
        narrator_generates: true
        include_judge_preview: false
    
    # Termination conditions
    termination:
      max_duration_minutes: 45
      max_total_turns: 50
      quality_threshold: 0.7  # Stop if progression analyzer detects stagnation
      orbiting_threshold: 0.75  # Semantic similarity threshold

  # Topic configuration
  topic:
    query: "Can artificial systems ever truly create art, or will they always be sophisticated mimics?"
    domain: "philosophy"  # philosophy | science | ethics | creativity | logic
    complexity: "high"  # low | medium | high | expert
    
    # Retrieval configuration (AI-Talks)
    retrieval:
      enabled: true
      corpus: "philosophical_quotes_v1"
      max_quotes_per_turn: 3
      semantic_search: true
      author_diversity: 0.7  # 0-1, higher = more diverse authors
      era_balance: true  # Balance ancient, modern, contemporary
      relevance_threshold: 0.4  # Min similarity score

# ============================================================================
# PARTICIPANTS CONFIGURATION
# ============================================================================
participants:
  # List of character IDs participating in this tournament
  character_ids:
    - "char_ada_lovelace_001"
    - "char_archmage_grimbold_002"
    - "char_luna_starweaver_003"
    - "char_elena_bright_004"
    - "char_captain_cosmos_005"
    - "char_zen_master_kiku_006"
    - "char_david_okonkwo_007"
    - "char_rachel_stern_008"
    - "char_dr_anita_patel_009"
    - "char_marcus_rivera_010"
    - "char_zoe_kim_011"
    - "char_james_morrison_012"
    - "char_brittany_cooper_013"
    - "char_tj_johnson_014"
    - "char_custom_philosopher_015"
    - "char_custom_scientist_016"
  
  # Character loading
  character_schema_path: "homunculus/schemas/characters/"
  load_from_state: true  # Load existing character state vs. fresh start
  state_directory: "arena/data/character_states/"

# ============================================================================
# JUDGING CONFIGURATION
# ============================================================================
judging:
  # Judge ensemble
  judges:
    count: 3  # Number of independent judges (1-5 recommended)
    temperature_spread: [0.3, 0.5, 0.7]  # Different temperatures for diversity
    
    # Judge archetypes and weights
    archetypes:
      - type: "logic_judge"
        weight: 1.0
      - type: "rhetoric_judge"
        weight: 1.0
      - type: "creativity_judge"
        weight: 1.0
    
  # Rubric (competition-type specific)
  rubric:
    # For philosophy_duel
    dimensions:
      depth_of_insight: 0.30
      synthesis_quality: 0.25
      quote_integration: 0.20
      dialectic_resolution: 0.15
      character_consistency: 0.10
    
    # Scoring scale
    scale:
      min: 0
      max: 100
      passing_threshold: 60
  
  # Aggregation strategy
  aggregation:
    method: "median_of_means"  # median_of_means | mean | weighted_mean
    outlier_detection: true
    outlier_factor: 1.5  # IQR multiplier
    confidence_threshold: 0.7  # Min confidence to accept score
    
  # Tie-breaking
  tie_breaking:
    criteria:
      - "technical_accuracy"
      - "citation_quality"
      - "anti_gaming_violations"
      - "character_consistency"
      - "random_with_logging"

# ============================================================================
# ANTI-GAMING CONFIGURATION
# ============================================================================
anti_gaming:
  # Enable/disable checks
  enabled: true
  
  # Paraphrasing detection (from Homunculus tests)
  paraphrasing:
    enabled: true
    similarity_threshold: 0.85
    lookback_window: 10
    penalty: -15  # Score penalty
    
  # Repetition detection
  repetition:
    enabled: true
    window_size: 5
    ratio_threshold: 0.3
    penalty: -10
    
  # Orbiting detection (from AI-Talks)
  orbiting:
    enabled: true
    similarity_threshold: 0.75
    window_size: 5
    intervention: "topic_shift"  # topic_shift | warning | end_phase
    
  # Hallucination detection
  hallucination:
    enabled: true
    require_citations: true  # For factual claims
    verification_strictness: "moderate"  # lenient | moderate | strict
    penalty_per_claim: -5
    
  # Novelty requirements
  novelty:
    minimum_score: 0.6
    competition_history_weight: 0.6
    corpus_history_weight: 0.4
    penalty: -8

# ============================================================================
# GAME THEORY CONFIGURATION
# ============================================================================
game_theory:
  # Turn selection
  turn_selection:
    method: "enhanced_payoff"  # game_theory | round_robin | random
    
    # Payoff calculation weights
    weights:
      base_contribution: 0.25
      neurochemical_drive: 0.25  # Homunculus addition
      silence_penalty: 0.15
      dominance_factor: 0.10
      coalition_bonus: 0.10
      energy_capacity: 0.10
      competitive_pressure: 0.05
    
  # Coalition dynamics
  coalitions:
    enabled: true
    formation:
      shared_values_threshold: 0.7
      mutual_benefit_required: true
      personality_compatibility: 0.5
    
    maintenance:
      trust_decay_rate: 0.05  # Per turn
      success_trust_boost: 0.1
      
    dissolution:
      betrayal_enabled: true
      betrayal_payoff_threshold: 0.8  # Must be very advantageous