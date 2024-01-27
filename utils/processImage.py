import mediapipe as mp
from .resizeFrame import resizeFrame
from .colorConverters import convertToBGR, convertToRGB

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def processImage(frame, instance):
    # Resizes the frame
    resized_frame = resizeFrame(frame)

    # Recolor image to RGB
    image = convertToRGB(resized_frame)
    
    # Make detection
    results = instance.process(image)

    # Recolor back to BGR
    image = convertToBGR(image)

    # Extract landmarks
    try:
      landmarks = results.pose_landmarks.landmark
    except:
      pass
    
    # # Render detections
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS, mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2))

    return image