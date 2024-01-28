first playing around with cv2 to try the camera and how it records/processes frames

once set up, tried the mindpipe library to see if it would work with the camera and check how it maps the skeleton

after that worked, i recorded a video of me doing the exercises and tried to see if the library could detect the exercises
  first issue occurred since the video was too big so it needed to be resized
  besides resizing, the video needed to be compressed as it was in slow motion
  REALIZED that it was due to the slower processing since the first calibration video was filmed at 60fps on a 2k resolution, while the second was filmed at 30fps on 1080p


Next issue was when I tried to implement a rep counter. The inital logic for that was based on the angle of between the hip knee and heel, as that represents the bend and the squat itself.

The issue which I faced was with the logic to count the rep. The inital thought was to seperate the top part to be above 160 deg, and the bottom to be under 100deg.

    if angle > 165:
          if stage == 'up':
              stage = 'down'
              print("On top")
      elif angle < 100 and stage == 'down':
          stage = 'up'
          counter += 1
          print("On bottom")


What I encountered was that the reps were being counted down and not when the user finishes the squat up.
in order to fix this, I added a middle step in between, and based on that it will only count if the stage changes from middle to up.

      # Increments the counter if the person does a squat
      if angle > 155 and stage == "middle":
          stage = "up"
          counter += 1
          print("At the Top.")
      if angle < 155 and angle > 100:
          stage = "middle"
      if angle < 100 and stage == "middle":
          stage = "down"
          print("At the bottom.")

Then ANOTHER issue was that i noticed in the case that I go from 156deg to 154 deg and go up, it will count as a rep which is not the case. Due to this, instead of having a 'middle' stage, based on which one was before it, it will be more detailed which solved the problem.


      # Increments the counter if the person does a squat
      if angle > 155 and stage == "raising":
          stage = "up"
          counter += 1
          print("At the Top.")
      if angle < 155 and angle > 100:
          if stage == "up":
              stage = "lowering"
          else:
              stage = "raising"
      if angle < 100 and stage == "lowering":
          stage = "bottom"
          print("At the bottom.")


This worked great for the reps, but the model seems to mix up the stages and incorrectly predicts them for some reason. The stages should be done like this:

Top position
Top -> Bottom (Lowering)
Bottom position
Bottom -> Top (Raising)

The reason for the incorrect prediction is dxue to only a check in the middle if the stage is up, and if it isn't then the stage was switched to raising. What i failed to notice is that once the user lowers, the stage will be switched to lowering hence it will not trigger the up statement. This was an easy fix:

      # Increments the counter if the person does a squat
      if angle > 155 and stage == "raising":
          stage = "top"
          counter += 1
          print("At the Top.")
      if angle < 155 and angle > 100:
          if stage == "top":
              stage = "lowering"
          elif stage == "bottom":
              stage = "raising"
      if angle < 100 and stage == "lowering":
          stage = "bottom"
          print("At the bottom.")

So far the reps work like a charm, and the stages are correctly predicted. The next step is to implement the tilting direction. What I also realized is that it would be ideal to keep track of the highest and deepest angles during the squat..

This was easily added by adding two new variables.

Next thing I want to add to the model, is the tilting of shoulders, to know whether someone is leaning left or right. This can be crucial to know if someone is doing the exercise correctly or not.

The logic for this is to calculate the horizontal differences between shoulders, as if one is higher than th eother

tiltAngle = round(tiltLandmarks[0] - tiltLandmarks[1], 3)

if positive, then the left shoulder is higher than the right, and vice versa.
ONE THING TO NOTE, currently the model predicts the tilt in the correct direction in real life, but if the video is flipped, it will be opposite.

in other words, it looks from your perspective, so if you are facing in front of the camera it will be wrong
