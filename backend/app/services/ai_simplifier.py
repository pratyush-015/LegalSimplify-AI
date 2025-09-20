"""
AI-powered document simplification service
"""

import os
import re
from typing import Dict, List
import asyncio

class AISimplifier:
    """Service for AI-powered document simplification"""
    
    def __init__(self):
        self.legal_terms_db = {
            "whereas": "A legal term meaning 'considering that'",
            "hereinafter": "From this point forward in the document", 
            "premises": "The property or building being discussed",
            "consideration": "Something of value exchanged between parties",
            "covenant": "A formal agreement or promise in a contract",
            "indemnify": "To compensate someone for harm or loss",
            "jurisdiction": "The authority of a court to hear cases",
            "liability": "Legal responsibility for damages or debts"
        }
    
    async def initialize(self):
        """Initialize the AI service"""
        print("✅ AI Simplifier initialized")
    
    async def simplify_text(self, text: str) -> Dict:
        """Simplify legal document text"""
        # Simulate AI processing delay
        await asyncio.sleep(0.5)
        
        # Simple rule-based simplification for demo
        simplified = text
        
        replacements = {
            "whereas": "considering that",
            "hereinafter": "from now on",
            "heretofore": "up until now", 
            "thereof": "of it",
            "whereby": "by which",
            "forthwith": "immediately"
        }
        
        for legal_term, simple_term in replacements.items():
            simplified = re.sub(legal_term, simple_term, simplified, flags=re.IGNORECASE)
        
        # Create summary
        words = simplified.split()
        summary = " ".join(words[:50]) + "..." if len(words) > 50 else simplified
        
        return {
            "simplified_text": simplified,
            "summary": summary,
            "legal_terms": {k: v for k, v in self.legal_terms_db.items() 
                           if k.lower() in text.lower()}
        }
    
    async def extract_key_insights(self, text: str) -> List[str]:
        """Extract key insights from legal document"""
        insights = []
        
        if "rental" in text.lower() or "lease" in text.lower():
            insights.extend([
                "This appears to be a rental or lease agreement",
                "Check the terms for rent amount and due dates",
                "Review any restrictions on property use"
            ])
        
        if "employment" in text.lower():
            insights.extend([
                "This is an employment-related document",
                "Review compensation and benefits carefully", 
                "Check for non-compete or confidentiality clauses"
            ])
        
        return insights[:5]
    
    def calculate_complexity_score(self, text: str) -> int:
        """Calculate document complexity score (0-100)"""
        score = 50
        
        word_count = len(text.split())
        if word_count > 1000:
            score += 20
        elif word_count > 500:
            score += 10
        
        legal_terms = ["whereas", "hereinafter", "notwithstanding"]
        jargon_count = sum(1 for term in legal_terms if term in text.lower())
        score += jargon_count * 5
        
        return min(100, max(0, score))
    
    def classify_document(self, text: str) -> str:
        """Classify the type of legal document"""
        text_lower = text.lower()
        
        if any(term in text_lower for term in ["lease", "rental", "tenant"]):
            return "Rental Agreement"
        elif any(term in text_lower for term in ["employment", "employee"]):
            return "Employment Contract"
        elif any(term in text_lower for term in ["confidential", "nda"]):
            return "Non-Disclosure Agreement"
        else:
            return "Legal Document"