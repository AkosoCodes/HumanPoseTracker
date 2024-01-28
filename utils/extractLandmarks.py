
def extractLandmarks(results, mp_pose):
    """
    Extracts landmarks for the left hip, knee, and heel from the results of pose detection.

    Parameters:
    - results: Pose detection results from MediaPipe.

    Returns:
    - tuple: Tuple containing the landmarks for the left hip, knee, and heel.
    """
    landmarks = results.pose_landmarks.landmark

    hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
    knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
    heel = [landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].y]

    leftShoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
    rightShoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]

    depthLandmarks = [hip, knee, heel]
    tiltLandmarks = [leftShoulder.y, rightShoulder.y]

    return depthLandmarks, tiltLandmarks