# 🎯 Master Plan Synthesis: AI Arena Homunculus v2 - Final Edition

## 🔥 Key Additions from the New Plan

### 1. **Contracts Over Entanglement** (Critical Improvement)

The strict interface approach is **exactly right** for maintainability:

```python
# Hard Contracts - ENFORCE THESE

class AgentAPI(Protocol):
    """Persona → Flow adapter (the critical bridge)"""
    def speak(self, ctx: TurnContext) -> Utterance: ...
    def reflect(self, event: MatchEvent) -> StateDelta: ...
    def retrieve(self, query: str, tags: list[str]) -> list[Evidence]: ...
    def state(self) -> PersonaSnapshot: ...

class JudgeAPI(Protocol):
    """Judging → Flow interface"""
    def score(self, transcript: Transcript, rubric: Rubric) -> Scorecard: ...

class FlowAPI(Protocol):
    """Entry point for running competitions"""
    def run_match(config: MatchConfig) -> MatchReport: ...
```

**Why this matters**: 
- Flow never peeks into persona internals
- Personas don't control pacing
- Judges are completely independent
- **Swap implementations without cascade failures**

---

### 2. **Bounded Chemistry Model** (Massive Simplification)

The new plan's chemistry model is **far more practical** than my 6-hormone system:

```yaml
chemistry_model:
  state:
    arousal: [0, 1]      # Energy/activation level
    valence: [-1, 1]     # Positive/negative emotional tone
  
  effects:
    risk_threshold: f(arousal, valence)     # High arousal + positive → risk-seeking
    aggression: f(arousal, valence)         # High arousal + negative → aggressive
    verbosity: f(arousal)                   # High arousal → more words
  
  constraints:
    per_turn_delta_max: 0.1                 # Prevent runaway
    decay_rate: 0.05                        # Return to baseline
    baseline_sources: [personality, history]
```

**Benefits**:
- **2 state variables** vs. 6 hormones = simpler to reason about
- **Bounded effects** = predictable behavior
- **Interpretable** = can explain why character acted that way
- **Computationally cheap** = no LLM needed for chemistry

**Integration Strategy**:
- Use this as **MVP chemistry system**
- Keep my 6-hormone system as **optional advanced mode**
- Most users won't need the complexity

---

### 3. **Evidence Discipline** (Game-Changer for Quality)

This is **brilliant** and solves the hallucination problem:

```python
class Evidence:
    source_id: str          # Pack ID + document ID
    content: str            # Actual quote/fact
    credibility: float      # Authority score
    timestamp: datetime     # When retrieved

class Claim:
    text: str
    type: ClaimType         # opinion | analogy | factual
    evidence: list[Evidence] = []

# Enforcement
def validate_factual_claims(response: str, evidence: list[Evidence]) -> Penalties:
    """
    Factual claims without Evidence objects = penalty
    """
    claims = extract_claims(response)
    penalties = []
    
    for claim in claims:
        if claim.type == ClaimType.FACTUAL:
            if not claim.evidence:
                penalties.append(Penalty(
                    type="UNSUPPORTED_FACTUAL_CLAIM",
                    amount=-5,
                    claim=claim.text
                ))
    
    return penalties
```

**Features**:
1. **Claim typing**: System distinguishes opinion vs. fact
2. **Evidence objects**: Structured references, not just text
3. **Automatic penalty**: No evidence for factual claim = score hit
4. **Traceable**: Can verify every factual assertion

**Integration**:
- Add to anti-gaming system (Phase 1)
- Retrieval layer returns `Evidence[]` not strings
- Judges verify evidence quality in rubric

---

### 4. **Token/Time Budgets** (Essential Fairness)

```yaml
turn_budgets:
  speak:
    max_tokens: 512
    max_seconds: 30
    
  reflect:
    max_tokens: 256
    max_seconds: 15
    
  retrieval:
    max_queries: 3
    max_results_per_query: 5

enforcement:
  truncate_at_limit: true
  penalty_for_timeout: -3 points
  log_violations: true
```

