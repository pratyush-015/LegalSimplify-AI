# """
# LegalSimplify AI - FastAPI Backend
# Main application entry point
# """

# from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import JSONResponse
# import os
# from typing import List, Optional
# import asyncio
# from datetime import datetime

# # Import our services
# from app.services.document_processor import DocumentProcessor
# from app.services.ai_simplifier import AISimplifier
# from app.services.risk_analyzer import RiskAnalyzer
# from app.models.document import DocumentModel, SimplificationResponse
# from app.utils.helpers import get_file_type, validate_file_size

# # Initialize FastAPI app
# app = FastAPI(
#     title="LegalSimplify AI",
#     description="AI-powered legal document simplification API",
#     version="1.0.0",
#     docs_url="/api/docs",
#     redoc_url="/api/redoc"
# )

# # Configure CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Configure appropriately for production
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Initialize services
# document_processor = DocumentProcessor()
# ai_simplifier = AISimplifier()
# risk_analyzer = RiskAnalyzer()

# @app.on_event("startup")
# async def startup_event():
#     """Initialize services on startup"""
#     print("🚀 LegalSimplify AI Backend Starting...")
#     await ai_simplifier.initialize()
#     print("✅ AI Services initialized")

# @app.get("/")
# async def root():
#     """Health check endpoint"""
#     return {"message": "LegalSimplify AI Backend is running", "status": "healthy"}

# @app.get("/api/health")
# async def health_check():
#     """Detailed health check"""
#     return {
#         "status": "healthy",
#         "timestamp": datetime.now().isoformat(),
#         "services": {
#             "document_processor": "active",
#             "ai_simplifier": "active",
#             "risk_analyzer": "active"
#         }
#     }

# @app.post("/api/simplify", response_model=SimplificationResponse)
# async def simplify_document(file: UploadFile = File(...)):
#     """
#     Main endpoint to simplify a legal document
#     """
#     try:
#         # Validate file
#         if not validate_file_size(file):
#             raise HTTPException(status_code=413, detail="File too large (max 10MB)")
        
#         file_type = get_file_type(file.filename)
#         if file_type not in ["pdf", "docx", "txt"]:
#             raise HTTPException(status_code=400, detail="Unsupported file type")
        
#         # Process document
#         print(f"📄 Processing {file.filename} ({file_type})")
        
#         # Extract text from document
#         document_content = await document_processor.extract_text(file, file_type)
        
#         # Create document model
#         document = DocumentModel(
#             filename=file.filename,
#             file_type=file_type,
#             original_text=document_content,
#             upload_time=datetime.now()
#         )
        
#         # Simplify document using AI
#         print("🤖 Starting AI simplification...")
#         simplified_result = await ai_simplifier.simplify_text(document_content)
        
#         # Analyze risks
#         print("⚠️ Analyzing document risks...")
#         risk_analysis = await risk_analyzer.analyze_risks(document_content)
        
#         # Extract key insights
#         print("🔍 Extracting key insights...")
#         key_insights = await ai_simplifier.extract_key_insights(document_content)
        
#         # Calculate complexity score
#         complexity_score = ai_simplifier.calculate_complexity_score(document_content)
        
#         # Create response
#         response = SimplificationResponse(
#             document_id=f"doc_{int(datetime.now().timestamp())}",
#             original_text=document_content,
#             simplified_text=simplified_result["simplified_text"],
#             summary=simplified_result["summary"],
#             key_insights=key_insights,
#             risk_score=risk_analysis["overall_score"],
#             risk_factors=risk_analysis["risk_factors"],
#             legal_terms=simplified_result.get("legal_terms", {}),
#             complexity_reduction=max(0, complexity_score - 30),  # Show improvement
#             processing_time=2.5,  # Simulated processing time
#             document_type=ai_simplifier.classify_document(document_content)
#         )
        
#         print(f"✅ Document processing complete for {file.filename}")
#         return response
        
#     except Exception as e:
#         print(f"❌ Error processing document: {str(e)}")
#         raise HTTPException(status_code=500, detail=f"Document processing failed: {str(e)}")

# @app.get("/api/sample-documents")
# async def get_sample_documents():
#     """Get available sample documents for testing"""
#     return {
#         "samples": [
#             {
#                 "id": "rental_agreement",
#                 "name": "Rental Agreement",
#                 "type": "Contract",
#                 "description": "Standard residential rental agreement with common clauses"
#             },
#             {
#                 "id": "employment_contract",
#                 "name": "Employment Contract", 
#                 "type": "Employment",
#                 "description": "Employment agreement with non-compete and confidentiality clauses"
#             },
#             {
#                 "id": "nda",
#                 "name": "Non-Disclosure Agreement",
#                 "type": "Legal Agreement", 
#                 "description": "Mutual NDA with standard confidentiality terms"
#             }
#         ]
#     }

