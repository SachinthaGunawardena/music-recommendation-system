function SongCard({ song }) {

  return (
    <div className="bg-zinc-800 p-4 rounded-xl">
      <h2 className="font-bold">
        {song.track_name}
      </h2>

      <p>{song.artist_name}</p>
    </div>
  )
}

export default SongCard