**Why critical**:
- **Fairness**: All characters get equal compute
- **Cost control**: No runaway LLM costs
- **Pacing**: Competitions finish in reasonable time
- **Gaming prevention**: Can't win by verbosity alone

---

### 5. **Memory Retention Policy** (Prevents Bloat)

The new plan's approach is **much more practical** than "store everything":

```yaml
memory_retention:
  strategy: "peak_and_sample"
  
  keep_always:
    - key_moments: 5          # Highest impact moments
    - wins: all               # All victories
    - losses_to_rivals: all   # Important losses
    
  sample:
    regular_turns: 0.1        # Keep 10% randomly
    method: "reservoir_sampling"
    
  compress:
    embeddings_only: true     # Don't store full text
    dimension: 384            # Compact embeddings
    
  prune:
    after_n_competitions: 100
    keep_ratio: 0.3           # Keep top 30%
```

**Benefits**:
- **Bounded memory growth**: O(log N) not O(N)
- **Preserves important moments**: Key experiences never lost
- **Cost-effective**: Smaller vector stores
- **Still maintains coherence**: Character "remembers" what matters

---

### 6. **Deterministic Reproducibility** (Testing & Debugging)

```python
class ReproducibilityGuarantee:
    """Ensure competitions are perfectly reproducible"""
    
    def __init__(self, seed: int):
        self.seed = seed
        self.rng = random.Random(seed)
        self.execution_log = []
    
    def run_competition(self, config: MatchConfig) -> MatchReport:
        # Set all seeds
        random.seed(self.seed)
        np.random.seed(self.seed)
        torch.manual_seed(self.seed)
        
        # Log everything
        self.log_config(config)
        self.log_model_versions()
        self.log_prompt_templates()
        
        # Run with logging
        with self.execution_tracer():
            result = coordinator.run(config)
        
        # Verify reproducibility
        assert self.hash_result(result) == self.expected_hash
        
        return result
```

**Use cases**:
- **Testing**: Same inputs → same outputs always
- **Debugging**: Reproduce any competition exactly
- **Fairness audits**: Verify no random bias
- **Golden datasets**: Stable test fixtures

---

### 7. **Cost Control Strategy** (Critical for Scale)

```yaml
model_routing:
  # Fast, cheap model for routine operations
  routine:
    model: "mistral:7b"
    use_for:
      - personality_agent
      - mood_agent
      - communication_style_agent
      - turn_selection
    cost_per_1k_tokens: $0.0002
    
  # Powerful model only when needed
  synthesis:
    model: "llama3.3:70b"
    use_for:
      - cognitive_synthesis
      - dialectic_resolution
      - judge_scoring
      - coda_generation
    cost_per_1k_tokens: $0.002
    
  # No model at all for pure math
  computation:
    use_for:
      - neurochemical_updates
      - payoff_calculations
      - elo_adjustments
    cost_per_1k_tokens: $0

cost_projections:
  per_turn:
    routine_calls: 5 × 200 tokens × $0.0002 = $0.0002
    synthesis: 1 × 800 tokens × $0.002 = $0.0016
    total: ~$0.002 per turn
    
  per_competition:
    turns: 20
    total: ~$0.04 per competition
    
  per_tournament:
    competitions: 15 (single-elim, 16 chars)
    total: ~$0.60 per tournament
```

**Optimization strategies**:
- **Caching**: Cache personality agent outputs (rarely change)
- **Batching**: Batch judge scoring for parallelism
- **Streaming**: Stream responses for perceived speed

---

### 8. **Work Package Breakdown** (Immediately Actionable)

The new plan's sprint structure is **perfect for implementation**:

