import cv2 as cv
import mediapipe as mp
from utils.processImage import processImage

# Video source (0 for webcam  or path to video file)
video_path = "assets/calibration4.mp4"

## Setup video capture
capture = cv.VideoCapture(video_path)

## Setup mediapipe instance
with mp.solutions.pose.Pose(min_detection_confidence=0.45, min_tracking_confidence=0.45) as pose:

  stage = 'top'
  counter = 0
  
  while capture.isOpened():
    success, frame = capture.read()

    # Check if the video has ended
    if not success:
      print("The video has ended.")
      break

    # Processes the image
    image, counter, stage = processImage(frame, pose, counter, stage)
    
    # Display the resulting frame
    cv.imshow('Mediapipe Feed', image)
    
    # Press Q on keyboard to exit the program
    if cv.waitKey(10) & 0xFF == ord('q'):
        break

# Release the capture when done
capture.release()
cv.destroyAllWindows()