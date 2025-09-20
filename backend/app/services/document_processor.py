"""
Document processing service for extracting text from various file formats
"""

import fitz  # pymupdf
from docx import Document
import io
from typing import Optional
from fastapi import UploadFile

class DocumentProcessor:
    """Service for processing uploaded documents"""
    
    def __init__(self):
        self.supported_formats = ["pdf", "docx", "txt"]
    
    async def extract_text(self, file: UploadFile, file_type: str) -> str:
        """Extract text content from uploaded file"""
        try:
            content = await file.read()
            
            if file_type == "pdf":
                return self._extract_pdf_text(content)
            elif file_type == "docx":
                return self._extract_docx_text(content)
            elif file_type == "txt":
                return content.decode('utf-8')
            else:
                raise ValueError(f"Unsupported file type: {file_type}")
                
        except Exception as e:
            raise Exception(f"Failed to extract text from {file.filename}: {str(e)}")
    
    def _extract_pdf_text(self, content: bytes) -> str:
        """Extract text from PDF content"""
        text = ""
        try:
            pdf_doc = fitz.open(stream=content, filetype="pdf")
            
            for page_num in range(pdf_doc.page_count):
                page = pdf_doc[page_num]
                text += page.get_text()
                text += "\n"
            
            pdf_doc.close()
            return text.strip()
            
        except Exception as e:
            raise Exception(f"PDF extraction failed: {str(e)}")
    
    def _extract_docx_text(self, content: bytes) -> str:
        """Extract text from DOCX content"""
        try:
            doc = Document(io.BytesIO(content))
            text = ""
            
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            
            return text.strip()
            
        except Exception as e:
            raise Exception(f"DOCX extraction failed: {str(e)}")