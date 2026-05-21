import { useState, useEffect } from "react";
import axios from "axios";
import CameraFeed from "./components/CameraFeed";
import MoodCard from "./components/MoodCard";

function App() {
  const [song, setSong] = useState("");
  const [recommendations, setRecommendations] = useState([]);
  const [mood, setMood] = useState("Happy");
  const [genre, setGenre] = useState("");

  const getRecommendations = async () => {
    try {
      const response = await axios.get(
        `http://localhost:8000/recommend/${song}`
      );

      console.log(response.data);

      setRecommendations(response.data.recommendations || []);
    } catch (error) {
      console.error(error);
      alert("Error getting recommendations");
    }
  };

   const detectMood = async () => {

  try {

    const response = await axios.get(
      "http://127.0.0.1:8000/detect_mood"
    );

    setMood(response.data.mood);

  } catch (error) {

    console.error(error);

  }
};

const getMoodRecommendations = async () => {

  try {

    const response = await axios.get(
      "http://127.0.0.1:8000/mood_recommendations"
    );

    setMood(response.data.mood);

    setRecommendations(
      response.data.recommendations
    );

    setGenre(response.data.genre);

  } catch (error) {

    console.error(error);

  }

};
useEffect(() => {

  getMoodRecommendations();

  const interval = setInterval(() => {

    getMoodRecommendations();

  }, 5000);

  return () => clearInterval(interval);

}, []);

  return (
    <div className="container">
      <h1>Music Recommendation System</h1>

      <input
        type="text"
        placeholder="Enter song name..."
        value={song}
        onChange={(e) => setSong(e.target.value.toLowerCase())}
      />

      <button onClick={getRecommendations}>
        Get Recommendations
      </button>


      
      {/* Camera Section */}
<div className="p-6">

  <h2 className="text-3xl font-bold mb-4">
    Live Camera
  </h2>

  <CameraFeed />

  <div className="p-6">

  <MoodCard mood={mood} />

</div>

</div>

      <div className="recommendations">

  {recommendations.length > 0 ? (

    recommendations.map((item, index) => (

      <div className="card" key={index}>

        <h3>{item.track_name}</h3>

        <p>{item.artist_name}</p>

        <span>{item.genre}</span>

      </div>

    ))

  ) : (

    <p>No recommendations yet</p>

  )}

</div>
    </div>
  );
}

export default App;

