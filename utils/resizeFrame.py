import cv2 as cv

def resizeFrame(frame, target_width = 300, target_height = 700):
  """
  Resizes the input frame while maintaining its aspect ratio to fit within
  a target width and height.

  Parameters:
  - frame (numpy.ndarray): The input frame (image) to be resized.
  - target_width (int, optional): The target width for resizing. Default is 300.
  - target_height (int, optional): The target height for resizing. Default is 700.

  Returns:
  - numpy.ndarray: The resized frame.
  """

  # Original width, height and aspect ratio
  original_width = frame.shape[1]
  original_height = frame.shape[0]
  aspect_ratio_original = original_width / original_height

  # Target aspect ratio
  target_aspect_ratio = target_width / target_height

  # Determines the new width and height for resizing while maintaining the aspect ratio
  if aspect_ratio_original > target_aspect_ratio:
      new_width = target_width
      new_height = int(target_width / aspect_ratio_original)
  else:
      new_width = int(target_height * aspect_ratio_original)
      new_height = target_height

  # Resizes the frame
  resized_frame = cv.resize(frame, (new_width, new_height))

  # Returns the frame
  return resized_frame
