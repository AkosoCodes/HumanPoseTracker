
def extractLandmarks(results, mp_pose):
    """
    Extracts landmarks for the left hip, knee, and heel from the results of pose detection.

    Parameters:
    - results: Pose detection results from MediaPipe.

    Returns:
    - tuple: Tuple containing the landmarks for the left hip, knee, and heel.
    """
    landmarks = results.pose_landmarks.landmark

    leftHip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
    leftKnee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
    leftHeel = [landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].y]

    rightHeel = [landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value].y]

    leftShoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
    rightShoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]



    depthLandmarks = [leftHip, leftKnee, leftHeel]
    tiltLandmarks = [rightShoulder.y, leftShoulder.y]
    stanceLandmarks = [leftHeel, rightHeel]

    return depthLandmarks, tiltLandmarks, stanceLandmarks