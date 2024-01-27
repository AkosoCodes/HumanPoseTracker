import mediapipe as mp
from .resizeFrame import resizeFrame
from .colorConverters import convertToBGR, convertToRGB

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def processImage(frame, instance):
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
    except:
      pass
    
    # Renders pose landmarks on the image
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS, mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2))

    return image