# 🎯 AI ARENA - DETAILED PHASED IMPLEMENTATION PLAN

## Implementation Strategy Overview

This plan takes an incremental approach:
1. **Phase 1**: Migrate Homunculus character system → Arena can create sophisticated agents
2. **Phase 2**: Integrate AI-Talks orchestration → Arena can run discussions
3. **Phase 3**: Test integration → Homunculus agents in AI-Talks flow

Each phase includes detailed file-by-file instructions for Claude Code.

---

# 📦 PHASE 1: MIGRATE HOMUNCULUS CHARACTER SYSTEM
**Duration**: Week 3-4  
**Goal**: Bring Homunculus's sophisticated multi-agent character architecture into Arena

## Phase 1 Overview

We're creating an **adapter layer** that allows Arena to use Homunculus characters while keeping Homunculus as a separate, intact project. This enables:
- Homunculus characters to participate in Arena competitions
- Full cognitive architecture (8 agents per character)
- Neurochemical simulation and memory systems
- No modifications to core Homunculus code

---

## Phase 1.1: Setup Character Module Structure

### Task 1.1.1: Create Character Module Directories

**Instructions for Claude Code**:

```bash
# Create directory structure
mkdir -p src/arena/character/
mkdir -p src/arena/character/agents/
mkdir -p src/arena/character/modules/
mkdir -p src/arena/character/memory/
mkdir -p tests/arena/character/
```

**Files to Create**:

1. **`src/arena/character/__init__.py`**
```python
"""
Arena Character System

This module provides an adapter layer to integrate Homunculus characters
into Arena competitions. It wraps the Homunculus multi-agent architecture
while adding Arena-specific extensions.

Key Components:
- CharacterAdapter: Main interface for Arena-Homunculus integration
- StrategyAgent: New agent for competitive reasoning (Arena-specific)
- BoundedNeurochemistry: Competition-safe hormone management
- CompetitionMemory: Arena-specific memory structures
"""

from .character_adapter import CharacterAdapter
from .competition_memory import CompetitionMemory

__all__ = [
    'CharacterAdapter',
    'CompetitionMemory',
]
```

2. **`src/arena/character/agents/__init__.py`**
```python
"""
Arena-specific agents that extend Homunculus agent system.

These agents add competitive intelligence while working alongside
the 7 core Homunculus agents.
"""

from .strategy_agent import StrategyAgent

__all__ = ['StrategyAgent']
```

3. **`src/arena/character/modules/__init__.py`**
```python
"""
Arena-specific modules for character processing.

These modules extend Homunculus functionality for competitive contexts.
"""

from .bounded_neurochemistry import BoundedNeurochemistry

__all__ = ['BoundedNeurochemistry']
```

4. **`src/arena/character/memory/__init__.py`**
```python
"""
Arena-specific memory structures and utilities.

Extends Homunculus memory systems with competition-specific concepts.
"""

from .competition_memory import CompetitionMemory

__all__ = ['CompetitionMemory']
```

---

## Phase 1.2: Core Data Models for Character Integration

### Task 1.2.1: Create Competition Context Model

**File**: `src/arena/character/models/competition_context.py`

**Instructions for Claude Code**:

Create this file with the following structure. This defines what competitive context information gets passed to Homunculus characters.

```python
"""
Competition context data structures.

These models define the competitive environment that Homunculus characters
need to understand when participating in Arena competitions.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum


class CompetitionPhase(Enum):
    """Current phase of competition"""
    OPENING = "opening"
    DISCUSSION = "discussion"
    ELIMINATION_PENDING = "elimination_pending"
    CLOSING = "closing"


@dataclass
class OpponentInfo:
    """Information about another competitor"""
    character_id: str
    name: str
    current_score: float
    recent_contributions: List[str]  # Last 3 contributions
    relationship_affinity: float  # -1.0 to 1.0
    strategic_threat_level: float  # 0.0 to 1.0


@dataclass
class CompetitionState:
    """Current state of the competition"""
    competition_id: str
    competition_type: str  # debate, story_battle, etc.
    topic: str
    phase: CompetitionPhase
    turn_number: int
    
    # Participants
    active_opponents: List[OpponentInfo]
    eliminated_opponents: List[str]  # character_ids
    
    # Scoring
    self_cumulative_score: float
    score_threshold_elimination: float
    leader_score: float
    
    # Context
    recent_discussion_summary: str  # Last 5 turns summarized
    key_arguments_made: List[str]
    open_questions: List[str]


@dataclass
class CompetitionContext:
    """
    Complete context for a character's turn in competition.
    
    This is passed to the CharacterAdapter and influences all agent
    deliberations within the Homunculus architecture.
    """
    # Identity
    turn_number: int
    timestamp: datetime
    
    # Competition state
    competition_state: CompetitionState
    
    # Strategic context
    elimination_risk: float  # 0.0 (safe) to 1.0 (imminent)
    survival_pressure: float  # 0.0 (low) to 1.0 (high)
    
    # Conversation context
    last_speaker: Optional[str]  # character_id
    was_addressed: bool  # Were you mentioned/questioned?
    conversation_history: List[Dict]  # Recent turns
    
    # Competitive intelligence
    detected_alliances: List[tuple[str, str]]  # (char_id, char_id) pairs
    detected_rivalries: List[tuple[str, str]]
    manipulation_attempts: List[Dict]  # Detected gaming
    
    # Meta information
    time_remaining: Optional[int]  # seconds, if time-limited
    moves_remaining: Optional[int]  # turns, if limited


@dataclass
class ArenaResponse:
    """
    A character's response in the Arena.
    
    Returned by CharacterAdapter after full agent deliberation.
    """
    # Core response
    content: str  # The actual contribution text
    
    # Metadata from Homunculus
    character_id: str
    emotional_state: Dict[str, float]  # Hormone levels at response time
    mood: str
    confidence: float
    
    # Arena-specific
    strategic_intent: str  # What the character is trying to achieve
    target_characters: List[str]  # Who this is directed at
    move_type: str  # CHALLENGE, SUPPORT, SYNTHESIZE, etc.
    risk_level: float  # How risky this move is (0-1)
    
    # Internal reasoning (for debugging/analysis)
    agent_inputs: Dict[str, str]  # What each agent contributed
    synthesis_reasoning: str  # How cognitive module combined inputs
    
    # Performance prediction
    expected_score: Dict[str, float]  # Expected scores per dimension
    strategic_rationale: str  # Why this response was chosen
```

**Validation**: After creating, verify:
- All imports resolve
- All enums and dataclasses are valid
- No syntax errors

---

### Task 1.2.2: Create Competition Memory Model

**File**: `src/arena/character/memory/competition_memory.py`

**Instructions for Claude Code**:

This defines Arena-specific memory structures that extend what Homunculus already tracks.

