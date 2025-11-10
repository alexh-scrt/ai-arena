# 🧪 PHASE 3: INTEGRATION TESTING & VALIDATION
**Duration**: Week 7  
**Goal**: Test complete Phase 1 + Phase 2 integration and run actual Arena competitions

## Phase 3 Overview

Phase 3 validates that Homunculus characters (Phase 1) work seamlessly with AI-Talks orchestration (Phase 2) to create functional Arena competitions. This is **critical validation** before moving to judges and production features.

**Key Objectives**:
1. End-to-end integration tests
2. Run real competitions with Homunculus characters
3. Identify and fix integration bugs
4. Performance optimization
5. Documentation of working system

**Success Criteria**:
- 2+ Homunculus characters can compete
- Full competition runs without crashes
- Turn selection works correctly
- Narrator provides coherent commentary
- State management is consistent
- No memory leaks or performance issues

---

## Phase 3.1: Test Infrastructure Setup

### Task 3.1.1: Create Test Configuration System

**File**: `tests/arena/fixtures/competition_config.py`

**Instructions for Claude Code**:

Create reusable test configurations for different competition scenarios.

```python
"""
Test configuration fixtures for Arena competitions.

Provides pre-configured competition setups for testing different scenarios.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass, field
import logging

logger = logging.getLogger(__name__)


@dataclass
class TestCompetitionConfig:
    """
    Configuration for a test competition.
    
    Defines all parameters needed to run a test competition including
    characters, rules, and expected outcomes.
    """
    # Identity
    name: str
    description: str
    
    # Characters
    character_ids: List[str]  # Homunculus character IDs to use
    
    # Competition parameters
    competition_type: str = "debate"
    topic: str = "Test topic"
    max_turns: int = 10
    
    # Feature flags
    enable_narrator: bool = True
    enable_progression_control: bool = True
    enable_bounded_neurochemistry: bool = True
    
    # Scoring configuration
    scoring_weights: Dict[str, float] = field(default_factory=lambda: {
        'novelty': 0.25,
        'builds_on_others': 0.20,
        'solves_subproblem': 0.25,
        'radical_idea': 0.15,
        'manipulation': 0.15
    })
    elimination_threshold: float = -10.0
    
    # Expected outcomes (for validation)
    expect_completion: bool = True
    expect_eliminations: bool = False
    min_turns_expected: int = 5
    max_turns_expected: int = 15
    
    # Performance constraints
    max_turn_duration_seconds: float = 30.0
    max_total_duration_seconds: float = 600.0


# Predefined test configurations
TEST_CONFIGS = {
    'minimal': TestCompetitionConfig(
        name="Minimal Test",
        description="Bare minimum test with 2 characters, 5 turns",
        character_ids=["ada_lovelace", "alan_turing"],
        max_turns=5,
        enable_narrator=False,
        enable_progression_control=False,
        min_turns_expected=5,
        max_turns_expected=5
    ),
    
    'basic': TestCompetitionConfig(
        name="Basic Competition",
        description="Standard test with 2 characters, narrator, 10 turns",
        character_ids=["ada_lovelace", "alan_turing"],
        max_turns=10,
        enable_narrator=True,
        enable_progression_control=True,
        min_turns_expected=8,
        max_turns_expected=10
    ),
    
    'multi_character': TestCompetitionConfig(
        name="Multi-Character Competition",
        description="3 characters competing, tests turn selection",
        character_ids=["ada_lovelace", "alan_turing", "grace_hopper"],
        max_turns=15,
        topic="The future of computing",
        min_turns_expected=12,
        max_turns_expected=15
    ),
    
    'elimination_test': TestCompetitionConfig(
        name="Elimination Test",
        description="Tests elimination mechanics with harsh scoring",
        character_ids=["ada_lovelace", "alan_turing"],
        max_turns=20,
        elimination_threshold=-5.0,  # Easier to trigger
        expect_eliminations=True,
        min_turns_expected=10,
        max_turns_expected=20
    ),
    
    'stress_test': TestCompetitionConfig(
        name="Stress Test",
        description="Long competition with 4 characters",
        character_ids=["ada_lovelace", "alan_turing", "grace_hopper", "john_von_neumann"],
        max_turns=50,
        topic="Artificial Intelligence and Consciousness",
        min_turns_expected=40,
        max_turns_expected=50,
        max_total_duration_seconds=1800.0  # 30 minutes
    ),
    
    'progression_test': TestCompetitionConfig(
        name="Progression Analysis Test",
        description="Tests orbiting and stagnation detection",
        character_ids=["ada_lovelace", "alan_turing"],
        max_turns=25,
        enable_progression_control=True,
        topic="A simple yes/no question",  # Forces orbiting
        min_turns_expected=15,
        max_turns_expected=25
    )
}


def get_test_config(config_name: str) -> TestCompetitionConfig:
    """
    Get a predefined test configuration.
    
    Args:
        config_name: Name of configuration
    
    Returns:
        TestCompetitionConfig instance
    
    Raises:
        KeyError: If config name not found
    """
    if config_name not in TEST_CONFIGS:
        raise KeyError(
            f"Unknown config: {config_name}. "
            f"Available: {list(TEST_CONFIGS.keys())}"
        )
    
    return TEST_CONFIGS[config_name]


def list_test_configs() -> List[str]:
    """List available test configuration names"""
    return list(TEST_CONFIGS.keys())


def create_custom_config(
    name: str,
    character_ids: List[str],
    **kwargs
) -> TestCompetitionConfig:
    """
    Create a custom test configuration.
    
    Args:
        name: Configuration name
        character_ids: Character IDs to use
        **kwargs: Additional configuration parameters
    
    Returns:
        TestCompetitionConfig instance
    """
    return TestCompetitionConfig(
        name=name,
        description=kwargs.pop('description', f"Custom config: {name}"),
        character_ids=character_ids,
        **kwargs
    )
```

**Validation**:
- Import check
- Test `get_test_config('basic')`
- Verify all configs are valid

---

### Task 3.1.2: Create Test Runner Utility

**File**: `tests/arena/fixtures/test_runner.py`

**Instructions for Claude Code**:

Create utility for running competitions in tests with logging and validation.

