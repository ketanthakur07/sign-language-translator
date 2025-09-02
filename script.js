const videoElement = document.getElementById("webcam");
const outputElement = document.getElementById("output");

// Get webcam
async function setupCamera() {
  const stream = await navigator.mediaDevices.getUserMedia({
    video: true,
  });
  videoElement.srcObject = stream;
}

setupCamera();

// Placeholder: Real model integration needed
// For now, it just displays a dummy message
setInterval(() => {
  outputElement.innerText = "👋 Detected Hand (demo)";
}, 2000);
