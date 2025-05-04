import React, { useState } from 'react';

function App() {
  const [status, setStatus] = useState('');
  const [audioUrl, setAudioUrl] = useState(null);

  const handleUpload = async (event) => {
    event.preventDefault();
    setStatus('Processing... this may take a minute.');
    setAudioUrl(null);

    const formData = new FormData();
    formData.append('file', event.target.file.files[0]);

    try {
      const response = await fetch('/generate-podcast', {
        method: 'POST',
        body: formData
      });

      if (!response.ok) {
        throw new Error('Upload failed');
      }

      const blob = await response.blob();
      const url = URL.createObjectURL(blob);
      setAudioUrl(url);
      setStatus('✅ Podcast generated!');
    } catch (error) {
      setStatus('❌ Error generating podcast.');
      console.error(error);
    }
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h1>📚 Book to Podcast</h1>
      <form onSubmit={handleUpload}>
        <input type="file" name="file" accept=".pdf" required />
        <br /><br />
        <button type="submit">Generate Podcast</button>
      </form>

      <p>{status}</p>

      {audioUrl && (
        <audio controls src={audioUrl} style={{ marginTop: '1rem' }} />
      )}
    </div>
  );
}

export default App;