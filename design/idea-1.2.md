# 🏆 AI Arena: Homunculus v2 - Master Plan (Continued)

---

## 🔧 Configuration System (Continued)

```yaml
# ============================================================================
# CHARACTER AGENT CONFIGURATION (Homunculus)
# ============================================================================
character_agents:
  # Agent orchestration
  orchestration:
    parallel_execution: true  # Run agents in parallel vs sequential
    timeout_per_agent_seconds: 3
    failure_handling: "graceful_degradation"  # fail_fast | graceful_degradation
    
  # Agent priority hierarchy
  priority:
    always_consult:
      - personality_agent
      - neurochemical_agent
    
    consult_when_relevant:
      - mood_agent
      - goals_agent
      - memory_agent
      - strategy_agent
    
    optional:
      - communication_style_agent
      - development_agent
  
  # Neurochemistry configuration
  neurochemistry:
    simulation_enabled: true
    
    decay_rates:
      dopamine: 0.15
      serotonin: 0.08
      oxytocin: 0.05
      endorphins: 0.12
      cortisol: 0.03
      adrenaline: 0.20
    
    update_frequency: "per_turn"  # per_turn | per_phase | per_competition
    
  # Memory configuration
  memory:
    episodic:
      enabled: true
      retention_policy: "all"  # all | last_n | time_based
      semantic_search: true
      max_retrieval: 5
      
    knowledge_graph:
      enabled: true
      relationship_tracking: true
      strategy_pattern_detection: true
      
  # Character state updates
  state_updates:
    neurochemistry_after_turn: true
    mood_recalculation: true
    memory_formation_after_phase: true
    relationship_update_after_competition: true
    skill_progression_after_competition: true
    personality_drift_after_n_competitions: 20

# ============================================================================
# COGNITIVE MODULE CONFIGURATION
# ============================================================================
cognitive_module:
  # LLM configuration
  llm:
    primary_model: "llama3.3:70b"  # For synthesis, complex reasoning
    fast_model: "mistral"  # For routine agents
    
    # Model selection by agent
    model_routing:
      personality_agent: "fast_model"
      mood_agent: "fast_model"
      neurochemical_agent: "none"  # Pure math
      goals_agent: "primary_model"
      communication_style_agent: "fast_model"
      memory_agent: "primary_model"
      development_agent: "fast_model"
      strategy_agent: "primary_model"
      cognitive_synthesis: "primary_model"
      
  # Synthesis configuration
  synthesis:
    conflict_resolution:
      enabled: true
      priority_based: true  # High priority agents override low priority
      dialectic_synthesis: true  # AI-Talks synthesis for perspectives
      
    # RAG integration (AI-Talks)
    rag:
      enabled: true
      style_transfer: true
      context_window: 2000  # Max tokens for retrieval context
      
  # Response generation
  response_generation:
    quality_checks:
      anti_paraphrasing: true
      anti_repetition: true
      novelty_threshold: 0.6
      length_constraints: true
      
    length_targets:
      quick_fire: [50, 150]    # words
      standard_turn: [150, 400]
      opening_statement: [200, 500]
      closing_statement: [150, 350]

# ============================================================================
# MEMORY & KNOWLEDGE INFRASTRUCTURE
# ============================================================================
infrastructure:
  # ChromaDB (Episodic Memory)
  chromadb:
    enabled: true
    host: "localhost"
    port: 8000
    
    collections:
      character_memories:
        embedding_model: "sentence-transformers/all-MiniLM-L6-v2"
        embedding_dimension: 384
        distance_metric: "cosine"
        
    persistence:
      directory: "arena/data/chroma_db/"
      backup_frequency: "daily"
      
  # Neo4j (Knowledge Graph)
  neo4j:
    enabled: true
    uri: "bolt://localhost:7687"
    database: "arena"
    
    indexes:
      - node: "Character"
        property: "character_id"
      - node: "Competition"
        property: "competition_id"
      - relationship: "COMPETED_AGAINST"
        property: "date"
        
    persistence:
      backup_frequency: "daily"
      backup_directory: "arena/data/neo4j_backups/"
      
  # FAISS (Vector Search)
  faiss:
    enabled: true
    
    indexes:
      philosophical_quotes:
        path: "arena/data/vector_stores/philosophical_quotes.index"
        size: 543
        
      scientific_references:
        path: "arena/data/vector_stores/scientific_references.index"
        size: 1200
        
      competition_corpus:
        path: "arena/data/vector_stores/competition_corpus.index"
        size: "growing"
        rebuild_threshold: 1000  # Rebuild after N new documents
        
  # Redis (State Cache)
  redis:
    enabled: true
    host: "localhost"
    port: 6379
    
    cache:
      ttl_competition_state: 3600  # 1 hour
      ttl_character_session: 7200  # 2 hours
      
    rate_limiting:
      enabled: true
      llm_requests_per_minute: 60
      
    pubsub:
      enabled: true
      channels:
        - "competition:events"
        - "character:updates"
        - "system:monitoring"

# ============================================================================
# CONTENT GENERATION CONFIGURATION
# ============================================================================
content_generation:
  # Narrator configuration
  narrator:
    enabled: true
    
    styles:
      primary: "sports_commentary"  # Primary style for live narration
      fallback: "documentary"       # Fallback if primary fails
      
    style_profiles:
      sports_commentary:
        energy_level: "high"
        metaphor_frequency: 0.7
        play_by_play: true
        
      documentary:
        analytical: true
        educational: true
        pacing: "measured"
        
      reality_tv:
        drama_focused: true
        suspense: "high"
        cliffhangers: true
        
    arc_tracking:
      enabled: true
      track_across_competitions: true
      
  # Format generators
  formats:
    podcast:
      enabled: true
      output_directory: "arena/outputs/podcasts/"
      
      structure:
        cold_open: 30  # seconds
        intro: 120
        act_1: 300
        act_2: 1080
        act_3: 300
        act_4: 300
        outro: 120
        
      audio_cues: true
      timestamp_markers: true
      
    youtube:
      enabled: true
      output_directory: "arena/outputs/youtube/"
      
      chapters: true
      visual_elements:
        - character_portraits
        - score_graphics
        - quote_overlays
        - mood_indicators
        
      seo_optimization: true
      
    blog:
      enabled: true
      output_directory: "arena/outputs/blog/"
      
      format: "markdown"  # markdown | html | rich_text
      include_graphics: true
      pull_quotes: 3
      
    social_clips:
      enabled: true
      output_directory: "arena/outputs/social/"
      
      types:
        - highlight_moment
        - character_quote
        - score_reveal
        - rivalry_moment
        
      platforms:
        - twitter
        - instagram
        - tiktok
        - youtube_shorts
        
  # Cognitive Coda Generator (AI-Talks)
  coda_generator:
    enabled: true
    
    components:
      philosophical_theorem: true
      character_development: true
      strategic_lesson: true
      memorable_quote: true
      meta_commentary: true
      
    style: "mathematical_poetic"
    max_theorem_words: 15

# ============================================================================
# PROGRESSION & RANKING CONFIGURATION
# ============================================================================
progression:
  # ELO system
  elo:
    enabled: true
    
    starting_rating: 1500
    
    k_factor:
      default: 32
      new_character: 40      # Higher volatility for new characters
      veteran: 24            # Lower volatility for experienced
      championship: 48       # Higher stakes
      
    performance_multiplier:
      enabled: true
      range: [0.5, 1.5]
      
    tiers:
      - {range: [1000, 1200], label: "Novice Competitor"}
      - {range: [1200, 1400], label: "Apprentice Debater"}
      - {range: [1400, 1600], label: "Skilled Competitor"}
      - {range: [1600, 1800], label: "Expert Strategist"}
      - {range: [1800, 2000], label: "Master of Arena"}
      - {range: [2000, 2200], label: "Grandmaster Champion"}
      - {range: [2200, 2500], label: "Legendary Competitor"}
      
  # Experience & leveling
  experience:
    enabled: true
    
    sources:
      competition_participation: 10
      competition_win_bonus: 15
      judge_score_bonus: "score_minus_70"  # (score - 70) XP
      novelty_bonus: 5  # If novelty > 0.8
      consistency_bonus: 3  # If character consistency > 0.9
      
    domain_knowledge:
      max_gain_per_competition: 5
      formula: "xp * topic_relevance * (1 - current_knowledge/100)"
      
    skill_proficiency:
      max_gain_per_competition: 0.05
      formula: "xp * skill_usage * (1 - current_proficiency)"
      
  # Unlockables
  unlockables:
    enabled: true
    
    strategies:
      - id: "coalition_master"
        requirement: "form_5_coalitions"
        benefit: "+10% coalition formation success"
        
      - id: "comeback_specialist"
        requirement: "win_3_from_20_down"
        benefit: "+15% performance when losing"
        
    abilities:
      - id: "second_wind"
        requirement: "complete_50_competitions"
        benefit: "regain_30_energy_once_per_tournament"
        
      - id: "rivalry_boost"
        requirement: "maintain_rivalry_10_matches"
        benefit: "+10% performance against rivals"
        
  # Achievements
  achievements:
    enabled: true
    tracking: true
    
    categories:
      - combat
      - style
      - social
      - meta
      
    display_in_profile: true

# ============================================================================
# OUTPUT CONFIGURATION
# ============================================================================
output:
  # Directory structure
  base_directory: "arena/outputs/"
  
  subdirectories:
    transcripts: "transcripts/"
    scores: "scores/"
    states: "character_states/"
    content: "content/"
    analytics: "analytics/"
    
  # File formats
  formats:
    transcripts: "jsonl"  # jsonl | json | txt
    scores: "json"        # json | yaml | csv
    states: "json"        # json | yaml | pickle
    
  # Naming conventions
  naming:
    timestamp_format: "ISO8601"
    include_competition_id: true
    include_character_ids: true
    
  # Retention policy
  retention:
    transcripts: "permanent"
    scores: "permanent"
    states: "permanent"
    content: "permanent"
    analytics: "1_year"
    
  # Export options
  export:
    enabled: true
    
    formats:
      - json
      - csv
      - yaml
      
    compression: "gzip"

# ============================================================================
# MONITORING & TELEMETRY
# ============================================================================
monitoring:
  # Logging
  logging:
    enabled: true
    level: "INFO"  # DEBUG | INFO | WARNING | ERROR | CRITICAL
    
    handlers:
      console:
        enabled: true
        level: "INFO"
        
      file:
        enabled: true
        level: "DEBUG"
        path: "arena/logs/"
        rotation: "daily"
        retention_days: 30
        
      structured:
        enabled: true
        format: "json"
        
  # Metrics
  metrics:
    enabled: true
    
    prometheus:
      enabled: true
      port: 9090
      
    collection_interval_seconds: 10
    
    metrics_to_track:
      - competition_duration
      - turn_response_time
      - agent_consultation_time
      - llm_inference_time
      - judge_scoring_time
      - memory_retrieval_time
      - cache_hit_rate
      - error_rate
      - anti_gaming_violations
      
  # Alerting
  alerts:
    enabled: true
    
    conditions:
      - metric: "response_time"
        threshold: 10  # seconds
        action: "log_warning"
        
      - metric: "error_rate"
        threshold: 0.05  # 5%
        action: "send_notification"
        
      - metric: "anti_gaming_violations"
        threshold: 3  # per competition
        action: "flag_for_review"
        
  # Performance profiling
  profiling:
    enabled: false  # Enable in development only
    output_directory: "arena/profiles/"

# ============================================================================
# API CONFIGURATION (Future)
# ============================================================================
api:
  enabled: false  # Not implemented in MVP
  
  rest:
    host: "0.0.0.0"
    port: 8080
    
    endpoints:
      - "/api/v1/competitions"
      - "/api/v1/characters"
      - "/api/v1/tournaments"
      - "/api/v1/content/generate"
      
    authentication:
      enabled: true
      method: "jwt"
      
    rate_limiting:
      enabled: true
      requests_per_minute: 60
      
  websocket:
    enabled: false
    host: "0.0.0.0"
    port: 8081
    
    channels:
      - "competition:live"
      - "tournament:updates"

# ============================================================================
# FEATURE FLAGS
# ============================================================================
features:
  # Core features
  character_agents: true
  competition_flow: true
  judging_system: true
  tournament_management: true
  
  # Advanced features
  coalitions: true
  neurochemistry: true
  memory_systems: true
  knowledge_graphs: true
  
  # Content generation
  narrator: true
  multi_format_output: true
  cognitive_coda: true
  
  # Experimental features
  audience_simulation: false  # Not implemented
  web_dashboard: false        # Not implemented
  multi_language: false       # Not implemented
  voice_synthesis: false      # Not implemented
  
  # Debug features
  debug_mode: false
  agent_visualization: false
  state_snapshots: false

# ============================================================================
# DEVELOPMENT & TESTING
# ============================================================================
development:
  # Environment
  environment: "development"
  
  # Seed data
  seed_data:
    enabled: true
    characters: 16
    past_competitions: 50
    
  # Testing
  testing:
    enable_test_mode: false
    mock_llm_responses: false
    deterministic_random: false  # Use fixed seed for reproducibility
    random_seed: 42
    
  # Development tools
  tools:
    hot_reload: true
    verbose_logging: true
    state_inspection: true
```