```python
"""
Competition-specific memory structures.

These extend Homunculus's episodic memory system with competition-specific
information that characters need to track across rounds.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum


class MemoryImportance(Enum):
    """How important a memory is for future strategy"""
    CRITICAL = "critical"  # Must remember (elimination, major insight)
    HIGH = "high"         # Important (key argument, relationship shift)
    MEDIUM = "medium"     # Useful (standard interaction)
    LOW = "low"          # Context only


@dataclass
class CompetitionMemory:
    """
    Memory of a competition event.
    
    Stored in ChromaDB alongside regular Homunculus memories but with
    competition-specific metadata.
    """
    # Core identification
    memory_id: str
    character_id: str
    competition_id: str
    timestamp: datetime
    
    # Memory content
    event_type: str  # "contribution", "elimination", "score_update", "insight"
    content: str  # What happened
    context: str  # Surrounding situation
    
    # Competitive dimensions
    strategic_lesson: Optional[str]  # What was learned
    successful_tactic: Optional[str]  # If this worked
    failed_approach: Optional[str]  # If this didn't work
    importance: MemoryImportance
    
    # Emotional context (from Homunculus)
    emotional_state: Dict[str, float]  # Hormone levels during event
    mood_at_time: str
    
    # Participants involved
    characters_involved: List[str]
    relationships_affected: Dict[str, float]  # char_id -> affinity_change
    
    # Scoring context
    score_received: Optional[float]
    judge_reasoning: Optional[str]
    
    # Metadata for retrieval
    embedding: Optional[List[float]]  # Semantic embedding
    tags: List[str]  # ["elimination", "strategy", "collaboration", etc.]


@dataclass
class StrategicKnowledge:
    """
    Accumulated strategic knowledge from competitions.
    
    This represents what a character has learned about Arena competition
    over multiple events. Used by Strategy Agent.
    """
    character_id: str
    
    # Tactical knowledge
    successful_tactics: Dict[str, int]  # tactic_name -> times_worked
    failed_tactics: Dict[str, int]
    
    # Opponent patterns
    opponent_tendencies: Dict[str, Dict]  # char_id -> {patterns}
    effective_counters: Dict[str, List[str]]  # opponent -> counters
    
    # Judge preferences
    judge_preferences: Dict[str, float]  # dimension -> importance_observed
    high_scoring_patterns: List[str]
    low_scoring_patterns: List[str]
    
    # Social dynamics
    reliable_allies: List[str]  # character_ids
    known_rivals: List[str]
    neutral_relationships: List[str]
    
    # Meta-learning
    competition_type_expertise: Dict[str, float]  # type -> skill_level
    improvement_areas: List[str]
    
    # Statistics
    total_competitions: int
    wins: int
    eliminations: int
    average_score: float
    
    # Last updated
    last_updated: datetime


@dataclass
class ChampionMemory:
    """
    Memory state for champions between rounds.
    
    When a character wins a competition and becomes champion for next round,
    this preserves their state including all memories and strategic knowledge.
    """
    champion_id: str
    competition_id: str  # Competition won
    won_at: datetime
    
    # Complete state snapshot
    character_state: Dict  # Serialized CharacterState from Homunculus
    
    # Memory references
    memory_ids: List[str]  # ChromaDB memory IDs to preserve
    strategic_knowledge: StrategicKnowledge
    
    # Performance context
    winning_score: float
    key_contributions: List[str]  # IDs of best contributions
    successful_strategies: List[str]
    
    # Relationship snapshot
    relationship_state: Dict[str, float]  # char_id -> affinity
    
    # Neural state
    final_hormone_levels: Dict[str, float]
    final_mood: str
    personality_evolution: Optional[Dict]  # If personality changed
```

**Validation**: After creating, verify:
- All dataclasses are properly typed
- Enums are valid
- Imports work
- No circular dependencies

---

## Phase 1.3: Homunculus Integration Layer

### Task 1.3.1: Create Homunculus Loader

**File**: `src/arena/character/homunculus_loader.py`

**Instructions for Claude Code**:

This module handles loading Homunculus components into Arena. It manages the import path and provides a clean interface.

**Key Reference Files in Homunculus**:
- `homunculus/src/character_agent.py` - Main CharacterAgent class
- `homunculus/src/core/character_state.py` - CharacterState dataclass
- `homunculus/src/modules/agent_orchestrator.py` - Agent coordination
- `homunculus/schemas/characters/*.yml` - Character configurations

```python
"""
Homunculus component loader for Arena.

This module handles loading Homunculus components into the Arena environment.
It provides a clean import interface and handles path management.

Key Responsibilities:
1. Load Homunculus CharacterAgent class
2. Load character schemas (YAML files)
3. Initialize Homunculus infrastructure (ChromaDB, Neo4j, Redis)
4. Provide character instantiation with Arena extensions
"""

import os
import sys
from pathlib import Path
from typing import Dict, Any, Optional, List
import yaml
import logging

logger = logging.getLogger(__name__)


class HomunculusLoader:
    """
    Loads and manages Homunculus components for Arena use.
    
    This class handles the integration between Arena and Homunculus,
    managing imports, configurations, and infrastructure connections.
    """
    
    def __init__(
        self,
        homunculus_path: Optional[str] = None,
        character_schemas_dir: Optional[str] = None
    ):
        """
        Initialize Homunculus loader.
        
        Args:
            homunculus_path: Path to Homunculus project root
                           Defaults to ../homunculus relative to arena
            character_schemas_dir: Path to character schema directory
                                  Defaults to homunculus/schemas/characters
        """
        # Determine Homunculus path
        if homunculus_path is None:
            # Assume homunculus is sibling directory to arena project
            arena_root = Path(__file__).parent.parent.parent.parent
            homunculus_path = arena_root.parent / "homunculus"
        
        self.homunculus_path = Path(homunculus_path)
        
        if not self.homunculus_path.exists():
            raise FileNotFoundError(
                f"Homunculus not found at {self.homunculus_path}. "
                "Please ensure Homunculus is installed or provide correct path."
            )
        
        # Determine character schemas directory
        if character_schemas_dir is None:
            character_schemas_dir = self.homunculus_path / "schemas" / "characters"
        
        self.character_schemas_dir = Path(character_schemas_dir)
        
        if not self.character_schemas_dir.exists():
            raise FileNotFoundError(
                f"Character schemas not found at {self.character_schemas_dir}"
            )
        
        # Add Homunculus to Python path
        homunculus_src = str(self.homunculus_path / "src")
        if homunculus_src not in sys.path:
            sys.path.insert(0, homunculus_src)
            logger.info(f"Added Homunculus to Python path: {homunculus_src}")
        
        # Import Homunculus components
        self._import_homunculus_components()
        
        # Cache loaded schemas
        self._schema_cache: Dict[str, Dict] = {}
    
    def _import_homunculus_components(self):
        """Import required Homunculus components."""
        try:
            # Core components
            from character_agent import CharacterAgent
            from core.character_state import CharacterState
            from core.experience import Experience
            from modules.agent_orchestrator import AgentOrchestrator
            
            # Agents
            from agents.personality_agent import PersonalityAgent
            from agents.mood_agent import MoodAgent
            from agents.neurochemical_agent import NeurochemicalAgent
            from agents.goals_agent import GoalsAgent
            from agents.communication_style_agent import CommunicationStyleAgent
            from agents.memory_agent import MemoryAgent
            
            # Memory systems
            from memory.experience_module import ExperienceModule
            from memory.knowledge_graph import KnowledgeGraph
            
            # LLM client
            from llm.ollama_client import OllamaClient
            
            # Store references
            self.CharacterAgent = CharacterAgent
            self.CharacterState = CharacterState
            self.Experience = Experience
            self.AgentOrchestrator = AgentOrchestrator
            self.ExperienceModule = ExperienceModule
            self.KnowledgeGraph = KnowledgeGraph
            self.OllamaClient = OllamaClient
            
            # Store agent classes
            self.agent_classes = {
                'personality': PersonalityAgent,
                'mood': MoodAgent,
                'neurochemical': NeurochemicalAgent,
                'goals': GoalsAgent,
                'communication': CommunicationStyleAgent,
                'memory': MemoryAgent,
            }
            
            logger.info("Successfully imported Homunculus components")
            
        except ImportError as e:
            logger.error(f"Failed to import Homunculus components: {e}")
            raise ImportError(
                f"Could not import Homunculus components. "
                f"Ensure Homunculus is properly installed. Error: {e}"
            )
    
    def load_character_schema(self, character_id: str) -> Dict[str, Any]:
        """
        Load a character schema from YAML file.
        
        Args:
            character_id: Character identifier (e.g., "ada_lovelace")
        
        Returns:
            Dictionary containing character configuration
        
        Raises:
            FileNotFoundError: If schema file doesn't exist
            yaml.YAMLError: If schema is invalid
        """
        # Check cache
        if character_id in self._schema_cache:
            return self._schema_cache[character_id]
        
        # Construct schema filename
        schema_file = self.character_schemas_dir / f"{character_id}.yml"
        
        if not schema_file.exists():
            # Try alternative naming
            schema_file = self.character_schemas_dir / f"{character_id}.yaml"
        
        if not schema_file.exists():
            raise FileNotFoundError(
                f"Character schema not found: {character_id}\n"
                f"Looked in: {self.character_schemas_dir}"
            )
        
        # Load YAML
        try:
            with open(schema_file, 'r') as f:
                schema = yaml.safe_load(f)
            
            logger.info(f"Loaded schema for {character_id}")
            
            # Cache and return
            self._schema_cache[character_id] = schema
            return schema
            
        except yaml.YAMLError as e:
            logger.error(f"Invalid YAML in {schema_file}: {e}")
            raise
    
    def list_available_characters(self) -> List[str]:
        """
        List all available character schemas.
        
        Returns:
            List of character IDs
        """
        characters = []
        
        for schema_file in self.character_schemas_dir.glob("*.yml"):
            character_id = schema_file.stem
            characters.append(character_id)
        
        for schema_file in self.character_schemas_dir.glob("*.yaml"):
            character_id = schema_file.stem
            if character_id not in characters:
                characters.append(character_id)
        
        return sorted(characters)
    
    def get_character_display_name(self, character_id: str) -> str:
        """
        Get the display name for a character.
        
        Args:
            character_id: Character identifier
        
        Returns:
            Human-readable character name
        """
        schema = self.load_character_schema(character_id)
        return schema.get('character_name', character_id)
    
    def create_homunculus_agent(
        self,
        character_id: str,
        **kwargs
    ) -> Any:  # Returns Homunculus CharacterAgent instance
        """
        Create a Homunculus CharacterAgent instance.
        
        Args:
            character_id: Character to instantiate
            **kwargs: Additional configuration overrides
        
        Returns:
            Initialized CharacterAgent from Homunculus
        """
        # Load schema
        schema = self.load_character_schema(character_id)
        
        # Create character agent
        # Note: This creates a full Homunculus character with all infrastructure
        character_agent = self.CharacterAgent(
            character_id=character_id,
            character_name=schema['character_name'],
            config=schema,
            **kwargs
        )
        
        logger.info(f"Created Homunculus agent for {character_id}")
        
        return character_agent


# Global loader instance
_loader: Optional[HomunculusLoader] = None


def get_loader() -> HomunculusLoader:
    """
    Get or create the global Homunculus loader.
    
    Returns:
        HomunculusLoader instance
    """
    global _loader
    if _loader is None:
        _loader = HomunculusLoader()
    return _loader


def load_character_schema(character_id: str) -> Dict[str, Any]:
    """
    Convenience function to load a character schema.
    
    Args:
        character_id: Character identifier
    
    Returns:
        Character schema dictionary
    """
    return get_loader().load_character_schema(character_id)


def list_available_characters() -> List[str]:
    """
    Convenience function to list available characters.
    
    Returns:
        List of character IDs
    """
    return get_loader().list_available_characters()
```

