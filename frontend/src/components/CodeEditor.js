import React, { useState } from 'react';

function CodeEditor({ code, onCodeChange, onGenerateCode }) {
  const [intent, setIntent] = useState('');

  const handleIntentChange = (event) => {
    setIntent(event.target.value);
  };

  const handleGenerateCode = () => {
    onGenerateCode(intent);
  };

  return (
    <div className="code-editor">
      <textarea
        value={intent}
        onChange={handleIntentChange}
        placeholder="Décrivez ce que vous voulez faire avec vos données..."
      />
      <button onClick={handleGenerateCode}>Générer le code</button>
      <pre>
        <code>{code}</code>
      </pre>
    </div>
  );
}

export default CodeEditor;