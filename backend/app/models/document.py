"""
Pydantic models for document processing
"""

from pydantic import BaseModel
from datetime import datetime
from typing import List, Dict, Optional

class DocumentModel(BaseModel):
    """Model for uploaded documents"""
    filename: str
    file_type: str
    original_text: str
    upload_time: datetime
    
class SimplificationResponse(BaseModel):
    """Response model for document simplification"""
    document_id: str
    original_text: str
    simplified_text: str
    summary: str
    key_insights: List[str]
    risk_score: int
    risk_factors: List[str]
    legal_terms: Dict[str, str]
    complexity_reduction: int
    processing_time: float
    document_type: str

class RiskAnalysis(BaseModel):
    """Model for risk analysis results"""
    overall_score: int
    risk_factors: List[str]
    recommendations: List[str]