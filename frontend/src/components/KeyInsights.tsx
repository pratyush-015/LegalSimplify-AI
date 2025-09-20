import React from 'react';
import { SimplificationResult } from '../types';

interface KeyInsightsProps {
  result: SimplificationResult;
}

const KeyInsights: React.FC<KeyInsightsProps> = ({ result }) => {
  const getRiskColor = (score: number) => {
    if (score >= 70) return 'text-red-600 bg-red-100';
    if (score >= 40) return 'text-yellow-600 bg-yellow-100';
    return 'text-green-600 bg-green-100';
  };
  const riskFactors = result.riskFactors ?? [];

  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold text-gray-900">Key Insights</h2>

      {/* Risk Score */}
      <div className="bg-white border rounded-lg p-6">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-lg font-semibold text-gray-800">Risk Assessment</h3>
          <span className={`px-3 py-1 rounded-full text-sm font-medium ${getRiskColor(result.riskScore)}`}>
            {result.riskScore}/100
          </span>
        </div>
        <div className="w-full bg-gray-200 rounded-full h-3 mb-4">
          <div
            className={`h-3 rounded-full ${
              result.riskScore >= 70 ? 'bg-red-500' : 
              result.riskScore >= 40 ? 'bg-yellow-500' : 'bg-green-500'
            }`}
            style={{ width: `${result.riskScore}%` }}
          ></div>
        </div>
        <div className="space-y-2">
          {riskFactors.map((factor, index) => (
            <p key={index} className="text-sm text-gray-600 flex items-start">
              <span className="text-red-500 mr-2">⚠️</span>
              {factor}
            </p>
          ))}
        </div>
      </div>

      {/* Key Insights */}
      <div className="bg-white border rounded-lg p-6">
        <h3 className="text-lg font-semibold text-gray-800 mb-4">Key Points</h3>
        <div className="space-y-3">
          {(result.keyInsights ?? []).map((insight, index) => (
            <div key={index} className="flex items-start">
              <span className="text-blue-500 mr-2">💡</span>
              <p className="text-sm text-gray-700">{insight}</p>
            </div>
          ))}
        </div>
      </div>

      {/* Document Info */}
      <div className="bg-white border rounded-lg p-6">
        <h3 className="text-lg font-semibold text-gray-800 mb-4">Document Information</h3>
        <div className="space-y-3">
          <div className="flex justify-between">
            <span className="text-gray-600">Type:</span>
            <span className="font-medium text-gray-900">{result.documentType}</span>
          </div>
          <div className="flex justify-between">
            <span className="text-gray-600">Processing Time:</span>
            <span className="font-medium text-gray-900">{result.processingTime}s</span>
          </div>
          <div className="flex justify-between">
            <span className="text-gray-600">Complexity Reduced:</span>
            <span className="font-medium text-green-600">{result.complexityReduction}%</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default KeyInsights;
