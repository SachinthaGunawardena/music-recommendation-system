import { useState, useEffect } from "react";
import axios from "axios";
import {
  FaSmile,
  FaSadTear,
  FaAngry,
  FaMeh,
  FaMusic
} from "react-icons/fa";

function App() {

  const [mood, setMood] = useState(null);
  const [songs, setSongs] = useState([]);
  const [loading, setLoading] = useState(false);
  const [isDetecting, setIsDetecting] = useState(false);

  const moodGenres = {
    happy: "Pop",
    sad: "Blues",
    angry: "Rock",
    neutral: "Jazz",
    surprise: "Pop",
    fear: "Blues",
    disgust: "Rock"
  };

  const moodIcons = {
    happy: <FaSmile />,
    sad: <FaSadTear />,
    angry: <FaAngry />,
    neutral: <FaMeh />,
    surprise: <FaSmile />,
    fear: <FaSadTear />,
    disgust: <FaAngry />
  };

  const detectMood = async () => {

    if (isDetecting) return;

    try {

      setIsDetecting(true);
      setLoading(true);

      const moodResponse = await axios.get(
        "http://127.0.0.1:8000/detect-mood"
      );

      const detectedMood = moodResponse.data.mood;

      setMood(detectedMood);

      const recResponse = await axios.get(
        `http://127.0.0.1:8000/recommend-by-mood/${detectedMood}`
      );

      setSongs(recResponse.data.recommendations);

    } catch (error) {

      console.error(error);

    } finally {

      setLoading(false);
      setIsDetecting(false);

    }
  };

  useEffect(() => {

    detectMood();

    const interval = setInterval(() => {

      detectMood();

    }, 10000);

    return () => clearInterval(interval);

  }, []);

  return (

    <div className="min-h-screen bg-gradient-to-b from-black via-[#121212] to-black text-white">

      {/* NAVBAR */}
      <div className="
        flex
        justify-between
        items-center
        px-8
        py-5
        border-b
        border-gray-800
      ">

        <h1 className="
          text-3xl
          font-bold
          text-green-500
          flex
          items-center
          gap-3
        ">
          <FaMusic />
          AI Music Recommendation
        </h1>

        <button
          onClick={detectMood}
          className="
            bg-green-500
            hover:bg-green-400
            px-6
            py-3
            rounded-full
            text-black
            font-bold
            transition-all
            duration-300
            hover:scale-105
          "
        >
          Refresh Mood
        </button>

      </div>

      {/* MAIN CONTENT */}
      <div className="max-w-7xl mx-auto px-6 py-10">

        {/* MOOD SECTION */}
        <div className="
          bg-[#181818]
          rounded-3xl
          p-8
          shadow-2xl
          border
          border-gray-800
          mb-10
        ">

          <div className="
            flex
            flex-col
            md:flex-row
            items-center
            justify-between
            gap-8
          ">

            {/* LEFT */}
            <div>

              <p className="text-gray-400 mb-2 text-lg">
                Live Emotion Detection
              </p>

              <h2 className="
                text-5xl
                font-bold
                capitalize
                flex
                items-center
                gap-4
              ">

                <span className="text-green-400 text-6xl">
                  {moodIcons[mood]}
                </span>

                {mood || "Detecting..."}

              </h2>

              <p className="mt-4 text-2xl text-gray-300">

                Recommended Genre:

                <span className="text-green-500 ml-3 font-bold">
                  {moodGenres[mood]}
                </span>

              </p>

            </div>

            {/* RIGHT */}
            <div className="
              w-40
              h-40
              rounded-full
              bg-green-500/20
              flex
              items-center
              justify-center
              text-green-400
              text-7xl
              border
              border-green-500
            ">

              {moodIcons[mood]}

            </div>

          </div>

        </div>

        {/* LOADING */}
        {loading && (

          <div className="flex justify-center mb-10">

            <div className="
              w-16
              h-16
              border-4
              border-green-500
              border-t-transparent
              rounded-full
              animate-spin
            "></div>

          </div>

        )}

        {/* SONG GRID */}
        <div className="
          grid
          grid-cols-1
          sm:grid-cols-2
          lg:grid-cols-3
          xl:grid-cols-4
          gap-8
        ">

          {songs.map((song, index) => (

            <div
              key={index}
              className="
                bg-[#181818]
                rounded-3xl
                overflow-hidden
                shadow-xl
                hover:scale-105
                hover:bg-[#222]
                transition-all
                duration-300
                border
                border-gray-800
              "
            >

              <img
                src={`https://picsum.photos/500/500?random=${index}`}
                alt="album"
                className="
                  w-full
                  h-64
                  object-cover
                "
              />

              <div className="p-5">

                <h3 className="
                  text-xl
                  font-bold
                  mb-2
                  line-clamp-1
                ">
                  {song.track_name}
                </h3>

                <p className="
                  text-gray-400
                  mb-4
                  line-clamp-1
                ">
                  {song.artist_name}
                </p>

                <div className="flex justify-between items-center">

                  <span className="
                    bg-green-500
                    text-black
                    px-4
                    py-2
                    rounded-full
                    text-sm
                    font-bold
                  ">
                    {song.genre}
                  </span>

                  <button className="
                    bg-white/10
                    hover:bg-white/20
                    px-4
                    py-2
                    rounded-full
                    text-sm
                    transition
                  ">
                    Play
                  </button>

                </div>

              </div>

            </div>

          ))}

        </div>

      </div>

    </div>
  );
}

export default App;