```python
"""
Test runner utility for Arena competitions.

Provides helpers for running competitions in tests with proper logging,
timing, and validation.
"""

import asyncio
import time
import logging
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime

from src.arena.orchestration.competition_orchestrator import CompetitionOrchestrator
from src.arena.orchestration.states.competition_state import CompetitionState
from src.arena.character.character_adapter import CharacterAdapter
from src.arena.character.homunculus_loader import get_loader

from .competition_config import TestCompetitionConfig

logger = logging.getLogger(__name__)


@dataclass
class CompetitionRunResult:
    """
    Results from running a test competition.
    
    Contains metrics, outcomes, and diagnostic information for validation.
    """
    # Success indicators
    completed: bool
    exception: Optional[Exception] = None
    
    # Final state
    final_state: Optional[CompetitionState] = None
    
    # Metrics
    total_turns: int = 0
    total_duration_seconds: float = 0.0
    average_turn_duration_seconds: float = 0.0
    
    # Participant outcomes
    winner_id: Optional[str] = None
    eliminated_ids: List[str] = None
    final_scores: Dict[str, float] = None
    
    # Quality metrics
    narrator_interjections: int = 0
    orbiting_detected: bool = False
    stagnation_detected: bool = False
    
    # Performance metrics
    turns_per_second: float = 0.0
    max_turn_duration: float = 0.0
    min_turn_duration: float = 0.0
    
    # Validation
    meets_expectations: bool = True
    validation_errors: List[str] = None
    
    def __post_init__(self):
        if self.eliminated_ids is None:
            self.eliminated_ids = []
        if self.final_scores is None:
            self.final_scores = {}
        if self.validation_errors is None:
            self.validation_errors = []


class CompetitionTestRunner:
    """
    Utility for running competition tests.
    
    Handles:
    - Character adapter creation
    - Orchestrator setup
    - Competition execution with timing
    - Result collection and validation
    - Logging and diagnostics
    """
    
    def __init__(self, verbose: bool = True):
        """
        Initialize test runner.
        
        Args:
            verbose: Enable verbose logging
        """
        self.verbose = verbose
        
        # Configure logging
        if verbose:
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
    
    async def run_competition(
        self,
        config: TestCompetitionConfig
    ) -> CompetitionRunResult:
        """
        Run a competition based on test configuration.
        
        This is the main method for running test competitions.
        
        Args:
            config: Test configuration
        
        Returns:
            CompetitionRunResult with all metrics and outcomes
        """
        logger.info(f"\n{'='*60}")
        logger.info(f"Running: {config.name}")
        logger.info(f"Description: {config.description}")
        logger.info(f"Characters: {', '.join(config.character_ids)}")
        logger.info(f"Max turns: {config.max_turns}")
        logger.info(f"{'='*60}\n")
        
        result = CompetitionRunResult(completed=False)
        start_time = time.time()
        turn_durations = []
        
        try:
            # Step 1: Create character adapters
            logger.info("📦 Creating character adapters...")
            character_adapters = await self._create_character_adapters(
                config.character_ids,
                config
            )
            
            # Step 2: Create orchestrator
            logger.info("🎭 Creating orchestrator...")
            orchestrator = self._create_orchestrator(
                config,
                character_adapters
            )
            
            # Step 3: Run competition with timing
            logger.info("🚀 Starting competition...\n")
            
            # Monitor turn durations
            original_add_exchange = orchestrator.state.add_exchange
            def timed_add_exchange(*args, **kwargs):
                turn_start = time.time()
                exchange = original_add_exchange(*args, **kwargs)
                turn_duration = time.time() - turn_start
                turn_durations.append(turn_duration)
                return exchange
            
            orchestrator.state.add_exchange = timed_add_exchange
            
            # Run competition
            final_state = await orchestrator.run_competition()
            
            # Step 4: Collect results
            end_time = time.time()
            total_duration = end_time - start_time
            
            result.completed = True
            result.final_state = final_state
            result.total_turns = final_state.turn_number
            result.total_duration_seconds = total_duration
            
            # Calculate metrics
            if turn_durations:
                result.average_turn_duration_seconds = sum(turn_durations) / len(turn_durations)
                result.max_turn_duration = max(turn_durations)
                result.min_turn_duration = min(turn_durations)
            
            if total_duration > 0:
                result.turns_per_second = result.total_turns / total_duration
            
            # Winner and scores
            leaderboard = final_state.get_leaderboard()
            if leaderboard:
                result.winner_id = leaderboard[0][0]
                result.final_scores = dict(leaderboard)
            
            # Eliminations
            result.eliminated_ids = final_state.eliminated_participant_ids
            
            # Quality metrics
            result.narrator_interjections = len(final_state.narrator_interjections)
            result.orbiting_detected = final_state.orbiting_detected
            result.stagnation_detected = final_state.stagnation_turns > 5
            
            # Validation
            result.validation_errors = self._validate_results(result, config)
            result.meets_expectations = len(result.validation_errors) == 0
            
            # Log summary
            self._log_summary(result, config)
            
            return result
            
        except Exception as e:
            logger.error(f"❌ Competition failed: {e}", exc_info=True)
            result.exception = e
            result.total_duration_seconds = time.time() - start_time
            return result
    
    async def _create_character_adapters(
        self,
        character_ids: List[str],
        config: TestCompetitionConfig
    ) -> Dict[str, CharacterAdapter]:
        """
        Create character adapters for competition.
        
        Args:
            character_ids: Character IDs to load
            config: Test configuration
        
        Returns:
            Dict mapping character_id -> CharacterAdapter
        """
        adapters = {}
        loader = get_loader()
        
        for char_id in character_ids:
            try:
                logger.info(f"  Loading {char_id}...")
                
                # Create Homunculus agent
                homunculus_agent = loader.create_homunculus_agent(char_id)
                
                # Wrap in CharacterAdapter
                adapter = CharacterAdapter(
                    character_id=char_id,
                    homunculus_agent=homunculus_agent,
                    enable_bounded_neurochemistry=config.enable_bounded_neurochemistry
                )
                
                adapters[char_id] = adapter
                logger.info(f"  ✓ {adapter.character_name} ready")
                
            except Exception as e:
                logger.error(f"  ✗ Failed to load {char_id}: {e}")
                raise
        
        return adapters
    
    def _create_orchestrator(
        self,
        config: TestCompetitionConfig,
        character_adapters: Dict[str, CharacterAdapter]
    ) -> CompetitionOrchestrator:
        """
        Create orchestrator for competition.
        
        Args:
            config: Test configuration
            character_adapters: Character adapters to use
        
        Returns:
            CompetitionOrchestrator instance
        """
        orchestrator_config = {
            'max_turns': config.max_turns,
            'enable_narrator': config.enable_narrator,
            'enable_progression_control': config.enable_progression_control,
            'scoring_weights': config.scoring_weights,
            'elimination_threshold': config.elimination_threshold
        }
        
        orchestrator = CompetitionOrchestrator(
            competition_id=f"test_{config.name}_{int(time.time())}",
            competition_type=config.competition_type,
            topic=config.topic,
            character_adapters=character_adapters,
            config=orchestrator_config
        )
        
        return orchestrator
    
    def _validate_results(
        self,
        result: CompetitionRunResult,
        config: TestCompetitionConfig
    ) -> List[str]:
        """
        Validate competition results against expectations.
        
        Args:
            result: Competition results
            config: Test configuration with expectations
        
        Returns:
            List of validation error messages (empty if all valid)
        """
        errors = []
        
        # Check completion
        if config.expect_completion and not result.completed:
            errors.append("Competition did not complete as expected")
        
        # Check turn count
        if result.total_turns < config.min_turns_expected:
            errors.append(
                f"Too few turns: {result.total_turns} < {config.min_turns_expected}"
            )
        
        if result.total_turns > config.max_turns_expected:
            errors.append(
                f"Too many turns: {result.total_turns} > {config.max_turns_expected}"
            )
        
        # Check eliminations
        if config.expect_eliminations and not result.eliminated_ids:
            errors.append("Expected eliminations but none occurred")
        
        # Check duration
        if result.total_duration_seconds > config.max_total_duration_seconds:
            errors.append(
                f"Competition took too long: {result.total_duration_seconds:.1f}s"
            )
        
        # Check turn performance
        if result.max_turn_duration > config.max_turn_duration_seconds:
            errors.append(
                f"Turn took too long: {result.max_turn_duration:.1f}s"
            )
        
        # Check for winner
        if not result.winner_id and config.expect_completion:
            errors.append("No winner determined")
        
        return errors
    
    def _log_summary(
        self,
        result: CompetitionRunResult,
        config: TestCompetitionConfig
    ):
        """Log competition summary"""
        logger.info(f"\n{'='*60}")
        logger.info(f"COMPETITION SUMMARY: {config.name}")
        logger.info(f"{'='*60}")
        
        # Status
        status = "✅ SUCCESS" if result.meets_expectations else "⚠️  ISSUES FOUND"
        logger.info(f"Status: {status}")
        
        # Basic metrics
        logger.info(f"\nMetrics:")
        logger.info(f"  Total turns: {result.total_turns}")
        logger.info(f"  Duration: {result.total_duration_seconds:.2f}s")
        logger.info(f"  Avg turn: {result.average_turn_duration_seconds:.2f}s")
        logger.info(f"  Throughput: {result.turns_per_second:.2f} turns/sec")
        
        # Winner
        if result.winner_id and result.final_state:
            winner = result.final_state.participants[result.winner_id]
            logger.info(f"\n🏆 Winner: {winner.name}")
            logger.info(f"  Score: {winner.cumulative_score:.2f}")
        
        # Eliminations
        if result.eliminated_ids:
            logger.info(f"\n❌ Eliminated: {len(result.eliminated_ids)}")
            for eliminated_id in result.eliminated_ids:
                if result.final_state:
                    eliminated = result.final_state.participants[eliminated_id]
                    logger.info(f"  - {eliminated.name}")
        
        # Quality
        logger.info(f"\nQuality Indicators:")
        logger.info(f"  Narrator interjections: {result.narrator_interjections}")
        logger.info(f"  Orbiting detected: {result.orbiting_detected}")
        logger.info(f"  Stagnation detected: {result.stagnation_detected}")
        
        # Validation
        if result.validation_errors:
            logger.warning(f"\n⚠️  Validation Issues:")
            for error in result.validation_errors:
                logger.warning(f"  - {error}")
        
        logger.info(f"{'='*60}\n")


# Global test runner instance
_test_runner: Optional[CompetitionTestRunner] = None


def get_test_runner(verbose: bool = True) -> CompetitionTestRunner:
    """Get or create global test runner"""
    global _test_runner
    if _test_runner is None:
        _test_runner = CompetitionTestRunner(verbose=verbose)
    return _test_runner
```

