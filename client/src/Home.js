import React from 'react';
import './Home.css'; 
import titleImage from './assets/Images/TitleImage.png';

function Home() {
  console.log('Home component rendered');
  return (
    <div className="home-container">
      <img src={titleImage} alt="Title" className="home-image" /> {}
      <div className="search-container">
        <i className="fas fa-search search-icon"></i> {}
        <input type="text" id="myTextInput" className="home-textbox" placeholder="Enter text here" /> {}
      </div>
    </div>
  );
}

export default Home;
