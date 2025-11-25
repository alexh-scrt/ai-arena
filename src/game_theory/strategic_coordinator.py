# src/game_theory/strategic_coordinator.py

import logging
from typing import Dict, List, Optional
from src.states.participant_state import ParticipantState
from src.states.group_state import GroupDiscussionState
from src.game_theory import DialogueMove
from src.game_theory.agent_objective import AgentObjective
from src.utils.originality_assessor import OriginalityAssessor

logger = logging.getLogger(__name__)


class StrategicCoordinator:
    """
    Meta-level evaluator that scores strategic alignment and quality.
    
    This coordinator evaluates each turn to determine:
    1. How well the move aligns with the agent's objectives
    2. How original/novel the contribution is
    3. Overall strategic quality of the turn
    
    Maintains history of all evaluations for aggregate analytics.
    """
    
    def __init__(self):
        self.turn_scores: List[Dict] = []
        self.originality_assessor = OriginalityAssessor()
        logger.info("Initialized Strategic Coordinator with unified originality assessment")

    async def evaluate_turn(
        self,
        agent: ParticipantState,
        move: DialogueMove,
        response: str,
        group_state: GroupDiscussionState
    ) -> Dict:
        """
        Evaluate the strategic quality of a turn.
        
        Args:
            agent: The participant who spoke
            move: The dialogue move executed
            response: The actual response text
            group_state: Current discussion state
        
        Returns:
            Dictionary with scoring metrics
        """
        
        # Analyze response features
        context = self._analyze_response(response, move, group_state)
        
        # Compute objective alignment
        alignment = agent.objective.score_move(move, context)
        
        # Compute originality using unified assessor
        originality = await self._compute_originality(response, group_state)
        
        # Compute strategic quality (weighted combination)
        strategic_quality = (alignment * 0.6) + (originality * 0.4)
        
        # Create evaluation record
        evaluation = {
            "agent": agent.name,
            "turn": group_state.turn_number,
            "move": move.move_type,
            "dominant_objective": agent.objective.get_dominant_objective(),
            "alignment_score": round(alignment, 3),
            "originality_score": round(originality, 3),
            "strategic_quality": round(strategic_quality, 3),
            "context_features": context
        }
        
        self.turn_scores.append(evaluation)
        
        logger.info(
            f"📊 Strategic evaluation for {agent.name}: "
            f"alignment={alignment:.2f}, "
            f"originality={originality:.2f} (unified), "
            f"quality={strategic_quality:.2f}"
        )
        
        return evaluation

    def _analyze_response(
        self,
        response: str,
        move: DialogueMove,
        group_state: GroupDiscussionState
    ) -> Dict:
        """
        Analyze response for strategic features.
        
        Returns dictionary of boolean/numeric features used in scoring.
        """
        response_lower = response.lower()
        
        # Detect metaphorical language
        metaphor_indicators = [
            'like', 'as if', 'imagine', 'picture', 'metaphor',
            'analogy', 'similar to', 'reminds me of', 'think of it as'
        ]
        uses_metaphor = any(indicator in response_lower for indicator in metaphor_indicators)
        
        # Detect evidence citation (even after style transfer, some markers remain)
        evidence_indicators = [
            'evidence', 'data', 'research', 'study', 'experiment',
            'observation', 'finding', 'result', 'measurement', 'empirical'
        ]
        cites_evidence = any(indicator in response_lower for indicator in evidence_indicators)
        
        # Detect logical structure
        logical_indicators = [
            'therefore', 'thus', 'consequently', 'it follows',
            'because', 'since', 'given that', 'implies', 'if', 'then'
        ]
        logical_structure = any(indicator in response_lower for indicator in logical_indicators)
        
        # Detect ethical considerations
        ethical_indicators = [
            'ought', 'should', 'right', 'wrong', 'moral',
            'ethical', 'justice', 'fairness', 'duty', 'virtue', 'good'
        ]
        ethical_consideration = any(indicator in response_lower for indicator in ethical_indicators)
        
        # Detect assumption challenges
        challenge_indicators = [
            'assume', 'assumption', 'presuppose', 'take for granted',
            'question whether', 'skeptical that', 'doubt'
        ]
        challenges_assumption = any(indicator in response_lower for indicator in challenge_indicators)
        
        # Detect consensus building
        consensus_indicators = [
            'we can agree', 'common ground', 'both', 'together',
            'shared', 'unify', 'reconcile', 'integrate', 'synthesis'
        ]
        builds_consensus = any(indicator in response_lower for indicator in consensus_indicators)
        
        # Check if tools were used (would need to be passed from agent if tracked)
        uses_tool_results = False  # Placeholder - enhance if tool metadata available
        
        return {
            "uses_metaphor": uses_metaphor,
            "cites_evidence": cites_evidence,
            "logical_structure": logical_structure,
            "ethical_consideration": ethical_consideration,
            "challenges_assumption": challenges_assumption,
            "builds_consensus": builds_consensus,
            "uses_tool_results": uses_tool_results,
            "response_length": len(response.split()),
            "addresses_target": move.target is not None
        }

    async def _compute_originality(
        self,
        response: str,
        group_state: GroupDiscussionState
    ) -> float:
        """
        Compute originality score using the unified OriginalityAssessor.
        
        This ensures consistency with the dynamic creativity adjustment system.
        
        Args:
            response: Current response text
            group_state: Discussion state with exchange history
        
        Returns:
            Originality score (0.0 to 1.0)
        """
        # Extract recent responses for comparison
        recent_responses = []
        if group_state.exchanges:
            # Get content from recent exchanges (excluding current turn)
            recent_responses = [
                exchange['content'] for exchange in group_state.exchanges[-5:]
                if exchange.get('content')
            ]
        
        # Use the unified originality assessor
        assessment_result = self.originality_assessor.assess_response(
            response=response,
            recent_responses=recent_responses,
            turn_number=group_state.turn_number,
            max_turns=100  # Default max turns for strategic assessment
        )
        
        return assessment_result.originality_score

    def get_aggregate_metrics(self) -> Dict:
        """
        Get aggregate strategic metrics for the entire discussion.
        
        Returns:
            Dictionary with summary statistics
        """
        if not self.turn_scores:
            return {}
        
        alignment_scores = [s['alignment_score'] for s in self.turn_scores]
        originality_scores = [s['originality_score'] for s in self.turn_scores]
        quality_scores = [s['strategic_quality'] for s in self.turn_scores]
        
        # Count objective pursuits
        objective_counts = {}
        for score in self.turn_scores:
            obj = score['dominant_objective']
            objective_counts[obj] = objective_counts.get(obj, 0) + 1
        
        dominant_theme = max(objective_counts.items(), key=lambda x: x[1])[0] if objective_counts else "none"
        
        return {
            "total_turns_evaluated": len(self.turn_scores),
            "avg_alignment": round(sum(alignment_scores) / len(alignment_scores), 3),
            "avg_originality": round(sum(originality_scores) / len(originality_scores), 3),
            "avg_quality": round(sum(quality_scores) / len(quality_scores), 3),
            "dominant_theme": dominant_theme,
            "objective_distribution": objective_counts
        }

    def get_participant_metrics(self, participant_id: str) -> Optional[Dict]:
        """
        Get metrics for a specific participant.
        
        Args:
            participant_id: ID or name of the participant
        
        Returns:
            Dictionary with participant-specific metrics, or None if not found
        """
        participant_scores = [s for s in self.turn_scores if s['agent'] == participant_id]
        
        if not participant_scores:
            return None
        
        alignment_scores = [s['alignment_score'] for s in participant_scores]
        originality_scores = [s['originality_score'] for s in participant_scores]
        quality_scores = [s['strategic_quality'] for s in participant_scores]
        
        return {
            "participant": participant_id,
            "turns": len(participant_scores),
            "avg_alignment": round(sum(alignment_scores) / len(alignment_scores), 3),
            "avg_originality": round(sum(originality_scores) / len(originality_scores), 3),
            "avg_quality": round(sum(quality_scores) / len(quality_scores), 3),
            "dominant_objective": participant_scores[0]['dominant_objective']
        }