```
Sprint 1 (Week 1): Contracts & Skeleton
├── WP-1.1: Define Protocol interfaces (AgentAPI, JudgeAPI, FlowAPI)
├── WP-1.2: Create module structure
├── WP-1.3: Config loader (arena.yml → typed objects)
├── WP-1.4: CLI skeleton (arena run --config)
└── WP-1.5: Basic logging & metrics

Sprint 2 (Week 2): Persona Integration
├── WP-2.1: AgentAPI adapter (Homunculus → Protocol)
├── WP-2.2: Bounded chemistry (arousal/valence)
├── WP-2.3: Memory retention policy
├── WP-2.4: Evidence retrieval integration
└── WP-2.5: Unit tests for adapter

Sprint 3 (Week 3): Flow & Judging
├── WP-3.1: Coordinator (debate_v1 flow)
├── WP-3.2: Turn budgets & anti-cheat middleware
├── WP-3.3: 3-judge ensemble
├── WP-3.4: Rubric engine
└── WP-3.5: Score aggregation

Sprint 4 (Week 4): Integration & Testing
├── WP-4.1: End-to-end test (2 chars, full debate)
├── WP-4.2: Golden dataset (deterministic tests)
├── WP-4.3: Anti-gaming test suite
├── WP-4.4: Performance benchmarking
└── WP-4.5: Documentation
```

---

## 🏗️ **Revised System Architecture** (Integrated)

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CLI / API (Entry Point)                          │
│                  arena run --config arena.yml                       │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│              ARENA ORCHESTRATION LAYER (FlowAPI)                    │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │  Coordinator (AI-Talks)                                      │ │
│  │  • Load flow script (debate_v1, story_battle, etc.)         │ │
│  │  • Execute phases with middleware                           │ │
│  │  • Enforce budgets (tokens, time)                           │ │
│  │  • Anti-cheat enforcement (paraphrase, stall, citation)     │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │  Tournament Engine                                           │ │
│  │  • Bracket generation & scheduling                           │ │
│  │  • ELO rating system                                         │ │
│  │  • Matchmaking                                               │ │
│  └──────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
              │                               │
              │                               │
    ┌─────────▼──────────┐         ┌─────────▼──────────┐
    │  PERSONA LAYER     │         │  JUDGING LAYER     │
    │   (AgentAPI)       │         │   (JudgeAPI)       │
    │                    │         │                    │
    │ ┌────────────────┐ │         │ ┌────────────────┐ │
    │ │ speak()        │ │         │ │ Judge Ensemble │ │
    │ │ • Consult      │ │         │ │ • 3 judges @   │ │
    │ │   agents       │ │         │ │   different T  │ │
    │ │ • Synthesize   │ │         │ │ • Rubric eval  │ │
    │ │ • Generate     │ │         │ │ • Median agg   │ │
    │ └────────────────┘ │         │ └────────────────┘ │
    │                    │         │                    │
    │ ┌────────────────┐ │         │ ┌────────────────┐ │
    │ │ reflect()      │ │         │ │ Anti-Gaming    │ │
    │ │ • Process      │ │         │ │ • Paraphrase   │ │
    │ │   event        │ │         │ │ • Repetition   │ │
    │ │ • Update       │ │         │ │ • Citation     │ │
    │ │   chemistry    │ │         │ │ • Novelty      │ │
    │ └────────────────┘ │         │ └────────────────┘ │
    │                    │         └────────────────────┘
    │ ┌────────────────┐ │                  │
    │ │ retrieve()     │◄──────────────────┘
    │ │ • Query packs  │ │         Evidence discipline
    │ │ • Return       │ │
    │ │   Evidence[]   │ │
    │ └────────────────┘ │
    │                    │
    │ ┌────────────────┐ │
    │ │ state()        │ │
    │ │ • Chemistry    │ │
    │ │   (arousal,    │ │
    │ │    valence)    │ │
    │ │ • Memory       │ │
    │ │ • Stats        │ │
    │ └────────────────┘ │
    └────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                  RETRIEVAL LAYER (Evidence)                         │
