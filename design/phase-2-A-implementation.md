# 🎼 PHASE 2: INTEGRATE AI-TALKS ORCHESTRATION
**Duration**: Week 5-6  
**Goal**: Bring AI-Talks orchestration, game theory, and flow control into Arena

## Phase 2 Overview

We're integrating the proven orchestration patterns from AI-Talks while adapting them for competitive Arena scenarios. This includes:
- Multi-agent discussion orchestration
- Game theory turn selection
- Narrator agent
- Progression analysis
- Semantic retrieval (quote system)
- Content generation

**Key Principle**: Keep AI-Talks logic intact, adapt interfaces for Arena competitive context.

---

## Phase 2.1: Setup Orchestration Module Structure

### Task 2.1.1: Create Orchestration Module Directories

**Instructions for Claude Code**:

```bash
# Create directory structure
mkdir -p src/arena/orchestration/
mkdir -p src/arena/orchestration/agents/
mkdir -p src/arena/orchestration/game_theory/
mkdir -p src/arena/orchestration/controllers/
mkdir -p src/arena/orchestration/states/
mkdir -p tests/arena/orchestration/
```

**Files to Create**:

1. **`src/arena/orchestration/__init__.py`**
```python
"""
Arena Orchestration System

This module adapts AI-Talks orchestration patterns for competitive Arena
scenarios. It maintains the core AI-Talks architecture while adding
competitive mechanics.

Key Components:
- CompetitionOrchestrator: Main competition coordinator (from AI-Talks)
- TurnSelector: Game theory turn selection (from AI-Talks)
- NarratorAgent: Competition narrator (from AI-Talks)
- ProgressionController: Quality and orbiting detection (from AI-Talks)
- CompetitionState: State management (adapted from AI-Talks GroupState)

Architecture:
The orchestration follows AI-Talks patterns:
1. Centralized coordinator manages all agents
2. State machine tracks competition progress
3. Game theory selects next speaker
4. Narrator provides commentary
5. Progression controller monitors quality

Extensions for Arena:
- Scoring after each turn
- Elimination detection
- Champion persistence
- Competition-specific phases
"""

from .competition_orchestrator import CompetitionOrchestrator
from .states.competition_state import CompetitionState

__all__ = [
    'CompetitionOrchestrator',
    'CompetitionState',
]
```

2. **`src/arena/orchestration/agents/__init__.py`**
```python
"""
Orchestration agents for Arena competitions.

These agents are adapted from AI-Talks but extended for competitive context.
"""

from .narrator_agent import ArenaNarratorAgent
from .turn_selector_agent import TurnSelectorAgent

__all__ = [
    'ArenaNarratorAgent',
    'TurnSelectorAgent',
]
```

3. **`src/arena/orchestration/game_theory/__init__.py`**
```python
"""
Game theory components for Arena.

Adapted from AI-Talks game theory system with Arena extensions.
"""

from .turn_selector import ArenaTurnSelector
from .payoff_calculator import ArenaPayoffCalculator

__all__ = [
    'ArenaTurnSelector',
    'ArenaPayoffCalculator',
]
```

4. **`src/arena/orchestration/controllers/__init__.py`**
```python
"""
Controllers for competition flow and quality.

Based on AI-Talks controllers with Arena adaptations.
"""

from .progression_controller import ArenaProgressionController

__all__ = [
    'ArenaProgressionController',
]
```

5. **`src/arena/orchestration/states/__init__.py`**
```python
"""
State management for competitions.

Adapted from AI-Talks state structures.
"""

from .competition_state import CompetitionState
from .participant_state import ParticipantState

__all__ = [
    'CompetitionState',
    'ParticipantState',
]
```

---

## Phase 2.2: AI-Talks Integration Layer

### Task 2.2.1: Create AI-Talks Loader

**File**: `src/arena/orchestration/talks_loader.py`

**Instructions for Claude Code**:

This module handles loading AI-Talks components into Arena, similar to how we load Homunculus.

**Key Reference Files in AI-Talks**:
- `talks/src/orchestration/orchestrator.py` - Main orchestrator
- `talks/src/game_theory/turn_selector.py` - Turn selection
- `talks/src/agents/narrator_agent.py` - Narrator
- `talks/src/controllers/progression_controller.py` - Quality control

