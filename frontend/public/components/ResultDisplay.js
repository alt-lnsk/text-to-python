// ResultDisplay.js
import React from 'react';

function ResultDisplay({ result }) {
  if (!result) return null;

  return (
    <div className="result-display">
      <h2>Résultat</h2>
      {typeof result === 'string' && result.startsWith('data:image') ? (
        <img src={result} alt="Generated plot" />
      ) : (
        <pre>{JSON.stringify(result, null, 2)}</pre>
      )}
    </div>
  );
}

export default ResultDisplay;