---

## 📦 Module Structure & Dependencies

### Directory Structure

```
homunculus_v2/
├── arena/
│   ├── __init__.py
│   │
│   ├── core/                          # Core abstractions
│   │   ├── __init__.py
│   │   ├── competition.py             # Competition data model
│   │   ├── character.py               # Character abstractions
│   │   ├── agent_api.py               # AgentAPI adapter (Homunculus → AI-Talks)
│   │   ├── context.py                 # Shared context objects
│   │   └── config_loader.py           # Configuration management
│   │
│   ├── flow/                          # AI-Talks flow engine
│   │   ├── __init__.py
│   │   ├── coordinator.py             # Main flow coordinator
│   │   ├── narrator_agent.py          # Narrator with multi-style support
│   │   ├── progression_analyzer.py    # Orbiting detection, quality tracking
│   │   ├── phase_manager.py           # Phase execution logic
│   │   ├── terminator.py              # Termination conditions
│   │   └── templates/                 # Flow templates (YAML)
│   │       ├── debate_v1.yml
│   │       ├── philosophy_duel_v1.yml
│   │       ├── story_battle_v1.yml
│   │       └── quick_fire_v1.yml
│   │
│   ├── persona/                       # Homunculus character agents
│   │   ├── __init__.py
│   │   ├── character_state_manager.py # State management
│   │   ├── agent_orchestrator.py      # Agent coordination
│   │   ├── agents/                    # 8 specialized agents
│   │   │   ├── __init__.py
│   │   │   ├── personality_agent.py
│   │   │   ├── mood_agent.py
│   │   │   ├── neurochemical_agent.py
│   │   │   ├── goals_agent.py
│   │   │   ├── communication_style_agent.py
│   │   │   ├── memory_agent.py
│   │   │   ├── development_agent.py
│   │   │   └── strategy_agent.py      # NEW: Competition strategy
│   │   ├── cognitive_module.py        # Synthesis + dialectic
│   │   ├── response_generator.py      # NLG with quality checks
│   │   ├── state_updater.py           # Post-turn state updates
│   │   └── schemas/                   # Character YAML schemas
│   │       └── characters/
│   │           ├── ada_lovelace.yml
│   │           ├── archmage_grimbold.yml
│   │           └── ...
│   │
│   ├── game_theory/                   # Game theory & strategy
│   │   ├── __init__.py
│   │   ├── turn_selector.py           # Enhanced payoff calculation
│   │   ├── move_selector.py           # Attack/Defend/Support/etc.
│   │   ├── payoff_calculator.py       # Neurochemical + AI-Talks payoffs
│   │   └── coalition_engine.py        # Coalition dynamics (NEW)
│   │
│   ├── judging/                       # Judging & scoring system
│   │   ├── __init__.py
│   │   ├── judge_ensemble.py          # Multiple judge coordination
│   │   ├── judge.py                   # Single judge implementation
│   │   ├── rubric_engine.py           # Dynamic rubrics
│   │   ├── anti_gaming.py             # Homunculus tests as runtime checks
│   │   ├── aggregator.py              # Score aggregation with outlier detection
│   │   └── rubrics/                   # Rubric definitions
│   │       ├── debate.yml
│   │       ├── philosophy_duel.yml
│   │       └── ...
│   │
│   ├── retrieval/                     # AI-Talks knowledge retrieval
│   │   ├── __init__.py
│   │   ├── quote_retriever.py         # Enhanced semantic search
│   │   ├── corpus_builder.py          # Build vector stores
│   │   ├── knowledge_graph_builder.py # Build Neo4j graphs
│   │   └── corpora/                   # Knowledge base files
│   │       ├── philosophical_quotes.jsonl
│   │       ├── scientific_references.jsonl
│   │       └── ...
│   │
│   ├── memory/                        # Memory & knowledge infrastructure
│   │   ├── __init__.py
│   │   ├── episodic_store.py          # ChromaDB wrapper
│   │   ├── knowledge_graph_store.py   # Neo4j wrapper
│   │   ├── vector_search_store.py     # FAISS wrapper
│   │   ├── redis_cache.py             # Redis wrapper
│   │   └── memory_bridge.py           # Competition → memory adapter
│   │
│   ├── tournament/                    # Tournament management (NEW)
│   │   ├── __init__.py
│   │   ├── tournament_manager.py      # Main tournament orchestration
│   │   ├── bracket_generator.py       # Bracket creation
│   │   ├── matchmaking_engine.py      # Intelligent matchmaking
│   │   ├── elo_system.py              # ELO rating calculations
│   │   ├── progression_tracker.py     # XP, leveling, unlocks
│   │   └── scheduler.py               # Match scheduling
│   │
│   ├── content/                       # Content generation (NEW)
│   │   ├── __init__.py
│   │   ├── narrator_extended.py       # Extended narrator with arc tracking
│   │   ├── cognitive_coda_generator.py # AI-Talks coda
│   │   ├── formatters/
│   │   │   ├── __init__.py
│   │   │   ├── podcast_formatter.py
│   │   │   ├── youtube_formatter.py
│   │   │   ├── blog_formatter.py
│   │   │   └── social_formatter.py
│   │   └── templates/                 # Content templates
│   │       ├── podcast_template.yml
│   │       └── ...
│   │
│   ├── cli/                           # Command-line interface
│   │   ├── __init__.py
│   │   ├── arena_cli.py               # Main CLI (extended from Homunculus)
│   │   ├── commands/
│   │   │   ├── __init__.py
│   │   │   ├── competition_commands.py
│   │   │   ├── tournament_commands.py
│   │   │   ├── character_commands.py
│   │   │   └── content_commands.py
│   │   └── display/
│   │       ├── __init__.py
│   │       ├── debug_view.py          # From Homunculus
│   │       └── tournament_view.py
│   │
│   ├── utils/                         # Utilities
│   │   ├── __init__.py
│   │   ├── logging_config.py
│   │   ├── metrics.py
│   │   ├── serialization.py
│   │   └── validation.py
│   │
│   └── data/                          # Data storage
│       ├── chroma_db/                 # ChromaDB files
│       ├── neo4j_data/                # Neo4j data
│       ├── vector_stores/             # FAISS indexes
│       ├── character_states/          # Saved character states
│       ├── competition_history/       # Past competitions
│       └── outputs/                   # Generated content
│           ├── transcripts/
│           ├── scores/
│           ├── podcasts/
│           ├── youtube/
│           ├── blog/
│           └── social/
│
├── tests/                             # Test suite
│   ├── __init__.py
│   ├── test_integration/              # End-to-end tests
│   │   ├── test_full_competition.py
│   │   ├── test_tournament_flow.py
│   │   └── test_character_evolution.py
│   ├── test_unit/                     # Unit tests
│   │   ├── test_agents/
│   │   ├── test_flow/
│   │   ├── test_judging/
│   │   └── test_game_theory/
│   ├── test_anti_gaming/              # Homunculus anti-gaming tests
│   │   ├── test_anti_paraphrasing.py
│   │   ├── test_anti_repetition.py
│   │   └── test_orbiting_detection.py
│   └── fixtures/                      # Test data
│       ├── character_fixtures.py
│       ├── competition_fixtures.py
│       └── mock_llm_responses.py
│
├── scripts/                           # Utility scripts
│   ├── setup_databases.py             # Initialize databases
│   ├── build_knowledge_bases.py       # Build vector stores
│   ├── seed_characters.py             # Create test characters
│   ├── run_tournament.py              # Tournament runner
│   └── generate_analytics.py          # Analytics generation
│
├── docs/                              # Documentation
│   ├── README.md
│   ├── ARCHITECTURE.md                # This document
│   ├── API_REFERENCE.md
│   ├── CHARACTER_CREATION_GUIDE.md
│   ├── FLOW_TEMPLATE_GUIDE.md
│   ├── RUBRIC_DESIGN_GUIDE.md
│   ├── DEPLOYMENT_GUIDE.md
│   └── examples/
│       ├── example_competition.md
│       ├── example_tournament.md
│       └── example_character.yml
│
├── docker/                            # Docker configuration
│   ├── Dockerfile
│   ├── docker-compose.yml             # All services
│   ├── docker-compose.arena.yml       # Arena-specific
│   └── docker-compose.dev.yml         # Development
│
├── config/                            # Configuration files
│   ├── arena.yml                      # Master config (shown above)
│   ├── development.yml
│   ├── production.yml
│   └── panels/                        # Pre-configured panels
│       ├── philosophy_experts.yml
│       ├── science_panel.yml
│       └── creative_writers.yml
│
├── requirements.txt                   # Python dependencies
├── pyproject.toml                     # Poetry config
├── .env.example                       # Environment variables template
├── .gitignore
└── LICENSE
```

