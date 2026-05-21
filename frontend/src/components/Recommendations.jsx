import Recommendations from "../components/Recommendations"
import SongCard from "./SongCard"

function Recommendations() {

  const songs = [
    {
      track_name: "Blinding Lights",
      artist_name: "The Weeknd"
    },
    {
      track_name: "Believer",
      artist_name: "Imagine Dragons"
    }
  ]

  return (
    <div className="space-y-4">

      {songs.map((song, index) => (
        <SongCard
          key={index}
          song={song}
        />
      ))}

    </div>
  )
}

export default Recommendations