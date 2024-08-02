// FileUploads.js
import React, { useState } from 'react';

function FileUpload({ onUpload }) {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://127.0.0.1:5000/upload', {
        method: 'POST',
        body: formData,
      });
      const result = await response.json();
      onUpload(result.columns);
    } catch (error) {
      console.error('Error uploading file:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="file-upload">
      <input type="file" onChange={handleFileChange} accept=".xlsx" />
      <button type="submit">Télécharger le fichier Excel</button>
    </form>
  );
}

export default FileUpload;