---

## 🔗 Dependency Graph

### Core Dependencies

```
Competition Flow:
  arena.core.competition
    ↓
  arena.flow.coordinator
    ↓
  arena.persona.agent_api (ADAPTER LAYER)
    ↓
  ├─→ arena.persona.agent_orchestrator (Homunculus)
  │     ↓
  │   8 Specialized Agents
  │     ↓
  │   arena.persona.cognitive_module
  │     ↓
  │   arena.persona.response_generator
  │
  └─→ arena.retrieval.quote_retriever (AI-Talks)
        ↓
      arena.memory.vector_search_store

Judging:
  arena.judging.judge_ensemble
    ↓
  arena.judging.judge (multiple instances)
    ↓
  arena.judging.rubric_engine
    ↓
  arena.judging.anti_gaming (Homunculus tests)
    ↓
  arena.judging.aggregator

Memory:
  arena.memory.memory_bridge
    ↓
  ├─→ arena.memory.episodic_store (ChromaDB)
  ├─→ arena.memory.knowledge_graph_store (Neo4j)
  ├─→ arena.memory.vector_search_store (FAISS)
  └─→ arena.memory.redis_cache (Redis)

Content Generation:
  arena.content.narrator_extended
    ↓
  arena.content.cognitive_coda_generator
    ↓
  arena.content.formatters.* (podcast, youtube, blog, social)
```