```python
"""
AI-Talks component loader for Arena.

This module handles loading AI-Talks components into the Arena environment.
It provides a clean import interface and handles path management, similar
to the Homunculus loader.

Key Responsibilities:
1. Load AI-Talks orchestration components
2. Load game theory systems
3. Load narrator and progression controllers
4. Provide initialization for Arena context
"""

import os
import sys
from pathlib import Path
from typing import Dict, Any, Optional, List
import logging

logger = logging.getLogger(__name__)


class AITalksLoader:
    """
    Loads and manages AI-Talks components for Arena use.
    
    This class handles the integration between Arena and AI-Talks,
    managing imports, configurations, and component adaptation.
    """
    
    def __init__(
        self,
        talks_path: Optional[str] = None
    ):
        """
        Initialize AI-Talks loader.
        
        Args:
            talks_path: Path to AI-Talks project root
                       Defaults to ../talks relative to arena
        """
        # Determine AI-Talks path
        if talks_path is None:
            # Assume talks is sibling directory to arena project
            arena_root = Path(__file__).parent.parent.parent.parent
            talks_path = arena_root.parent / "talks"
        
        self.talks_path = Path(talks_path)
        
        if not self.talks_path.exists():
            raise FileNotFoundError(
                f"AI-Talks not found at {self.talks_path}. "
                "Please ensure AI-Talks is installed or provide correct path."
            )
        
        # Add AI-Talks to Python path
        talks_src = str(self.talks_path / "src")
        if talks_src not in sys.path:
            sys.path.insert(0, talks_src)
            logger.info(f"Added AI-Talks to Python path: {talks_src}")
        
        # Import AI-Talks components
        self._import_talks_components()
    
    def _import_talks_components(self):
        """Import required AI-Talks components."""
        try:
            # Core orchestration
            from orchestration.orchestrator import MultiAgentDiscussionOrchestrator
            
            # State management
            from states.group_state import GroupDiscussionState
            from states.participant_state import ParticipantState, Gender, PersonalityArchetype
            
            # Agents
            from agents.narrator_agent import NarratorAgent
            from agents.participant_agent import ParticipantAgent
            
            # Game theory
            from game_theory.turn_selector import TurnSelector
            from game_theory.payoff_calculator import PayoffCalculator
            
            # Controllers
            from controllers.progression_controller import (
                ProgressionController,
                ProgressionConfig
            )
            
            # Utilities
            from utils.redundancy_checker import RedundancyChecker
            from utils.entailment_detector import EntailmentDetector
            
            # Store references
            self.MultiAgentDiscussionOrchestrator = MultiAgentDiscussionOrchestrator
            self.GroupDiscussionState = GroupDiscussionState
            self.ParticipantState = ParticipantState
            self.Gender = Gender
            self.PersonalityArchetype = PersonalityArchetype
            self.NarratorAgent = NarratorAgent
            self.ParticipantAgent = ParticipantAgent
            self.TurnSelector = TurnSelector
            self.PayoffCalculator = PayoffCalculator
            self.ProgressionController = ProgressionController
            self.ProgressionConfig = ProgressionConfig
            self.RedundancyChecker = RedundancyChecker
            self.EntailmentDetector = EntailmentDetector
            
            logger.info("Successfully imported AI-Talks components")
            
        except ImportError as e:
            logger.error(f"Failed to import AI-Talks components: {e}")
            raise ImportError(
                f"Could not import AI-Talks components. "
                f"Ensure AI-Talks is properly installed. Error: {e}"
            )
    
    def get_orchestrator_class(self):
        """Get AI-Talks orchestrator class"""
        return self.MultiAgentDiscussionOrchestrator
    
    def get_turn_selector_class(self):
        """Get AI-Talks turn selector class"""
        return self.TurnSelector
    
    def get_narrator_class(self):
        """Get AI-Talks narrator class"""
        return self.NarratorAgent
    
    def get_progression_controller_class(self):
        """Get AI-Talks progression controller class"""
        return self.ProgressionController
    
    def create_turn_selector(self) -> Any:
        """
        Create AI-Talks TurnSelector instance.
        
        Returns:
            Initialized TurnSelector from AI-Talks
        """
        return self.TurnSelector()
    
    def create_payoff_calculator(self) -> Any:
        """
        Create AI-Talks PayoffCalculator instance.
        
        Returns:
            Initialized PayoffCalculator from AI-Talks
        """
        return self.PayoffCalculator()
    
    def create_progression_controller(
        self,
        config: Optional[Dict] = None
    ) -> Any:
        """
        Create AI-Talks ProgressionController instance.
        
        Args:
            config: Optional configuration overrides
        
        Returns:
            Initialized ProgressionController from AI-Talks
        """
        if config:
            progression_config = self.ProgressionConfig(**config)
        else:
            progression_config = self.ProgressionConfig()
        
        return self.ProgressionController(config=progression_config)
    
    def create_narrator(
        self,
        name: str = "Arena Narrator",
        session_id: str = None
    ) -> Any:
        """
        Create AI-Talks NarratorAgent instance.
        
        Args:
            name: Narrator name
            session_id: Session identifier
        
        Returns:
            Initialized NarratorAgent from AI-Talks
        """
        return self.NarratorAgent(
            name=name,
            session_id=session_id or "arena_session"
        )


# Global loader instance
_talks_loader: Optional[AITalksLoader] = None


def get_talks_loader() -> AITalksLoader:
    """
    Get or create the global AI-Talks loader.
    
    Returns:
        AITalksLoader instance
    """
    global _talks_loader
    if _talks_loader is None:
        _talks_loader = AITalksLoader()
    return _talks_loader


def load_talks_components():
    """
    Convenience function to ensure AI-Talks components are loaded.
    
    Returns:
        AITalksLoader instance
    """
    return get_talks_loader()
```

**Validation Steps**:
1. Create the file
2. Ensure `talks` is in the expected location (sibling directory)
3. Test import: `python -c "from src.arena.orchestration.talks_loader import get_talks_loader; print('OK')"`

---

## Phase 2.3: State Management (Adapted from AI-Talks)

### Task 2.3.1: Create Participant State

**File**: `src/arena/orchestration/states/participant_state.py`

**Instructions for Claude Code**:

This adapts AI-Talks ParticipantState for Arena characters.

**Reference**: `talks/src/states/participant_state.py`

```python
"""
Participant state for Arena competitions.

Adapted from AI-Talks ParticipantState but extended for:
- Homunculus character integration
- Competitive scoring tracking
- Elimination status
- Strategic positioning

This represents the state of one character participating in a competition.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
from datetime import datetime
from enum import Enum


class ParticipantStatus(Enum):
    """Current status of participant in competition"""
    ACTIVE = "active"
    ELIMINATED = "eliminated"
    CHAMPION = "champion"  # From previous round
    SPECTATOR = "spectator"  # Observing but not participating


@dataclass
class ParticipantState:
    """
    State of a single participant in Arena competition.
    
    This combines AI-Talks participant tracking with Arena-specific
    competitive state.
    
    Based on AI-Talks ParticipantState but extended with:
    - Scoring history
    - Elimination tracking
    - Homunculus character reference
    - Strategic position
    """
    
    # Identity (from AI-Talks)
    participant_id: str
    name: str
    
    # Character integration (Arena-specific)
    character_adapter: Optional[Any] = None  # CharacterAdapter instance
    is_homunculus_character: bool = True
    
    # Personality (from AI-Talks, but pulled from Homunculus)
    personality_traits: Dict[str, float] = field(default_factory=dict)
    
    # State tracking (from AI-Talks, adapted)
    turns_taken: int = 0
    last_spoke_turn: int = -1
    was_addressed: bool = False
    confidence: float = 0.7
    engagement: float = 0.7
    
    # Scoring (Arena-specific)
    cumulative_score: float = 0.0
    turn_scores: List[float] = field(default_factory=list)
    score_by_dimension: Dict[str, List[float]] = field(default_factory=dict)
    
    # Competitive state (Arena-specific)
    status: ParticipantStatus = ParticipantStatus.ACTIVE
    elimination_turn: Optional[int] = None
    elimination_reason: Optional[str] = None
    is_champion: bool = False  # From previous round
    
    # Strategic (Arena-specific)
    current_position: str = "middle"  # leading, middle, danger, elimination_risk
    elimination_risk: float = 0.0
    
    # Relationships (from AI-Talks, adapted)
    relationships: Dict[str, float] = field(default_factory=dict)  # participant_id -> affinity
    
    # Contribution tracking (from AI-Talks)
    contributions: List[str] = field(default_factory=list)  # contribution IDs
    total_words: int = 0
    
    # Metadata
    joined_at: datetime = field(default_factory=datetime.now)
    last_active: datetime = field(default_factory=datetime.now)
    
    def update_score(self, score: float, dimension_scores: Dict[str, float]):
        """Update participant's score after a turn"""
        self.cumulative_score += score
        self.turn_scores.append(score)
        
        # Track by dimension
        for dimension, dim_score in dimension_scores.items():
            if dimension not in self.score_by_dimension:
                self.score_by_dimension[dimension] = []
            self.score_by_dimension[dimension].append(dim_score)
    
    def eliminate(self, turn: int, reason: str):
        """Mark participant as eliminated"""
        self.status = ParticipantStatus.ELIMINATED
        self.elimination_turn = turn
        self.elimination_reason = reason
    
    def mark_spoke(self, turn: int):
        """Mark that participant spoke on this turn"""
        self.turns_taken += 1
        self.last_spoke_turn = turn
        self.was_addressed = False  # Reset
        self.last_active = datetime.now()
    
    def mark_addressed(self):
        """Mark that participant was addressed/mentioned"""
        self.was_addressed = True
    
    def update_relationship(self, other_id: str, delta: float):
        """Update relationship affinity with another participant"""
        current = self.relationships.get(other_id, 0.0)
        self.relationships[other_id] = max(-1.0, min(1.0, current + delta))
    
    def get_average_score(self) -> float:
        """Get average score per turn"""
        if not self.turn_scores:
            return 0.0
        return sum(self.turn_scores) / len(self.turn_scores)
    
    def get_recent_scores(self, n: int = 3) -> List[float]:
        """Get last N turn scores"""
        return self.turn_scores[-n:] if self.turn_scores else []
    
    @property
    def is_active(self) -> bool:
        """Check if participant is still active in competition"""
        return self.status == ParticipantStatus.ACTIVE
```