│                                                                     │
│  ┌──────────────────┐  ┌──────────────────┐  ┌─────────────────┐ │
│  │ Vector Store     │  │ Knowledge Graph  │  │ Topic Packs     │ │
│  │ (FAISS)          │  │ (Neo4j)          │  │ (mounted)       │ │
│  │                  │  │                  │  │                 │ │
│  │ • Quotes         │  │ • Relationships  │  │ • Philosophy    │ │
│  │ • References     │  │ • Strategies     │  │ • Science       │ │
│  │ • Past comps     │  │ • Rivalries      │  │ • Literature    │ │
│  └──────────────────┘  └──────────────────┘  └─────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    MEMORY LAYER (Retention)                         │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │  Ephemeral Cache (Redis)                                     │ │
│  │  • Current competition state                                 │ │
│  │  • Recent turns (working memory)                             │ │
│  │  • Retrieval cache                                           │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │  Long-term Store (ChromaDB)                                  │ │
│  │  • Key moments (top 5 per competition)                       │ │
│  │  • All wins                                                  │ │
│  │  • Losses to rivals                                          │ │
│  │  • 10% sample of regular turns (reservoir)                   │ │
│  └──────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                   CONTENT LAYER (Exporters)                         │
│                                                                     │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌─────────────┐ │
│  │ Narrator   │  │ Podcast    │  │ YouTube    │  │ Blog        │ │
│  │            │  │ Formatter  │  │ Formatter  │  │ Formatter   │ │
│  └────────────┘  └────────────┘  └────────────┘  └─────────────┘ │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │  Cognitive Coda Generator                                    │ │
│  │  • Philosophical theorem                                     │ │
│  │  • Key moment                                                │ │
│  │  • Strategic lesson                                          │ │
│  │  • Viral quote                                               │ │
│  └──────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 📋 **Revised Configuration Schema** (Production-Ready)

