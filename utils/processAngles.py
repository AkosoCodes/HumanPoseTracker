import numpy as np

def calculate_angle(landmarks):
    """
    Calculate the angle between three points (a, b, c) in a 2D plane.

    Parameters:
    - a (list or tuple): Coordinates of the first point.
    - b (list or tuple): Coordinates of the mid-point.
    - c (list or tuple): Coordinates of the end point.

    Returns:
    - angle (float): The calculated angle in degrees.
    """

    # Convert to NumPy array for vector operations
    a = np.array(landmarks[0])
    b = np.array(landmarks[1])
    c = np.array(landmarks[2])

    # Calculate angle using arctan2 and convert to degrees
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    # Ensure the angle is within the range [0, 180)
    if angle > 180.0:
        angle = 360 - angle

    return angle

def processTiltAngle(tilt, angle):
    """
    Processes the angle and updates the tilt value based on specific conditions.

    Parameters:
    - tilt (str): Current tilt ("left", "right", "center", or "none").
    - angle (float): Current angle between the left and right shoulders.

    Returns:
    - str: Updated tilt value.
    """
    
    #if positive number, tilt left
    if angle > 0:
        if angle > 0.04:
            tilt = "RIGHT"
        elif angle > 0.02:
            tilt = "SLIGHT-RIGHT"
    elif angle < 0:
        if angle < -0.04:
            tilt = "LEFT"
        elif angle < -0.02:
            tilt = "SLIGHT-LEFT"
    else:
        tilt = "NEUTRAL"


    return tilt

def processDepthAngle(stage, counter, angle):
    """
    Processes the angle and updates the stage and counter based on specific conditions.

    Parameters:
    - stage (str): Current stage ("raising", "lowering", "top", or "bottom").
    - counter (int): Current counter value.
    - angle (float): Current angle between hip, knee, and heel.

    Returns:
    - tuple: Tuple containing the updated stage and counter values.
    """
    if angle > 165 and stage == "raising":
        stage = "top"
        counter += 1
    if 165 > angle > 60:
        if stage == "top":
            stage = "lowering"
        elif stage == "bottom":
            stage = "raising"
    if angle < 60 and stage == "lowering":
        stage = "bottom"
    return stage, counter