**Validation**:
- Import check
- Verify dataclass is valid
- Check all methods work

---

### Task 2.3.2: Create Competition State

**File**: `src/arena/orchestration/states/competition_state.py`

**Instructions for Claude Code**:

This adapts AI-Talks GroupDiscussionState for Arena competitions.

**Reference**: `talks/src/states/group_state.py`

```python
"""
Competition state management for Arena.

Adapted from AI-Talks GroupDiscussionState but extended for:
- Competitive scoring
- Elimination tracking
- Multiple phases
- Judge integration
- Champion preservation

This is the central state object passed through the orchestration system.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
from datetime import datetime
from enum import Enum

from .participant_state import ParticipantState, ParticipantStatus


class CompetitionPhase(Enum):
    """Current phase of competition (from design docs)"""
    INITIALIZATION = "initialization"
    OPENING_STATEMENTS = "opening_statements"
    CROSS_EXAMINATION = "cross_examination"
    FREE_DISCUSSION = "free_discussion"
    ELIMINATION_PENDING = "elimination_pending"
    ELIMINATION_ANNOUNCEMENT = "elimination_announcement"
    FINAL_WORDS = "final_words"
    REBUTTALS = "rebuttals"
    CLOSING_STATEMENTS = "closing_statements"
    SYNTHESIS = "synthesis"
    COMPLETE = "complete"


@dataclass
class CompetitionExchange:
    """
    Single exchange in competition (from AI-Talks).
    
    Represents one turn/contribution.
    """
    turn_number: int
    participant_id: str
    speaker_name: str
    content: str
    timestamp: datetime
    
    # Arena-specific
    move_type: str = "general"  # challenge, support, synthesize, etc.
    targets: List[str] = field(default_factory=list)  # participant_ids
    
    # Scoring
    scores: Dict[str, float] = field(default_factory=dict)  # dimension -> score
    total_score: float = 0.0
    judge_reasoning: Optional[str] = None
    
    # Quality metrics
    novelty_score: float = 0.0
    semantic_similarity_to_previous: float = 0.0


@dataclass
class CompetitionState:
    """
    Central state object for Arena competition.
    
    Adapted from AI-Talks GroupDiscussionState with Arena extensions.
    Passed through entire orchestration system.
    
    Key additions over AI-Talks:
    - Competitive scoring
    - Elimination tracking
    - Multiple competition phases
    - Judge integration
    - Strategic metrics
    """
    
    # Identity
    competition_id: str
    competition_type: str  # debate, story_battle, etc.
    topic: str
    
    # Participants (from AI-Talks, adapted)
    participants: Dict[str, ParticipantState] = field(default_factory=dict)
    participant_order: List[str] = field(default_factory=list)  # For iteration
    
    # Competition progress
    phase: CompetitionPhase = CompetitionPhase.INITIALIZATION
    turn_number: int = 0
    round_number: int = 1  # For multi-round tournaments
    
    # Exchanges (from AI-Talks)
    exchanges: List[CompetitionExchange] = field(default_factory=list)
    
    # Active participants (Arena-specific)
    active_participant_ids: List[str] = field(default_factory=list)
    eliminated_participant_ids: List[str] = field(default_factory=list)
    
    # Champion (Arena-specific)
    champion_id: Optional[str] = None  # From previous round
    
    # Scoring configuration (Arena-specific)
    scoring_weights: Dict[str, float] = field(default_factory=dict)
    elimination_threshold: float = -10.0
    
    # Quality tracking (from AI-Talks, adapted)
    depth_level: int = 3  # Default depth
    target_depth: int = 3
    current_depth_coverage: Dict[int, int] = field(default_factory=dict)
    
    # Progression tracking (from AI-Talks)
    orbiting_detected: bool = False
    orbiting_score: float = 0.0
    stagnation_turns: int = 0
    
    # Strategic tracking (Arena-specific)
    detected_alliances: List[tuple[str, str]] = field(default_factory=list)
    detected_rivalries: List[tuple[str, str]] = field(default_factory=list)
    
    # Narrator tracking (from AI-Talks)
    narrator_interjections: List[Dict] = field(default_factory=list)
    last_narrator_turn: int = -1
    
    # Timing
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    
    # Configuration
    max_turns: int = 50
    enable_narrator: bool = True
    enable_progression_control: bool = True
    
    def add_exchange(
        self,
        participant_id: str,
        content: str,
        move_type: str = "general",
        targets: Optional[List[str]] = None
    ) -> CompetitionExchange:
        """
        Add an exchange to the competition.
        
        Args:
            participant_id: Who is speaking
            content: What they said
            move_type: Type of move
            targets: Who they're addressing
        
        Returns:
            Created exchange object
        """
        participant = self.participants[participant_id]
        
        exchange = CompetitionExchange(
            turn_number=self.turn_number,
            participant_id=participant_id,
            speaker_name=participant.name,
            content=content,
            timestamp=datetime.now(),
            move_type=move_type,
            targets=targets or []
        )
        
        self.exchanges.append(exchange)
        
        # Update participant state
        participant.mark_spoke(self.turn_number)
        participant.contributions.append(
            f"{self.competition_id}_{self.turn_number}"
        )
        participant.total_words += len(content.split())
        
        # Mark addressed participants
        for target_id in (targets or []):
            if target_id in self.participants:
                self.participants[target_id].mark_addressed()
        
        self.turn_number += 1
        
        return exchange
    
    def update_exchange_scores(
        self,
        turn: int,
        scores: Dict[str, float],
        total_score: float,
        judge_reasoning: str
    ):
        """
        Update scores for a specific exchange.
        
        Args:
            turn: Turn number to update
            scores: Dimension scores
            total_score: Aggregated total
            judge_reasoning: Judge's explanation
        """
        # Find exchange
        exchange = None
        for ex in self.exchanges:
            if ex.turn_number == turn:
                exchange = ex
                break
        
        if exchange:
            exchange.scores = scores
            exchange.total_score = total_score
            exchange.judge_reasoning = judge_reasoning
            
            # Update participant score
            participant = self.participants[exchange.participant_id]
            participant.update_score(total_score, scores)
    
    def eliminate_participant(
        self,
        participant_id: str,
        reason: str
    ):
        """
        Eliminate a participant from competition.
        
        Args:
            participant_id: Who to eliminate
            reason: Why they were eliminated
        """
        if participant_id in self.active_participant_ids:
            self.active_participant_ids.remove(participant_id)
        
        if participant_id not in self.eliminated_participant_ids:
            self.eliminated_participant_ids.append(participant_id)
        
        # Update participant state
        participant = self.participants[participant_id]
        participant.eliminate(self.turn_number, reason)
    
    def get_active_participants(self) -> List[ParticipantState]:
        """Get list of active participants"""
        return [
            self.participants[pid]
            for pid in self.active_participant_ids
            if pid in self.participants
        ]
    
    def get_leaderboard(self) -> List[tuple[str, float]]:
        """
        Get current leaderboard.
        
        Returns:
            List of (participant_id, score) sorted by score descending
        """
        leaderboard = [
            (pid, p.cumulative_score)
            for pid, p in self.participants.items()
            if p.is_active
        ]
        return sorted(leaderboard, key=lambda x: x[1], reverse=True)
    
    def get_at_risk_participants(self) -> List[str]:
        """
        Get participants at risk of elimination.
        
        Returns:
            List of participant_ids below threshold
        """
        at_risk = []
        for pid, participant in self.participants.items():
            if participant.is_active:
                if participant.cumulative_score < self.elimination_threshold:
                    at_risk.append(pid)
        return at_risk
    
    def should_eliminate(self) -> bool:
        """Check if elimination should occur"""
        # Elimination criteria (can be customized)
        return len(self.get_at_risk_participants()) > 0
    
    def get_leader_score(self) -> float:
        """Get highest current score"""
        active = self.get_active_participants()
        if not active:
            return 0.0
        return max(p.cumulative_score for p in active)
    
    def get_recent_discussion_summary(self, n: int = 5) -> str:
        """
        Get summary of recent discussion.
        
        Args:
            n: Number of recent turns to include
        
        Returns:
            Formatted summary string
        """
        recent = self.exchanges[-n:] if self.exchanges else []
        
        if not recent:
            return "No discussion yet."
        
        summary_parts = []
        for ex in recent:
            summary_parts.append(f"{ex.speaker_name}: {ex.content[:100]}...")
        
        return "\n".join(summary_parts)
    
    def advance_phase(self, new_phase: CompetitionPhase):
        """Advance to next phase"""
        self.phase = new_phase
```

