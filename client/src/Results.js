import React from 'react';
import './Results.css'; 

function Results() {
  return (
    <div className="results-container">
      <div className="results-content">
        <div className="left-half">
          <div className="results-header">
            5 most similar books:
          </div>
        </div>
        <div className="right-half">
          {}
        </div>
      </div>
    </div>
  );
}

export default Results;