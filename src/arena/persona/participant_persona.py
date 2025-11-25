"""
Persona for Participant Agent

This module implements the Persona class specifically for ParticipantAgent.
It handles character response post-processing, state management, and character development
within the confines of multi-person discussions.

Key Features:
- Character response post-processing and enhancement
- Internal state management (mood, relationships, goals)
- Character development and arc progression
- Style adaptation based on character traits
- Integration with character schemas from schemas/characters/

Author: AI Arena Team
"""

import logging
import random
from typing import Optional, Dict, Any, List
from datetime import datetime
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)


@dataclass
class CharacterState:
    """Internal state for character development and consistency"""
    
    # Emotional state
    current_mood: str = "neutral"
    mood_intensity: float = 0.5
    emotional_volatility: float = 0.5
    
    # Goals and motivations
    current_goals: List[str] = field(default_factory=list)
    goal_progress: Dict[str, float] = field(default_factory=dict)
    
    # Social dynamics
    relationships: Dict[str, float] = field(default_factory=dict)  # participant_id -> relationship strength
    trust_levels: Dict[str, float] = field(default_factory=dict)
    
    # Character development
    beliefs_evolution: List[str] = field(default_factory=list)
    arc_stage: str = "introduction"
    growth_areas: List[str] = field(default_factory=list)
    
    # Conversation context
    recent_topics: List[str] = field(default_factory=list)
    engagement_level: float = 0.8
    contribution_count: int = 0
    
    # Character consistency
    last_updated: str = field(default_factory=lambda: datetime.now().isoformat())


