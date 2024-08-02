// App.js
import React, { useState } from 'react';
import FileUpload from './FileUpload';
import CodeEditor from './CodeEditor';
import ResultDisplay from './ResultDisplay';
import Explanation from './Explanation';

function App() {
  const [data, setData] = useState(null);
  const [code, setCode] = useState('');
  const [result, setResult] = useState(null);
  const [explanation, setExplanation] = useState('');

  const handleFileUpload = (uploadedData) => {
    setData(uploadedData);
  };

  const handleCodeGeneration = async (intent) => {
    try {
      const response = await fetch('http://127.0.0.1:5000/generate_code', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ intent, data }),
      });
      const result = await response.json();
      setCode(result.code);
      setResult(result.result);
      setExplanation(result.explanation);
    } catch (error) {
      console.error('Error generating code:', error);
    }
  };

  return (
    <div className="app">
      <h1>Python Data Visualization Learning Tool</h1>
      <FileUpload onUpload={handleFileUpload} />
      {data && (
        <>
          <CodeEditor
            code={code}
            onCodeChange={setCode}
            onGenerateCode={handleCodeGeneration}
          />
          <ResultDisplay result={result} />
          <Explanation explanation={explanation} />
        </>
      )}
    </div>
  );
}

export default App;