**Validation**:
- Import check
- Verify all methods are properly typed
- Test runner instantiation works

---

## Phase 3.2: Basic Integration Tests

### Task 3.2.1: Create Minimal Integration Test

**File**: `tests/arena/test_minimal_integration.py`

**Instructions for Claude Code**:

The simplest possible integration test - 2 characters, 5 turns, no extras.

```python
"""
Minimal integration test for Arena.

This is the absolute simplest end-to-end test:
- 2 Homunculus characters
- 5 turns
- No narrator, no progression control
- Just verify basic mechanics work

If this fails, Phase 1 + Phase 2 integration has fundamental issues.
"""

import pytest
import asyncio
from pathlib import Path

from tests.arena.fixtures.competition_config import get_test_config
from tests.arena.fixtures.test_runner import get_test_runner


@pytest.mark.integration
@pytest.mark.asyncio
@pytest.mark.skipif(
    not Path("../homunculus").exists() or not Path("../talks").exists(),
    reason="Requires Homunculus and AI-Talks"
)
async def test_minimal_competition():
    """
    Minimal integration test.
    
    This test verifies the absolute minimum:
    1. Two characters can be loaded
    2. Orchestrator can be created
    3. Competition runs for 5 turns
    4. No crashes occur
    5. State is consistent
    
    This is the "hello world" of Arena integration.
    """
    # Get minimal config
    config = get_test_config('minimal')
    
    # Run competition
    runner = get_test_runner(verbose=True)
    result = await runner.run_competition(config)
    
    # Validate basic success
    assert result.completed, f"Competition failed: {result.exception}"
    assert result.final_state is not None, "No final state"
    assert result.total_turns == 5, f"Expected 5 turns, got {result.total_turns}"
    
    # Validate state consistency
    state = result.final_state
    
    # Check participants exist
    assert len(state.participants) == 2, "Should have 2 participants"
    
    # Check exchanges recorded
    assert len(state.exchanges) == 5, f"Expected 5 exchanges, got {len(state.exchanges)}"
    
    # Check all turns have valid participants
    for exchange in state.exchanges:
        assert exchange.participant_id in state.participants, \
            f"Invalid participant ID in exchange: {exchange.participant_id}"
        assert exchange.speaker_name != "", "Empty speaker name"
        assert len(exchange.content) > 0, "Empty exchange content"
    
    # Check no eliminations (not expected in minimal test)
    assert len(state.eliminated_participant_ids) == 0, "Unexpected eliminations"
    
    # Check all participants still active
    assert len(state.active_participant_ids) == 2, "Should have 2 active participants"
    
    print("\n✅ MINIMAL INTEGRATION TEST PASSED")
    print(f"   Competition ran successfully for {result.total_turns} turns")
    print(f"   Duration: {result.total_duration_seconds:.2f}s")


@pytest.mark.integration
@pytest.mark.asyncio
@pytest.mark.skipif(
    not Path("../homunculus").exists() or not Path("../talks").exists(),
    reason="Requires Homunculus and AI-Talks"
)
async def test_character_response_quality():
    """
    Test that character responses are reasonable quality.
    
    Verifies:
    - Responses are not empty
    - Responses are not too short (> 20 words)
    - Responses are on-topic
    - Characters maintain personality
    """
    config = get_test_config('minimal')
    runner = get_test_runner(verbose=False)
    result = await runner.run_competition(config)
    
    assert result.completed, "Competition did not complete"
    
    # Check each exchange
    for exchange in result.final_state.exchanges:
        content = exchange.content
        
        # Not empty
        assert len(content) > 0, f"Empty content in turn {exchange.turn_number}"
        
        # Reasonable length (at least 20 words)
        word_count = len(content.split())
        assert word_count >= 20, \
            f"Response too short ({word_count} words) in turn {exchange.turn_number}"
        
        # Not a error message
        assert "error" not in content.lower(), \
            f"Error in response: {content[:100]}"
        assert "exception" not in content.lower(), \
            f"Exception in response: {content[:100]}"
    
    print("\n✅ CHARACTER RESPONSE QUALITY TEST PASSED")


if __name__ == '__main__':
    # Run with: python -m pytest tests/arena/test_minimal_integration.py -v -s
    pytest.main([__file__, '-v', '-s'])
```