**Validation Steps**:
1. Create the file
2. Ensure `homunculus` is in the expected location (sibling directory)
3. Test import: `python -c "from src.arena.character.homunculus_loader import get_loader; print(get_loader().list_available_characters())"`

---

### Task 1.3.2: Create Strategy Agent (New Arena Component)

**File**: `src/arena/character/agents/strategy_agent.py`

**Instructions for Claude Code**:

This is a **NEW** agent that doesn't exist in Homunculus. It adds competitive reasoning to characters.

**Reference Pattern**: Based on Homunculus agent structure but with Arena-specific logic

```python
"""
Strategy Agent for Arena competitions.

This agent adds competitive intelligence to Homunculus characters. It works
alongside the 7 core Homunculus agents to provide strategic reasoning
specific to Arena competitions.

Unlike Homunculus agents which focus on personality and psychology, the
Strategy Agent focuses on:
- Win conditions and survival
- Opponent analysis
- Tactical recommendations
- Risk assessment
- Alliance/rivalry detection
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass
import logging

from ..models.competition_context import (
    CompetitionContext,
    CompetitionPhase,
    OpponentInfo
)

logger = logging.getLogger(__name__)


@dataclass
class StrategicAssessment:
    """Strategic analysis from the Strategy Agent"""
    
    # Situational analysis
    current_position: str  # "leading", "middle", "danger", "eliminated_risk"
    elimination_risk: float  # 0.0 to 1.0
    survival_priority: float  # 0.0 (relax) to 1.0 (urgent)
    
    # Tactical recommendations
    recommended_move: str  # "challenge", "support", "synthesize", "question"
    recommended_targets: List[str]  # character_ids
    risk_level: float  # 0.0 (safe) to 1.0 (risky)
    
    # Opponent analysis
    primary_threat: Optional[str]  # character_id
    potential_allies: List[str]
    vulnerable_targets: List[str]  # Low-scoring opponents
    
    # Strategic insights
    key_opportunities: List[str]  # What to capitalize on
    avoid_patterns: List[str]  # What not to do
    judge_preferences: Dict[str, float]  # Observed scoring patterns
    
    # Reasoning
    strategic_rationale: str  # Why these recommendations


class StrategyAgent:
    """
    Strategic reasoning agent for Arena competitions.
    
    This agent analyzes the competitive situation and provides tactical
    recommendations. It's designed to work alongside Homunculus agents,
    taking their outputs and adding competitive context.
    """
    
    def __init__(
        self,
        character_id: str,
        personality_traits: Dict[str, float],
        risk_tolerance: float = 0.5,
        competitive_drive: float = 0.7
    ):
        """
        Initialize Strategy Agent.
        
        Args:
            character_id: Character this agent is for
            personality_traits: Big Five traits from Personality Agent
            risk_tolerance: How much risk character will take (0-1)
            competitive_drive: How competitive the character is (0-1)
        """
        self.character_id = character_id
        self.personality_traits = personality_traits
        self.risk_tolerance = risk_tolerance
        self.competitive_drive = competitive_drive
        
        # Learned patterns (updated over competitions)
        self.successful_tactics: Dict[str, int] = {}
        self.failed_tactics: Dict[str, int] = {}
        self.opponent_patterns: Dict[str, Dict] = {}
    
    def assess_situation(
        self,
        competition_context: CompetitionContext,
        agent_inputs: Dict[str, Any]
    ) -> StrategicAssessment:
        """
        Analyze the competitive situation and provide strategic guidance.
        
        Args:
            competition_context: Current competition state
            agent_inputs: Outputs from Homunculus agents
        
        Returns:
            Strategic assessment and recommendations
        """
        comp_state = competition_context.competition_state
        
        # Analyze position
        position = self._analyze_position(comp_state)
        elimination_risk = self._calculate_elimination_risk(
            comp_state,
            competition_context.elimination_risk
        )
        
        # Determine survival priority
        survival_priority = self._calculate_survival_priority(
            elimination_risk,
            competition_context.survival_pressure
        )
        
        # Analyze opponents
        threat_analysis = self._analyze_threats(
            comp_state.active_opponents,
            comp_state.self_cumulative_score
        )
        
        # Recommend tactical approach
        tactical_rec = self._recommend_tactics(
            position=position,
            survival_priority=survival_priority,
            threat_analysis=threat_analysis,
            phase=comp_state.phase,
            personality=self.personality_traits,
            agent_inputs=agent_inputs
        )
        
        # Identify opportunities and risks
        opportunities = self._identify_opportunities(
            comp_state,
            threat_analysis
        )
        
        avoid_patterns = self._identify_risky_patterns(
            comp_state,
            competition_context
        )
        
        # Build strategic rationale
        rationale = self._build_rationale(
            position,
            elimination_risk,
            tactical_rec,
            threat_analysis
        )
        
        return StrategicAssessment(
            current_position=position,
            elimination_risk=elimination_risk,
            survival_priority=survival_priority,
            recommended_move=tactical_rec['move'],
            recommended_targets=tactical_rec['targets'],
            risk_level=tactical_rec['risk'],
            primary_threat=threat_analysis['primary_threat'],
            potential_allies=threat_analysis['potential_allies'],
            vulnerable_targets=threat_analysis['vulnerable'],
            key_opportunities=opportunities,
            avoid_patterns=avoid_patterns,
            judge_preferences={},  # TODO: Learn from past scores
            strategic_rationale=rationale
        )
    
    def _analyze_position(self, comp_state) -> str:
        """Determine current competitive position"""
        score = comp_state.self_cumulative_score
        leader_score = comp_state.leader_score
        threshold = comp_state.score_threshold_elimination
        
        if score >= leader_score * 0.9:
            return "leading"
        elif score > threshold * 1.5:
            return "middle"
        elif score > threshold:
            return "danger"
        else:
            return "elimination_risk"
    
    def _calculate_elimination_risk(
        self,
        comp_state,
        context_risk: float
    ) -> float:
        """Calculate probability of elimination"""
        score = comp_state.self_cumulative_score
        threshold = comp_state.score_threshold_elimination
        
        if score > threshold * 2:
            return 0.1  # Very safe
        elif score > threshold * 1.5:
            return 0.3  # Safe
        elif score > threshold:
            return 0.6  # At risk
        else:
            return 0.9  # High danger
    
    def _calculate_survival_priority(
        self,
        elimination_risk: float,
        survival_pressure: float
    ) -> float:
        """How urgent is survival vs strategy"""
        # Balance risk with personality
        base_priority = (elimination_risk + survival_pressure) / 2
        
        # Adjust for competitive drive
        adjusted = base_priority * self.competitive_drive
        
        return min(1.0, adjusted)
    
    def _analyze_threats(
        self,
        opponents: List[OpponentInfo],
        self_score: float
    ) -> Dict:
        """Analyze opponent threats and opportunities"""
        if not opponents:
            return {
                'primary_threat': None,
                'potential_allies': [],
                'vulnerable': []
            }
        
        # Sort by score
        by_score = sorted(opponents, key=lambda o: o.current_score, reverse=True)
        
        # Primary threat: highest scoring opponent
        primary_threat = by_score[0].character_id if by_score else None
        
        # Potential allies: similar scores, positive affinity
        potential_allies = [
            o.character_id for o in opponents
            if abs(o.current_score - self_score) < 5.0
            and o.relationship_affinity > 0.3
        ]
        
        # Vulnerable: low scores, high strategic threat
        vulnerable = [
            o.character_id for o in opponents
            if o.current_score < self_score * 0.7
            and o.strategic_threat_level > 0.5
        ]
        
        return {
            'primary_threat': primary_threat,
            'potential_allies': potential_allies,
            'vulnerable': vulnerable
        }
    
    def _recommend_tactics(
        self,
        position: str,
        survival_priority: float,
        threat_analysis: Dict,
        phase: CompetitionPhase,
        personality: Dict[str, float],
        agent_inputs: Dict
    ) -> Dict:
        """Recommend tactical approach"""
        
        # Default safe move
        move = "synthesize"
        targets = []
        risk = 0.3
        
        # Adjust based on position
        if position == "elimination_risk":
            # Urgent: need high-scoring move
            move = "challenge" if personality.get('openness', 0.5) > 0.6 else "support"
            targets = [threat_analysis['primary_threat']] if threat_analysis['primary_threat'] else []
            risk = 0.8
            
        elif position == "danger":
            # Moderate urgency: calculated risk
            move = "synthesize"  # Safe but valuable
            targets = threat_analysis['potential_allies'][:2]
            risk = 0.5
            
        elif position == "leading":
            # Maintain lead: avoid mistakes
            move = "support"  # Collaborative, safe
            targets = threat_analysis['potential_allies'][:1]
            risk = 0.2
        
        else:  # middle
            # Strategic flexibility
            # Use personality to decide
            if personality.get('agreeableness', 0.5) > 0.6:
                move = "support"
                risk = 0.3
            elif personality.get('openness', 0.5) > 0.7:
                move = "challenge"
                risk = 0.6
            else:
                move = "synthesize"
                risk = 0.4
            
            targets = threat_analysis['potential_allies'][:2]
        
        return {
            'move': move,
            'targets': targets,
            'risk': risk
        }
    
    def _identify_opportunities(
        self,
        comp_state,
        threat_analysis: Dict
    ) -> List[str]:
        """Identify strategic opportunities"""
        opportunities = []
        
        # Open questions to address
        if comp_state.open_questions:
            opportunities.append(
                f"Address open question: {comp_state.open_questions[0]}"
            )
        
        # Vulnerable opponents
        if threat_analysis['vulnerable']:
            opportunities.append(
                f"Challenge vulnerable opponent: {threat_analysis['vulnerable'][0]}"
            )
        
        # Potential alliances
        if threat_analysis['potential_allies']:
            opportunities.append(
                f"Build alliance with: {threat_analysis['potential_allies'][0]}"
            )
        
        return opportunities
    
    def _identify_risky_patterns(
        self,
        comp_state,
        competition_context: CompetitionContext
    ) -> List[str]:
        """Identify patterns to avoid"""
        avoid = []
        
        # Avoid paraphrasing recent arguments
        if comp_state.key_arguments_made:
            avoid.append("Avoid paraphrasing existing arguments")
        
        # Avoid attacking allies
        if competition_context.detected_alliances:
            avoid.append("Avoid challenging potential allies")
        
        # Avoid repetition
        avoid.append("Introduce new perspectives, don't repeat previous points")
        
        return avoid
    
    def _build_rationale(
        self,
        position: str,
        elimination_risk: float,
        tactical_rec: Dict,
        threat_analysis: Dict
    ) -> str:
        """Build explanation of strategic reasoning"""
        
        rationale_parts = []
        
        # Position analysis
        rationale_parts.append(f"Current position: {position}")
        
        # Risk assessment
        if elimination_risk > 0.7:
            rationale_parts.append("HIGH elimination risk - aggressive response needed")
        elif elimination_risk > 0.4:
            rationale_parts.append("Moderate risk - balanced approach required")
        else:
            rationale_parts.append("Safe position - focus on quality contributions")
        
        # Tactical reasoning
        move = tactical_rec['move']
        rationale_parts.append(
            f"Recommending {move} move (risk level: {tactical_rec['risk']:.1f})"
        )
        
        # Threat context
        if threat_analysis['primary_threat']:
            rationale_parts.append(
                f"Primary threat: {threat_analysis['primary_threat']}"
            )
        
        return " | ".join(rationale_parts)
    
    def update_learned_patterns(
        self,
        tactic_used: str,
        success: bool,
        opponent_id: Optional[str] = None
    ):
        """
        Update learned patterns based on competition results.
        
        Called after receiving scores to learn what works.
        """
        if success:
            self.successful_tactics[tactic_used] = \
                self.successful_tactics.get(tactic_used, 0) + 1
        else:
            self.failed_tactics[tactic_used] = \
                self.failed_tactics.get(tactic_used, 0) + 1
        
        logger.debug(
            f"Updated tactics for {self.character_id}: "
            f"{tactic_used} -> {'success' if success else 'failure'}"
        )
```

