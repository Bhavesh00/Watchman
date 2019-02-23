import face_recognition
import cv2
import os
from os import *

#Setting up a video capture stream
input_video = cv2.VideoCapture(0)
length = int(input_video.get(cv2.CAP_PROP_FRAME_COUNT))

known_faces = []
def getKnownFaces():
    my_dir = "./KnownFaces/"
    facesFiles = [file for file in listdir(my_dir)]
    for file in facesFiles:
        image = my_dir + file
        file_name, file_extension = os.path.splitext(file)
        if file_extension != ".jpg":
            continue
        image = face_recognition.load_image_file(file)
        encoding = face_recognition.face_encodings(image)[0]
        known_faces.append(encoding)

getKnownFaces()

#This is arrays for the locations of the faces, encodings and the names associated with the faces
face_locations = []
face_encodings = []
face_names = []

#This is for the the frames in the video stream to make sure every element in the video stream is run
frame_number = 0

#While the video stream is on
while True:
    ret, frame = input_video.read()
    frame_number += 1

    if not ret:
        break

    #This is the conversion between rgb and bgr
    rgb_frame = frame[:, :, ::-1]

    #This passes in the locations of the faces
    face_locations = face_recognition.face_locations(rgb_frame)

    #This sets up the face encoding section from the  image stream
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    #This sets up an array of the face names present from the video stream
    face_names = []

    #Runs while there is a face encoding in the list
    for face_encoding in face_encodings:
        
        #Compares the current face_encoding object with thee set of known faces to find a match
        match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.5)

        #Annotates the images with the names
        name = None
        if match[0]:
            name = "Vishnu"
        elif match[1]:
            name = "Bhavesh"
        elif match[2]:
            name = "Pablo"

        #Addes the name of the face to the name of the faces
        face_names.append(name)

    #This sets up the boxes and draws around the images
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        if not name:
            continue

        #This sets up the rectangle around thee face in green
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        #This sets up the rectangle around the face in green filled
        cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 255, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        #
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)


    print("Writing frame {} / {}".format(frame_number, length))
    cv2.imshow('frame', frame)

    #This exits the video feed when we hit esc
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        input_video.release()
        cv2.destroyAllWindows()


input_video.release()
cv2.destroyAllWindows()