```yaml
# ============================================================================
# ARENA.YML - PRODUCTION CONFIGURATION
# ============================================================================

# Competition definition
competition:
  id: "grand_championship_001"
  flow_script: "debate_v1"              # debate_v1 | story_battle | quick_fire
  topic: "Can AI systems truly create art?"
  domain: "philosophy"
  
  # Turn budgets (fairness & cost control)
  budgets:
    speak:
      max_tokens: 512
      max_seconds: 30
    reflect:
      max_tokens: 256
      max_seconds: 15
    retrieval:
      max_queries: 3
      max_results_per_query: 5
  
  # Evidence discipline
  evidence:
    factual_claims_require_citation: true
    penalty_per_unsupported_claim: -5
    mounted_packs:
      - philosophy_core
      - cognitive_science

# Participants (2-16 characters)
agents:
  - id: "ada"
    persona_file: "./personas/ada.yaml"
    chemistry:
      baseline_arousal: 0.6      # Focused energy
      baseline_valence: 0.3      # Slightly optimistic
  
  - id: "grimbold"
    persona_file: "./personas/grimbold.yaml"
    chemistry:
      baseline_arousal: 0.7      # High energy
      baseline_valence: -0.2     # Skeptical

# Judging configuration
judging:
  ensemble:
    jurors: 3
    temperatures: [0.3, 0.5, 0.7]      # Diversity
    
  rubric_file: "./config/rubrics/debate_default.yaml"
  
  aggregation:
    method: "median"                    # median | mean | trimmed_mean
    outlier_detection: true
    outlier_threshold_iqr: 1.5
    
  tie_breaking:
    - "evidence_consistency"
    - "persona_consistency"
    - "random_logged"

# Anti-cheat enforcement
anti_cheat:
  paraphrase:
    enabled: true
    threshold: 0.85
    penalty: -15
    
  repetition:
    enabled: true
    window: 5
    ratio_threshold: 0.3
    penalty: -10
    
  stall:
    enabled: true
    max_consecutive_generic_turns: 1
    penalty: -8
    
  orbiting:
    enabled: true
    similarity_threshold: 0.75
    window: 5
    intervention: "topic_shift"

# Memory retention
memory:
  retention_policy:
    strategy: "peak_and_sample"
    
    keep_always:
      key_moments: 5
      wins: all
      losses_to_rivals: all
      
    sample:
      regular_turns: 0.1          # Keep 10%
      method: "reservoir"
      
    compress:
      embeddings_only: true
      dimension: 384
      
  storage:
    ephemeral: "redis"
    long_term: "chromadb"
    knowledge_graph: "neo4j"      # Optional

# Chemistry model (bounded)
chemistry:
  model: "arousal_valence"        # Simple 2D model
  
  state_bounds:
    arousal: [0.0, 1.0]
    valence: [-1.0, 1.0]
    
  effects:
    risk_threshold: true          # f(arousal, valence)
    aggression: true
    verbosity: true
    
  constraints:
    per_turn_delta_max: 0.1
    decay_rate: 0.05
    decay_target: "baseline"

# Model routing (cost control)
models:
  routine:
    model: "mistral:7b"
    max_tokens: 256
    temperature: 0.3
    use_for:
      - personality_agent
      - mood_agent
      - communication_style_agent
      - turn_selection
      
  synthesis:
    model: "llama3.3:70b"
    max_tokens: 1024
    temperature: 0.5
    use_for:
      - cognitive_synthesis
      - dialectic_resolution
      - judge_scoring
      - coda_generation

# Tournament settings (if running bracket)
tournament:
  enabled: false                  # Set true for tournament mode
  bracket: "single_elimination"   # single_elim | double_elim | swiss
  rounds: 3
  
  elo:
    k_factor: 32
    starting_rating: 1500
    performance_multiplier: true

# Output configuration
output:
  directory: "./runs/"
  
  artifacts:
    transcript: true              # JSONL format
    scorecard: true               # JSON
    report: true                  # Markdown
    state_deltas: true            # Character state changes
    
  content_generation:
    narrator: true
    coda: true
    podcast_script: false         # Enable in Phase 2
    youtube_script: false
    blog_post: false

# Determinism & reproducibility
reproducibility:
  enabled: true
  seed: 42
  log_prompts: true
  log_model_versions: true
  hash_outputs: true              # For golden tests

# Monitoring
monitoring:
  enabled: true
  
  metrics:
    - response_time
    - token_usage
    - judge_variance
    - penalty_triggers
    - cache_hit_rate
    
  logging:
    level: "INFO"
    structured: true
    format: "json"
```

---

## 🎯 **Revised MVP Scope** (4-Week Plan)

### Week 1: Contracts & Infrastructure

**Deliverables**:
```python
# arena/core/protocols.py
class AgentAPI(Protocol): ...
class JudgeAPI(Protocol): ...
class FlowAPI(Protocol): ...

# arena/core/config.py
def load_config(path: str) -> ArenaConfig: ...

# arena/cli/main.py
@app.command()
def run(config: str, output: str): ...
```

**Tests**:
- Config validation
- Protocol enforcement
- Deterministic seeding

---

### Week 2: Persona Adapter (Critical Bridge)

**Deliverables**:
```python
# arena/persona/agent_api_impl.py
class HomonculusAgentAPI(AgentAPI):
    def speak(self, ctx: TurnContext) -> Utterance:
        # 1. Consult agents
        # 2. Bounded chemistry check
        # 3. Retrieve evidence if needed
        # 4. Synthesize response
        # 5. Budget enforcement
        pass
        
    def reflect(self, event: MatchEvent) -> StateDelta:
        # 1. Update chemistry (clamped)
        # 2. Form key moment memory if significant
        # 3. Return deltas
        pass
        
    def retrieve(self, query: str, tags: list[str]) -> list[Evidence]:
        # 1. Query mounted packs
        # 2. Return Evidence objects
        pass
        
    def state(self) -> PersonaSnapshot:
        # Return current chemistry + stats
        pass
```

