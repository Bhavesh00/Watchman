# module and library required to build a Face Recognition System
import face_recognition
import cv2
# objective: this code will help you in running face recognition on a video file and saving the results to a new video file.
# Open the input movie file
# "VideoCapture" is a class for video capturing from video files, image sequences or cameras
input_video = cv2.VideoCapture(0)
#"CAP_PROP_FRAME_COUNT": it helps in finding number of frames in the video file.
length = int(input_video.get(cv2.CAP_PROP_FRAME_COUNT))
# Create an output movie file (make sure resolution/frame rate matches input video!)
#  So we capture a video, process it frame-by-frame and we want to save that video, it only possible by using "VideoWriter" object
# FourCC is a 4-byte code used to specify the video codec. The list of available codes can be found in fourcc.org. It is platform dependent.
fourcc = cv2.VideoWriter_fourcc('M','P','E','G')
# 25.07-  number of frames per second (fps)
#(1280,720)- frame size
output_video = cv2.VideoWriter('output.avi', fourcc, 25.07, (1280, 720))

#  "face_recognition.face_encodings": it's a face_recognition package which returns a list of 128-dimensional face encodings
male_image = face_recognition.load_image_file("vishnu.jpg")
male_face_encoding = face_recognition.face_encodings(male_image)[0]

known_faces = [
    male_face_encoding
]
# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
frame_number = 0
while input_video:
    # Grab a single frame of video
    ret, frame = input_video.read()
    frame_number += 1
# Quit when the input video file ends
    if not ret:
        break
# Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]
# Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
face_names = []
for face_encoding in face_encodings:
	match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.50)
	name = None
	if match[0]:
		name = "vishnu"
        
face_names.append(name)
# Label the results
for (top, right, bottom, left), name in zip(face_locations, face_names):
	if not name:
		continue
    # Draw a box around the face
	cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    # Draw a label with a name below the face
	cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
	font = cv2.FONT_HERSHEY_DUPLEX
	cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
    cv2.imshow('frame',frame)
# All done!
input_video.release()
cv2.destroyAllWindows()
