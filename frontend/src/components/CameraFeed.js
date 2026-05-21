import Webcam from "react-webcam";

function CameraFeed() {

  return (

    <div className="rounded-2xl overflow-hidden">

      <Webcam
        height={300}
        width={400}
        mirrored={true}
      />

    </div>

  );
}

export default CameraFeed;