### External Dependencies

```yaml
llm_infrastructure:
  - ollama: ">=0.1.0"  # Local LLM serving
  - langchain: ">=0.1.0"
  - langchain-community: ">=0.1.0"

databases:
  - chromadb: ">=0.4.0"  # Vector DB for episodic memory
  - neo4j: ">=5.0.0"     # Graph DB for knowledge
  - redis: ">=7.0.0"     # Cache & pub/sub
  - faiss-cpu: ">=1.7.0" # Vector search (or faiss-gpu)

ml_nlp:
  - sentence-transformers: ">=2.2.0"  # Embeddings
  - torch: ">=2.0.0"  # PyTorch
  - transformers: ">=4.30.0"  # HuggingFace

data_processing:
  - pandas: ">=2.0.0"
  - numpy: ">=1.24.0"
  - pydantic: ">=2.0.0"  # Data validation

cli_web:
  - typer: ">=0.9.0"  # CLI framework
  - rich: ">=13.0.0"  # Beautiful terminal
  - fastapi: ">=0.100.0"  # API (future)
  - websockets: ">=11.0.0"  # WebSocket (future)

monitoring:
  - prometheus-client: ">=0.17.0"
  - python-json-logger: ">=2.0.0"

testing:
  - pytest: ">=7.4.0"
  - pytest-asyncio: ">=0.21.0"
  - pytest-cov: ">=4.1.0"

utilities:
  - pyyaml: ">=6.0.0"
  - python-dotenv: ">=1.0.0"
  - tenacity: ">=8.2.0"  # Retry logic
```

