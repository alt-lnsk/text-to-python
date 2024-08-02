// Explanation.js
import React from 'react';

function Explanation({ explanation }) {
  if (!explanation) return null;

  return (
    <div className="explanation">
      <h2>Explication du code</h2>
      <p>{explanation}</p>
    </div>
  );
}

export default Explanation;
