import { useState } from "react";
import axios from "axios";

function App() {
  const [song, setSong] = useState("");
  const [recommendations, setRecommendations] = useState([]);

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