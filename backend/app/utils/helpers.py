"""
Utility functions for the backend
"""

from fastapi import UploadFile
import os

def get_file_type(filename: str) -> str:
    """Get file type from filename"""
    if not filename:
        return ""
    
    extension = filename.split('.')[-1].lower()
    return extension

def validate_file_size(file: UploadFile, max_size_mb: int = 10) -> bool:
    """Validate file size"""
    if hasattr(file, 'size'):
        return file.size <= max_size_mb * 1024 * 1024
    return True  # Cannot determine size, assume valid

def create_document_id(filename: str) -> str:
    """Create unique document ID"""
    import time
    timestamp = int(time.time())
    clean_name = filename.replace(' ', '_').replace('.', '_')
    return f"doc_{clean_name}_{timestamp}"