import cv2 as cv

# Converts a BGR frame to RGB
def convertToRGB(frame):
    image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    image.flags.writeable = False

    return image

# Converts a RGB frame to BGR
def convertToBGR(frame):
    image = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    image.flags.writeable = True
    return image