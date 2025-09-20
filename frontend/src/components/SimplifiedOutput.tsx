import React from 'react';
import { SimplificationResult } from '../types';

interface SimplifiedOutputProps {
  result: SimplificationResult;
}

const SimplifiedOutput: React.FC<SimplifiedOutputProps> = ({ result }) => {
  // Safety: default to empty object if legalTerms is null or undefined
  const legalTerms = result.legalTerms ?? {};

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-gray-900">Simplified Document</h2>
        <span className="bg-green-100 text-green-800 px-3 py-1 rounded-full text-sm font-medium">
          {result.complexityReduction}% Complexity Reduction
        </span>
      </div>

      <div className="bg-gray-50 rounded-lg p-6">
        <h3 className="text-lg font-semibold text-gray-800 mb-3">Summary</h3>
        <p className="text-gray-700 leading-relaxed">{result.summary}</p>
      </div>

      <div className="bg-gray-50 rounded-lg p-6">
        <h3 className="text-lg font-semibold text-gray-800 mb-3">Simplified Text</h3>
        <div className="prose max-w-none">
          <p className="text-gray-700 leading-relaxed whitespace-pre-wrap">
            {result.simplifiedText}
          </p>
        </div>
      </div>

      <div className="bg-blue-50 rounded-lg p-6">
        <h3 className="text-lg font-semibold text-blue-800 mb-3">Legal Terms Explained</h3>
        <div className="space-y-3">
          {Object.entries(legalTerms).map(([term, definition]) => (
            <div key={term} className="border-l-4 border-blue-400 pl-4">
              <span className="font-semibold text-blue-900 capitalize">{term}:</span>
              <span className="text-blue-700 ml-2">{definition}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default SimplifiedOutput;
