import React from 'react';

interface DocumentViewerProps {
  content: string;
  title: string;
}

const DocumentViewer: React.FC<DocumentViewerProps> = ({ content, title }) => {
  return (
    <div className="bg-white border rounded-lg p-6">
      <h3 className="text-lg font-semibold text-gray-800 mb-4">{title}</h3>
      <div className="bg-gray-50 rounded p-4 max-h-96 overflow-y-auto">
        <pre className="whitespace-pre-wrap text-sm text-gray-700 font-sans">
          {content}
        </pre>
      </div>
    </div>
  );
};

export default DocumentViewer;
