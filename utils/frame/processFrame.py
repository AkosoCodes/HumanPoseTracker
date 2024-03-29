import mediapipe as mp
import cv2 as cv
import numpy as np
from .resizeFrame import resizeFrame
from ..color.convertColorFormat import convertToBGR, convertToRGB
from theme.theme import *
from ..angles.processAngles import *
from ..information.renderInformation import renderStatusBox
from ..landmarks.extractLandmarks import *

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


def processFrame(frame, instance, counter, stage, tilt, stance, lowest_angle, highest_angle):
    """
    Processes the frame (image) and returns the processed frame (image) and updated values.

    Parameters:
    - frame (numpy.ndarray): The input frame (image) to be processed.
    - instance: An instance of a MediaPipe pose detection module.
    - counter (int): The current counter value.
    - stage (str): The current stage of the squat.
    - tilt (str): The current tilt of the squat.
    - stance (str): The current stance of the squat.
    - lowest_angle (float): The lowest depth angle recorded.
    - highest_angle (float): The highest depth angle recorded.

    Returns:
    - image (numpy.ndarray): The processed frame (image).
    - counter (int): The updated counter value.
    - stage (str): The updated stage of the squat.
    - tilt (str): The updated tilt of the squat.
    - stance (str): The updated stance of the squat.
    - [lowest_angle, highest_angle] (list): The updated lowest and highest depth angles recorded.
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
      depthLandmarks, tiltLandmarks, stanceLandmarks = extractLandmarks(results, mp_pose)

      # Calculates the angle between the hip, knee, and heel
      depthAngle = calculateAngle(depthLandmarks)

      # Calculates the vertical distance between the left and right shoulder
      tiltAngle = round(tiltLandmarks[0] - tiltLandmarks[1], 3)

      # Calculates the horizontal distance between the left and right heel
      stanceDistance = round(stanceLandmarks[0][0] - stanceLandmarks[1][0], 3)

      # Updates the lowest and highest angles
      if depthAngle < lowest_angle:
        lowest_angle = depthAngle
      if depthAngle > highest_angle:
        highest_angle = depthAngle

      # Processing the depth angle and tilt angles
      stage, counter = processDepthAngle(stage, counter, depthAngle)
      tilt = processTiltAngle(tilt, tiltAngle)
      stance = processStance(stance, stanceDistance)

    except Exception as e:
        print(f"Error processing frame: {e}")
        depthAngle = 170
        tiltAngle = 0
        tilt = "NEUTRAL"
        stance = "NEUTRAL"

    # Renders the status box
    renderStatusBox(image, counter, depthAngle, tilt, stance, stage)

    # Renders pose landmarks on the image
    mp_drawing.draw_landmarks(
    image, 
    results.pose_landmarks, 
    mp_pose.POSE_CONNECTIONS, 
    mp_drawing.DrawingSpec(color=pointColor, thickness=2, circle_radius=2),
    mp_drawing.DrawingSpec(color=lineColor, thickness=2, circle_radius=2)
    )

    return image, counter, stage, tilt, stance, [lowest_angle, highest_angle]