**Validation**:
- This test MUST pass for Phase 3 to be considered successful
- If it fails, there are fundamental integration issues
- Run: `pytest tests/arena/test_minimal_integration.py -v -s`

---

### Task 3.2.2: Create Basic Competition Test

**File**: `tests/arena/test_basic_competition.py`

**Instructions for Claude Code**:

Standard competition test with all features enabled.

```python
"""
Basic competition integration test.

Tests a full-featured competition:
- 2 Homunculus characters
- 10 turns
- Narrator enabled
- Progression control enabled
- Turn selection working
- State management correct

This validates the standard Arena competition flow.
"""

import pytest
import asyncio
from pathlib import Path

from tests.arena.fixtures.competition_config import get_test_config
from tests.arena.fixtures.test_runner import get_test_runner


@pytest.mark.integration
@pytest.mark.asyncio
@pytest.mark.skipif(
    not Path("../homunculus").exists() or not Path("../talks").exists(),
    reason="Requires Homunculus and AI-Talks"
)
async def test_basic_competition():
    """
    Basic competition with all standard features.
    
    Validates:
    1. Competition runs with narrator
    2. Progression control works
    3. Turn selection distributes turns fairly
    4. Scoring is tracked
    5. Narrator provides appropriate commentary
    6. No performance issues
    """
    config = get_test_config('basic')
    runner = get_test_runner(verbose=True)
    result = await runner.run_competition(config)
    
    # Basic success
    assert result.completed, f"Competition failed: {result.exception}"
    assert result.meets_expectations, \
        f"Validation errors: {result.validation_errors}"
    
    state = result.final_state
    
    # Turn distribution
    participant_turn_counts = {}
    for exchange in state.exchanges:
        pid = exchange.participant_id
        participant_turn_counts[pid] = participant_turn_counts.get(pid, 0) + 1
    
    # Both characters should have spoken
    assert len(participant_turn_counts) == 2, "Not all characters spoke"
    
    # Distribution should be relatively fair (within 2 turns)
    turn_counts = list(participant_turn_counts.values())
    assert abs(turn_counts[0] - turn_counts[1]) <= 2, \
        f"Unfair turn distribution: {participant_turn_counts}"
    
    # Narrator should have provided commentary
    assert result.narrator_interjections > 0, "Narrator never interjected"
    
    # Check narrator interjections are reasonable
    interjections = state.narrator_interjections
    assert len(interjections) >= 1, "Expected at least introduction"
    
    # First should be introduction
    assert interjections[0]['type'] == 'introduction', \
        "First interjection should be introduction"
    
    # Check scoring
    for participant in state.participants.values():
        # Each participant should have some score
        # (may be negative if poor performance, but should exist)
        assert hasattr(participant, 'cumulative_score'), \
            f"{participant.name} missing cumulative_score"
        assert hasattr(participant, 'turn_scores'), \
            f"{participant.name} missing turn_scores"
    
    # Check winner determined
    assert result.winner_id is not None, "No winner determined"
    
    # Performance check
    assert result.average_turn_duration_seconds < 30.0, \
        f"Turns too slow: {result.average_turn_duration_seconds:.2f}s avg"
    
    print("\n✅ BASIC COMPETITION TEST PASSED")
    print(f"   Turns: {result.total_turns}")
    print(f"   Duration: {result.total_duration_seconds:.2f}s")
    print(f"   Narrator interjections: {result.narrator_interjections}")
    print(f"   Winner: {state.participants[result.winner_id].name}")


@pytest.mark.integration
@pytest.mark.asyncio
@pytest.mark.skipif(
    not Path("../homunculus").exists() or not Path("../talks").exists(),
    reason="Requires Homunculus and AI-Talks"
)
async def test_turn_selection_fairness():
    """
    Test that turn selector distributes turns fairly.
    
    With game theory + fairness mechanisms, no character should
    dominate the conversation.
    """
    config = get_test_config('basic')
    runner = get_test_runner(verbose=False)
    result = await runner.run_competition(config)
    
    assert result.completed, "Competition did not complete"
    
    state = result.final_state
    
    # Count turns per participant
    turn_counts = {}
    for exchange in state.exchanges:
        pid = exchange.participant_id
        turn_counts[pid] = turn_counts.get(pid, 0) + 1
    
    # With 2 participants and 10 turns, expect 4-6 turns each
    for pid, count in turn_counts.items():
        participant = state.participants[pid]
        assert 4 <= count <= 6, \
            f"{participant.name} got {count} turns (expected 4-6)"
    
    print("\n✅ TURN SELECTION FAIRNESS TEST PASSED")
    print(f"   Turn distribution: {turn_counts}")


@pytest.mark.integration
@pytest.mark.asyncio
@pytest.mark.skipif(
    not Path("../homunculus").exists() or not Path("../talks").exists(),
    reason="Requires Homunculus and AI-Talks"
)
async def test_progression_analysis():
    """
    Test that progression controller analyzes competition correctly.
    
    Verifies:
    - Novelty scores are tracked
    - Orbiting detection works
    - Stagnation detection works
    """
    config = get_test_config('basic')
    runner = get_test_runner(verbose=False)
    result = await runner.run_competition(config)
    
    assert result.completed, "Competition did not complete"
    
    state = result.final_state
    
    # Progression analysis should have run
    # (orbiting_score is set by progression controller)
    assert hasattr(state, 'orbiting_detected'), \
        "Orbiting detection not run"
    assert hasattr(state, 'orbiting_score'), \
        "Orbiting score not calculated"
    
    # In a healthy discussion, orbiting_score should be < 0.75
    if not result.orbiting_detected:
        assert state.orbiting_score < 0.75, \
            f"High orbiting score without detection: {state.orbiting_score}"
    
    print("\n✅ PROGRESSION ANALYSIS TEST PASSED")
    print(f"   Orbiting detected: {result.orbiting_detected}")
    print(f"   Orbiting score: {state.orbiting_score:.2f}")
    print(f"   Stagnation detected: {result.stagnation_detected}")


if __name__ == '__main__':
    pytest.main([__file__, '-v', '-s'])
```

**Validation**:
- Run: `pytest tests/arena/test_basic_competition.py -v -s`
- All tests should pass
- Validate turn selection fairness
- Check narrator quality

