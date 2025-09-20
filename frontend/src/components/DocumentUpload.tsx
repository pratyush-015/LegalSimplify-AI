import React, { useState } from 'react';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';
import toast from 'react-hot-toast';
import { SimplificationResult } from '../types';

interface DocumentUploadProps {
  onUploadComplete: (result: SimplificationResult) => void;
}

const DocumentUpload: React.FC<DocumentUploadProps> = ({ onUploadComplete }) => {
  const [loading, setLoading] = useState(false);
  const [progress, setProgress] = useState(0);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    accept: {
      'application/pdf': ['.pdf'],
      'application/vnd.openxmlformats-officedocument.wordprocessingml.document': ['.docx'],
      'text/plain': ['.txt']
    },
    maxSize: 10 * 1024 * 1024, // 10MB
    onDrop: handleFileUpload,
  });

  async function handleFileUpload(files: File[]) {
    if (!files.length) return;
    
    const file = files[0];
    setLoading(true);
    setProgress(0);

    // Simulate progress
    const progressInterval = setInterval(() => {
      setProgress(prev => Math.min(prev + 10, 90));
    }, 200);

    try {
      const formData = new FormData();
      formData.append('file', file);

      const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
      const response = await axios.post(`${API_URL}/api/simplify`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });

      setProgress(100);
      clearInterval(progressInterval);
      
      toast.success('Document processed successfully!');
      onUploadComplete(response.data);
      
    } catch (error) {
      clearInterval(progressInterval);
      toast.error('Failed to process document. Please try again.');
      console.error('Upload error:', error);
    } finally {
      setLoading(false);
      setProgress(0);
    }
  }

  const handleSampleDocument = async () => {
    setLoading(true);
    try {
      const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
      const response = await axios.post(`${API_URL}/api/sample-documents/rental`);
      toast.success('Sample document loaded!');
      onUploadComplete(response.data);
    } catch (error) {
      toast.error('Failed to load sample document');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="text-center">
      <div
        {...getRootProps()}
        className={`border-2 border-dashed rounded-lg p-12 transition-colors cursor-pointer ${
          isDragActive
            ? 'border-blue-400 bg-blue-50'
            : 'border-gray-300 hover:border-blue-400'
        }`}
      >
        <input {...getInputProps()} />
        
        {loading ? (
          <div className="space-y-4">
            <div className="animate-spin rounded-full h-12 w-12 border-4 border-blue-600 border-t-transparent mx-auto"></div>
            <p className="text-lg font-medium text-gray-700">Processing document...</p>
            {progress > 0 && (
              <div className="w-full bg-gray-200 rounded-full h-2 max-w-md mx-auto">
                <div
                  className="bg-blue-600 h-2 rounded-full transition-all duration-300"
                  style={{ width: `${progress}%` }}
                ></div>
              </div>
            )}
          </div>
        ) : (
          <div className="space-y-4">
            <div className="text-6xl text-gray-400">📄</div>
            <div>
              <p className="text-xl font-medium text-gray-700 mb-2">
                {isDragActive ? 'Drop your document here' : 'Drag & drop your legal document'}
              </p>
              <p className="text-gray-500 mb-4">
                or click to browse (PDF, DOCX, TXT - max 10MB)
              </p>
              <button
                type="button"
                className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg font-medium transition-colors"
              >
                Choose File
              </button>
            </div>
          </div>
        )}
      </div>

      <div className="mt-8">
        <p className="text-gray-600 mb-4">Or try a sample document:</p>
        <button
          onClick={handleSampleDocument}
          disabled={loading}
          className="bg-gray-100 hover:bg-gray-200 text-gray-700 px-4 py-2 rounded-lg transition-colors disabled:opacity-50"
        >
          Load Rental Agreement Sample
        </button>
      </div>
    </div>
  );
};

export default DocumentUpload;