**Validation**:
- Import check
- Verify all methods work
- Check dataclass is valid

---

## Phase 2.4: Game Theory Integration (from AI-Talks)

### Task 2.4.1: Create Arena Turn Selector

**File**: `src/arena/orchestration/game_theory/turn_selector.py`

**Instructions for Claude Code**:

This adapts AI-Talks TurnSelector for Arena with competitive extensions.

**Reference**: `talks/src/game_theory/turn_selector.py` (CRITICAL - study lines 1-300)

```python
"""
Turn Selector for Arena competitions.

Adapted from AI-Talks TurnSelector with Arena competitive extensions.

Key changes from AI-Talks:
1. Elimination risk factor (characters near elimination get priority)
2. Champion advantage (previous winner gets slight boost)
3. Strategic tension creation (can select for drama)
4. Accusation priority (involved parties get urgency)

Core AI-Talks logic preserved:
- Multi-factor urgency calculation
- Fairness mechanisms
- Personality-based baselines
- Strategic randomness (80/20 rule)
"""

from typing import Dict, List, Optional, Tuple
import random
import logging

from ..states.competition_state import CompetitionState, ParticipantState
from .payoff_calculator import ArenaPayoffCalculator

logger = logging.getLogger(__name__)


class ArenaTurnSelector:
    """
    Turn selector for Arena competitions.
    
    Based on AI-Talks TurnSelector but extended for competitive dynamics.
    
    Urgency calculation (from AI-Talks):
    - Personality baseline (30%)
    - Time since last spoke (20%)
    - Was addressed (40%)
    - Confidence level (10%)
    - Engagement level (20%)
    
    Arena additions:
    - Elimination risk (15%) - urgent if near elimination
    - Champion bonus (5%) - slight priority for previous winner
    - Dramatic tension (10%) - can amplify for key moments
    """
    
    def __init__(
        self,
        enable_fairness: bool = True,
        randomness_factor: float = 0.20,  # AI-Talks standard
        enable_dramatic_tension: bool = True
    ):
        """
        Initialize Arena turn selector.
        
        Args:
            enable_fairness: Apply fairness mechanisms (prevent domination)
            randomness_factor: 0-1, how much randomness (AI-Talks uses 0.20)
            enable_dramatic_tension: Allow amplification for drama
        """
        self.enable_fairness = enable_fairness
        self.randomness_factor = randomness_factor
        self.enable_dramatic_tension = enable_dramatic_tension
        
        self.payoff_calculator = ArenaPayoffCalculator()
    
    def select_next_speaker(
        self,
        competition_state: CompetitionState
    ) -> str:
        """
        Select next speaker using game theory + Arena factors.
        
        This is the main method called by orchestrator.
        
        Args:
            competition_state: Current competition state
        
        Returns:
            participant_id of selected speaker
        """
        active_participants = competition_state.get_active_participants()
        
        if not active_participants:
            raise ValueError("No active participants")
        
        if len(active_participants) == 1:
            return active_participants[0].participant_id
        
        # Calculate urgency for each participant
        urgencies = self._calculate_all_urgencies(
            competition_state,
            active_participants
        )
        
        # Apply fairness mechanisms (from AI-Talks)
        if self.enable_fairness:
            urgencies = self._apply_fairness(
                urgencies,
                competition_state
            )
        
        # Apply dramatic tension (Arena-specific)
        if self.enable_dramatic_tension:
            urgencies = self._apply_dramatic_tension(
                urgencies,
                competition_state
            )
        
        # Select speaker
        selected_id = self._select_from_urgencies(urgencies)
        
        logger.info(
            f"Selected {competition_state.participants[selected_id].name} "
            f"(urgency: {urgencies[selected_id]:.2f})"
        )
        
        return selected_id
    
    def _calculate_all_urgencies(
        self,
        competition_state: CompetitionState,
        participants: List[ParticipantState]
    ) -> Dict[str, float]:
        """
        Calculate urgency scores for all participants.
        
        Based on AI-Talks multi-factor urgency with Arena additions.
        """
        urgencies = {}
        
        for participant in participants:
            urgency = self._calculate_urgency(
                participant,
                competition_state
            )
            urgencies[participant.participant_id] = urgency
        
        return urgencies
    
    def _calculate_urgency(
        self,
        participant: ParticipantState,
        competition_state: CompetitionState
    ) -> float:
        """
        Calculate urgency for a single participant.
        
        Combines AI-Talks factors with Arena competitive factors.
        """
        # AI-Talks factors
        personality_urgency = self._calculate_personality_urgency(participant)
        time_urgency = self._calculate_time_urgency(
            participant,
            competition_state.turn_number
        )
        addressed_urgency = 1.0 if participant.was_addressed else 0.0
        confidence_urgency = participant.confidence
        engagement_urgency = participant.engagement
        
        # Arena factors
        elimination_urgency = self._calculate_elimination_urgency(
            participant,
            competition_state
        )
        champion_bonus = 0.05 if participant.is_champion else 0.0
        
        # Weighted combination (AI-Talks weights + Arena additions)
        urgency = (
            personality_urgency * 0.25 +      # Reduced from 0.30
            time_urgency * 0.15 +             # Reduced from 0.20
            addressed_urgency * 0.35 +        # Reduced from 0.40
            confidence_urgency * 0.08 +       # Reduced from 0.10
            engagement_urgency * 0.15 +       # Reduced from 0.20 (total was 1.20)
            elimination_urgency * 0.15 +      # NEW
            champion_bonus * 0.05             # NEW
        )
        
        # Note: Weights now sum to ~1.18, intentionally slightly over
        # to allow urgency to exceed 1.0 in critical situations
        
        return max(0.0, urgency)  # Clamp to non-negative
    
    def _calculate_personality_urgency(
        self,
        participant: ParticipantState
    ) -> float:
        """
        Calculate baseline urgency from personality (AI-Talks).
        
        Extraverts have higher baseline urgency to speak.
        """
        # From AI-Talks: extraversion drives baseline
        extraversion = participant.personality_traits.get('extraversion', 0.5)
        openness = participant.personality_traits.get('openness', 0.5)
        
        # Blend extraversion and openness
        baseline = (extraversion * 0.7 + openness * 0.3)
        
        return baseline
    
    def _calculate_time_urgency(
        self,
        participant: ParticipantState,
        current_turn: int
    ) -> float:
        """
        Calculate urgency based on time since last spoke (AI-Talks).
        
        Linear increase with turns elapsed.
        """
        if participant.last_spoke_turn < 0:
            # Never spoken - high urgency
            return 1.0
        
        turns_since = current_turn - participant.last_spoke_turn
        
        # From AI-Talks: linear scaling, cap at 1.0
        urgency = min(1.0, turns_since / 5.0)
        
        return urgency
    
    def _calculate_elimination_urgency(
        self,
        participant: ParticipantState,
        competition_state: CompetitionState
    ) -> float:
        """
        Calculate urgency based on elimination risk (Arena-specific).
        
        Characters near elimination need opportunity to recover.
        """
        threshold = competition_state.elimination_threshold
        score = participant.cumulative_score
        
        if score > threshold * 2:
            return 0.0  # Very safe
        elif score > threshold * 1.5:
            return 0.2  # Somewhat safe
        elif score > threshold:
            return 0.6  # At risk
        else:
            return 1.0  # Critical danger
    
    def _apply_fairness(
        self,
        urgencies: Dict[str, float],
        competition_state: CompetitionState
    ) -> Dict[str, float]:
        """
        Apply fairness mechanisms to prevent domination (AI-Talks).
        
        Reduces urgency for participants who have spoken too much.
        """
        total_turns = competition_state.turn_number
        if total_turns == 0:
            return urgencies
        
        adjusted = urgencies.copy()
        
        for pid, participant in competition_state.participants.items():
            if pid not in adjusted:
                continue
            
            # Calculate speaking share
            speaking_share = participant.turns_taken / total_turns
            expected_share = 1.0 / len(competition_state.active_participant_ids)
            
            # If over-represented, reduce urgency (AI-Talks pattern)
            if speaking_share > expected_share * 1.5:
                penalty = 0.5  # Significant reduction
                adjusted[pid] = adjusted[pid] * penalty
                
                logger.debug(
                    f"Applied fairness penalty to {participant.name} "
                    f"(share: {speaking_share:.2f})"
                )
        
        return adjusted
    
    def _apply_dramatic_tension(
        self,
        urgencies: Dict[str, float],
        competition_state: CompetitionState
    ) -> Dict[str, float]:
        """
        Apply dramatic tension modifiers (Arena-specific).
        
        Can amplify urgencies during key moments for entertainment value.
        """
        # Identify dramatic moments
        at_risk = competition_state.get_at_risk_participants()
        
        if not at_risk:
            return urgencies
        
        # Amplify urgency for at-risk participants
        adjusted = urgencies.copy()
        
        for pid in at_risk:
            if pid in adjusted:
                # Boost urgency for dramatic tension
                adjusted[pid] = adjusted[pid] * 1.3
                
                logger.debug(
                    f"Applied dramatic tension boost to "
                    f"{competition_state.participants[pid].name}"
                )
        
        return adjusted
    
    def _select_from_urgencies(
        self,
        urgencies: Dict[str, float]
    ) -> str:
        """
        Select speaker from urgencies with controlled randomness (AI-Talks).
        
        Uses 80/20 rule: 80% game theory, 20% random (AI-Talks standard).
        """
        if random.random() < self.randomness_factor:
            # Random selection
            selected = random.choice(list(urgencies.keys()))
            logger.debug(f"Random selection (20% branch)")
        else:
            # Game theory selection (weighted random based on urgency)
            participants = list(urgencies.keys())
            weights = [urgencies[pid] for pid in participants]
            
            # Normalize weights
            total_weight = sum(weights)
            if total_weight == 0:
                # All zero urgency - random
                selected = random.choice(participants)
            else:
                normalized_weights = [w / total_weight for w in weights]
                selected = random.choices(participants, weights=normalized_weights)[0]
            
            logger.debug(f"Game theory selection (80% branch)")
        
        return selected
```