---

## 🚀 Implementation Roadmap

### Phase 0: Repository Setup & Integration (Week 1)

**Goal**: Establish codebase foundation and verify both source repos work.

**Tasks**:
1. Create `homunculus_v2` repository structure
2. Clone both source repos for reference
3. Audit Homunculus:
   - ✅ Character loading system
   - ✅ Multi-agent orchestration
   - ✅ Memory systems (ChromaDB, Neo4j)
   - ✅ Anti-gaming tests
4. Audit AI-Talks:
   - ✅ Flow templates
   - ✅ Coordinator/Narrator
   - ✅ Quote retrieval
   - ✅ Progression analyzer
5. Set up development environment:
   - Docker Compose with all services
   - Virtual environment with dependencies
   - Development tooling (linters, formatters)

**Deliverables**:
- Empty module structure
- Working Docker Compose setup
- Both source systems running independently
- Development environment documented

---

### Phase 1: Core Integration - MVP (Weeks 2-4)

**Goal**: First working competition between 2 characters.

#### Week 2: Adapter Layer & Basic Flow

**Tasks**:
1. Implement `AgentAPI` adapter:
   ```python
   class AgentAPI:
       def __init__(self, character_id: str)
       def speak(self, context: FlowContext) -> Response
       def update_state(self, outcome: Outcome)
   ```

2. Port AI-Talks coordinator to `arena/flow/coordinator.py`:
   - Load flow template
   - Execute phases sequentially
   - Call AgentAPI for character responses

3. Port 1 flow template: `philosophy_duel_v1.yml`

4. Implement minimal judging:
   - Single LLM judge
   - Basic rubric (4 dimensions)
   - Simple scoring

**Deliverable**: 2 characters complete 1 philosophy duel with scoring.

#### Week 3: Memory Integration

**Tasks**:
1. Implement `memory_bridge.py`:
   - Store competition in ChromaDB
   - Create Neo4j relationships
   - Update character state

2. Neurochemistry updates:
   - Post-turn hormone decay
   - Post-competition deltas (win/loss)
   - Mood recalculation

3. Episodic memory retrieval:
   - Memory Agent queries past competitions
   - Semantic search for relevant experiences

**Deliverable**: Characters remember past competitions and show state changes.

#### Week 4: Anti-Gaming & Quality

**Tasks**:
1. Port Homunculus anti-gaming tests as runtime checks:
   - Anti-paraphrasing
   - Anti-repetition
   - Novelty scoring

2. Integrate AI-Talks progression analyzer:
   - Orbiting detection
   - Quality degradation alerts

3. Apply penalties to scores

**Deliverable**: System detects and penalizes gaming attempts.

---

### Phase 2: Expansion (Weeks 5-8)

#### Week 5: Multi-Character & Game Theory

**Tasks**:
1. Extend to 3-4 character competitions
2. Implement enhanced turn selection:
   - Neurochemical drive component
   - Energy capacity component
3. Test game-theoretic fairness

**Deliverable**: 4-character philosophy duel with fair turn distribution.

#### Week 6: Judge Ensemble

**Tasks**:
1. Implement 3-judge system:
   - Different temperature settings
   - Different judge archetypes