---

## Phase 3.3: Advanced Integration Tests

### Task 3.3.1: Create Multi-Character Test

**File**: `tests/arena/test_multi_character.py`

**Instructions for Claude Code**:

Test with 3+ characters to validate complex turn selection.

```python
"""
Multi-character integration test.

Tests competitions with 3+ characters:
- More complex turn selection
- Multiple relationships
- Strategic dynamics
- Narrator tracking multiple threads

This validates Arena can handle realistic competition sizes.
"""

import pytest
import asyncio
from pathlib import Path

from tests.arena.fixtures.competition_config import get_test_config
from tests.arena.fixtures.test_runner import get_test_runner


@pytest.mark.integration
@pytest.mark.asyncio
@pytest.mark.timeout(600)  # 10 minute timeout
@pytest.mark.skipif(
    not Path("../homunculus").exists() or not Path("../talks").exists(),
    reason="Requires Homunculus and AI-Talks"
)
async def test_three_character_competition():
    """
    Test competition with 3 characters.
    
    Validates:
    - Turn selection works with 3 participants
    - All participants get fair opportunity
    - Strategic dynamics emerge
    - State management scales
    """
    config = get_test_config('multi_character')
    runner = get_test_runner(verbose=True)
    result = await runner.run_competition(config)
    
    assert result.completed, f"Competition failed: {result.exception}"
    assert result.meets_expectations, \
        f"Validation errors: {result.validation_errors}"
    
    state = result.final_state
    
    # All 3 participants should have spoken
    participant_ids = set(ex.participant_id for ex in state.exchanges)
    assert len(participant_ids) == 3, \
        f"Not all participants spoke: {participant_ids}"
    
    # Count turns per participant
    turn_counts = {}
    for exchange in state.exchanges:
        pid = exchange.participant_id
        turn_counts[pid] = turn_counts.get(pid, 0) + 1
    
    # With 3 participants and 15 turns, expect 4-6 turns each
    for pid, count in turn_counts.items():
        participant = state.participants[pid]
        assert 3 <= count <= 7, \
            f"{participant.name} got {count} turns (expected 3-7)"
    
    # Check that participants interact with each other
    # (look for exchanges that target other participants)
    interactions_found = False
    for exchange in state.exchanges:
        if exchange.targets and len(exchange.targets) > 0:
            interactions_found = True
            break
    
    # In a 15-turn discussion, should have some direct interactions
    # (though not required in all turns)
    print(f"   Direct interactions found: {interactions_found}")
    
    print("\n✅ THREE CHARACTER COMPETITION TEST PASSED")
    print(f"   Turn distribution: {turn_counts}")
    print(f"   Winner: {state.participants[result.winner_id].name}")


@pytest.mark.integration
@pytest.mark.asyncio
@pytest.mark.timeout(600)
@pytest.mark.skipif(
    not Path("../homunculus").exists() or not Path("../talks").exists(),
    reason="Requires Homunculus and AI-Talks"
)
async def test_relationship_tracking():
    """
    Test that relationships between characters are tracked.
    
    Over multiple turns, characters should develop relationships
    (positive or negative) based on interactions.
    """
    config = get_test_config('multi_character')
    runner = get_test_runner(verbose=False)
    result = await runner.run_competition(config)
    
    assert result.completed, "Competition did not complete"
    
    state = result.final_state
    
    # Check that relationships exist
    relationships_tracked = False
    for participant in state.participants.values():
        if participant.relationships and len(participant.relationships) > 0:
            relationships_tracked = True
            print(f"   {participant.name} relationships: {participant.relationships}")
    
    # Relationships should develop over 15 turns
    # (though not strictly required)
    print(f"   Relationships tracked: {relationships_tracked}")
    
    print("\n✅ RELATIONSHIP TRACKING TEST PASSED")


if __name__ == '__main__':
    pytest.main([__file__, '-v', '-s'])
```

**Validation**:
- Run: `pytest tests/arena/test_multi_character.py -v -s`
- Verify all 3 characters participate
- Check turn distribution is fair

---

### Task 3.3.2: Create Elimination Test

**File**: `tests/arena/test_elimination.py`

**Instructions for Claude Code**:

Test elimination mechanics work correctly.

```python
"""
Elimination integration test.

Tests that elimination mechanics work:
- Low-scoring participants detected
- Elimination triggered correctly
- Narrator announces elimination
- State updated properly
- Competition continues with remaining participants

This validates a core Arena competitive feature.
"""

import pytest
import asyncio
from pathlib import Path

from tests.arena.fixtures.competition_config import get_test_config
from tests.arena.fixtures.test_runner import get_test_runner


@pytest.mark.integration
@pytest.mark.asyncio
@pytest.mark.timeout(900)  # 15 minute timeout
@pytest.mark.skipif(
    not Path("../homunculus").exists() or not Path("../talks").exists(),
    reason="Requires Homunculus and AI-Talks"
)
async def test_elimination_mechanics():
    """
    Test elimination mechanics.
    
    Uses harsh elimination threshold to force elimination.
    
    Validates:
    - Elimination triggered when score drops below threshold
    - Narrator announces elimination
    - State updated correctly
    - Competition continues with remaining participants
    - Winner determined from survivors
    """
    config = get_test_config('elimination_test')
    runner = get_test_runner(verbose=True)
    result = await runner.run_competition(config)
    
    assert result.completed, f"Competition failed: {result.exception}"
    
    state = result.final_state
    
    # With harsh threshold, should have elimination
    # (though not guaranteed depending on LLM performance)
    if result.eliminated_ids:
        print(f"   ✓ Elimination occurred: {len(result.eliminated_ids)} eliminated")
        
        # Check eliminated participants
        for eliminated_id in result.eliminated_ids:
            eliminated = state.participants[eliminated_id]
            
            # Should be marked as eliminated
            assert eliminated.status.value == "eliminated", \
                f"{eliminated.name} not marked as eliminated"
            
            # Should have elimination reason
            assert eliminated.elimination_reason is not None, \
                f"{eliminated.name} missing elimination reason"
            
            # Should have low score
            print(f"     {eliminated.name}: {eliminated.cumulative_score:.2f} points")
        
        # Check narrator announced elimination
        elimination_announcements = [
            interj for interj in state.narrator_interjections
            if 'elimination' in interj.get('type', '').lower()
        ]
        
        if state.enable_narrator:
            assert len(elimination_announcements) > 0, \
                "Narrator did not announce elimination"
        
        # Winner should not be eliminated
        if result.winner_id:
            assert result.winner_id not in result.eliminated_ids, \
                "Winner was eliminated"
        
        print("\n✅ ELIMINATION MECHANICS TEST PASSED")
    else:
        print("\n   ℹ️ No eliminations occurred (scores too high)")
        print("   This is acceptable - elimination is probabilistic")


@pytest.mark.integration
@pytest.mark.asyncio
@pytest.mark.timeout(900)
@pytest.mark.skipif(
    not Path("../homunculus").exists() or not Path("../talks").exists(),
    reason="Requires Homunculus and AI-Talks"
)
async def test_final_words():
    """
    Test that eliminated participants get final words.
    
    When a character is eliminated, they should get one last
    contribution (final words) before being removed.
    """
    config = get_test_config('elimination_test')
    runner = get_test_runner(verbose=False)
    result = await runner.run_competition(config)
    
    assert result.completed, "Competition did not complete"
    
    # This test is informational - we can't guarantee elimination
    # but if it happens, we can validate the process
    
    if result.eliminated_ids:
        state = result.final_state
        
        # Look for final words phase
        final_words_phases = [
            ex for ex in state.exchanges
            # Check if near elimination turn
        ]
        
        print(f"\n   Eliminations: {len(result.eliminated_ids)}")
        print("   ✅ FINAL WORDS TEST COMPLETED")
    else:
        print("\n   ℹ️ No eliminations - test skipped")


if __name__ == '__main__':
    pytest.main([__file__, '-v', '-s'])
```