**Validation**:
- Import check
- Test urgency calculation with mock data
- Verify selection works

---

### Task 2.4.2: Create Arena Payoff Calculator

**File**: `src/arena/orchestration/game_theory/payoff_calculator.py`

**Instructions for Claude Code**:

This adapts AI-Talks PayoffCalculator for Arena.

**Reference**: `talks/src/game_theory/payoff_calculator.py`

```python
"""
Payoff Calculator for Arena competitions.

Adapted from AI-Talks PayoffCalculator but extended for competitive scoring.

AI-Talks provides move type recommendations (CHALLENGE, SUPPORT, etc.).
Arena adds scoring predictions and strategic risk assessment.
"""

from typing import Dict, List, Optional, Tuple
from enum import Enum
import logging

from ..states.competition_state import CompetitionState, ParticipantState

logger = logging.getLogger(__name__)


class MoveType(Enum):
    """Types of moves (from AI-Talks)"""
    DEEPEN = "deepen"          # Explore deeper
    CHALLENGE = "challenge"     # Question/contest
    SUPPORT = "support"         # Agree/build on
    QUESTION = "question"       # Ask for clarification
    SYNTHESIZE = "synthesize"   # Combine perspectives
    CONCLUDE = "conclude"       # Wrap up discussion


class ArenaPayoffCalculator:
    """
    Calculate strategic payoffs for Arena moves.
    
    Based on AI-Talks PayoffCalculator with Arena scoring extensions.
    
    Provides:
    - Move type recommendations (from AI-Talks)
    - Expected scoring by move type (Arena)
    - Risk assessment (Arena)
    - Target selection (AI-Talks + Arena)
    """
    
    def __init__(self):
        """Initialize payoff calculator"""
        pass
    
    def calculate_move_payoffs(
        self,
        participant: ParticipantState,
        competition_state: CompetitionState,
        strategic_context: Optional[Dict] = None
    ) -> Dict[MoveType, float]:
        """
        Calculate expected payoffs for each move type.
        
        Args:
            participant: Who is considering moves
            competition_state: Current state
            strategic_context: Additional context from Strategy Agent
        
        Returns:
            Dict mapping move types to expected payoff scores
        """
        payoffs = {}
        
        for move_type in MoveType:
            payoff = self._calculate_move_payoff(
                move_type,
                participant,
                competition_state,
                strategic_context
            )
            payoffs[move_type] = payoff
        
        return payoffs
    
    def _calculate_move_payoff(
        self,
        move_type: MoveType,
        participant: ParticipantState,
        competition_state: CompetitionState,
        strategic_context: Optional[Dict]
    ) -> float:
        """Calculate payoff for a specific move type"""
        
        # Base payoff from personality fit (AI-Talks pattern)
        personality = participant.personality_traits
        base_payoff = self._personality_move_affinity(move_type, personality)
        
        # Context-based adjustments (AI-Talks pattern)
        context_mod = self._context_adjustment(
            move_type,
            competition_state,
            participant
        )
        
        # Scoring potential (Arena-specific)
        scoring_mod = self._scoring_potential(
            move_type,
            competition_state,
            participant
        )
        
        # Risk adjustment (Arena-specific)
        risk_mod = self._risk_adjustment(
            move_type,
            participant.elimination_risk
        )
        
        # Combine factors
        total_payoff = (
            base_payoff * 0.3 +
            context_mod * 0.3 +
            scoring_mod * 0.3 +
            risk_mod * 0.1
        )
        
        return total_payoff
    
    def _personality_move_affinity(
        self,
        move_type: MoveType,
        personality: Dict[str, float]
    ) -> float:
        """How well does this move fit the personality? (AI-Talks)"""
        
        openness = personality.get('openness', 0.5)
        agreeableness = personality.get('agreeableness', 0.5)
        conscientiousness = personality.get('conscientiousness', 0.5)
        
        if move_type == MoveType.CHALLENGE:
            # Challenging requires low agreeableness, high openness
            return (1.0 - agreeableness) * 0.6 + openness * 0.4
        
        elif move_type == MoveType.SUPPORT:
            # Supporting requires high agreeableness
            return agreeableness
        
        elif move_type == MoveType.DEEPEN:
            # Deepening requires high openness, conscientiousness
            return openness * 0.6 + conscientiousness * 0.4
        
        elif move_type == MoveType.SYNTHESIZE:
            # Synthesizing requires balance
            return (openness + conscientiousness + agreeableness) / 3
        
        elif move_type == MoveType.QUESTION:
            # Questioning requires openness
            return openness * 0.7 + conscientiousness * 0.3
        
        elif move_type == MoveType.CONCLUDE:
            # Concluding requires conscientiousness
            return conscientiousness
        
        return 0.5  # Default
    
    def _context_adjustment(
        self,
        move_type: MoveType,
        competition_state: CompetitionState,
        participant: ParticipantState
    ) -> float:
        """Adjust based on current context (AI-Talks pattern)"""
        
        # If addressed, SUPPORT or CHALLENGE is more appropriate
        if participant.was_addressed:
            if move_type in [MoveType.CHALLENGE, MoveType.SUPPORT]:
                return 0.8
            else:
                return 0.3
        
        # If many turns have passed, SYNTHESIZE is valuable
        if competition_state.turn_number > 15:
            if move_type == MoveType.SYNTHESIZE:
                return 0.9
            elif move_type == MoveType.CONCLUDE:
                return 0.7
        
        # Early in competition, DEEPEN is valuable
        if competition_state.turn_number < 5:
            if move_type == MoveType.DEEPEN:
                return 0.8
        
        return 0.5  # Neutral
    
    def _scoring_potential(
        self,
        move_type: MoveType,
        competition_state: CompetitionState,
        participant: ParticipantState
    ) -> float:
        """
        Estimate scoring potential for this move (Arena-specific).
        
        Different moves have different expected scores based on:
        - Current phase
        - Judge preferences (learned over time)
        - Recent scoring patterns
        """
        # Base scoring potential by move type
        base_scores = {
            MoveType.SYNTHESIZE: 0.8,    # High value
            MoveType.DEEPEN: 0.7,        # Good value
            MoveType.CHALLENGE: 0.6,     # Medium value, risky
            MoveType.SUPPORT: 0.5,       # Safe but lower
            MoveType.QUESTION: 0.5,      # Situational
            MoveType.CONCLUDE: 0.4,      # Low unless appropriate
        }
        
        return base_scores.get(move_type, 0.5)
    
    def _risk_adjustment(
        self,
        move_type: MoveType,
        elimination_risk: float
    ) -> float:
        """
        Adjust for risk level (Arena-specific).
        
        When elimination risk is high, prefer safer moves.
        """
        # Risk levels by move type
        move_risks = {
            MoveType.CHALLENGE: 0.7,     # Risky
            MoveType.SUPPORT: 0.2,       # Safe
            MoveType.SYNTHESIZE: 0.3,    # Relatively safe
            MoveType.DEEPEN: 0.4,        # Medium
            MoveType.QUESTION: 0.3,      # Safe
            MoveType.CONCLUDE: 0.5,      # Medium
        }
        
        move_risk = move_risks.get(move_type, 0.5)
        
        # If high elimination risk, penalize risky moves
        if elimination_risk > 0.7:
            penalty = move_risk * elimination_risk
            return 1.0 - penalty
        
        return 1.0  # No adjustment
    
    def recommend_move_and_target(
        self,
        participant: ParticipantState,
        competition_state: CompetitionState
    ) -> Tuple[MoveType, Optional[str]]:
        """
        Recommend best move and target (AI-Talks + Arena).
        
        Returns:
            (move_type, target_participant_id)
        """
        # Calculate payoffs
        payoffs = self.calculate_move_payoffs(
            participant,
            competition_state
        )
        
        # Select best move
        best_move = max(payoffs, key=payoffs.get)
        
        # Select target based on move type
        target = self._select_target(
            best_move,
            participant,
            competition_state
        )
        
        return (best_move, target)
    
    def _select_target(
        self,
        move_type: MoveType,
        participant: ParticipantState,
        competition_state: CompetitionState
    ) -> Optional[str]:
        """Select appropriate target for move"""
        
        active = competition_state.get_active_participants()
        
        if not active:
            return None
        
        # Remove self
        others = [p for p in active if p.participant_id != participant.participant_id]
        
        if not others:
            return None
        
        # Select based on move type
        if move_type == MoveType.CHALLENGE:
            # Challenge the leader or high-scoring opponent
            return max(others, key=lambda p: p.cumulative_score).participant_id
        
        elif move_type == MoveType.SUPPORT:
            # Support someone with positive relationship
            friendly = [
                p for p in others
                if participant.relationships.get(p.participant_id, 0) > 0
            ]
            if friendly:
                return friendly[0].participant_id
            return others[0].participant_id
        
        elif move_type == MoveType.SYNTHESIZE:
            # Synthesize multiple viewpoints - return None for "general audience"
            return None
        
        else:
            # Default: address last speaker if available
            if competition_state.exchanges:
                last_speaker = competition_state.exchanges[-1].participant_id
                if last_speaker != participant.participant_id:
                    return last_speaker
        
        return None
```

