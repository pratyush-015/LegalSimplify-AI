export interface Document {
  id: string;
  filename: string;
  fileType: string;
  uploadTime: Date;
  status: 'uploading' | 'processing' | 'completed' | 'error';
}

export interface SimplificationResult {
  documentId: string;
  originalText: string;
  simplifiedText: string;
  summary: string;
  keyInsights: string[];
  riskScore: number;
  riskFactors: string[];
  legalTerms: Record<string, string>;
  complexityReduction: number;
  processingTime: number;
  documentType: string;
}

export interface RiskAnalysis {
  overallScore: number;
  riskFactors: string[];
  recommendations: string[];
}

export interface LegalTerm {
  term: string;
  definition: string;
  category?: string;
}

export interface ProcessingStep {
  step: number;
  title: string;
  description: string;
  completed: boolean;
}

export interface APIResponse<T> {
  success: boolean;
  data: T;
  error?: string;
  message?: string;
}