import logging
import re
import statistics
from typing import List, Dict, Tuple, Optional
from collections import Counter
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class AssessmentResult:
    """Results of originality and quality assessment"""
    originality_score: float  # 0-1, higher = more original
    quality_score: float      # 0-1, higher = better quality
    vocabulary_diversity: float
    semantic_similarity: float
    argument_complexity: float
    novel_concepts: int
    explanation: str


class OriginalityAssessor:
    """Assesses originality and quality of responses for dynamic creativity adjustment"""
    
    def __init__(self):
        self.model = None
        self._initialized = False
        self.vocab_cache = {}  # Cache for vocabulary analysis
        
    def _initialize_model(self):
        """Lazy initialization of sentence transformer model"""
        if self._initialized:
            return
        
        try:
            from sentence_transformers import SentenceTransformer
            import numpy as np
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
            self.np = np
            self._initialized = True
            logger.debug("Sentence transformer model initialized for originality assessment")
        except ImportError:
            logger.warning("sentence-transformers not available, using fallback assessment")
            self._initialized = True
        except Exception as e:
            logger.error(f"Failed to initialize sentence transformer for assessment: {e}")
            self._initialized = True
    
    def assess_response(
        self, 
        response: str, 
        recent_responses: List[str],
        turn_number: int,
        max_turns: int
    ) -> AssessmentResult:
        """
        Assess originality and quality of a response
        
        Args:
            response: The response to assess
            recent_responses: List of recent responses for comparison
            turn_number: Current turn number
            max_turns: Maximum turns in discussion
            
        Returns:
            AssessmentResult with scores and explanation
        """
        
        if not response.strip():
            return AssessmentResult(0.0, 0.0, 0.0, 1.0, 0.0, 0, "Empty response")
        
        # Calculate individual metrics
        vocab_diversity = self._calculate_vocabulary_diversity(response, recent_responses)
        semantic_similarity = self._calculate_semantic_similarity(response, recent_responses)
        argument_complexity = self._calculate_argument_complexity(response)
        novel_concepts = self._count_novel_concepts(response, recent_responses)
        
        # Calculate originality score (inverse of similarity + diversity + novelty)
        originality_score = self._compute_originality_score(
            vocab_diversity, semantic_similarity, novel_concepts
        )
        
        # Calculate quality score (complexity + coherence)
        quality_score = self._compute_quality_score(
            argument_complexity, response
        )
        
        # Generate explanation
        explanation = self._generate_explanation(
            originality_score, quality_score, vocab_diversity, 
            semantic_similarity, argument_complexity, novel_concepts
        )
        
        return AssessmentResult(
            originality_score=originality_score,
            quality_score=quality_score,
            vocabulary_diversity=vocab_diversity,
            semantic_similarity=semantic_similarity,
            argument_complexity=argument_complexity,
            novel_concepts=novel_concepts,
            explanation=explanation
        )
    
    def _calculate_vocabulary_diversity(self, response: str, recent_responses: List[str]) -> float:
        """Calculate vocabulary diversity compared to recent responses"""
        
        # Extract words from response
        response_words = set(self._extract_meaningful_words(response))
        
        if not response_words:
            return 0.0
        
        # Extract words from recent responses
        recent_words = set()
        for recent in recent_responses:
            recent_words.update(self._extract_meaningful_words(recent))
        
        if not recent_words:
            return 1.0  # First response is inherently diverse
        
        # Calculate unique word ratio
        unique_words = response_words - recent_words
        diversity_ratio = len(unique_words) / len(response_words)
        
        return min(1.0, diversity_ratio * 1.5)  # Boost score slightly
    
    def _calculate_semantic_similarity(self, response: str, recent_responses: List[str]) -> float:
        """Calculate semantic similarity to recent responses"""
        
        if not recent_responses:
            return 0.0
        
        self._initialize_model()
        
        if self.model is None:
            return self._fallback_semantic_similarity(response, recent_responses)
        
        try:
            embeddings = self.model.encode([response] + recent_responses)
            response_emb = embeddings[0]
            recent_embs = embeddings[1:]
            
            similarities = self.np.dot(recent_embs, response_emb) / (
                self.np.linalg.norm(recent_embs, axis=1) * self.np.linalg.norm(response_emb)
            )
            
            return float(self.np.max(similarities))
        except Exception as e:
            logger.error(f"Error in semantic similarity calculation: {e}")
            return self._fallback_semantic_similarity(response, recent_responses)
    
    def _calculate_argument_complexity(self, response: str) -> float:
        """Calculate complexity of arguments in response"""
        
        complexity_indicators = [
            # Logical connectors
            r'\b(however|nevertheless|furthermore|moreover|consequently|therefore|thus|hence)\b',
            # Conditional reasoning
            r'\b(if|unless|provided that|given that|assuming|suppose)\b',
            # Causal relationships
            r'\b(because|since|due to|as a result|leads to|causes|results in)\b',
            # Comparative reasoning
            r'\b(whereas|while|compared to|in contrast|similarly|likewise)\b',
            # Qualification/nuance
            r'\b(arguably|potentially|presumably|conceivably|ostensibly)\b',
            # Abstract concepts
            r'\b(concept|principle|framework|paradigm|perspective|dimension)\b'
        ]
        
        response_lower = response.lower()
        complexity_score = 0.0
        
        for pattern in complexity_indicators:
            matches = len(re.findall(pattern, response_lower))
            complexity_score += matches * 0.1
        
        # Length-normalized complexity
        word_count = len(response.split())
        if word_count > 0:
            complexity_score = complexity_score / (word_count / 50)  # Normalize per ~50 words
        
        return min(1.0, complexity_score)
    
    def _count_novel_concepts(self, response: str, recent_responses: List[str]) -> int:
        """Count novel philosophical concepts introduced"""
        
        # Philosophical concept patterns
        concept_patterns = [
            r'\b(nature of|essence of|meaning of|concept of|idea of)\s+\w+',
            r'\b(epistemological|ontological|metaphysical|ethical|aesthetic)\b',
            r'\b(consciousness|existence|reality|truth|knowledge|belief|justice|freedom)\b',
            r'\b(determinism|free will|causation|necessity|possibility)\b'
        ]
        
        response_concepts = set()
        for pattern in concept_patterns:
            matches = re.findall(pattern, response.lower())
            response_concepts.update(matches)
        
        # Find concepts in recent responses
        recent_concepts = set()
        for recent in recent_responses:
            for pattern in concept_patterns:
                matches = re.findall(pattern, recent.lower())
                recent_concepts.update(matches)
        
        # Count novel concepts
        novel_concepts = response_concepts - recent_concepts
        return len(novel_concepts)
    
    def _compute_originality_score(
        self, 
        vocab_diversity: float, 
        semantic_similarity: float, 
        novel_concepts: int
    ) -> float:
        """Compute overall originality score"""
        
        # Originality is inverse of similarity + diversity + novelty
        similarity_penalty = semantic_similarity
        diversity_bonus = vocab_diversity * 0.6
        novelty_bonus = min(0.4, novel_concepts * 0.1)
        
        originality = (1.0 - similarity_penalty) * 0.5 + diversity_bonus + novelty_bonus
        
        return max(0.0, min(1.0, originality))
    
    def _compute_quality_score(self, argument_complexity: float, response: str) -> float:
        """Compute overall quality score"""
        
        # Quality factors
        complexity_score = argument_complexity * 0.4
        
        # Length appropriateness (not too short, not too verbose)
        word_count = len(response.split())
        length_score = 0.0
        if 20 <= word_count <= 100:
            length_score = 0.3
        elif 10 <= word_count <= 150:
            length_score = 0.2
        elif word_count >= 5:
            length_score = 0.1
        
        # Coherence indicators (simple heuristics)
        coherence_score = 0.0
        if self._has_clear_structure(response):
            coherence_score = 0.3
        
        quality = complexity_score + length_score + coherence_score
        
        return max(0.0, min(1.0, quality))
    
    def _has_clear_structure(self, response: str) -> bool:
        """Check if response has clear argumentative structure"""
        
        structure_indicators = [
            r'\b(first|second|third|finally|in conclusion)\b',
            r'\b(on one hand|on the other hand|in contrast|however)\b',
            r'^[A-Z][^.!?]*[.!?]\s+[A-Z]',  # Multiple sentences
        ]
        
        response_lower = response.lower()
        for pattern in structure_indicators:
            if re.search(pattern, response_lower):
                return True
        
        return False
    
    def _extract_meaningful_words(self, text: str) -> List[str]:
        """Extract meaningful words, excluding common stop words"""
        
        stop_words = {
            'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from',
            'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the',
            'to', 'was', 'were', 'will', 'with', 'would', 'i', 'you', 'we',
            'they', 'this', 'these', 'those', 'have', 'had', 'can', 'could',
            'should', 'would', 'may', 'might'
        }
        
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        meaningful_words = [w for w in words if w not in stop_words and len(w) > 2]
        
        return meaningful_words
    
    def _fallback_semantic_similarity(self, response: str, recent_responses: List[str]) -> float:
        """Fallback semantic similarity using word overlap"""
        
        response_words = set(self._extract_meaningful_words(response))
        
        if not response_words:
            return 0.0
        
        max_similarity = 0.0
        for recent in recent_responses:
            recent_words = set(self._extract_meaningful_words(recent))
            
            if not recent_words:
                continue
            
            overlap = len(response_words & recent_words)
            union = len(response_words | recent_words)
            
            if union > 0:
                jaccard_sim = overlap / union
                max_similarity = max(max_similarity, jaccard_sim)
        
        return max_similarity
    
    def _generate_explanation(
        self, 
        originality: float, 
        quality: float,
        vocab_diversity: float,
        semantic_similarity: float,
        argument_complexity: float,
        novel_concepts: int
    ) -> str:
        """Generate human-readable explanation of assessment"""
        
        parts = []
        
        # Originality
        if originality >= 0.7:
            parts.append("High originality")
        elif originality >= 0.4:
            parts.append("Moderate originality")
        else:
            parts.append("Low originality")
        
        # Quality
        if quality >= 0.7:
            parts.append("high quality")
        elif quality >= 0.4:
            parts.append("moderate quality")
        else:
            parts.append("needs improvement in quality")
        
        # Details
        details = []
        if vocab_diversity >= 0.6:
            details.append("diverse vocabulary")
        if semantic_similarity >= 0.7:
            details.append("similar to recent responses")
        if argument_complexity >= 0.5:
            details.append("complex argumentation")
        if novel_concepts > 0:
            details.append(f"{novel_concepts} novel concepts")
        
        result = f"{parts[0]}, {parts[1]}"
        if details:
            result += f" ({', '.join(details)})"
        
        return result