2. Score aggregation with outlier detection
3. Tie-breaking logic

**Deliverable**: Robust scoring with judge agreement metrics.

#### Week 7: Additional Competition Types

**Tasks**:
1. Create 2 more flow templates:
   - `story_battle_v1.yml`
   - `quick_fire_v1.yml`
2. Competition-specific rubrics
3. Test character performance across types

**Deliverable**: 3 working competition types.

#### Week 8: Content Generation - Basic

**Tasks**:
1. Implement Narrator Agent with 2 styles:
   - Sports commentary
   - Documentary
2. Cognitive Coda Generator
3. Basic transcript formatter

**Deliverable**: Narrated competitions with codas.

---

### Phase 3: Tournament System (Weeks 9-12)

#### Week 9: Tournament Infrastructure

**Tasks**:
1. Implement bracket generator:
   - Single elimination
   - Seeding by ELO
2. Matchmaking engine
3. Schedule management

**Deliverable**: 8-character single-elimination tournament.

#### Week 10: ELO & Progression

**Tasks**:
1. ELO rating system with performance multipliers
2. Experience & leveling
3. Domain knowledge growth
4. Skill proficiency tracking

**Deliverable**: Characters improve over time with visible stats.

#### Week 11: Coalitions (Experimental)

**Tasks**:
1. Coalition formation logic
2. Trust mechanics
3. Betrayal opportunities
4. Coalition tracking in Neo4j

**Deliverable**: Characters form/break alliances strategically.

#### Week 12: Integration & Testing

**Tasks**:
1. End-to-end tournament testing
2. Performance optimization
3. Bug fixes
4. Documentation updates

**Deliverable**: Stable tournament system running 16-character bracket.

---

### Phase 4: Content Generation Pipeline (Weeks 13-16)

#### Week 13: Multi-Format Foundations

**Tasks**:
1. Podcast script formatter with timing
2. YouTube chapter generator
3. Blog post formatter

**Deliverable**: 1 competition → 3 content formats.

#### Week 14: Social Media Clips

**Tasks**:
1. Highlight moment detector
2. Clip generators for:
   - Twitter
   - Instagram
   - TikTok
3. Auto-captions

**Deliverable**: 1 competition → 5-10 social clips.

#### Week 15: Narrator Styles & Arc Tracking

**Tasks**:
1. Add 3 more narrator styles:
   - Reality TV
   - Academic
   - Poetic
2. Character arc tracker
3. Key moment identifier

**Deliverable**: Rich narration with long-term story tracking.

#### Week 16: Polish & Automation

**Tasks**:
1. Automate content pipeline
2. Template customization
3. Quality checks for all formats

**Deliverable**: Fully automated content generation from competition data.

---

### Phase 5: Advanced Features (Weeks 17-20)

#### Week 17: Knowledge Base Expansion

**Tasks**:
1. Add 3 more domain corpora:
   - Scientific references
   - Literary canon
   - Historical events
2. Expand philosophical quotes to 1000+
3. Improve retrieval quality

**Deliverable**: 5 domain-specific knowledge bases.

#### Week 18: Character Creation Tools

**Tasks**:
1. Character YAML validator
2. Character creation wizard (CLI)
3. Personality conflict detector
4. Balance analyzer

**Deliverable**: Easy character creation with validation.

#### Week 19: Analytics & Insights

**Tasks**:
1. Competition analytics dashboard (CLI)
2. Character performance metrics
3. Meta-game analysis
4. Strategy pattern detection

**Deliverable**: Rich analytics for understanding arena dynamics.

#### Week 20: Optimization & Scaling

**Tasks**:
1. Parallel agent execution
2. Response caching
3. Model routing optimization
4. Database indexing improvements

**Deliverable**: <5s response time, support for 50+ characters.

---

### Phase 6: Platform Features (Months 6-12)

**Long-term roadmap items**:

1. **Web Dashboard** (Months 6-7):
   - Live competition viewer
   - Character profiles
   - Tournament brackets
   - Historical archive

2. **API & Webhooks** (Month 8):
   - RESTful API
   - WebSocket for live updates
   - Content generation API
   - Webhook integrations

3. **Community Features** (Month 9):
   - Custom character submissions
   - Community tournaments
   - Voting systems
   - Leaderboards

4. **Advanced AI** (Month 10):
   - Multi-modal inputs (images, video)
   - Voice synthesis for characters
   - Real-time human participation
   - Character personality fine-tuning

5. **Distribution & Monetization** (Months 11-12):
   - Content marketplace
   - Podcast network setup
   - YouTube automation
   - Sponsor integration
   - NFT character system (optional)

---

## 🎯 Critical Success Factors

### Technical Excellence

1. **Response Time**: Target <5s for turn generation
   - Parallel agent execution
   - Intelligent caching
   - Model routing (fast vs. slow models)

2. **Quality Assurance**: >80% judge agreement
   - Multiple judges with outlier detection
   - Anti-gaming systems active
   - Continuous quality monitoring

3. **Scalability**: Support 50+ characters simultaneously
   - Database sharding by character_id
   - Horizontal scaling for competitions
   - Efficient memory management

4. **Reliability**: >95% uptime
   - Graceful failure handling
   - State snapshots for recovery
   - Comprehensive error logging

### Content Quality

1. **Character Consistency**: >90% alignment score
   - Strong personality agent enforcement
   - Historical behavior tracking
   - Contradiction detection

2. **Novelty**: <10% repetition rate
   - Anti-gaming systems
   - Corpus comparison
   - Creativity scoring

3. **Engagement**: Memorable moments per competition
   - Key moment detection
   - Dramatic arc tracking
   - Viral quote identification

