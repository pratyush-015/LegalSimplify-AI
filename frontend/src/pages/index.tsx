import React, { useState } from 'react';
import Layout from '../components/Layout';
import DocumentUpload from '../components/DocumentUpload';
import DocumentViewer from '../components/DocumentViewer';
import SimplifiedOutput from '../components/SimplifiedOutput';
import Comparison from '../components/Comparison';
import KeyInsights from '../components/KeyInsights';
import { SimplificationResult } from '../types';

const HomePage: React.FC = () => {
  const [result, setResult] = useState<SimplificationResult | null>(null);
  const [activeTab, setActiveTab] = useState<'upload' | 'results' | 'comparison'>('upload');

  const handleUploadComplete = (data: SimplificationResult) => {
    setResult(data);
    setActiveTab('results');
  };

  return (
    <Layout>
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
        <div className="max-w-7xl mx-auto px-4 py-8">
          {/* Header */}
          <div className="text-center mb-12">
            <h1 className="text-4xl md:text-6xl font-bold text-gray-900 mb-4">
              Legal<span className="text-blue-600">Simplify</span> AI
            </h1>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              Transform complex legal documents into clear, accessible guidance with AI-powered simplification
            </p>
          </div>

          {/* Navigation Tabs */}
          <div className="flex justify-center mb-8">
            <div className="bg-white rounded-lg p-1 shadow-sm">
              <button
                onClick={() => setActiveTab('upload')}
                className={`px-6 py-2 rounded-md text-sm font-medium transition-colors ${
                  activeTab === 'upload'
                    ? 'bg-blue-600 text-white'
                    : 'text-gray-500 hover:text-gray-700'
                }`}
              >
                Upload Document
              </button>
              <button
                onClick={() => setActiveTab('results')}
                disabled={!result}
                className={`px-6 py-2 rounded-md text-sm font-medium transition-colors ${
                  activeTab === 'results'
                    ? 'bg-blue-600 text-white'
                    : 'text-gray-500 hover:text-gray-700 disabled:text-gray-300'
                }`}
              >
                Results
              </button>
              <button
                onClick={() => setActiveTab('comparison')}
                disabled={!result}
                className={`px-6 py-2 rounded-md text-sm font-medium transition-colors ${
                  activeTab === 'comparison'
                    ? 'bg-blue-600 text-white'
                    : 'text-gray-500 hover:text-gray-700 disabled:text-gray-300'
                }`}
              >
                Comparison
              </button>
            </div>
          </div>

          {/* Content */}
          <div className="bg-white rounded-xl shadow-lg p-8">
            {activeTab === 'upload' && (
              <DocumentUpload onUploadComplete={handleUploadComplete} />
            )}
            
            {activeTab === 'results' && result && (
              <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                <div className="lg:col-span-2">
                  <SimplifiedOutput result={result} />
                </div>
                <div>
                  <KeyInsights result={result} />
                </div>
              </div>
            )}
            
            {activeTab === 'comparison' && result && (
              <Comparison result={result} />
            )}
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default HomePage;