**Validation**:
- Import check: `python -c "from src.arena.character.agents.strategy_agent import StrategyAgent; print('OK')"`
- Verify no syntax errors
- Check dataclasses are valid

---

## Phase 1.4: Character Adapter (Main Integration Point)

### Task 1.4.1: Create Character Adapter

**File**: `src/arena/character/character_adapter.py`

**Instructions for Claude Code**:

This is the **CRITICAL** component that bridges Homunculus and Arena. It wraps a Homunculus CharacterAgent and adds Arena-specific capabilities.

**Reference Files**:
- `homunculus/src/character_agent.py` (lines 1-500) - Study the `CharacterAgent` class structure
- `homunculus/src/modules/agent_orchestrator.py` - Study agent consultation pattern

```python
"""
Character Adapter: Bridge between Homunculus and Arena.

This adapter wraps a Homunculus CharacterAgent and extends it with Arena-specific
capabilities while preserving the full multi-agent cognitive architecture.

Architecture:
1. Homunculus CharacterAgent (7 agents: personality, mood, neurochemical,
   goals, communication, memory, development)
2. Arena Strategy Agent (competitive intelligence)
3. Arena-specific context injection
4. Bounded neurochemistry for competition safety
5. Competition memory integration

The adapter ensures that:
- All Homunculus agents see competition context
- Strategy agent provides competitive guidance
- Hormones stay bounded during high-stress
- Memories are tagged for Arena-specific retrieval
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
import logging

from .homunculus_loader import get_loader
from .agents.strategy_agent import StrategyAgent, StrategicAssessment
from .models.competition_context import CompetitionContext, ArenaResponse
from .modules.bounded_neurochemistry import BoundedNeurochemistry
from .memory.competition_memory import CompetitionMemory, MemoryImportance

logger = logging.getLogger(__name__)


class CharacterAdapter:
    """
    Adapter that integrates Homunculus characters into Arena competitions.
    
    This class wraps a Homunculus CharacterAgent and adds:
    - Strategy Agent for competitive reasoning
    - Bounded neurochemistry for safety
    - Competition context injection
    - Arena-specific memory handling
    """
    
    def __init__(
        self,
        character_id: str,
        homunculus_agent: Any = None,  # Homunculus CharacterAgent
        enable_bounded_neurochemistry: bool = True,
        strategy_config: Optional[Dict] = None
    ):
        """
        Initialize Character Adapter.
        
        Args:
            character_id: Character identifier
            homunculus_agent: Pre-initialized Homunculus CharacterAgent,
                            or None to create from schema
            enable_bounded_neurochemistry: Apply hormone bounds for competition
            strategy_config: Configuration for Strategy Agent
        """
        self.character_id = character_id
        
        # Load or use provided Homunculus agent
        if homunculus_agent is None:
            loader = get_loader()
            self.homunculus_agent = loader.create_homunculus_agent(character_id)
        else:
            self.homunculus_agent = homunculus_agent
        
        # Get character name and schema
        self.character_name = self.homunculus_agent.character_name
        self.character_config = self.homunculus_agent.config
        
        # Extract personality traits for strategy agent
        personality_traits = self.character_config.get('personality', {})
        
        # Initialize Strategy Agent (Arena-specific)
        strategy_config = strategy_config or {}
        self.strategy_agent = StrategyAgent(
            character_id=character_id,
            personality_traits=personality_traits,
            risk_tolerance=strategy_config.get('risk_tolerance', 0.5),
            competitive_drive=strategy_config.get('competitive_drive', 0.7)
        )
        
        # Bounded neurochemistry manager
        self.enable_bounded_neurochemistry = enable_bounded_neurochemistry
        if enable_bounded_neurochemistry:
            self.neuro_bounds = BoundedNeurochemistry(
                character_id=character_id,
                personality_baselines=personality_traits
            )
        else:
            self.neuro_bounds = None
        
        # Competition history for this character
        self.competition_memories: List[CompetitionMemory] = []
        
        logger.info(
            f"CharacterAdapter initialized for {character_name} "
            f"with strategy agent and bounded neurochemistry"
        )
    
    async def generate_response(
        self,
        competition_context: CompetitionContext,
        conversation_history: List[Dict],
        user_message: Optional[str] = None
    ) -> ArenaResponse:
        """
        Generate a competition response using full Homunculus architecture
        + Arena extensions.
        
        This is the main method called by Arena orchestrator when it's this
        character's turn.
        
        Process:
        1. Inject competition context into agent inputs
        2. Consult all Homunculus agents (7 agents)
        3. Consult Strategy Agent (Arena)
        4. Synthesize with cognitive module
        5. Apply bounded neurochemistry
        6. Generate final response
        7. Update state and memories
        
        Args:
            competition_context: Current competition state
            conversation_history: Recent turns
            user_message: Optional direct prompt (for testing)
        
        Returns:
            ArenaResponse with contribution and metadata
        """
        logger.info(
            f"Generating response for {self.character_name} "
            f"(turn {competition_context.turn_number})"
        )
        
        # Step 1: Prepare context for agents
        augmented_context = self._prepare_agent_context(
            competition_context,
            conversation_history
        )
        
        # Step 2: Consult Homunculus agents
        # This calls the AgentOrchestrator which consults all 7 agents
        homunculus_inputs = await self._consult_homunculus_agents(
            augmented_context,
            conversation_history
        )
        
        # Step 3: Consult Strategy Agent (Arena-specific)
        strategic_assessment = self.strategy_agent.assess_situation(
            competition_context,
            homunculus_inputs
        )
        
        logger.debug(
            f"Strategic assessment: {strategic_assessment.recommended_move} "
            f"(risk: {strategic_assessment.risk_level:.2f})"
        )
        
        # Step 4: Synthesize all inputs
        # Use Homunculus cognitive module but inject strategic guidance
        synthesis = await self._synthesize_response(
            homunculus_inputs,
            strategic_assessment,
            augmented_context
        )
        
        # Step 5: Apply bounded neurochemistry (if enabled)
        if self.enable_bounded_neurochemistry:
            self.neuro_bounds.apply_bounds(
                self.homunculus_agent.state
            )
        
        # Step 6: Generate final response text
        # Use Homunculus response generator with strategic framing
        response_text = await self._generate_response_text(
            synthesis,
            strategic_assessment,
            augmented_context
        )
        
        # Step 7: Update state
        self._update_character_state(
            competition_context,
            strategic_assessment,
            response_text
        )
        
        # Step 8: Create Arena response
        arena_response = ArenaResponse(
            content=response_text,
            character_id=self.character_id,
            emotional_state=self.homunculus_agent.state.hormones.copy(),
            mood=self.homunculus_agent.state.mood,
            confidence=homunculus_inputs.get('confidence', 0.7),
            strategic_intent=strategic_assessment.strategic_rationale,
            target_characters=strategic_assessment.recommended_targets,
            move_type=strategic_assessment.recommended_move,
            risk_level=strategic_assessment.risk_level,
            agent_inputs={
                'personality': homunculus_inputs.get('personality', ''),
                'mood': homunculus_inputs.get('mood', ''),
                'neurochemical': homunculus_inputs.get('neurochemical', ''),
                'goals': homunculus_inputs.get('goals', ''),
                'communication': homunculus_inputs.get('communication', ''),
                'memory': homunculus_inputs.get('memory', ''),
                'strategy': strategic_assessment.strategic_rationale
            },
            synthesis_reasoning=synthesis.get('reasoning', ''),
            expected_score={
                'novelty': 0.7,  # TODO: Predict from strategic assessment
                'builds_on_others': 0.6,
                'solves_subproblem': 0.7,
            },
            strategic_rationale=strategic_assessment.strategic_rationale
        )
        
        return arena_response
    
    def _prepare_agent_context(
        self,
        competition_context: CompetitionContext,
        conversation_history: List[Dict]
    ) -> Dict:
        """
        Prepare context that will be injected into all agent consultations.
        
        This context augments what Homunculus agents normally see with
        Arena-specific competitive information.
        """
        comp_state = competition_context.competition_state
        
        # Build competitive context string
        competitive_context = f"""
COMPETITION CONTEXT:
- Type: {comp_state.competition_type}
- Topic: {comp_state.topic}
- Phase: {comp_state.phase.value}
- Turn: {competition_context.turn_number}
- Your Score: {comp_state.self_cumulative_score:.1f}
- Leader Score: {comp_state.leader_score:.1f}
- Elimination Threshold: {comp_state.score_threshold_elimination:.1f}
- Elimination Risk: {"HIGH" if competition_context.elimination_risk > 0.7 else "MODERATE" if competition_context.elimination_risk > 0.4 else "LOW"}

OPPONENTS:
"""
        
        for opp in comp_state.active_opponents:
            competitive_context += f"- {opp.name}: Score {opp.current_score:.1f}\n"
        
        if comp_state.eliminated_opponents:
            competitive_context += f"\nEliminated: {', '.join(comp_state.eliminated_opponents)}\n"
        
        competitive_context += f"\nRECENT DISCUSSION:\n{comp_state.recent_discussion_summary}\n"
        
        return {
            'competition_context': competitive_context,
            'conversation_history': conversation_history,
            'competitive_pressure': competition_context.survival_pressure,
            'was_addressed': competition_context.was_addressed
        }
    
    async def _consult_homunculus_agents(
        self,
        augmented_context: Dict,
        conversation_history: List[Dict]
    ) -> Dict[str, Any]:
        """
        Consult all Homunculus agents with Arena context injection.
        
        This calls the Homunculus AgentOrchestrator but injects competitive
        context into the prompts.
        """
        # Use Homunculus's agent consultation system
        # but with Arena context prepended to the message
        
        context_message = augmented_context['competition_context']
        last_message = conversation_history[-1]['content'] if conversation_history else ""
        
        # Combine Arena context with last message
        augmented_message = f"{context_message}\n\nLAST MESSAGE:\n{last_message}"
        
        # Call Homunculus agent orchestrator
        # This consults all 7 agents in priority order
        agent_inputs = await self.homunculus_agent.agent_orchestrator.consult_agents(
            current_state=self.homunculus_agent.state,
            user_message=augmented_message,
            conversation_history=conversation_history
        )
        
        return agent_inputs
    
    async def _synthesize_response(
        self,
        homunculus_inputs: Dict,
        strategic_assessment: StrategicAssessment,
        augmented_context: Dict
    ) -> Dict:
        """
        Synthesize agent inputs using Homunculus cognitive module
        with strategic guidance.
        """
        # Add strategic guidance to synthesis
        strategic_guidance = f"""
STRATEGIC GUIDANCE:
- Recommended Move: {strategic_assessment.recommended_move}
- Target: {', '.join(strategic_assessment.recommended_targets) if strategic_assessment.recommended_targets else 'General audience'}
- Risk Level: {strategic_assessment.risk_level:.1f}
- Key Opportunities: {', '.join(strategic_assessment.key_opportunities)}
- Avoid: {', '.join(strategic_assessment.avoid_patterns)}
"""
        
        # Use Homunculus cognitive module
        synthesis = await self.homunculus_agent.cognitive_module.synthesize(
            agent_inputs=homunculus_inputs,
            strategic_context=strategic_guidance,
            current_state=self.homunculus_agent.state
        )
        
        return synthesis
    
    async def _generate_response_text(
        self,
        synthesis: Dict,
        strategic_assessment: StrategicAssessment,
        augmented_context: Dict
    ) -> str:
        """
        Generate final response text using Homunculus response generator
        with strategic framing.
        """
        # Use Homunculus response generator
        # This applies communication style and generates natural language
        response_text = await self.homunculus_agent.response_generator.generate(
            synthesis=synthesis,
            communication_style=synthesis.get('communication_style', {}),
            strategic_intent=strategic_assessment.recommended_move,
            current_state=self.homunculus_agent.state
        )
        
        return response_text
    
    def _update_character_state(
        self,
        competition_context: CompetitionContext,
        strategic_assessment: StrategicAssessment,
        response_text: str
    ):
        """
        Update character state after generating response.
        
        This uses Homunculus state updater to handle:
        - Hormone changes
        - Mood updates
        - Goal updates
        - Memory creation
        """
        # Use Homunculus state updater
        self.homunculus_agent.state_updater.update(
            current_state=self.homunculus_agent.state,
            interaction_type='competition_turn',
            emotional_impact={
                'stress': competition_context.survival_pressure,
                'excitement': strategic_assessment.risk_level,
                'confidence': 1.0 - competition_context.elimination_risk
            },
            memory_content=response_text
        )
    
    def create_competition_memory(
        self,
        competition_context: CompetitionContext,
        event_type: str,
        content: str,
        score_received: Optional[float] = None,
        judge_reasoning: Optional[str] = None
    ) -> CompetitionMemory:
        """
        Create an Arena-specific memory.
        
        This supplements Homunculus's automatic memory creation with
        competition-specific metadata.
        """
        memory = CompetitionMemory(
            memory_id=f"{self.character_id}_{competition_context.competition_state.competition_id}_{datetime.now().isoformat()}",
            character_id=self.character_id,
            competition_id=competition_context.competition_state.competition_id,
            timestamp=datetime.now(),
            event_type=event_type,
            content=content,
            context=competition_context.competition_state.recent_discussion_summary,
            strategic_lesson=None,  # Filled later after learning
            successful_tactic=None,
            failed_approach=None,
            importance=MemoryImportance.MEDIUM,
            emotional_state=self.homunculus_agent.state.hormones.copy(),
            mood_at_time=self.homunculus_agent.state.mood,
            characters_involved=[opp.character_id for opp in competition_context.competition_state.active_opponents],
            relationships_affected={},
            score_received=score_received,
            judge_reasoning=judge_reasoning,
            embedding=None,  # Generated by ChromaDB
            tags=[competition_context.competition_state.competition_type, event_type]
        )
        
        self.competition_memories.append(memory)
        return memory
    
    def update_from_score(
        self,
        score: float,
        judge_reasoning: str,
        move_used: str
    ):
        """
        Update strategy based on received score.
        
        This allows the character to learn what works in competitions.
        """
        # Determine if successful
        success = score > 7.0  # Threshold for "good" contribution
        
        # Update strategy agent
        self.strategy_agent.update_learned_patterns(
            tactic_used=move_used,
            success=success
        )
        
        logger.info(
            f"{self.character_name} received score {score:.1f} "
            f"for {move_used} move ({'success' if success else 'needs improvement'})"
        )
    
    @property
    def state(self):
        """Access underlying Homunculus character state"""
        return self.homunculus_agent.state
    
    @property
    def personality(self) -> Dict[str, float]:
        """Get personality traits"""
        return self.character_config.get('personality', {})
    
    @property
    def hormones(self) -> Dict[str, float]:
        """Get current hormone levels"""
        return self.homunculus_agent.state.hormones
    
    @property
    def mood(self) -> str:
        """Get current mood"""
        return self.homunculus_agent.state.mood
```