4. **Educational Value**: Learning opportunities
   - Dialectic synthesis quality
   - Quote integration depth
   - Concept exploration

### Platform Sustainability

1. **Maintainability**: Clean architecture
   - Modular design
   - Comprehensive documentation
   - Extensive test coverage (>80%)

2. **Extensibility**: Easy to add features
   - Plugin architecture for competition types
   - Template-based flows
   - Config-driven behavior

3. **Community**: User engagement
   - Clear character creation guide
   - Example competitions
   - Active documentation

4. **Performance Monitoring**: Continuous improvement
   - Prometheus metrics
   - Grafana dashboards
   - Automated alerting

---

## 🧪 Testing Strategy

### Test Pyramid

```
                    ┌──────────────┐
                    │  E2E Tests   │  10%
                    │  (Slow)      │
                ┌───┴──────────────┴───┐
                │  Integration Tests   │  30%
                │  (Medium)            │
        ┌───────┴──────────────────────┴───────┐
        │        Unit Tests                    │  60%
        │        (Fast)                        │
        └──────────────────────────────────────┘
```

### Test Categories

**1. Unit Tests** (60% of test suite):
```python
# Agent tests
tests/test_unit/test_agents/test_personality_agent.py
tests/test_unit/test_agents/test_neurochemical_agent.py
...

# Flow tests
tests/test_unit/test_flow/test_coordinator.py
tests/test_unit/test_flow/test_narrator.py
...

# Judging tests
tests/test_unit/test_judging/test_rubric_engine.py
tests/test_unit/test_judging/test_anti_gaming.py
...
```

**2. Integration Tests** (30% of test suite):
```python
# Agent orchestration
tests/test_integration/test_agent_orchestrator.py
- Test all agents consulted
- Test synthesis from agent inputs
- Test state updates

# Flow execution
tests/test_integration/test_flow_execution.py
- Test full phase progression
- Test termination conditions
- Test progression analyzer

# Memory systems
tests/test_integration/test_memory_integration.py
- Test ChromaDB + Neo4j together
- Test memory formation and retrieval
- Test relationship updates
```

**3. End-to-End Tests** (10% of test suite):
```python
# Full competition
tests/test_e2e/test_full_competition.py
- 2 characters complete competition
- State persisted correctly
- Content generated successfully

# Full tournament
tests/test_e2e/test_full_tournament.py
- 8 characters, single-elimination
- ELO updates correct
- Character evolution observed
```

### Anti-Gaming Test Suite (from Homunculus)

```python
# Promoted to runtime checks
tests/test_anti_gaming/test_anti_paraphrasing.py
tests/test_anti_gaming/test_anti_repetition.py
tests/test_anti_gaming/test_orbiting_detection.py
tests/test_anti_gaming/test_novelty_scoring.py
tests/test_anti_gaming/test_hallucination_detection.py

# These run during competition and apply penalties
```

### Performance Tests

```python
tests/test_performance/test_response_time.py
- Target: <5s per turn
- Measure: agent consultation, synthesis, generation

tests/test_performance/test_memory_operations.py
- Target: <500ms for retrieval
- Test: ChromaDB, Neo4j, FAISS queries

tests/test_performance/test_concurrent_competitions.py
- Target: 10 concurrent competitions
- Measure: resource utilization, response degradation
```

### Test Data & Fixtures

```python
tests/fixtures/character_fixtures.py
- 20 pre-configured test characters
- Various personality profiles
- Different experience levels

tests/fixtures/competition_fixtures.py
- Mock competition data
- Sample transcripts
- Known outcomes for validation

tests/fixtures/mock_llm_responses.py
- Deterministic LLM responses for testing
- Edge cases (very short, very long, nonsensical)
```

---

## 📊 Metrics & Monitoring

### Key Performance Indicators

**Competition Metrics**:
```yaml
competition_kpis:
  duration:
    target: "20-30 minutes"
    alert_if: ">45 minutes"
    
  turn_response_time:
    target: "<5 seconds"
    p95: "<8 seconds"
    alert_if: ">10 seconds"
    
  quality_score:
    target: ">70/100"
    excellent: ">85/100"
    alert_if: "<60/100"
    
  novelty_rate:
    target: ">0.7"
    alert_if: "<0.5"
    
  anti_gaming_violations:
    target: "0"
    acceptable: "1"
    alert_if: ">2"
```

**Character Metrics**:
```yaml
character_kpis:
  personality_consistency:
    target: ">0.9"
    alert_if: "<0.7"
    
  memory_retrieval_relevance:
    target: ">0.75"
    alert_if: "<0.5"
    
  neurochemistry_stability:
    baseline_deviation: "<30%"
    alert_if: ">50%"
    
  performance_variance:
    acceptable_range: "±15%"
    alert_if: "±30%"
```

**System Metrics**:
```yaml
system_kpis:
  llm_inference_time:
    target: "<2s"
    p95: "<4s"
    
  database_query_time:
    target: "<100ms"
    p95: "<500ms"
    
  cache_hit_rate:
    target: ">60%"
    alert_if: "<40%"
    
  error_rate:
    target: "<1%"
    alert_if: ">5%"
    
  memory_usage:
    target: "<4GB per competition"
    alert_if: ">8GB"
```

### Monitoring Dashboard (Grafana)

**Competition Dashboard**:
- Active competitions count
- Average turn response time
- Quality score distribution
- Anti-gaming violation rate
- Competition success rate

**Character Dashboard**:
- Character performance trends (ELO over time)
- Personality consistency scores
- Memory retrieval statistics
- Neurochemistry patterns
- Win rate by competition type

**System Dashboard**:
- LLM inference times
- Database performance
- Cache statistics
- Error rates
- Resource utilization (CPU, memory, disk)

