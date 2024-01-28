
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
    return hip, knee, heel

def processAngle(stage, counter, angle):
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
        print("At the Top.")
    if 165 > angle > 60:
        if stage == "top":
            stage = "lowering"
        elif stage == "bottom":
            stage = "raising"
    if angle < 60 and stage == "lowering":
        stage = "bottom"
        print("At the bottom.")
    return stage, counter