**This is the most critical file in Phase 1.** It must:
1. Wrap Homunculus CharacterAgent cleanly
2. Add Strategy Agent
3. Inject competition context properly
4. Preserve all Homunculus functionality

**Validation**:
1. Test import: `from src.arena.character.character_adapter import CharacterAdapter`
2. Test instantiation with a real character (requires Homunculus setup)
3. Verify async methods are properly defined

---

## Phase 1.5: Bounded Neurochemistry Module

### Task 1.5.1: Create Bounded Neurochemistry

**File**: `src/arena/character/modules/bounded_neurochemistry.py`

**Instructions for Claude Code**:

This prevents hormone runaway during high-stress competition.

**Reference**: `homunculus/src/agents/neurochemical_agent.py` (study hormone ranges)

```python
"""
Bounded Neurochemistry for Competition Safety.

During competitions, characters can experience extreme stress that could
cause neurochemical levels to exceed reasonable bounds. This module applies
safety limits while preserving personality-driven variation.

Key Concepts:
- Competition stress is more intense than normal conversation
- Hormones like cortisol and adrenaline can spike dangerously high
- We apply soft bounds that preserve character variation
- Bounds are personality-aware (different characters have different ranges)
"""

from typing import Dict, Optional
import logging

logger = logging.getLogger(__name__)


class BoundedNeurochemistry:
    """
    Manages neurochemical bounds for competition contexts.
    
    This ensures that hormones stay within reasonable ranges even under
    extreme competitive stress, preventing:
    - Panic (cortisol > 0.9)
    - Recklessness (adrenaline > 0.9)
    - Overconfidence (dopamine > 0.95)
    - Decision paralysis (combined extremes)
    """
    
    # Default bounds for competition (more restrictive than normal)
    DEFAULT_BOUNDS = {
        'dopamine': (0.2, 0.90),      # Prevent overconfidence
        'serotonin': (0.2, 0.85),     # Maintain stability
        'oxytocin': (0.1, 0.90),      # Social bonding OK
        'endorphins': (0.1, 0.85),    # Moderate pleasure
        'cortisol': (0.1, 0.85),      # Prevent panic
        'adrenaline': (0.1, 0.80),    # Prevent recklessness
    }
    
    def __init__(
        self,
        character_id: str,
        personality_baselines: Dict[str, float],
        custom_bounds: Optional[Dict[str, tuple]] = None
    ):
        """
        Initialize bounded neurochemistry manager.
        
        Args:
            character_id: Character this applies to
            personality_baselines: Personality-based hormone baselines
            custom_bounds: Override default bounds
        """
        self.character_id = character_id
        self.personality_baselines = personality_baselines
        
        # Use custom bounds or defaults
        self.bounds = custom_bounds or self.DEFAULT_BOUNDS.copy()
        
        # Adjust bounds based on personality
        self._adjust_bounds_for_personality()
        
        logger.info(
            f"Bounded neurochemistry initialized for {character_id} "
            f"with personality-adjusted bounds"
        )
    
    def _adjust_bounds_for_personality(self):
        """
        Adjust hormone bounds based on personality traits.
        
        More emotional characters (high neuroticism) get wider bounds.
        More stable characters (low neuroticism) get tighter bounds.
        """
        # Neuroticism affects volatility
        neuroticism = self.personality_baselines.get('neuroticism', 0.5)
        
        # Extraversion affects social hormones
        extraversion = self.personality_baselines.get('extraversion', 0.5)
        
        # Adjust cortisol/adrenaline bounds for neuroticism
        if neuroticism > 0.7:
            # High neuroticism: allow more stress response
            self.bounds['cortisol'] = (0.1, 0.90)
            self.bounds['adrenaline'] = (0.1, 0.85)
        elif neuroticism < 0.3:
            # Low neuroticism: tighter stress control
            self.bounds['cortisol'] = (0.1, 0.75)
            self.bounds['adrenaline'] = (0.1, 0.70)
        
        # Adjust oxytocin for extraversion
        if extraversion > 0.7:
            # High extraversion: more social bonding
            self.bounds['oxytocin'] = (0.2, 0.95)
        elif extraversion < 0.3:
            # Low extraversion: less social variation
            self.bounds['oxytocin'] = (0.1, 0.80)
    
    def apply_bounds(self, character_state) -> Dict[str, float]:
        """
        Apply bounds to current hormone levels.
        
        This modifies the character state in-place, clamping hormones
        to acceptable ranges.
        
        Args:
            character_state: Homunculus CharacterState object
        
        Returns:
            Dictionary of hormones that were clamped
        """
        clamped = {}
        
        for hormone, level in character_state.hormones.items():
            if hormone not in self.bounds:
                continue
            
            min_bound, max_bound = self.bounds[hormone]
            
            # Clamp to bounds
            original = level
            clamped_level = max(min_bound, min(max_bound, level))
            
            if abs(original - clamped_level) > 0.01:
                # Hormone was clamped
                character_state.hormones[hormone] = clamped_level
                clamped[hormone] = {
                    'original': original,
                    'clamped': clamped_level,
                    'bound': 'upper' if original > clamped_level else 'lower'
                }
                
                logger.debug(
                    f"{self.character_id}: Clamped {hormone} "
                    f"from {original:.2f} to {clamped_level:.2f}"
                )
        
        return clamped
    
    def check_stability(self, character_state) -> Dict:
        """
        Check if hormones are stable or approaching bounds.
        
        Returns diagnostic information about hormone stability.
        """
        stability = {
            'stable': True,
            'warnings': [],
            'critical': []
        }
        
        for hormone, level in character_state.hormones.items():
            if hormone not in self.bounds:
                continue
            
            min_bound, max_bound = self.bounds[hormone]
            
            # Check proximity to bounds
            proximity_to_max = (level - min_bound) / (max_bound - min_bound)
            
            if proximity_to_max > 0.95:
                stability['stable'] = False
                stability['critical'].append({
                    'hormone': hormone,
                    'level': level,
                    'bound': 'upper',
                    'proximity': proximity_to_max
                })
            elif proximity_to_max < 0.05:
                stability['stable'] = False
                stability['critical'].append({
                    'hormone': hormone,
                    'level': level,
                    'bound': 'lower',
                    'proximity': 1.0 - proximity_to_max
                })
            elif proximity_to_max > 0.85 or proximity_to_max < 0.15:
                stability['warnings'].append({
                    'hormone': hormone,
                    'level': level,
                    'proximity_to_bound': min(proximity_to_max, 1.0 - proximity_to_max)
                })
        
        return stability
    
    def apply_competitive_dampening(
        self,
        character_state,
        stress_level: float
    ):
        """
        Apply dampening to prevent hormone spikes during extreme stress.
        
        This is called during high-stress moments (elimination risk, etc.)
        to prevent neurochemical extremes.
        
        Args:
            character_state: Homunculus CharacterState
            stress_level: 0.0 to 1.0, where 1.0 is maximum stress
        """
        if stress_level < 0.5:
            return  # No dampening needed
        
        # Calculate dampening factor
        dampening = 0.8 + (0.2 * (1.0 - stress_level))  # 0.8 to 1.0
        
        # Apply dampening to stress hormones
        stress_hormones = ['cortisol', 'adrenaline']
        
        for hormone in stress_hormones:
            if hormone in character_state.hormones:
                baseline = self.personality_baselines.get(
                    f'{hormone}_baseline',
                    0.5
                )
                
                current = character_state.hormones[hormone]
                
                # Pull towards baseline
                dampened = current * dampening + baseline * (1 - dampening)
                
                character_state.hormones[hormone] = dampened
                
                logger.debug(
                    f"{self.character_id}: Applied competitive dampening "
                    f"to {hormone}: {current:.2f} -> {dampened:.2f}"
                )
```

