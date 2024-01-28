import mediapipe as mp
import cv2 as cv
import numpy as np
from .resizeFrame import resizeFrame
from .colorConverters import convertToBGR, convertToRGB
from theme.theme import *

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def calculate_angle(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
        
    return angle 

def renderStatusBox(image, counter, angle, stage):
    # Draw a semi-transparent background rectangle for better readability
    cv.rectangle(image, (0, 0), (225, 110), statusBox, -1)

    # Display "REPS" label
    cv.putText(image, 'REPS:', (15, 25), cv.FONT_HERSHEY_SIMPLEX, 0.7, statusLabel, 2, cv.LINE_AA)

    # Display the counter value
    cv.putText(image, str(counter), (100, 25), cv.FONT_HERSHEY_SIMPLEX, 0.7, statusValue, 2, cv.LINE_AA)

    # Display "ANGLE" label
    cv.putText(image, 'ANGLE:', (15, 60), cv.FONT_HERSHEY_SIMPLEX, 0.7, statusLabel, 2, cv.LINE_AA)

    # Display the angle value
    if angle != None:
        cv.putText(image, str(int(angle)), (100, 60), cv.FONT_HERSHEY_SIMPLEX, 0.7, statusValue, 2, cv.LINE_AA)

    # Display the "STAGE" label
    cv.putText(image, 'STAGE:', (15, 95), cv.FONT_HERSHEY_SIMPLEX, 0.7, statusLabel, 2, cv.LINE_AA)

    # Display the stage value
    cv.putText(image, str(stage), (100, 95), cv.FONT_HERSHEY_SIMPLEX, 0.7, statusValue, 2, cv.LINE_AA)

    # Display additional information under the angle value
    cv.putText(image, '* Refers to angle between hip, knee, and heel', (15, 115), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv.LINE_AA)

def processImage(frame, instance, counter, stage):
    """
    Processes an input frame by resizing, recoloring, and applying pose detection.

    Parameters:
    - frame (numpy.ndarray): The input frame (image) to be processed.
    - instance: An instance of a MediaPipe pose detection module.

    Returns:
    - numpy.ndarray: The processed frame with pose landmarks drawn.
    """
        
    # Resizes the frame
    resized_frame = resizeFrame(frame)

    # Colors the image to RGB
    image = convertToRGB(resized_frame)
    
    # Makes detections
    results = instance.process(image)

    # Recolors the image back to BGR
    image = convertToBGR(image)

    # Extracts landmarks
    try:
      landmarks = results.pose_landmarks.landmark

      # Gets the landmarks for the left hip, knee, and heel
      hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
      knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
      heel = [landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].y]

      # Calculates the angle between the hip, knee, and heel
      angle = calculate_angle(hip, knee, heel)

      # Increments the counter if the person does a squat
      if angle > 165 and stage == "raising":
          stage = "top"
          counter += 1
          print("At the Top.")
      if angle < 165 and angle > 60:
          if stage == "top":
              stage = "lowering"
          elif stage == "bottom":
              stage = "raising"
      if angle < 60 and stage == "lowering":
          stage = "bottom"
          print("At the bottom.")

    except Exception as e:
        print(f"Error processing frame: {e}")
        angle = 170

    # Renders the status box
    renderStatusBox(image, counter, angle, stage)

    # Renders pose landmarks on the image
    mp_drawing.draw_landmarks(
    image, 
    results.pose_landmarks, 
    mp_pose.POSE_CONNECTIONS, 
    mp_drawing.DrawingSpec(color=pointColor, thickness=2, circle_radius=2),  # Adjust the color and circle_radius for landmarks
    mp_drawing.DrawingSpec(color=lineColor, thickness=2, circle_radius=2)   # Adjust the color and circle_radius for connections
    )


    return image, counter, stage