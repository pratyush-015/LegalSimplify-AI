"""
Risk analysis service for legal documents
"""

import re
from typing import Dict, List
import asyncio

class RiskAnalyzer:
    """Service for analyzing risks in legal documents"""
    
    def __init__(self):
        self.risk_patterns = {
            "vague_terms": [
                r"reasonable\s+time",
                r"as\s+soon\s+as\s+possible",
                r"best\s+efforts"
            ],
            "unfavorable_clauses": [
                r"non-compete", 
                r"exclusive\s+dealing",
                r"penalty\s+clause"
            ]
        }
    
    async def analyze_risks(self, text: str) -> Dict:
        """Analyze document for potential risks"""
        await asyncio.sleep(0.3)  # Simulate processing
        
        risk_score = 0
        risk_factors = []
        
        # Check for vague terms
        vague_count = self._count_patterns(text, self.risk_patterns["vague_terms"])
        if vague_count > 0:
            risk_score += vague_count * 10
            risk_factors.append(f"Contains {vague_count} vague term(s)")
        
        # Check for unfavorable clauses
        unfavorable_count = self._count_patterns(text, self.risk_patterns["unfavorable_clauses"])
        if unfavorable_count > 0:
            risk_score += unfavorable_count * 15
            risk_factors.append(f"Contains {unfavorable_count} potentially unfavorable clause(s)")
        
        # Document length risk
        word_count = len(text.split())
        if word_count < 100:
            risk_score += 20
            risk_factors.append("Document is very short - may be missing details")
        
        final_score = min(100, risk_score)
        
        return {
            "overall_score": final_score,
            "risk_factors": risk_factors
        }
    
    def _count_patterns(self, text: str, patterns: List[str]) -> int:
        """Count occurrences of risk patterns in text"""
        count = 0
        for pattern in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            count += len(matches)
        return count