**Validation**:
- Import check
- Test payoff calculation
- Verify move recommendations

---

## Phase 2.5: Narrator Agent (from AI-Talks)

### Task 2.5.1: Create Arena Narrator Agent

**File**: `src/arena/orchestration/agents/narrator_agent.py`

**Instructions for Claude Code**:

This adapts AI-Talks NarratorAgent for Arena competitions.

**Reference**: `talks/src/agents/narrator_agent.py` (study entire file)

```python
"""
Narrator Agent for Arena competitions.

Adapted from AI-Talks NarratorAgent with Arena competitive extensions.

The narrator provides:
- Competition introduction (multi-phase, from AI-Talks)
- Periodic commentary (from AI-Talks)
- Score updates (Arena-specific)
- Elimination announcements (Arena-specific)
- Dramatic tension building (Arena-specific)
- Final synthesis (from AI-Talks + Arena)

Key AI-Talks patterns preserved:
- Multi-phase introduction
- Contextual interjections
- Closing synthesis
- Natural commentary style
"""

from typing import Dict, List, Optional
import logging

from ..states.competition_state import CompetitionState, CompetitionPhase
from ..talks_loader import get_talks_loader

logger = logging.getLogger(__name__)


class ArenaNarratorAgent:
    """
    Narrator for Arena competitions.
    
    Based on AI-Talks NarratorAgent with competitive extensions.
    
    Responsibilities:
    - Introduce competition and participants
    - Provide periodic commentary
    - Announce score updates
    - Build dramatic tension
    - Announce eliminations
    - Synthesize conclusions
    """
    
    def __init__(
        self,
        name: str = "Arena Narrator",
        session_id: str = "arena_session",
        llm_client: Optional[Any] = None
    ):
        """
        Initialize Arena narrator.
        
        Args:
            name: Narrator name
            session_id: Session identifier
            llm_client: LLM client for generation
        """
        self.name = name
        self.session_id = session_id
        self.llm_client = llm_client
        
        # Load AI-Talks narrator as base
        talks_loader = get_talks_loader()
        self.talks_narrator = talks_loader.create_narrator(
            name=name,
            session_id=session_id
        )
        
        logger.info(f"ArenaNarratorAgent initialized: {name}")
    
    async def generate_introduction(
        self,
        competition_state: CompetitionState
    ) -> str:
        """
        Generate multi-phase competition introduction (from AI-Talks).
        
        Phases:
        1. Welcome
        2. Topic introduction
        3. Participant introductions
        4. Stakes explanation (Arena-specific)
        5. Competition start
        
        Args:
            competition_state: Current state
        
        Returns:
            Complete introduction text
        """
        # Phase 1: Welcome
        welcome = self._generate_welcome(competition_state)
        
        # Phase 2: Topic
        topic_intro = self._generate_topic_introduction(competition_state)
        
        # Phase 3: Participants
        participant_intro = self._generate_participant_introductions(
            competition_state
        )
        
        # Phase 4: Stakes (Arena-specific)
        stakes = self._generate_stakes_explanation(competition_state)
        
        # Phase 5: Start
        start = self._generate_start_transition(competition_state)
        
        # Combine all phases
        full_intro = "\n\n".join([
            welcome,
            topic_intro,
            participant_intro,
            stakes,
            start
        ])
        
        return full_intro
    
    def _generate_welcome(self, competition_state: CompetitionState) -> str:
        """Generate welcome (Arena-specific)"""
        return (
            f"Welcome to AI Arena - where artificial minds clash in "
            f"intellectual combat. I'm {self.name}, and I'll be your guide "
            f"through today's {competition_state.competition_type}."
        )
    
    def _generate_topic_introduction(
        self,
        competition_state: CompetitionState
    ) -> str:
        """Generate topic introduction (from AI-Talks pattern)"""
        return (
            f"Today's arena challenge: {competition_state.topic}\n\n"
            f"This {competition_state.competition_type} will test our "
            f"competitors' ability to reason, argue, and ultimately survive "
            f"through intellectual prowess alone."
        )
    
    def _generate_participant_introductions(
        self,
        competition_state: CompetitionState
    ) -> str:
        """Generate participant introductions (from AI-Talks + Arena)"""
        intros = ["Our competitors today:"]
        
        for participant in competition_state.get_active_participants():
            # Basic intro
            intro = f"\n• {participant.name}"
            
            # Add champion status if applicable
            if participant.is_champion:
                intro += " - **Reigning Champion**"
            
            # Add personality flavor (from character traits)
            traits = participant.personality_traits
            if traits.get('openness', 0) > 0.7:
                intro += " (Known for innovative thinking)"
            elif traits.get('conscientiousness', 0) > 0.7:
                intro += " (Known for rigorous analysis)"
            elif traits.get('agreeableness', 0) > 0.7:
                intro += " (Known for collaborative approach)"
            
            intros.append(intro)
        
        return "".join(intros)
    
    def _generate_stakes_explanation(
        self,
        competition_state: CompetitionState
    ) -> str:
        """Explain competition stakes (Arena-specific)"""
        n_participants = len(competition_state.active_participant_ids)
        
        return (
            f"The stakes are high. {n_participants} enter, but not all will "
            f"survive. Contributions will be scored on novelty, synthesis, "
            f"problem-solving, and strategic insight. Fall below the "
            f"threshold... and elimination awaits.\n\n"
            f"Only the strongest mind will emerge victorious."
        )
    
    def _generate_start_transition(
        self,
        competition_state: CompetitionState
    ) -> str:
        """Generate transition to competition start (from AI-Talks)"""
        return "Let the competition begin."
    
    async def generate_commentary(
        self,
        competition_state: CompetitionState,
        trigger: str = "periodic"
    ) -> Optional[str]:
        """
        Generate contextual commentary (from AI-Talks pattern).
        
        Args:
            competition_state: Current state
            trigger: Why commentary is being generated
                    ("periodic", "score_update", "tension", "elimination_pending")
        
        Returns:
            Commentary text or None if not appropriate
        """
        if trigger == "periodic":
            return self._generate_periodic_commentary(competition_state)
        
        elif trigger == "score_update":
            return self._generate_score_commentary(competition_state)
        
        elif trigger == "tension":
            return self._generate_tension_commentary(competition_state)
        
        elif trigger == "elimination_pending":
            return self._generate_elimination_warning(competition_state)
        
        return None
    
    def _generate_periodic_commentary(
        self,
        competition_state: CompetitionState
    ) -> str:
        """Generate periodic commentary (from AI-Talks)"""
        
        turn = competition_state.turn_number
        leaderboard = competition_state.get_leaderboard()
        
        if not leaderboard:
            return ""
        
        leader_id, leader_score = leaderboard[0]
        leader = competition_state.participants[leader_id]
        
        commentary = (
            f"After {turn} turns, {leader.name} holds the lead "
            f"with {leader_score:.1f} points. "
        )
        
        # Add context about discussion quality
        if competition_state.orbiting_detected:
            commentary += (
                "The discussion is beginning to circle back on itself. "
                "Fresh perspectives are needed."
            )
        else:
            commentary += (
                "The intellectual exchange remains vigorous and productive."
            )
        
        return commentary
    
    def _generate_score_commentary(
        self,
        competition_state: CompetitionState
    ) -> str:
        """Comment on recent scoring (Arena-specific)"""
        
        if not competition_state.exchanges:
            return ""
        
        last_exchange = competition_state.exchanges[-1]
        
        if last_exchange.total_score == 0.0:
            return ""  # Not yet scored
        
        score = last_exchange.total_score
        speaker = competition_state.participants[last_exchange.participant_id]
        
        if score >= 8.0:
            return f"A strong contribution from {speaker.name}! Impressive."
        elif score >= 6.0:
            return f"{speaker.name} delivers a solid contribution."
        elif score >= 4.0:
            return f"A modest showing from {speaker.name}."
        else:
            return f"{speaker.name} struggles to make an impact."
    
    def _generate_tension_commentary(
        self,
        competition_state: CompetitionState
    ) -> str:
        """Build dramatic tension (Arena-specific)"""
        
        at_risk = competition_state.get_at_risk_participants()
        
        if not at_risk:
            return ""
        
        at_risk_names = [
            competition_state.participants[pid].name
            for pid in at_risk
        ]
        
        if len(at_risk_names) == 1:
            return (
                f"Tension mounts. {at_risk_names[0]} hovers dangerously "
                f"close to the elimination threshold."
            )
        else:
            names = ", ".join(at_risk_names[:-1]) + f" and {at_risk_names[-1]}"
            return (
                f"Multiple competitors in jeopardy. {names} must elevate "
                f"their game or face elimination."
            )
    
    def _generate_elimination_warning(
        self,
        competition_state: CompetitionState
    ) -> str:
        """Warn about impending elimination (Arena-specific)"""
        return (
            "The judges have reached their decision. "
            "An elimination is imminent."
        )
    
    async def announce_elimination(
        self,
        eliminated_name: str,
        reason: str,
        competition_state: CompetitionState
    ) -> str:
        """
        Announce elimination with drama (Arena-specific).
        
        Args:
            eliminated_name: Who was eliminated
            reason: Why they were eliminated
            competition_state: Current state
        
        Returns:
            Elimination announcement
        """
        remaining = len(competition_state.active_participant_ids)
        
        announcement = (
            f"The Arena has spoken.\n\n"
            f"{eliminated_name}, your time in this competition has ended. "
            f"{reason}\n\n"
        )
        
        if remaining > 1:
            announcement += (
                f"{remaining} competitors remain. The battle continues."
            )
        else:
            announcement += (
                f"Only one remains. We have our champion."
            )
        
        return announcement
    
    async def generate_closing_synthesis(
        self,
        competition_state: CompetitionState
    ) -> str:
        """
        Generate final synthesis (from AI-Talks + Arena).
        
        Args:
            competition_state: Final state
        
        Returns:
            Closing synthesis and winner announcement
        """
        # Identify winner
        leaderboard = competition_state.get_leaderboard()
        if not leaderboard:
            return "The competition concludes."
        
        winner_id, winner_score = leaderboard[0]
        winner = competition_state.participants[winner_id]
        
        # Build synthesis
        synthesis = (
            f"After {competition_state.turn_number} intense turns, "
            f"the Arena crowns its champion.\n\n"
            f"**{winner.name}** emerges victorious with {winner_score:.1f} points, "
            f"demonstrating superior intellectual prowess and strategic acumen.\n\n"
        )
        
        # Add context about the competition
        synthesis += self._synthesize_competition_narrative(competition_state)
        
        # Champion coronation
        synthesis += (
            f"\n\nCongratulations, {winner.name}. You have earned your place "
            f"in the Arena Hall of Champions."
        )
        
        return synthesis
    
    def _synthesize_competition_narrative(
        self,
        competition_state: CompetitionState
    ) -> str:
        """Create narrative synthesis of competition (from AI-Talks pattern)"""
        
        # Count eliminations
        n_eliminated = len(competition_state.eliminated_participant_ids)
        
        # Describe the arc
        narrative = (
            f"This {competition_state.competition_type} saw fierce intellectual "
            f"combat, with {n_eliminated} competitors eliminated along the way. "
        )
        
        # Add quality context
        if competition_state.orbiting_detected:
            narrative += (
                "While the discussion occasionally circled familiar territory, "
                "the competitors ultimately pushed through to new insights. "
            )
        else:
            narrative += (
                "The quality of discourse remained high throughout, "
                "with each turn bringing fresh perspectives. "
            )
        
        # Acknowledge all participants
        active = competition_state.get_active_participants()
        if len(active) > 1:
            narrative += "All competitors demonstrated admirable skill."
        
        return narrative
```

**Validation**:
- Import check
- Test intro generation with mock state
- Verify commentary methods work

---
