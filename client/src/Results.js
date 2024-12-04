import React, { useState } from 'react';
import './Results.css';

function Results() {
  const [title, setTitle] = useState('');
  const [genre, setGenre] = useState('');
  const [results, setResults] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    const response = await fetch('/get_user_input', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ title, genre }),
    });
    const data = await response.json();
    setResults(`DFS Connections: ${data.dfs.join(', ')}\nBFS Connections: ${data.bfs.join(', ')}`);
  };

  return (
    <div className="results-container">
      <div className="results-content">
        <div className="left-half">
          <div className="results-header">
            Enter Book Title and Genre
          </div>
          <form onSubmit={handleSubmit}>
            <label htmlFor="title">Title:</label>
            <input
              type="text"
              id="title"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
            /><br /><br />
            <label htmlFor="genre">Genre:</label>
            <input
              type="text"
              id="genre"
              value={genre}
              onChange={(e) => setGenre(e.target.value)}
            /><br /><br />
            <input type="submit" value="Submit" />
          </form>
        </div>
        <div className="right-half">
          <textarea
            className="results-textbox"
            value={results}
            readOnly
          />
        </div>
      </div>
    </div>
  );
}

export default Results;