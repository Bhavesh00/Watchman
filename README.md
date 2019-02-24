# Watchman
## WATCHMAN
“The Watchman” is a video surveillance tool which helps a given user to perform human face recognition using an existing knowledge base and validate whether the human in the given video is a threat to the user or not.

## PROJECT FEATURES
Human Face Recognition
Dynamic Security
User Feedback
User Surveillance
In-depth Authentication 
Real-time Recognition

## USAGE
A usage scenario for our application is security surveillance at homes which will help people keep the home and surrounding safe and prevent accidents.’

## BUILD/INSTALLATION INSTRUCTIONS
Python version 2.7 or 3.6
Operating System: MacOS, Windows
Main Dependencies - face recognition, glob, threading, cv2 and time.
Pip install -- DEPENDENCY_NAME 
Other Dependencies - CMake (Guide for installing CMake on your OS: https://cmake.org/install/)
You can run our program with a conventional python StreamRecognition.py command in the working directory of the code. Our images for testing and training are stored in the images directory and follows a naming format - “num_imagePerson_Name.jpg” (example 01Vishnu.jpg). You can add more images and remove to tune your image recognition model. Just change the path file and the image extraction method accordingly. Additionally, boxes with a green overlay mean that the face is from one of the images dropped in with the name, and red means it is a new person. Any time a red box pops up, the script records the stream and will save a video of the person.

## OTHER SOURCES OF DOCUMENTATION
[Face Recognition API](https://face-recognition.readthedocs.io/en/latest/face_recognition.html)

## Contributor Guide
[CONTRIBUTING.md](/CONTRIBUTING.md)

## License
The Watchman project is licensed under the MIT License. 
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