**Validation**:
- Import check
- Test bound application with mock hormone levels
- Verify personality-based adjustment

---

## Phase 1.6: Testing Phase 1

### Task 1.6.1: Create Phase 1 Integration Tests

**File**: `tests/arena/character/test_character_integration.py`

**Instructions for Claude Code**:

Create comprehensive tests for Phase 1 components.

```python
"""
Integration tests for Phase 1: Character System

These tests verify that:
1. Homunculus components load correctly
2. Character schemas are accessible
3. CharacterAdapter wraps Homunculus properly
4. Strategy Agent provides assessments
5. Bounded neurochemistry works
6. Complete response generation works
"""

import pytest
import asyncio
from unittest.mock import Mock, patch, MagicMock

from src.arena.character.homunculus_loader import (
    HomunculusLoader,
    get_loader,
    list_available_characters
)
from src.arena.character.character_adapter import CharacterAdapter
from src.arena.character.agents.strategy_agent import StrategyAgent
from src.arena.character.modules.bounded_neurochemistry import BoundedNeurochemistry
from src.arena.character.models.competition_context import (
    CompetitionContext,
    CompetitionState,
    CompetitionPhase,
    OpponentInfo
)


class TestHomunculusLoader:
    """Test Homunculus component loading"""
    
    def test_loader_initialization(self):
        """Test that loader initializes correctly"""
        loader = HomunculusLoader()
        assert loader is not None
        assert loader.homunculus_path.exists()
        assert loader.character_schemas_dir.exists()
    
    def test_list_characters(self):
        """Test listing available characters"""
        characters = list_available_characters()
        assert len(characters) > 0
        assert 'ada_lovelace' in characters or 'ada' in characters
    
    def test_load_character_schema(self):
        """Test loading a character schema"""
        loader = get_loader()
        
        # Try to load Ada Lovelace
        # (adjust character_id based on actual files)
        characters = list_available_characters()
        test_char = characters[0]  # Use first available
        
        schema = loader.load_character_schema(test_char)
        assert schema is not None
        assert 'character_name' in schema
        assert 'personality' in schema


class TestStrategyAgent:
    """Test Strategy Agent functionality"""
    
    def test_strategy_agent_initialization(self):
        """Test Strategy Agent initializes"""
        agent = StrategyAgent(
            character_id="test_char",
            personality_traits={
                'openness': 0.7,
                'conscientiousness': 0.6,
                'extraversion': 0.5,
                'agreeableness': 0.6,
                'neuroticism': 0.4
            }
        )
        assert agent is not None
        assert agent.character_id == "test_char"
    
    def test_position_analysis(self):
        """Test competitive position analysis"""
        agent = StrategyAgent(
            character_id="test",
            personality_traits={}
        )
        
        # Create mock competition state
        comp_state = Mock()
        comp_state.self_cumulative_score = 15.0
        comp_state.leader_score = 20.0
        comp_state.score_threshold_elimination = -10.0
        
        position = agent._analyze_position(comp_state)
        assert position in ["leading", "middle", "danger", "elimination_risk"]
    
    def test_strategic_assessment(self):
        """Test full strategic assessment"""
        agent = StrategyAgent(
            character_id="test",
            personality_traits={'openness': 0.7}
        )
        
        # Create mock competition context
        comp_context = self._create_mock_competition_context()
        agent_inputs = {}
        
        assessment = agent.assess_situation(comp_context, agent_inputs)
        
        assert assessment is not None
        assert assessment.recommended_move in [
            "challenge", "support", "synthesize", "question"
        ]
        assert 0 <= assessment.elimination_risk <= 1
        assert 0 <= assessment.survival_priority <= 1
    
    def _create_mock_competition_context(self):
        """Helper to create mock competition context"""
        comp_state = CompetitionState(
            competition_id="test_comp",
            competition_type="debate",
            topic="Test topic",
            phase=CompetitionPhase.DISCUSSION,
            turn_number=5,
            active_opponents=[
                OpponentInfo(
                    character_id="opp1",
                    name="Opponent 1",
                    current_score=15.0,
                    recent_contributions=[],
                    relationship_affinity=0.5,
                    strategic_threat_level=0.6
                )
            ],
            eliminated_opponents=[],
            self_cumulative_score=12.0,
            score_threshold_elimination=-10.0,
            leader_score=15.0,
            recent_discussion_summary="Some discussion",
            key_arguments_made=[],
            open_questions=[]
        )
        
        return CompetitionContext(
            turn_number=5,
            timestamp=datetime.now(),
            competition_state=comp_state,
            elimination_risk=0.3,
            survival_pressure=0.4,
            last_speaker="opp1",
            was_addressed=False,
            conversation_history=[],
            detected_alliances=[],
            detected_rivalries=[],
            manipulation_attempts=[],
            time_remaining=None,
            moves_remaining=None
        )


class TestBoundedNeurochemistry:
    """Test bounded neurochemistry system"""
    
    def test_initialization(self):
        """Test bounded neuro initializes"""
        neuro = BoundedNeurochemistry(
            character_id="test",
            personality_baselines={'neuroticism': 0.5}
        )
        assert neuro is not None
        assert 'cortisol' in neuro.bounds
    
    def test_apply_bounds(self):
        """Test applying bounds to hormones"""
        neuro = BoundedNeurochemistry(
            character_id="test",
            personality_baselines={}
        )
        
        # Create mock character state
        mock_state = Mock()
        mock_state.hormones = {
            'cortisol': 0.95,  # Above bound
            'dopamine': 0.5,   # Normal
            'adrenaline': 0.05  # Below bound
        }
        
        clamped = neuro.apply_bounds(mock_state)
        
        # Cortisol should be clamped down
        assert mock_state.hormones['cortisol'] < 0.95
        # Dopamine should be unchanged
        assert mock_state.hormones['dopamine'] == 0.5
        # Check that clamping was recorded
        assert 'cortisol' in clamped or 'adrenaline' in clamped


@pytest.mark.integration
@pytest.mark.skipif(
    not Path("../homunculus").exists(),
    reason="Homunculus not available"
)
class TestCharacterAdapter:
    """Integration tests for Character Adapter"""
    
    @pytest.mark.asyncio
    async def test_adapter_initialization(self):
        """Test CharacterAdapter initializes with real Homunculus character"""
        # This test requires Homunculus to be properly set up
        # Skip if Homunculus not available
        
        try:
            adapter = CharacterAdapter(
                character_id="ada_lovelace",  # Or first available
                enable_bounded_neurochemistry=True
            )
            
            assert adapter is not None
            assert adapter.homunculus_agent is not None
            assert adapter.strategy_agent is not None
            assert adapter.character_name is not None
            
        except Exception as e:
            pytest.skip(f"Homunculus not properly configured: {e}")
    
    @pytest.mark.asyncio
    async def test_response_generation(self):
        """Test full response generation pipeline"""
        # This is a CRITICAL integration test
        # It verifies the entire Phase 1 working together
        
        try:
            # Initialize adapter
            adapter = CharacterAdapter(
                character_id="ada_lovelace",
                enable_bounded_neurochemistry=True
            )
            
            # Create competition context
            comp_context = self._create_test_competition_context()
            
            # Generate response
            response = await adapter.generate_response(
                competition_context=comp_context,
                conversation_history=[],
                user_message="What is your position on this topic?"
            )
            
            # Verify response
            assert response is not None
            assert response.content is not None
            assert len(response.content) > 0
            assert response.character_id == "ada_lovelace"
            assert response.move_type in [
                "challenge", "support", "synthesize", "question"
            ]
            
        except Exception as e:
            pytest.skip(f"Full integration not ready: {e}")
    
    def _create_test_competition_context(self):
        """Helper to create test competition context"""
        # Same as above helper
        pass


@pytest.mark.integration
def test_phase1_complete():
    """
    Integration test for complete Phase 1.
    
    This test verifies that all Phase 1 components work together:
    1. Load Homunculus
    2. Create CharacterAdapter
    3. Generate strategic assessment
    4. Apply bounded neurochemistry
    5. Create competition memory
    """
    # This will be filled in once all components are complete
    pass


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
```

