import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Home.css'; 
import titleImage from './assets/Images/TitleImage.png';

function Home() {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate('/results');
  };

  return (
    <div className="home-container">
      <img src={titleImage} alt="Title" className="home-image" />
      <div className="search-container">
        <i className="fas fa-search search-icon"></i>
        <input type="text" id="myTextInput" className="home-textbox" placeholder="Enter text here" />
      </div>
      <button onClick={handleClick} className="home-button">Search</button>
    </div>
  );
}

export default Home;