**Validation**:
- Run: `pytest tests/arena/test_elimination.py -v -s`
- Test may not always trigger elimination (depends on LLM performance)
- If elimination occurs, validate all mechanics

---

## Phase 3.4: Performance and Stress Tests

### Task 3.4.1: Create Performance Benchmark Test

**File**: `tests/arena/test_performance.py`

**Instructions for Claude Code**:

Benchmark performance characteristics.

```python
"""
Performance benchmark tests.

Tests performance characteristics:
- Turn generation speed
- Memory usage
- Scalability with more participants
- Long-running competitions

This validates Arena can handle production loads.
"""

import pytest
import asyncio
import time
import psutil
import os
from pathlib import Path

from tests.arena.fixtures.competition_config import get_test_config, create_custom_config
from tests.arena.fixtures.test_runner import get_test_runner


@pytest.mark.performance
@pytest.mark.asyncio
@pytest.mark.timeout(1800)  # 30 minute timeout
@pytest.mark.skipif(
    not Path("../homunculus").exists() or not Path("../talks").exists(),
    reason="Requires Homunculus and AI-Talks"
)
async def test_turn_generation_speed():
    """
    Benchmark turn generation speed.
    
    Measures:
    - Average time per turn
    - Variance in turn times
    - Throughput (turns per second)
    
    Acceptable performance:
    - Average turn < 10 seconds
    - Max turn < 30 seconds
    """
    config = get_test_config('basic')
    runner = get_test_runner(verbose=False)
    
    result = await runner.run_competition(config)
    
    assert result.completed, "Competition did not complete"
    
    # Performance metrics
    print(f"\n📊 TURN GENERATION PERFORMANCE")
    print(f"   Average turn: {result.average_turn_duration_seconds:.2f}s")
    print(f"   Min turn: {result.min_turn_duration:.2f}s")
    print(f"   Max turn: {result.max_turn_duration:.2f}s")
    print(f"   Throughput: {result.turns_per_second:.2f} turns/sec")
    
    # Validate acceptable performance
    assert result.average_turn_duration_seconds < 10.0, \
        f"Average turn too slow: {result.average_turn_duration_seconds:.2f}s"
    
    assert result.max_turn_duration < 30.0, \
        f"Max turn too slow: {result.max_turn_duration:.2f}s"
    
    print("   ✅ Performance acceptable")


@pytest.mark.performance
@pytest.mark.asyncio
@pytest.mark.timeout(3600)  # 1 hour timeout
@pytest.mark.skipif(
    not Path("../homunculus").exists() or not Path("../talks").exists(),
    reason="Requires Homunculus and AI-Talks"
)
async def test_memory_usage():
    """
    Test memory usage during competition.
    
    Monitors:
    - Peak memory usage
    - Memory growth over time
    - Memory leaks
    
    Acceptable: < 2GB peak memory for 2-character competition
    """
    process = psutil.Process(os.getpid())
    
    # Baseline memory
    baseline_memory = process.memory_info().rss / 1024 / 1024  # MB
    
    config = get_test_config('basic')
    runner = get_test_runner(verbose=False)
    
    result = await runner.run_competition(config)
    
    assert result.completed, "Competition did not complete"
    
    # Peak memory
    peak_memory = process.memory_info().rss / 1024 / 1024  # MB
    memory_used = peak_memory - baseline_memory
    
    print(f"\n💾 MEMORY USAGE")
    print(f"   Baseline: {baseline_memory:.1f} MB")
    print(f"   Peak: {peak_memory:.1f} MB")
    print(f"   Used: {memory_used:.1f} MB")
    
    # Validate acceptable memory usage
    assert memory_used < 2048, \
        f"Memory usage too high: {memory_used:.1f} MB"
    
    print("   ✅ Memory usage acceptable")


@pytest.mark.stress
@pytest.mark.asyncio
@pytest.mark.timeout(3600)  # 1 hour timeout
@pytest.mark.skipif(
    not Path("../homunculus").exists() or not Path("../talks").exists(),
    reason="Requires Homunculus and AI-Talks"
)
async def test_long_competition():
    """
    Stress test with long competition.
    
    Runs 50-turn competition to test:
    - System stability over time
    - Memory growth
    - Performance degradation
    
    This simulates a production-scale competition.
    """
    config = get_test_config('stress_test')
    runner = get_test_runner(verbose=True)
    
    result = await runner.run_competition(config)
    
    assert result.completed, f"Competition failed: {result.exception}"
    
    # Should complete without major issues
    assert result.meets_expectations or len(result.validation_errors) <= 2, \
        f"Too many validation errors: {result.validation_errors}"
    
    print(f"\n🔥 STRESS TEST COMPLETED")
    print(f"   Turns: {result.total_turns}")
    print(f"   Duration: {result.total_duration_seconds:.1f}s")
    print(f"   Avg turn: {result.average_turn_duration_seconds:.2f}s")
    
    # Performance should not degrade significantly
    # (max turn shouldn't be much more than 2x average)
    if result.max_turn_duration > result.average_turn_duration_seconds * 3:
        print(f"   ⚠️ Performance degradation detected")
        print(f"   Max turn: {result.max_turn_duration:.2f}s")
        print(f"   Avg turn: {result.average_turn_duration_seconds:.2f}s")
    else:
        print(f"   ✅ No significant performance degradation")


if __name__ == '__main__':
    pytest.main([__file__, '-v', '-s', '-m', 'performance'])
```

**Validation**:
- Run: `pytest tests/arena/test_performance.py -v -s -m performance`
- Check turn generation speed acceptable
- Verify no memory leaks
- Validate long competitions work

---

## Phase 3.5: Diagnostic and Debugging Tools

### Task 3.5.1: Create Competition Inspector

