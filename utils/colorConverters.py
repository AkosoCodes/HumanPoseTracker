import cv2 as cv

def convertToRGB(frame):
  """
    Converts a BGR (Blue-Green-Red) format frame to RGB (Red-Green-Blue) format.

    Parameters:
    - frame (numpy.ndarray): The input frame in BGR format.

    Returns:
    - numpy.ndarray: The frame converted to RGB format.
  """

  image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
  image.flags.writeable = False

  return image

def convertToBGR(frame):
  """
    Converts an RGB (Red-Green-Blue) format frame to BGR (Blue-Green-Red) format.

    Parameters:
    - frame (numpy.ndarray): The input frame in RGB format.

    Returns:
    - numpy.ndarray: The frame converted to BGR format.
  """

  image = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
  image.flags.writeable = True
  return image