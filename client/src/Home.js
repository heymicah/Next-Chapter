import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Home.css'; 
import titleImage from './assets/Images/TitleImage.png';

function Home() {
  const navigate = useNavigate();
  const [genre, setGenre] = useState('');
  const handleClick = async () => {
    const title = document.getElementById('TextInput').value;
    console.log(`Sending title: ${title}, genre: ${genre}`);
    try {
      // Send the title and genre to the backend
      const response = await fetch(`http://127.0.0.1:8000/book-connections?title=${encodeURIComponent(title)}&genre=${encodeURIComponent(genre)}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      console.log(`Received response: ${JSON.stringify(data)}`);
      // Navigate to the results page
      navigate('/results', { state: { data } });
    } catch (error) {
      console.error('Failed to fetch:', error);
    }
  };

  const handleGenreChange = (event) => {
    setGenre(event.target.value);
  };

  return (
    <div className="home-container">
      <img src={titleImage} alt="Title" className="home-image" />
      <div className="content-container">
        <div className="search-container">
          <i className="fas fa-search search-icon"></i>
          <input type="text" id="TextInput" className="home-textbox" placeholder="Enter text here" />
        </div>
        <div className="dropdown-container">
          <select className="home-dropdown" value={genre} onChange={handleGenreChange}>
            <option value="" disabled>Select a genre</option>
            <option value="History">History</option>
            <option value="Biography & Autobiography">Biography & Autobiography</option>
            <option value="Business & Economics">Business & Economics</option>
            <option value="Political Science">Political Science</option>
            <option value="Romance">Romance</option>
            <option value="Fantasy">Fantasy</option>
            <option value="Fiction">Fiction</option>
            <option value="Science Fiction">Science Fiction</option>
            <option value="Young Adult Fiction">Young Adult Fiction</option>
            <option value="Juvenile Nonfiction">Juvenile Nonfiction</option>
            <option value="Classics">Classics</option>
            <option value="Action & Adventure">Action & Adventure</option>
            <option value="Mystery & Detective">Mystery & Detective</option>
            <option value="Thrillers">Thrillers</option>
            <option value="Poetry">Poetry</option>
            <option value="Cooking">Cooking</option>
            <option value="Religion">Religion</option>
            <option value="General">General</option>
          </select>
          <button onClick={handleClick} className="home-searchButton">Search</button>
        </div>
      </div>
    </div>
  );
}

export default Home;