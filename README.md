## Deployment Instructions

### Quick Start
1. Clone the repository
2. Copy `.env.example` to `.env` and add your API keys
3. Run `docker-compose up --build`
4. Access the application at `http://localhost:3000`

### Manual Development Setup

#### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Key Features

✅ **Frontend Web Application**: Modern React/Next.js interface with animations
✅ **Backend API**: FastAPI with comprehensive endpoints
✅ **AI Integration**: Google Gemini for document simplification
✅ **Document Processing**: Support for PDF, DOCX, TXT files
✅ **Risk Analysis**: Automated risk detection and scoring
✅ **TypeScript Support**: Full type safety across the application
✅ **Docker Configuration**: Easy deployment with containers
✅ **Responsive Design**: Works on all devices
✅ **Real-time Processing**: Live updates during document analysis

## Architecture Highlights

- **Microservices**: Separate frontend, backend, and AI services
- **REST API**: Clean API design with OpenAPI documentation
- **Asynchronous Processing**: Non-blocking document processing
- **Error Handling**: Comprehensive error handling and validation
- **Security**: CORS configuration and file validation
- **Scalability**: Docker-based deployment for easy scaling
- **Monitoring**: Health checks and logging throughout the system