### Alerting Rules

```yaml
alerts:
  critical:
    - name: "System Down"
      condition: "no_competitions_in_10_minutes"
      action: "page_on_call"
      
    - name: "High Error Rate"
      condition: "error_rate > 10%"
      action: "page_on_call"
      
  warning:
    - name: "Slow Response Time"
      condition: "p95_response_time > 10s"
      action: "slack_notification"
      
    - name: "High Anti-Gaming Violations"
      condition: "violations > 5 in last hour"
      action: "email_team"
      
  info:
    - name: "Low Cache Hit Rate"
      condition: "cache_hit_rate < 40%"
      action: "log_alert"
```

---

## 🔒 Security & Privacy Considerations

### Data Privacy

1. **Character State**: Sensitive neurochemistry, memory data
   - Encrypted at rest
   - Access controls by character owner
   - Audit logging for state modifications

2. **Competition Transcripts**: May contain personal info if custom characters
   - Optional anonymization
   - Retention policies configurable
   - GDPR compliance for EU users

3. **User Data**: If API/web interface added
   - No PII stored unless necessary
   - JWT authentication
   - Rate limiting to prevent abuse

### LLM Safety

1. **Prompt Injection Prevention**:
   - Sanitize all user inputs
   - Character prompts isolated from flow control
   - System prompts protected

2. **Content Moderation**:
   - Filter harmful content in character responses
   - Block toxic patterns
   - Respect content policies

3. **Resource Limits**:
   - Maximum token limits per response
   - Timeout enforcement
   - Rate limiting on LLM requests

---

## 🎓 Documentation Requirements

### User Documentation

1. **README.md**: Quick start guide
2. **ARCHITECTURE.md**: This document
3. **CHARACTER_CREATION_GUIDE.md**: How to create characters
4. **FLOW_TEMPLATE_GUIDE.md**: How to design competition flows
5. **RUBRIC_DESIGN_GUIDE.md**: How to create custom rubrics
6. **DEPLOYMENT_GUIDE.md**: Production deployment

### Developer Documentation

1. **API_REFERENCE.md**: Internal API docs
2. **CONTRIBUTING.md**: How to contribute
3. **TESTING_GUIDE.md**: How to run and write tests
4. **PERFORMANCE_TUNING.md**: Optimization strategies

### Example Documentation

1. **examples/example_competition.md**: Annotated competition walkthrough
2. **examples/example_tournament.md**: Tournament setup example
3. **examples/example_character.yml**: Commented character schema

---

## 🎉 Success Milestones

### MVP Milestone (Week 4)
✅ 2 characters complete philosophy duel
✅ Single judge scores competition
✅ Anti-gaming detects violations
✅ Memory persists to ChromaDB
✅ Basic CLI works

### Alpha Milestone (Week 8)
✅ 4 characters, 3 competition types
✅ 3-judge ensemble with aggregation
✅ Content generation (transcript + coda)
✅ Character state evolution observed

### Beta Milestone (Week 12)
✅ 16-character tournament completes
✅ ELO system working
✅ Coalition formation observed
✅ Multi-format content generation

### Production Milestone (Week 20)
✅ 50+ characters supported
✅ <5s response time
✅ >95% uptime
✅ Full content pipeline automated
✅ Analytics dashboard functional

---

## 🌟 Unique Value Propositions

**What makes this platform special?**

1. **Psychological Realism**: Characters aren't roleplaying—they have genuine emergent personalities driven by neurochemistry and multi-agent cognition

2. **Intellectual Depth**: AI-Talks level philosophical reasoning combined with Homunculus memory and learning creates unprecedented sophistication

3. **Authentic Drama**: Outcomes aren't scripted—rivalries, alliances, and character arcs emerge naturally from the system dynamics

4. **Multi-Format Content**: One competition generates podcast, video, blog, and social content automatically

5. **Scientific Foundation**: Built on actual cognitive architecture, game theory, and affective computing research—not just prompt engineering

6. **Continuous Evolution**: Characters genuinely learn and improve over time, building coherent long-term narratives

7. **Research Platform**: Valuable for studying multi-agent systems, emergent behavior, and AI-to-AI interaction patterns

---

## 🚦 Go/No-Go Decision Points

### After Phase 1 (Week 4):
**Evaluate**:
- Does the integration between Homunculus and AI-Talks work smoothly?
- Are characters behaving consistently with their schemas?
- Is the quality acceptable (>70/100 average)?
- Are response times reasonable (<10s)?

**Decision**: Proceed to Phase 2 only if all YES.

### After Phase 2 (Week 8):
**Evaluate**:
- Do 3+ competition types work well?
- Is judge ensemble providing reliable scores?
- Is content generation producing usable output?
- Are characters showing interesting diversity?

**Decision**: Proceed to Phase 3 only if 3/4 YES.

### After Phase 3 (Week 12):
**Evaluate**:
- Can system handle 16-character tournament?
- Is ELO system working correctly?
- Are characters visibly improving over time?
- Is the platform stable enough for extended use?

**Decision**: Proceed to Phase 4 only if all YES.

---

## 📝 Final Notes

This master plan represents the synthesis of:
- **Homunculus's** deep psychological realism and emergent behavior
- **AI-Talks's** sophisticated orchestration and semantic intelligence  
- **Novel tournament infrastructure** for competitive evolution
- **Professional content generation** for multi-format distribution

The result is a platform that doesn't just generate AI content—it creates a **living universe of AI personalities** that compete, evolve, and produce stories worth following.

The architecture is modular, the roadmap is practical, and the vision is ambitious but achievable.

**Let's build the future of AI entertainment.** 🚀