class Persona:
    """
    Character persona for ParticipantAgent response post-processing.
    
    This class manages character state, response enhancement, and character development
    for participants in multi-person discussions. It's distinct from the Arena Persona
    system and focused specifically on ParticipantAgent needs.
    """
    
    def __init__(self, character_data: Dict[str, Any]):
        """
        Initialize persona from character dictionary.
        
        Args:
            character_data: Character configuration from schemas/characters/
        """
        self.character_data = character_data
        self.character_name = character_data.get('name', 'Unknown')
        self.character_id = character_data.get('character_id', 'unknown')
        self.archetype = character_data.get('archetype', 'balanced')
        
        # Initialize character state
        self.state = CharacterState()
        self._initialize_from_character_data(character_data)
        
        # Response enhancement settings
        self.enhancement_enabled = True
        self.style_adaptation_enabled = True
        self.relationship_tracking_enabled = True
        
        logger.info(f"Persona initialized for {self.character_name} ({self.archetype})")
    
    def _initialize_from_character_data(self, character_data: Dict[str, Any]) -> None:
        """Initialize internal state from character configuration."""
        
        # Set mood from character baseline
        mood_config = character_data.get('mood_baseline', {})
        self.state.current_mood = mood_config.get('current_state', 'neutral')
        self.state.mood_intensity = mood_config.get('intensity', 0.5)
        self.state.emotional_volatility = mood_config.get('emotional_volatility', 0.5)
        
        # Set initial goals
        self.state.current_goals = character_data.get('initial_goals', [])
        
        # Initialize goal progress tracking
        for goal in self.state.current_goals:
            self.state.goal_progress[goal] = 0.0
        
        # Set development stage
        development = character_data.get('development', {})
        self.state.arc_stage = development.get('arc_stage', 'introduction')
        self.state.growth_areas = development.get('growth_areas', [])
        
        # Set engagement level based on extraversion
        personality = character_data.get('personality', {})
        big_five = personality.get('big_five', {})
        extraversion = big_five.get('extraversion', 0.5)
        self.state.engagement_level = 0.5 + (extraversion * 0.3)  # 0.5-0.8 range
    
    def character_loop(self, response: str, context: Optional[Dict[str, Any]] = None) -> str:
        """
        Main character response post-processing method.
        
        This is the core method that enhances responses with character-specific
        traits, manages internal state, and ensures character consistency.
        
        Args:
            response: Raw response from the agent
            context: Optional context including other participants, recent exchanges, etc.
            
        Returns:
            Enhanced response with character personality applied
        """
        if not self.enhancement_enabled:
            return response
        
        # Update internal state based on context
        self._update_state_from_context(context)
        
        # Enhance response with character traits
        enhanced_response = self._enhance_response_with_personality(response, context)
        
        # Apply character-specific speech patterns
        styled_response = self._apply_character_style(enhanced_response)
        
        # Update state after response generation
        self._update_state_after_response(styled_response, context)
        
        return styled_response
    
    def _update_state_from_context(self, context: Optional[Dict[str, Any]]) -> None:
        """Update internal state based on discussion context."""
        if not context:
            return
        
        # Update relationship tracking
        if self.relationship_tracking_enabled and 'recent_exchanges' in context:
            self._update_relationships(context['recent_exchanges'])
        
        # Update mood based on discussion dynamics
        self._update_mood_from_context(context)
        
        # Track topics and engagement
        if 'current_topic' in context:
            self._track_topic_engagement(context['current_topic'])
        
        # Update goal progress
        self._assess_goal_progress(context)
    
    def _enhance_response_with_personality(self, response: str, context: Optional[Dict[str, Any]]) -> str:
        """Enhance response with character personality traits."""
        
        # Get character personality data
        personality = self.character_data.get('personality', {})
        communication_style = self.character_data.get('communication_style', {})
        specialty = self.character_data.get('specialty', {})
        
        # Apply personality-based modifications
        enhanced = self._apply_personality_traits(response, personality)
        enhanced = self._inject_expertise(enhanced, specialty)
        enhanced = self._add_character_perspective(enhanced, context)
        
        return enhanced
    
    def _apply_personality_traits(self, response: str, personality: Dict[str, Any]) -> str:
        """Apply Big Five personality traits to response."""
        
        big_five = personality.get('big_five', {})
        behavioral_traits = personality.get('behavioral_traits', [])
        quirks = personality.get('quirks', [])
        
        # Apply openness (creativity and intellectual curiosity)
        openness = big_five.get('openness', 0.5)
        if openness > 0.7 and 'what if' not in response.lower():
            if random.random() < 0.3:  # 30% chance for high-openness characters
                response = self._add_creative_element(response)
        
        # Apply conscientiousness (organization and planning)
        conscientiousness = big_five.get('conscientiousness', 0.5)
        if conscientiousness > 0.7:
            response = self._add_structured_approach(response)
        
        # Apply extraversion (social engagement)
        extraversion = big_five.get('extraversion', 0.5)
        if extraversion > 0.7:
            response = self._add_social_warmth(response)
        elif extraversion < 0.3:
            response = self._add_reserved_tone(response)
        
        # Apply behavioral traits
        if 'perfectionism' in [trait.lower() for trait in behavioral_traits]:
            response = self._add_precision_focus(response)
        
        # Apply character quirks
        response = self._apply_character_quirks(response, quirks)
        
        return response
    
    def _inject_expertise(self, response: str, specialty: Dict[str, Any]) -> str:
        """Inject domain expertise into response."""
        
        domain = specialty.get('domain', '')
        expertise_level = specialty.get('expertise_level', 0.5)
        subdomain_knowledge = specialty.get('subdomain_knowledge', [])
        
        # Add domain-specific perspective if expertise is high
        if expertise_level > 0.7 and domain:
            # Add expertise qualifier occasionally
            if random.random() < 0.4:  # 40% chance
                if 'experience' not in response.lower():
                    expertise_phrases = [
                        f"From my experience in {domain},",
                        f"In my work with {domain},",
                        f"What I've learned in {domain} is that",
                    ]
                    chosen_phrase = random.choice(expertise_phrases)
                    response = f"{chosen_phrase} {response.lower()}"
        
        return response
    
    def _add_character_perspective(self, response: str, context: Optional[Dict[str, Any]]) -> str:
        """Add character-specific perspective and backstory elements."""
        
        backstory = self.character_data.get('backstory', '')
        core_values = self.character_data.get('personality', {}).get('core_values', [])
        
        # Occasionally reference personal values (10% chance)
        if core_values and random.random() < 0.1:
            # Find a relevant value to reference
            for value in core_values:
                if any(word in response.lower() for word in value.lower().split()[:3]):
                    response += f" This aligns with my belief that {value.lower()}."
                    break
        
        return response
    
    def _apply_character_style(self, response: str) -> str:
        """Apply character-specific communication style."""
        
        communication_style = self.character_data.get('communication_style', {})
        
        # Get style parameters
        verbal_pattern = communication_style.get('verbal_pattern', 'moderate')
        formality_level = communication_style.get('formality_level', 'moderate')
        humor_style = communication_style.get('humor_style', 'none')
        
        # Apply formality adjustments
        if formality_level == 'formal':
            response = self._increase_formality(response)
        elif formality_level == 'casual':
            response = self._decrease_formality(response)
        
        # Apply verbal pattern
        if verbal_pattern == 'concise':
            response = self._make_more_concise(response)
        elif verbal_pattern == 'elaborate':
            response = self._add_elaboration(response)
        
        return response
    
    def _update_relationships(self, recent_exchanges: List[Dict[str, Any]]) -> None:
        """Update relationship tracking based on recent exchanges."""
        
        for exchange in recent_exchanges[-3:]:  # Look at last 3 exchanges
            speaker = exchange.get('speaker_id', '')
            move_type = exchange.get('move', '')
            
            if speaker and speaker != self.character_id:
                current_relationship = self.state.relationships.get(speaker, 0.0)
                
                # Adjust relationship based on interaction type
                if move_type == 'SUPPORT':
                    self.state.relationships[speaker] = min(1.0, current_relationship + 0.1)
                elif move_type == 'CHALLENGE':
                    self.state.relationships[speaker] = max(-1.0, current_relationship - 0.05)
                elif move_type == 'QUESTION':
                    self.state.relationships[speaker] = min(1.0, current_relationship + 0.05)
    
    def _update_mood_from_context(self, context: Dict[str, Any]) -> None:
        """Update mood based on discussion dynamics."""
        
        # Simple mood updates based on engagement and relationships
        avg_relationship = sum(self.state.relationships.values()) / max(1, len(self.state.relationships))
        
        # Positive relationships improve mood
        if avg_relationship > 0.3:
            self._adjust_mood_toward('positive', 0.1)
        elif avg_relationship < -0.3:
            self._adjust_mood_toward('defensive', 0.1)
        
        # Topic engagement affects mood
        engagement_in_specialty = context.get('topic_relevance_to_expertise', 0.5)
        if engagement_in_specialty > 0.7:
            self._adjust_mood_toward('energized', 0.1)
    
    def _adjust_mood_toward(self, target_mood: str, intensity: float) -> None:
        """Gradually adjust mood toward target."""
        
        # Simple mood transitions
        mood_transitions = {
            'neutral': 0.0,
            'positive': 0.3,
            'energized': 0.6,
            'defensive': -0.3,
            'frustrated': -0.5
        }
        
        current_value = mood_transitions.get(self.state.current_mood, 0.0)
        target_value = mood_transitions.get(target_mood, 0.0)
        
        # Move toward target
        if abs(target_value - current_value) > intensity:
            if target_value > current_value:
                new_value = current_value + intensity
            else:
                new_value = current_value - intensity
            
            # Find closest mood to new value
            closest_mood = min(mood_transitions.keys(), 
                             key=lambda x: abs(mood_transitions[x] - new_value))
            self.state.current_mood = closest_mood
    
    def _track_topic_engagement(self, topic: str) -> None:
        """Track engagement with discussion topics."""
        
        self.state.recent_topics.append(topic)
        
        # Keep only last 5 topics
        if len(self.state.recent_topics) > 5:
            self.state.recent_topics = self.state.recent_topics[-5:]
        
        # Check if topic matches character's interests
        interests = self.character_data.get('demographics', {}).get('interests', [])
        preferred_topics = self.character_data.get('communication_style', {}).get('preferred_topics', [])
        
        topic_interest = any(interest.lower() in topic.lower() 
                           for interest in interests + preferred_topics)
        
        if topic_interest:
            self.state.engagement_level = min(1.0, self.state.engagement_level + 0.1)
        else:
            self.state.engagement_level = max(0.3, self.state.engagement_level - 0.05)
    
    def _assess_goal_progress(self, context: Dict[str, Any]) -> None:
        """Assess progress toward character goals."""
        
        # Simple goal tracking based on participation
        for goal in self.state.current_goals:
            if 'share' in goal.lower() or 'contribute' in goal.lower():
                # Contributing to discussion advances these goals
                current_progress = self.state.goal_progress.get(goal, 0.0)
                self.state.goal_progress[goal] = min(1.0, current_progress + 0.1)
    
    def _update_state_after_response(self, response: str, context: Optional[Dict[str, Any]]) -> None:
        """Update state after generating response."""
        
        self.state.contribution_count += 1
        self.state.last_updated = datetime.now().isoformat()
        
        # Update engagement based on response length and quality
        response_length = len(response.split())
        if response_length > 10:  # Substantial response
            self.state.engagement_level = min(1.0, self.state.engagement_level + 0.05)
    
    # Character style helper methods
    
    def _add_creative_element(self, response: str) -> str:
        """Add creative element for high-openness characters."""
        creative_starters = [
            "What if we considered",
            "An interesting angle might be",
            "I wonder if",
            "Perhaps we could explore"
        ]
        if not any(starter.lower() in response.lower() for starter in creative_starters):
            return f"{random.choice(creative_starters)} {response.lower()}"
        return response
    
    def _add_structured_approach(self, response: str) -> str:
        """Add structured thinking for conscientious characters."""
        structure_words = ["first", "second", "specifically", "systematically", "clearly"]
        if not any(word in response.lower() for word in structure_words):
            return f"To approach this systematically, {response.lower()}"
        return response
    
    def _add_social_warmth(self, response: str) -> str:
        """Add social warmth for extraverted characters."""
        if not response.strip().endswith(('!', '?')):
            return response + "!"
        return response
    
    def _add_reserved_tone(self, response: str) -> str:
        """Add reserved tone for introverted characters."""
        reserved_starters = ["I think", "It seems to me", "Perhaps", "I'd suggest"]
        if not response.startswith(tuple(starter.lower() for starter in reserved_starters)):
            return f"I think {response.lower()}"
        return response
    
    def _add_precision_focus(self, response: str) -> str:
        """Add precision for perfectionist characters."""
        precision_words = ["exactly", "precisely", "specifically", "clearly"]
        if not any(word in response.lower() for word in precision_words):
            return response.replace("is", "is exactly").replace("are", "are precisely")
        return response
    
    def _apply_character_quirks(self, response: str, quirks: List[str]) -> str:
        """Apply character-specific quirks."""
        
        # Look for quirks that suggest speech patterns
        for quirk in quirks:
            if 'experience' in quirk.lower():
                # Add experiential references occasionally
                if random.random() < 0.2:
                    response = f"In my experience, {response.lower()}"
            elif 'direct' in quirk.lower():
                # Make more direct
                response = response.replace("I think maybe", "I believe")
                response = response.replace("perhaps", "definitely")
        
        return response
    
    def _increase_formality(self, response: str) -> str:
        """Increase formality level."""
        formal_replacements = {
            "can't": "cannot",
            "won't": "will not",
            "don't": "do not",
            "isn't": "is not"
        }
        for informal, formal in formal_replacements.items():
            response = response.replace(informal, formal)
        return response
    
    def _decrease_formality(self, response: str) -> str:
        """Decrease formality level."""
        # Already quite informal in base responses
        return response
    
    def _make_more_concise(self, response: str) -> str:
        """Make response more concise."""
        # Remove filler words
        filler_words = ["really", "quite", "very", "actually", "basically"]
        for filler in filler_words:
            response = response.replace(f" {filler} ", " ")
        return response.strip()
    
    def _add_elaboration(self, response: str) -> str:
        """Add elaboration for verbose characters."""
        if not any(phrase in response.lower() for phrase in ["that is to say", "in other words", "specifically"]):
            return f"{response} To elaborate on this point..."
        return response
    
    def get_character_summary(self) -> Dict[str, Any]:
        """Get current character state summary."""
        return {
            'character_name': self.character_name,
            'archetype': self.archetype,
            'current_mood': self.state.current_mood,
            'engagement_level': self.state.engagement_level,
            'contribution_count': self.state.contribution_count,
            'relationships': dict(self.state.relationships),
            'goal_progress': dict(self.state.goal_progress),
            'arc_stage': self.state.arc_stage
        }
    
    def update_relationship(self, participant_id: str, delta: float) -> None:
        """Manually update relationship with another participant."""
        current = self.state.relationships.get(participant_id, 0.0)
        self.state.relationships[participant_id] = max(-1.0, min(1.0, current + delta))
    
    def set_mood(self, mood: str, intensity: float = None) -> None:
        """Manually set character mood."""
        self.state.current_mood = mood
        if intensity is not None:
            self.state.mood_intensity = max(0.0, min(1.0, intensity))