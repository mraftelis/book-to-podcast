import React, { useState } from 'react';

function App() {
  const [status, setStatus] = useState('');
  const [audioUrl, setAudioUrl] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleUpload = async (event) => {
    event.preventDefault();
    setIsLoading(true);
    setStatus('');
    setAudioUrl(null);

    const formData = new FormData();
    formData.append('file', event.target.file.files[0]);

    try {
      const response = await fetch('/generate-podcast', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) throw new Error('Upload failed');

      const blob = await response.blob();
      const url = URL.createObjectURL(blob);
      setAudioUrl(url);
      setStatus('✅ Podcast generated!');
    } catch (err) {
      setStatus('❌ Error generating podcast.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-100 to-white flex items-center justify-center px-4">
      <div className="w-full max-w-xl bg-white shadow-xl rounded-2xl p-8 space-y-6 border border-slate-200">
      <h1 className="text-3xl font-bold text-center text-indigo-700 flex items-center justify-center gap-3">
      <h1 className="text-3xl font-bold text-center text-indigo-700 flex items-center justify-center gap-3">
  <img
    src="https://cdn-icons-png.flaticon.com/512/724/724715.png"
    alt="Podcast logo"
    className="w-10 h-10"
  />
  Book to Podcast
</h1>

      </h1>

        <p className="text-center text-gray-500 text-sm">Upload a PDF, get a podcast-ready MP3 summary</p>

        <form onSubmit={handleUpload} className="space-y-4">
          <label className="block">
            <input
              type="file"
              name="file"
              accept=".pdf"
              required
              className="block w-full text-sm text-gray-700
                         file:mr-4 file:py-2 file:px-4
                         file:rounded-full file:border-0
                         file:text-sm file:font-semibold
                         file:bg-indigo-50 file:text-indigo-700
                         hover:file:bg-indigo-100"
            />
          </label>
          <button
            type="submit"
            disabled={isLoading}
          className="px-6 py-2 bg-indigo-600 text-white rounded-md hover:bg-indigo-700 transition mx-auto block"
          >
         {isLoading ? 'Generating...' : 'Generate Podcast'}
          </button>
        </form>

        {status && (
          <p
            className={`text-center font-medium ${
              status.includes('✅') ? 'text-green-600' : 'text-red-500'
            }`}
          >
            {status}
          </p>
        )}

        {audioUrl && (
          <div className="pt-4">
            <audio controls src={audioUrl} className="w-full rounded-lg" />
          </div>
        )}
      </div>
    </div>
  );
}

export default App;