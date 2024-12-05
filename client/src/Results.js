import React from 'react';
import { useLocation } from 'react-router-dom';
import './Results.css';

function Results() {
  const location = useLocation();
  const { data } = location.state || {};

  if (!data) {
    return <div>No data received. Please go back and try again.</div>;
  }

  const { title, genre, dfs_connections, bfs_connections } = data;

  return (
    <div className="results-container">
      <h1>Search Results</h1>
      <div className="book-info">
        <p><strong>Title:</strong> {title}</p>
        <p><strong>Genre:</strong> {genre}</p>
      </div>
      <div className="connections">
        <h2>DFS Connections</h2>
        {dfs_connections && dfs_connections.length > 0 ? (
          <ul>
            {dfs_connections.map((connection, index) => (
              <li key={index}>{connection}</li>
            ))}
          </ul>
        ) : (
          <p>No DFS connections found.</p>
        )}
        <h2>BFS Connections</h2>
        {bfs_connections && bfs_connections.length > 0 ? (
          <ul>
            {bfs_connections.map((connection, index) => (
              <li key={index}>{connection}</li>
            ))}
          </ul>
        ) : (
          <p>No BFS connections found.</p>
        )}
      </div>
    </div>
  );
}

export default Results;