# @app.post("/api/sample-documents/{document_id}")
# async def process_sample_document(document_id: str):
#     """Process a sample document"""
#     sample_responses = {
#         "rental_agreement": {
#             "document_id": "sample_rental_001",
#             "original_text": "WHEREAS, the Landlord is desirous of leasing the hereinafter described premises to Tenant, and Tenant is desirous of leasing the same from Landlord for the term, at the rental, and upon the conditions hereinafter set forth; NOW THEREFORE, in consideration of the mutual covenants and agreements contained herein, and for other good and valuable consideration, the receipt and sufficiency of which are hereby acknowledged, the parties agree as follows: PREMISES. Landlord hereby leases to Tenant and Tenant hereby leases from Landlord the premises situated in the County of [County], State of [State], described as follows: [Property Description] (the 'Premises'). The Premises shall be used and occupied by Tenant exclusively as a residential dwelling and for no other purpose without the prior written consent of Landlord.",
#             "simplified_text": "The landlord wants to rent out their property to you (the tenant). You want to rent this property from them. Here are the key details:\\n\\n• Property Location: [Property Description]\\n• Use: You can only use this as your home - no business activities allowed without written permission\\n• This agreement is legally binding for both parties\\n\\nBoth parties agree to follow all the rules and conditions listed in this contract.",
#             "summary": "This is a residential rental agreement where the landlord rents property to a tenant for home use only. Both parties must follow the contract terms.",
#             "key_insights": [
#                 "This is a residential-only lease - no business use allowed",
#                 "You need written permission for any non-residential activities", 
#                 "The contract is legally binding once signed",
#                 "Property details need to be filled in before signing"
#             ],
#             "risk_score": 65,
#             "risk_factors": [
#                 "Vague property description could lead to disputes",
#                 "No business use clause may be restrictive",
#                 "Missing specific terms and conditions"
#             ],
#             "legal_terms": {
#                 "whereas": "A legal term meaning 'considering that' or 'given that' - used to provide background information",
#                 "hereinafter": "From this point forward in the document",
#                 "premises": "The property or building being discussed",
#                 "consideration": "Something of value exchanged between parties (money, services, etc.)"
#             },
#             "complexity_reduction": 75,
#             "processing_time": 1.8,
#             "document_type": "Rental Agreement"
#         }
#     }
    
#     if document_id not in sample_responses:
#         raise HTTPException(status_code=404, detail="Sample document not found")
    
#     # Add a small delay to simulate processing
#     await asyncio.sleep(1.5)
    
#     return sample_responses[document_id]

# @app.get("/api/legal-terms")
# async def get_legal_terms():
#     """Get common legal terms and their definitions"""
#     return {
#         "terms": {
#             "whereas": "A legal term meaning 'considering that' or 'given that' - used to provide background information",
#             "hereinafter": "From this point forward in the document", 
#             "premises": "The property or building being discussed",
#             "consideration": "Something of value exchanged between parties (money, services, etc.)",
#             "pecuniary": "Related to money or financial matters",
#             "covenant": "A formal agreement or promise in a contract",
#             "indemnify": "To compensate someone for harm or loss",
#             "jurisdiction": "The authority of a court to hear and decide cases",
#             "liability": "Legal responsibility for damages or debts",
#             "waiver": "The voluntary giving up of a right or claim"
#         }
#     }

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)


from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from datetime import datetime
import asyncio

from app.services.document_processor import DocumentProcessor
from app.services.ai_simplifier import AISimplifier  
from app.services.risk_analyzer import RiskAnalyzer
from app.models.document import SimplificationResponse
from app.utils.helpers import get_file_type, validate_file_size

app = FastAPI(title="LegalSimplify AI", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"],
)

document_processor = DocumentProcessor()
ai_simplifier = AISimplifier()
risk_analyzer = RiskAnalyzer()

@app.on_event("startup")
async def startup_event():
    await ai_simplifier.initialize()

@app.get("/")
async def root():
    return {"message": "LegalSimplify AI Backend", "status": "healthy"}

@app.post("/api/simplify", response_model=SimplificationResponse)
async def simplify_document(file: UploadFile = File(...)):
    try:
        if not validate_file_size(file):
            raise HTTPException(status_code=413, detail="File too large (max 10MB)")
        
        file_type = get_file_type(file.filename)
        if file_type not in ["pdf", "docx", "txt"]:
            raise HTTPException(status_code=400, detail="Unsupported file type")
        
        document_content = await document_processor.extract_text(file, file_type)
        simplified_result = await ai_simplifier.simplify_text(document_content)
        risk_analysis = await risk_analyzer.analyze_risks(document_content)
        key_insights = await ai_simplifier.extract_key_insights(document_content)
        complexity_score = ai_simplifier.calculate_complexity_score(document_content)
        
        return SimplificationResponse(
            document_id=f"doc_{int(datetime.now().timestamp())}",
            original_text=document_content,
            simplified_text=simplified_result["simplified_text"],
            summary=simplified_result["summary"],
            key_insights=key_insights,
            risk_score=risk_analysis["overall_score"],
            risk_factors=risk_analysis["risk_factors"],
            legal_terms=simplified_result.get("legal_terms", {}),
            complexity_reduction=max(0, complexity_score - 30),
            processing_time=2.5,
            document_type=ai_simplifier.classify_document(document_content)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")

@app.post("/api/sample-documents/{document_id}")
async def process_sample_document(document_id: str):
    sample_data = {
        "rental": {
            "document_id": "sample_rental_001", 
            "original_text": "WHEREAS, the Landlord is desirous of leasing the hereinafter described premises to Tenant...",
            "simplified_text": "The landlord wants to rent out their property to you (the tenant).",
            "summary": "This is a residential rental agreement.",
            "key_insights": ["This is a residential-only lease", "No business use allowed"],
            "risk_score": 65,
            "risk_factors": ["Vague property description could lead to disputes"],
            "legal_terms": {"whereas": "A legal term meaning 'considering that'"},
            "complexity_reduction": 75,
            "processing_time": 1.8,
            "document_type": "Rental Agreement"
        }
    }
    
    if document_id not in sample_data:
        raise HTTPException(status_code=404, detail="Sample document not found")
    
    await asyncio.sleep(1.5)
    return sample_data[document_id]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