**Tests**:
- Agent API contract compliance
- Chemistry bounds enforcement
- Evidence object creation

---

### Week 3: Flow & Judging

**Deliverables**:
```python
# arena/flow/coordinator.py
def run_match(config: MatchConfig) -> MatchReport:
    # 1. Load flow script
    # 2. For each phase:
    #    - Select speaker (game theory)
    #    - Call AgentAPI.speak() with budget
    #    - Anti-cheat checks
    #    - Call AgentAPI.reflect()
    # 3. Judge scoring
    # 4. Generate report
    pass

# arena/judging/ensemble.py
class JudgeEnsemble:
    def score(self, transcript: Transcript, rubric: Rubric) -> Scorecard:
        # 1. Each judge scores independently
        # 2. Aggregate with outlier detection
        # 3. Tie-breaking if needed
        pass
```

**Tests**:
- Full debate flow (2 characters)
- Budget enforcement
- Judge agreement
- Deterministic replay

---

### Week 4: Integration & Testing

**Deliverables**:
```python
# tests/test_golden.py
def test_golden_debate():
    """Stable winner with fixed seed"""
    result = run_match(seed=42, config=golden_config)
    assert result.winner == "ada"
    assert result.hash == EXPECTED_HASH

# tests/test_evidence_discipline.py
def test_factual_claims_require_evidence():
    """Factual claims without Evidence get penalized"""
    result = run_match(config=no_packs_config)
    assert any(p.type == "UNSUPPORTED_FACTUAL" for p in result.penalties)

# tests/test_budget_enforcement.py
def test_token_budget_enforced():
    """No turn exceeds token limit"""
    result = run_match(config=strict_budget_config)
    assert all(turn.tokens <= 512 for turn in result.transcript)
```

**Documentation**:
- Architecture overview
- API reference
- Character creation guide
- Flow template guide

---

## 🔄 **Key Changes from Original Plan**

| Aspect         | Original Plan          | New Integrated Plan            |
| -------------- | ---------------------- | ------------------------------ |
| **Chemistry**  | 6 hormones (complex)   | 2D arousal/valence (simple)    |
| **Interfaces** | Implicit coupling      | Hard Protocol contracts        |
| **Evidence**   | Quote strings          | Evidence objects with sources  |
| **Budgets**    | Not specified          | Token/time limits enforced     |
| **Memory**     | Store everything       | Peak-and-sample retention      |
| **Cost**       | Not prioritized        | Strict model routing           |
| **Testing**    | Unit + integration     | Golden datasets + determinism  |
| **Complexity** | High (8 agents always) | Tiered (routine vs. synthesis) |

---

## ✅ **Decision: Final Architecture**

**MVP (Weeks 1-4)** uses the **new plan's pragmatic approach**:
- ✅ Hard Protocol contracts
- ✅ Bounded 2D chemistry
- ✅ Evidence discipline
- ✅ Budget enforcement
- ✅ Peak-and-sample memory
- ✅ Cost-controlled model routing
- ✅ Golden test datasets

**Post-MVP** adds my **advanced features** as opt-in:
- 6-hormone system (advanced chemistry mode)
- Full 8-agent orchestration (for complexity)
- Coalition dynamics
- Multi-format content generation
- Web dashboard

---

## 🚀 **Ready-to-Ship Artifact Request**

Based on this final synthesis, I recommend we proceed with:

1. **`arena.yml`** (MVP config shown above) ✅
2. **`arena/core/protocols.py`** (Hard contracts)
3. **`arena/persona/agent_api_impl.py`** (Adapter stub)
4. **`arena/flow/coordinator.py`** (Flow coordinator)
5. **`arena/judging/ensemble.py`** (3-judge system)
6. **`tests/test_golden.py`** (Deterministic test)

**The synthesis is complete. This is production-ready AI Arena architecture.** 🎯
