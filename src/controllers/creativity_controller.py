import logging
import math
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
from collections import deque

from src.utils.originality_assessor import OriginalityAssessor, AssessmentResult

logger = logging.getLogger(__name__)


@dataclass 
class CreativityConfig:
    """Configuration for dynamic creativity adjustment"""
    enabled: bool = True
    base_temperature: float = 0.85
    creativity_range: Tuple[float, float] = (0.7, 1.2)
    progression_curve: str = "linear"
    assessment_window: int = 3
    originality_threshold: float = 0.6
    quality_threshold: float = 0.7
    early_creativity_boost: float = 0.15
    early_turns: int = 6
    late_quality_focus: float = 0.1
    max_temperature_adjustment: float = 0.2
    max_top_p_adjustment: float = 0.1
    max_frequency_penalty_adjustment: float = 0.3
    
    @classmethod
    def from_config(cls, config_dict: Dict) -> 'CreativityConfig':
        """Create from configuration dictionary"""
        return cls(
            enabled=config_dict.get('enabled', True),
            base_temperature=config_dict.get('base_temperature', 0.85),
            creativity_range=tuple(config_dict.get('creativity_range', [0.7, 1.2])),
            progression_curve=config_dict.get('progression_curve', 'linear'),
            assessment_window=config_dict.get('assessment_window', 3),
            originality_threshold=config_dict.get('originality_threshold', 0.6),
            quality_threshold=config_dict.get('quality_threshold', 0.7),
            early_creativity_boost=config_dict.get('early_creativity_boost', 0.15),
            early_turns=config_dict.get('early_turns', 6),
            late_quality_focus=config_dict.get('late_quality_focus', 0.1),
            max_temperature_adjustment=config_dict.get('adjustments', {}).get('temperature', 0.2),
            max_top_p_adjustment=config_dict.get('adjustments', {}).get('top_p', 0.1),
            max_frequency_penalty_adjustment=config_dict.get('adjustments', {}).get('frequency_penalty', 0.3)
        )


@dataclass
class ParticipantHistory:
    """Track assessment history for a participant"""
    assessments: deque  # Recent AssessmentResult objects
    responses: deque    # Recent responses for comparison
    current_temperature: float
    current_top_p: float
    current_frequency_penalty: float
    
    def __init__(self, window_size: int = 3, base_temp: float = 0.85):
        self.assessments = deque(maxlen=window_size)
        self.responses = deque(maxlen=window_size * 2)  # Keep more for comparison
        self.current_temperature = base_temp
        self.current_top_p = 0.9  # Default
        self.current_frequency_penalty = 0.0  # Default


@dataclass
class AdjustmentRecommendation:
    """Recommendation for parameter adjustments"""
    temperature: float
    top_p: Optional[float] = None
    frequency_penalty: Optional[float] = None
    explanation: str = ""
    confidence: float = 0.5