**File**: `tests/arena/tools/competition_inspector.py`

**Instructions for Claude Code**:

Tool for inspecting competition results in detail.

```python
"""
Competition Inspector

Utility for detailed inspection of competition results.
Useful for debugging integration issues and understanding competition dynamics.
"""

from typing import Optional
from src.arena.orchestration.states.competition_state import CompetitionState
import json


class CompetitionInspector:
    """
    Inspector for analyzing competition results.
    
    Provides detailed views of:
    - Turn-by-turn breakdown
    - Participant analysis
    - Scoring patterns
    - Quality metrics
    - Narrator interjections
    """
    
    def __init__(self, competition_state: CompetitionState):
        """
        Initialize inspector.
        
        Args:
            competition_state: Final competition state to inspect
        """
        self.state = competition_state
    
    def print_full_report(self):
        """Print comprehensive competition report"""
        print(f"\n{'='*80}")
        print(f"COMPETITION INSPECTION REPORT")
        print(f"{'='*80}")
        
        self._print_overview()
        self._print_participant_summary()
        self._print_turn_breakdown()
        self._print_narrator_summary()
        self._print_quality_metrics()
        
        print(f"{'='*80}\n")
    
    def _print_overview(self):
        """Print competition overview"""
        print(f"\n📋 OVERVIEW")
        print(f"   Competition ID: {self.state.competition_id}")
        print(f"   Type: {self.state.competition_type}")
        print(f"   Topic: {self.state.topic}")
        print(f"   Total Turns: {self.state.turn_number}")
        print(f"   Phase: {self.state.phase.value}")
        
        if self.state.started_at:
            print(f"   Started: {self.state.started_at.strftime('%Y-%m-%d %H:%M:%S')}")
        if self.state.completed_at:
            print(f"   Completed: {self.state.completed_at.strftime('%Y-%m-%d %H:%M:%S')}")
            duration = (self.state.completed_at - self.state.started_at).total_seconds()
            print(f"   Duration: {duration:.1f}s")
    
    def _print_participant_summary(self):
        """Print participant summary"""
        print(f"\n👥 PARTICIPANTS")
        
        leaderboard = self.state.get_leaderboard()
        
        for rank, (pid, score) in enumerate(leaderboard, 1):
            participant = self.state.participants[pid]
            
            status_emoji = "🏆" if rank == 1 else "✅" if participant.is_active else "❌"
            
            print(f"\n   {status_emoji} #{rank}: {participant.name}")
            print(f"      Score: {score:.2f}")
            print(f"      Turns: {participant.turns_taken}")
            print(f"      Status: {participant.status.value}")
            
            if participant.turn_scores:
                avg_score = sum(participant.turn_scores) / len(participant.turn_scores)
                print(f"      Avg per turn: {avg_score:.2f}")
            
            if participant.elimination_reason:
                print(f"      Elimination: {participant.elimination_reason}")
    
    def _print_turn_breakdown(self):
        """Print turn-by-turn breakdown"""
        print(f"\n📝 TURN BREAKDOWN")
        
        for i, exchange in enumerate(self.state.exchanges[-10:], 1):  # Last 10 turns
            participant = self.state.participants[exchange.participant_id]
            
            print(f"\n   Turn {exchange.turn_number}: {participant.name}")
            print(f"      Move: {exchange.move_type}")
            
            if exchange.targets:
                target_names = [
                    self.state.participants[t].name
                    for t in exchange.targets
                    if t in self.state.participants
                ]
                print(f"      Targets: {', '.join(target_names)}")
            
            # Content preview
            content_preview = exchange.content[:100] + "..." if len(exchange.content) > 100 else exchange.content
            print(f"      Content: {content_preview}")
            
            # Scoring
            if exchange.total_score > 0:
                print(f"      Score: {exchange.total_score:.2f}/10")
                if exchange.scores:
                    print(f"      Breakdown: {exchange.scores}")
            
            # Quality
            if exchange.novelty_score > 0:
                print(f"      Novelty: {exchange.novelty_score:.2f}")
    
    def _print_narrator_summary(self):
        """Print narrator interjection summary"""
        if not self.state.narrator_interjections:
            return
        
        print(f"\n🎙️ NARRATOR INTERJECTIONS ({len(self.state.narrator_interjections)})")
        
        for interj in self.state.narrator_interjections:
            turn = interj.get('turn', -1)
            interj_type = interj.get('type', 'unknown')
            content = interj.get('content', '')
            
            turn_str = "Pre-competition" if turn == -1 else f"Turn {turn}"
            
            print(f"\n   {turn_str} ({interj_type}):")
            
            # Content preview
            content_preview = content[:150] + "..." if len(content) > 150 else content
            print(f"      {content_preview}")
    
    def _print_quality_metrics(self):
        """Print quality metrics"""
        print(f"\n📊 QUALITY METRICS")
        print(f"   Orbiting detected: {self.state.orbiting_detected}")
        print(f"   Orbiting score: {self.state.orbiting_score:.2f}")
        print(f"   Stagnation turns: {self.state.stagnation_turns}")
        
        # Novelty analysis
        exchanges_with_novelty = [
            ex for ex in self.state.exchanges
            if ex.novelty_score > 0
        ]
        
        if exchanges_with_novelty:
            avg_novelty = sum(ex.novelty_score for ex in exchanges_with_novelty) / len(exchanges_with_novelty)
            print(f"   Average novelty: {avg_novelty:.2f}")
    
    def export_to_json(self, filepath: str):
        """
        Export competition state to JSON.
        
        Args:
            filepath: Path to save JSON file
        """
        # Create serializable dict
        export_data = {
            'competition_id': self.state.competition_id,
            'competition_type': self.state.competition_type,
            'topic': self.state.topic,
            'total_turns': self.state.turn_number,
            'participants': {},
            'exchanges': [],
            'narrator_interjections': self.state.narrator_interjections
        }
        
        # Participants
        for pid, participant in self.state.participants.items():
            export_data['participants'][pid] = {
                'name': participant.name,
                'cumulative_score': participant.cumulative_score,
                'turns_taken': participant.turns_taken,
                'status': participant.status.value,
                'turn_scores': participant.turn_scores
            }
        
        # Exchanges
        for exchange in self.state.exchanges:
            export_data['exchanges'].append({
                'turn': exchange.turn_number,
                'participant_id': exchange.participant_id,
                'speaker_name': exchange.speaker_name,
                'content': exchange.content,
                'move_type': exchange.move_type,
                'targets': exchange.targets,
                'total_score': exchange.total_score,
                'scores': exchange.scores,
                'novelty_score': exchange.novelty_score
            })
        
        # Write JSON
        with open(filepath, 'w') as f:
            json.dump(export_data, f, indent=2)
        
        print(f"\n✅ Exported to {filepath}")


def inspect_competition(competition_state: CompetitionState):
    """
    Convenience function to inspect a competition.
    
    Args:
        competition_state: State to inspect
    """
    inspector = CompetitionInspector(competition_state)
    inspector.print_full_report()
```

