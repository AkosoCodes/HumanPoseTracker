import numpy as np

def calculate_angle(a, b, c):
    """
    Calculate the angle between three points (a, b, c) in a 2D plane.

    Parameters:
    - a (list or tuple): Coordinates of the first point.
    - b (list or tuple): Coordinates of the mid-point.
    - c (list or tuple): Coordinates of the end point.

    Returns:
    - angle (float): The calculated angle in degrees.
    """
    a = np.array(a)  # Convert to NumPy array for vector operations
    b = np.array(b)  # Convert to NumPy array for vector operations
    c = np.array(c)  # Convert to NumPy array for vector operations

    # Calculate angle using arctan2 and convert to degrees
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    # Ensure the angle is within the range [0, 180)
    if angle > 180.0:
        angle = 360 - angle

    return angle