class DynamicCreativityController:
    """
    Controls dynamic adjustment of LLM creativity parameters based on 
    real-time assessment of response originality and quality
    """
    
    def __init__(self, config: CreativityConfig):
        self.config = config
        self.assessor = OriginalityAssessor()
        self.participant_histories: Dict[str, ParticipantHistory] = {}
        self.turn_number = 0
        self.max_turns = 100  # Will be updated by orchestrator
        
        logger.info(f"🎨 Dynamic creativity controller initialized (enabled: {config.enabled})")
    
    def set_max_turns(self, max_turns: int):
        """Set the maximum number of turns for progression calculation"""
        self.max_turns = max_turns
    
    def assess_response(
        self, 
        participant_id: str, 
        response: str,
        turn_number: int
    ) -> AssessmentResult:
        """
        Assess a participant's response and update their history
        
        Args:
            participant_id: ID of the participant
            response: The response to assess
            turn_number: Current turn number
            
        Returns:
            AssessmentResult with originality and quality scores
        """
        
        # Initialize participant history if needed
        if participant_id not in self.participant_histories:
            self.participant_histories[participant_id] = ParticipantHistory(
                window_size=self.config.assessment_window,
                base_temp=self.config.base_temperature
            )
        
        history = self.participant_histories[participant_id]
        
        # Get recent responses for comparison (excluding current participant's to avoid self-comparison)
        recent_responses = []
        for pid, h in self.participant_histories.items():
            if pid != participant_id:  # Exclude self
                recent_responses.extend(list(h.responses))
        
        # Assess the response
        assessment = self.assessor.assess_response(
            response=response,
            recent_responses=recent_responses,
            turn_number=turn_number,
            max_turns=self.max_turns
        )
        
        # Update history
        history.assessments.append(assessment)
        history.responses.append(response)
        
        logger.debug(f"📊 {participant_id} assessment: O={assessment.originality_score:.2f}, Q={assessment.quality_score:.2f}")
        
        return assessment
    
    def recommend_parameters(
        self, 
        participant_id: str,
        turn_number: int
    ) -> AdjustmentRecommendation:
        """
        Recommend LLM parameters for the next response
        
        Args:
            participant_id: ID of the participant
            turn_number: Current turn number
            
        Returns:
            AdjustmentRecommendation with suggested parameters
        """
        
        if not self.config.enabled:
            return AdjustmentRecommendation(
                temperature=self.config.base_temperature,
                explanation="Dynamic creativity adjustment disabled"
            )
        
        # Initialize if needed
        if participant_id not in self.participant_histories:
            self.participant_histories[participant_id] = ParticipantHistory(
                window_size=self.config.assessment_window,
                base_temp=self.config.base_temperature
            )
        
        history = self.participant_histories[participant_id]
        
        # Calculate base temperature with progression
        base_temp = self._calculate_progression_temperature(turn_number)
        
        # Apply assessment-based adjustments if we have history
        if history.assessments:
            temp_adjustment = self._calculate_assessment_adjustment(history)
            adjusted_temp = base_temp + temp_adjustment
        else:
            adjusted_temp = base_temp
            temp_adjustment = 0.0
        
        # Apply bounds
        min_temp, max_temp = self.config.creativity_range
        final_temp = max(min_temp, min(max_temp, adjusted_temp))
        
        # Calculate other parameters
        top_p = self._calculate_top_p(history, final_temp)
        freq_penalty = self._calculate_frequency_penalty(history)
        
        # Update history
        history.current_temperature = final_temp
        history.current_top_p = top_p
        history.current_frequency_penalty = freq_penalty
        
        # Generate explanation
        explanation = self._generate_explanation(
            base_temp, temp_adjustment, final_temp, turn_number, history
        )
        
        # Log parameter decision with details
        logger.info(f"🎨 {participant_id} parameter adjustment: {explanation}")
        if abs(temp_adjustment) > 0.05:
            logger.info(f"   📊 Significant adjustment: {temp_adjustment:+.2f} (base: {base_temp:.2f} → final: {final_temp:.2f})")
        
        return AdjustmentRecommendation(
            temperature=final_temp,
            top_p=top_p,
            frequency_penalty=freq_penalty,
            explanation=explanation,
            confidence=0.8 if history.assessments else 0.3
        )
    
    def _calculate_progression_temperature(self, turn_number: int) -> float:
        """Calculate temperature based on discussion progression"""
        
        progress = turn_number / self.max_turns if self.max_turns > 0 else 0.0
        progress = min(1.0, progress)
        
        base_temp = self.config.base_temperature
        
        # Early creativity boost
        if turn_number < self.config.early_turns:
            early_boost = self.config.early_creativity_boost * (1.0 - turn_number / self.config.early_turns)
            base_temp += early_boost
        
        # Late quality focus
        elif progress > 0.66:  # Final third
            late_reduction = self.config.late_quality_focus * ((progress - 0.66) / 0.34)
            base_temp -= late_reduction
        
        # Apply progression curve
        if self.config.progression_curve == "exponential":
            # Exponential decay from creativity to quality
            creativity_factor = math.exp(-3.0 * progress)
            base_temp = (base_temp * creativity_factor + 
                        self.config.base_temperature * (1.0 - creativity_factor))
        
        elif self.config.progression_curve == "sigmoid":
            # Sigmoid transition around midpoint
            sigmoid_progress = 1.0 / (1.0 + math.exp(-10.0 * (progress - 0.5)))
            creativity_reduction = sigmoid_progress * 0.1
            base_temp -= creativity_reduction
        
        # Linear is default (handled by early/late adjustments above)
        
        return base_temp
    
    def _calculate_assessment_adjustment(self, history: ParticipantHistory) -> float:
        """Calculate temperature adjustment based on recent assessments"""
        
        if not history.assessments:
            return 0.0
        
        recent_assessment = history.assessments[-1]
        
        # Average recent assessments for stability
        if len(history.assessments) >= 2:
            recent_orig = sum(a.originality_score for a in list(history.assessments)[-2:]) / 2
            recent_qual = sum(a.quality_score for a in list(history.assessments)[-2:]) / 2
        else:
            recent_orig = recent_assessment.originality_score
            recent_qual = recent_assessment.quality_score
        
        adjustment = 0.0
        
        # Boost creativity if originality is low
        if recent_orig < self.config.originality_threshold:
            originality_deficit = self.config.originality_threshold - recent_orig
            creativity_boost = originality_deficit * self.config.max_temperature_adjustment
            adjustment += creativity_boost
            logger.debug(f"   🔥 Creativity boost: +{creativity_boost:.2f} (originality {recent_orig:.2f} < {self.config.originality_threshold})")
        
        # Reduce creativity if quality is high (focus mode)
        if recent_qual > self.config.quality_threshold:
            quality_excess = recent_qual - self.config.quality_threshold
            quality_focus = quality_excess * self.config.max_temperature_adjustment * 0.5
            adjustment -= quality_focus
            logger.debug(f"   🎯 Quality focus: -{quality_focus:.2f} (quality {recent_qual:.2f} > {self.config.quality_threshold})")
        
        # Bound the adjustment
        max_adj = self.config.max_temperature_adjustment
        return max(-max_adj, min(max_adj, adjustment))
    
    def _calculate_top_p(self, history: ParticipantHistory, temperature: float) -> float:
        """Calculate top_p parameter based on temperature and assessment"""
        
        # Base top_p
        base_top_p = 0.9
        
        # Adjust based on temperature (higher temp -> slightly lower top_p for diversity)
        temp_adjustment = (temperature - self.config.base_temperature) * -0.1
        
        # Adjust based on recent semantic similarity (high similarity -> lower top_p)
        if history.assessments:
            recent_similarity = history.assessments[-1].semantic_similarity
            similarity_adjustment = recent_similarity * -0.1
        else:
            similarity_adjustment = 0.0
        
        final_top_p = base_top_p + temp_adjustment + similarity_adjustment
        
        return max(0.5, min(1.0, final_top_p))
    
    def _calculate_frequency_penalty(self, history: ParticipantHistory) -> float:
        """Calculate frequency penalty based on vocabulary diversity"""
        
        base_penalty = 0.0
        
        if history.assessments:
            # Higher penalty if vocabulary diversity is low
            recent_diversity = history.assessments[-1].vocabulary_diversity
            if recent_diversity < 0.5:
                diversity_deficit = 0.5 - recent_diversity
                base_penalty = diversity_deficit * self.config.max_frequency_penalty_adjustment
        
        return max(0.0, min(2.0, base_penalty))  # OpenAI/Ollama bounds
    
    def _generate_explanation(
        self, 
        base_temp: float, 
        adjustment: float, 
        final_temp: float,
        turn_number: int,
        history: ParticipantHistory
    ) -> str:
        """Generate human-readable explanation of parameter choices"""
        
        parts = []
        
        # Base reasoning
        if turn_number < self.config.early_turns:
            parts.append("Early creativity boost")
        elif turn_number / self.max_turns > 0.66:
            parts.append("Late quality focus")
        else:
            parts.append("Standard progression")
        
        # Assessment-based adjustments
        if adjustment > 0.05:
            parts.append("boosted for originality")
        elif adjustment < -0.05:
            parts.append("reduced for quality focus")
        
        # Recent assessment info
        if history.assessments:
            recent = history.assessments[-1]
            if recent.originality_score < 0.4:
                parts.append("low originality detected")
            elif recent.quality_score > 0.8:
                parts.append("high quality maintained")
        
        explanation = f"T={final_temp:.2f} ({', '.join(parts)})"
        
        return explanation
    
    def get_status_report(self) -> Dict[str, Any]:
        """Get status report for monitoring/debugging"""
        
        report = {
            "enabled": self.config.enabled,
            "turn_number": self.turn_number,
            "participants": {}
        }
        
        for pid, history in self.participant_histories.items():
            participant_data = {
                "current_temperature": history.current_temperature,
                "assessment_count": len(history.assessments),
                "recent_assessments": []
            }
            
            # Add recent assessment summaries
            for assessment in list(history.assessments)[-2:]:
                participant_data["recent_assessments"].append({
                    "originality": assessment.originality_score,
                    "quality": assessment.quality_score,
                    "explanation": assessment.explanation
                })
            
            report["participants"][pid] = participant_data
        
        return report
    
    def reset_participant(self, participant_id: str):
        """Reset history for a participant"""
        if participant_id in self.participant_histories:
            del self.participant_histories[participant_id]
            logger.debug(f"🔄 Reset creativity history for {participant_id}")
    
    def clear_all_histories(self):
        """Clear all participant histories"""
        self.participant_histories.clear()
        self.turn_number = 0
        logger.debug("🔄 Cleared all creativity histories")