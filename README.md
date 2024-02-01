<h1 align="center">Human Pose Tracker</h1>

<p align="center">This is a Computer Vision application developed in Python, which tracks the posture whilst doing a squatting movement.</p>


## 📝 | Table of Contents
- [📝 | Table of Contents](#--table-of-contents)
- [📸 | Demo ](#--demo-)
- [🧰 | Languages \& Tools ](#--languages--tools-)
- [🏁 | Getting Started ](#--getting-started-)
- [🫂 | Credits and Acknowledgments ](#--credits-and-acknowledgments-)
- [⚖ | License ](#--license-)


## 📸 | Demo <a name="demo"></a>

The snippet below shows the application in action. The application tracks the posture of the person in the video, and displays the results in real time. It displays the following information:
- The number of repetitions completed
- Depth angle of the squat
- The current stage of the movement
- The tilt position of the shoulders
- The stance of the feet

### Demonstration:
  
![Video of Squat](assets/demo.gif)

## 🧰 | Languages & Tools <a name="languages_tools"></a>

The application was built using Python, alongside the use of OpenCV and Media Pipe libraries.

<p>
  <a href="https://www.python.org/" target="_blank"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" width="50" height="50"/></a>
  <a href="https://opencv.org/" target="_blank"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/opencv/opencv-original.svg" alt="OpenCV" width="50" height="50"/></a>
  <a href="https://mediapipe.dev/" target="_blank"><img src="https://viz.mediapipe.dev/logo.png" alt="Media Pipe" width="50" height="50"/></a>
</p>


## 🏁 | Getting Started <a name="getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine.

**<h3>Requirements:</h3>**

- Python 3.11 or higher
- The following dependencies:
  - ```numpy == 1.23.5```
  - ```opencv-python == 4.9.0```
  - ```mediapipe == 0.10.9```


**<h3>Guide:</h3>**
1. Download and install Python
2. Clone the repository
3. Open the repository using the IDE of your choice
4. Install the required dependencies using ```pip install -r requirements.txt```
5. Configure the ```video_path``` variable in the ```main.py``` file to the path of the video you want to use. (Use ```0``` if you want to use your webcam)
6. Run the ```main.py``` file

## 🫂 | Credits and Acknowledgments <a name="credits"></a>

The video used for the demo and in the repository is not mine, and serves to demonstrate how the application works.
The original video was taken from [here](https://www.youtube.com/watch?v=124EvTRSLo8).

## ⚖ | License <a name="license"></a>
This repository is under the [MIT](https://opensource.org/licenses/MIT) license.
