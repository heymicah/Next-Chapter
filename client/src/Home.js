import React from 'react';
import './Home.css'; // Import the CSS file
import titleImage from './assets/Images/TitleImage.png'; // Import the image file

function Home() {
  console.log('Home component rendered');
  return (
    <div className="home-container">
      <img src={titleImage} alt="Title" className="home-image" /> {/* Use the imported image */}
      <div className="search-container">
        <i className="fas fa-search search-icon"></i> {/* Font Awesome search icon */}
        <input type="text" id="myTextInput" className="home-textbox" placeholder="Enter text here" /> {/* Corrected input element */}
      </div>
    </div>
  );
}

export default Home;
