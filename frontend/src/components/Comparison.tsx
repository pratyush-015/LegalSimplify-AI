import React from 'react';
import { SimplificationResult } from '../types';

interface ComparisonProps {
  result: SimplificationResult;
}

const Comparison: React.FC<ComparisonProps> = ({ result }) => {
  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold text-gray-900 text-center">Original vs Simplified</h2>
      
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Original Document */}
        <div className="bg-red-50 border border-red-200 rounded-lg p-6">
          <h3 className="text-lg font-semibold text-red-800 mb-4 flex items-center">
            <span className="mr-2">📜</span>
            Original Document
          </h3>
          <div className="bg-white rounded border p-4 max-h-96 overflow-y-auto">
            <p className="text-sm text-gray-700 whitespace-pre-wrap leading-relaxed">
              {result.originalText}
            </p>
          </div>
          <div className="mt-3 text-xs text-red-600">
            Complex legal language • Difficult to understand
          </div>
        </div>

        {/* Simplified Document */}
        <div className="bg-green-50 border border-green-200 rounded-lg p-6">
          <h3 className="text-lg font-semibold text-green-800 mb-4 flex items-center">
            <span className="mr-2">✨</span>
            Simplified Version
          </h3>
          <div className="bg-white rounded border p-4 max-h-96 overflow-y-auto">
            <p className="text-sm text-gray-700 whitespace-pre-wrap leading-relaxed">
              {result.simplifiedText}
            </p>
          </div>
          <div className="mt-3 text-xs text-green-600">
            Plain English • Easy to understand • {result.complexityReduction}% simpler
          </div>
        </div>
      </div>

      {/* Comparison Stats */}
      <div className="bg-gray-50 rounded-lg p-6">
        <h3 className="text-lg font-semibold text-gray-800 mb-4 text-center">Improvement Metrics</h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="text-center">
            <div className="text-2xl font-bold text-blue-600">{result.complexityReduction}%</div>
            <div className="text-sm text-gray-600">Complexity Reduction</div>
          </div>
          <div className="text-center">
            <div className="text-2xl font-bold text-green-600">{result.processingTime}s</div>
            <div className="text-sm text-gray-600">Processing Time</div>
          </div>
          <div className="text-center">
            <div className="text-2xl font-bold text-purple-600">{Object.keys(result.legalTerms ?? {}).length}</div>
            <div className="text-sm text-gray-600">Terms Explained</div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Comparison;