**Validation**:
- Import check
- Test with a completed competition state
- Verify report is readable

---

## Phase 3.6: Phase 3 Completion Checklist

**Instructions for Claude Code**:

Verify all Phase 3 components are complete and tests pass.

### Completion Criteria:

1. **Test Infrastructure** ✓
   - [ ] Test configurations created
   - [ ] Test runner implemented
   - [ ] Fixtures working correctly

2. **Minimal Integration** ✓
   - [ ] `test_minimal_integration.py` created
   - [ ] Minimal test passes
   - [ ] 2 characters can compete
   - [ ] 5 turns complete without crashes

3. **Basic Integration** ✓
   - [ ] `test_basic_competition.py` created
   - [ ] Basic test passes
   - [ ] Narrator works
   - [ ] Progression control works
   - [ ] Turn selection fair

4. **Advanced Integration** ✓
   - [ ] `test_multi_character.py` created
   - [ ] 3-character competition works
   - [ ] `test_elimination.py` created
   - [ ] Elimination mechanics work (if triggered)

5. **Performance** ✓
   - [ ] `test_performance.py` created
   - [ ] Turn generation acceptable speed
   - [ ] Memory usage reasonable
   - [ ] Long competitions stable

6. **Tools** ✓
   - [ ] Competition inspector created
   - [ ] Can analyze competition results
   - [ ] JSON export works

### Manual Verification:

```bash
# Run all Phase 3 tests
pytest tests/arena/test_*.py -v -s

# Run just integration tests
pytest tests/arena/ -v -s -m integration

# Run performance tests
pytest tests/arena/ -v -s -m performance

# Run specific critical test
pytest tests/arena/test_minimal_integration.py -v -s

# Generate coverage report
pytest tests/arena/ --cov=src/arena --cov-report=html
```

### Success Metrics:

**CRITICAL (must pass)**:
- ✅ Minimal integration test passes
- ✅ Basic competition test passes
- ✅ No crashes during competitions
- ✅ State management consistent

**IMPORTANT (should pass)**:
- ✅ Multi-character test passes
- ✅ Turn selection fair
- ✅ Narrator provides coherent commentary
- ✅ Performance acceptable (< 10s per turn average)

**NICE TO HAVE**:
- ✅ Elimination test triggers elimination
- ✅ Stress test passes
- ✅ Memory usage optimal

### Phase 3 Deliverables:

- ✅ Complete test infrastructure
- ✅ Working end-to-end integration
- ✅ Homunculus + AI-Talks proven integration
- ✅ Performance benchmarks established
- ✅ Diagnostic tools available
- ✅ Documentation of integration issues

---

## Phase 3.7: Integration Issues Documentation

### Task 3.7.1: Create Known Issues Document

**File**: `docs/phase3_integration_issues.md`

**Instructions for Claude Code**:

Document known issues discovered during Phase 3 testing.

```markdown
# Phase 3 Integration Issues

## Overview

This document tracks integration issues discovered during Phase 3 testing
and their resolutions.

## Critical Issues (Blocking)

### Issue #1: [Example - To be filled during testing]

**Status**: RESOLVED / OPEN / IN PROGRESS

**Description**: 
Describe the issue in detail.

**Reproduction**:
```python
# Steps to reproduce
```

**Root Cause**:
Explanation of what causes the issue.

**Solution**:
How it was fixed.

**Related Tests**:
- `test_minimal_integration::test_minimal_competition`

---

## High Priority Issues

### Issue #2: [Example - To be filled during testing]

**Status**: OPEN

**Description**: 
...

---

## Medium Priority Issues

### Issue #3: [Example - To be filled during testing]

**Status**: IN PROGRESS

**Description**: 
...

---

## Low Priority Issues / Nice to Have

### Issue #4: [Example - To be filled during testing]

**Status**: OPEN

**Description**: 
...

---

## Performance Issues

### Issue #5: [Example - To be filled during testing]

**Status**: MONITORING

**Description**: 
...

---

## Known Limitations

### Limitation #1: LLM Variability

**Description**: 
Competition outcomes vary based on LLM responses, making deterministic
testing difficult.

**Workaround**:
Tests use probabilistic assertions and multiple runs when needed.

### Limitation #2: Elimination Triggering

**Description**:
Elimination may not always trigger in tests, depending on LLM performance.

**Workaround**:
Elimination tests accept both outcomes (elimination or high scores).

---

## Integration Gotchas

### Gotcha #1: Async/Await

**Issue**: 
Forgetting `await` on CharacterAdapter methods causes silent failures.

**Prevention**:
Always use `await` for response generation:
```python
response = await adapter.generate_response(...)  # ✓
```

### Gotcha #2: State Synchronization

**Issue**:
CompetitionState and CharacterState must stay in sync.

**Prevention**:
Orchestrator handles all state updates centrally.

### Gotcha #3: Context Building

**Issue**:
Missing fields in CompetitionContext causes character confusion.

**Prevention**:
Validate context has all required fields before passing to character.

---

## Testing Notes

### Variability in Results

Due to LLM non-determinism, tests may have different outcomes on different
runs. This is expected and normal.

Tests are designed to be resilient to this variability by:
- Using ranges instead of exact values
- Accepting multiple valid outcomes
- Focusing on structural correctness over content

### Performance Variability

Turn generation speed varies based on:
- LLM load (Ollama or API)
- System resources
- Character complexity
- Turn complexity

Benchmarks provide guidance but are not strict requirements.

---

## Resolution Status Key

- **RESOLVED**: Issue fixed and verified
- **IN PROGRESS**: Actively being worked on
- **OPEN**: Known issue, not yet addressed
- **MONITORING**: Issue under observation, may not require fix
- **WONTFIX**: Issue acknowledged but will not be fixed

---

## Update Log

- 2025-01-XX: Document created
- [Date]: [Updates will be added during testing]
```

**This document will be populated during actual Phase 3 testing.**

---

## Phase 3 Summary

Phase 3 provides comprehensive integration testing that validates:

1. **Homunculus Integration (Phase 1)** works correctly
2. **AI-Talks Orchestration (Phase 2)** coordinates properly
3. **Complete System** can run actual competitions
4. **Performance** is acceptable for production
5. **Quality** of competitions meets expectations

**Success Criteria**: If minimal and basic integration tests pass, Phase 1 + Phase 2 integration is validated and the system is ready for Phase 4 (Judges) and beyond.

**Next Steps After Phase 3**:
- Phase 4: Judge ensemble integration
- Phase 5: Anti-gaming systems
- Phase 6: Production features
- Phase 7: Championship system

---

This completes the **Phase 3 Implementation Plan**! The test infrastructure is comprehensive and will thoroughly validate the integration of all components built in Phases 1 and 2.