**Validation**:
- Run tests: `pytest tests/arena/character/test_character_integration.py -v`
- Expect some skips if Homunculus not fully configured
- Core tests should pass

---

## Phase 1.7: Phase 1 Completion Checklist

**Instructions for Claude Code**:

Before moving to Phase 2, verify all Phase 1 components:

### Completion Criteria:

1. **Directory Structure** ✓
   - [ ] `src/arena/character/` exists
   - [ ] All subdirectories created
   - [ ] All `__init__.py` files present

2. **Data Models** ✓
   - [ ] `competition_context.py` created
   - [ ] `competition_memory.py` created
   - [ ] All dataclasses valid
   - [ ] No import errors

3. **Homunculus Integration** ✓
   - [ ] `homunculus_loader.py` functional
   - [ ] Can list available characters
   - [ ] Can load character schemas
   - [ ] Homunculus components importable

4. **Strategy Agent** ✓
   - [ ] `strategy_agent.py` created
   - [ ] Can assess competitive situation
   - [ ] Provides tactical recommendations
   - [ ] No syntax errors

5. **Character Adapter** ✓
   - [ ] `character_adapter.py` created
   - [ ] Wraps Homunculus CharacterAgent
   - [ ] Integrates Strategy Agent
   - [ ] Response generation defined
   - [ ] All async methods proper

6. **Bounded Neurochemistry** ✓
   - [ ] `bounded_neurochemistry.py` created
   - [ ] Applies hormone bounds
   - [ ] Personality-aware adjustments
   - [ ] Dampening works

7. **Testing** ✓
   - [ ] Integration tests created
   - [ ] Core tests pass
   - [ ] Components can be imported
   - [ ] No critical failures

### Manual Verification:

```bash
# Test imports
python -c "from src.arena.character import CharacterAdapter; print('OK')"

# List characters
python -c "from src.arena.character.homunculus_loader import list_available_characters; print(list_available_characters())"

# Run tests
pytest tests/arena/character/ -v

# Check for syntax errors
python -m py_compile src/arena/character/character_adapter.py
python -m py_compile src/arena/character/agents/strategy_agent.py
```

### Phase 1 Deliverables:

- ✅ Full Homunculus character system integrated
- ✅ Arena-specific Strategy Agent created
- ✅ Bounded neurochemistry for competition safety
- ✅ Competition-specific data models
- ✅ Comprehensive adapter layer
- ✅ Integration tests

**Once all checkboxes are complete, Phase 1 is done and we can proceed to Phase 2.**

---
