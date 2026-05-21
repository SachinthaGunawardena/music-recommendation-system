import CameraFeed from "../components/CameraFeed"
import MoodCard from "../components/MoodCard"
import Recommendations from "../components/Recommendations"

function Dashboard() {
  return (
    <div className="min-h-screen bg-black text-white">
      
      <div className="p-6">
        <h1 className="text-5xl font-bold mb-8">
          AI Music Dashboard
        </h1>

        <div className="grid grid-cols-3 gap-6">

         <div className="bg-zinc-900 p-6 rounded-2xl">

  <CameraFeed />

</div>

          <div className="bg-zinc-900 p-6 rounded-2xl">
            <MoodCard mood="Happy" />
          </div>

          <div className="bg-zinc-900 p-6 rounded-2xl">
 <Recommendations />
</div>
        </div>
      </div>

    </div>
  )
}

export default Dashboard