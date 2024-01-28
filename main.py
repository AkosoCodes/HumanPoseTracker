import cv2 as cv
import mediapipe as mp
from utils.processFrame import processFrame

# Video source (0 for webcam  or path to video file)
video_path = "assets/calibration4.mp4"

## Setup video capture
capture = cv.VideoCapture(video_path)

## Setup mediapipe instance
with mp.solutions.pose.Pose(min_detection_confidence=0.45, min_tracking_confidence=0.45) as pose:

  stage = 'top'
  counter = 0
  minAngle = float('inf')
  maxAngle = float('-inf')
  
  while capture.isOpened():
    success, frame = capture.read()

    # Check if the video has ended
    if not success:
      print("The video has ended.")
      break

    # Processes the image
    image, counter, stage, boundary = processFrame(frame, pose, counter, stage, minAngle, maxAngle)
    
    # Keep track of the lowest and highest angles
    if boundary[0] < minAngle:
      minAngle = boundary[0]
    if boundary[1] > maxAngle:
      maxAngle = boundary[1]

    # Display the resulting frame
    cv.imshow('Mediapipe Feed', image)
    
    # Press Q on keyboard to exit the program
    if cv.waitKey(10) & 0xFF == ord('q'):
        break

  print('Number of REPS:', counter)
  print('Lowest angle:', minAngle)
  print('Highest angle:', maxAngle)
# Release the capture when done
capture.release()
cv.destroyAllWindows()