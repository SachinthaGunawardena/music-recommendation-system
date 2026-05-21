function MoodCard({ mood }) {

  return (

    <div className="
      bg-zinc-900
      p-6
      rounded-2xl
      w-64
    ">

      <h2 className="text-2xl font-bold">
        Current Mood
      </h2>

      <p className="
        text-4xl
        text-green-500
        mt-4
        font-bold
      ">
        {mood}
      </p>

    </div>

  );

}

export default MoodCard;