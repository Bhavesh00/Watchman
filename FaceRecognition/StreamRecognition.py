# Authors -- Toby Liang, Vishnu Srinivasan
# Saturday Feb 23, 2019

import face_recognition
import cv2
from PIL import Image
import glob
import time
import threading

#This is arrays for the locations of the faces, encodings and the names associated with the faces
#This is for the the frames in the video stream to make sure every element in the video stream is run
#Setting up a video capture stream

#Populating the image objects from the directory
def populate_images(image_objects):
    filenames = [img for img in glob.glob("images/*.jpg")]
    filenames.sort() # ADD THIS LINE
    for img in filenames: #assuming jpg
        im = face_recognition.load_image_file(img)
        image_objects.append(im)
    return image_objects

#Isolate the names of the images from the names of the folder
def get_names(image_names):
    filenames = [img for img in glob.glob("images/*.jpg")]
    filenames.sort() # ADD THIS LINE
    image_names = []
    for name in filenames:
        s = name[7 : -4]
        image_names.append(''.join([i for i in s if not i.isdigit()]))
    return image_names

#This sets up the face and encoding arrays
def set_up(faces):
    image_objects = []
    image_objects = populate_images(image_objects)
    #Make a new face encoding list to pass in image objects into the list 
    face_encodings = []
    #Iterating through the list to get the images with the encoding method to 128 pixels
    for image in image_objects:
        face_encodings.append(face_recognition.face_encodings(image)[0])
    faces = face_encodings
    return faces

#Method to record the video that is passed into the detction algorithim
def recordVideo():
    cap = cv2.VideoCapture(0) # Capture video from camera
    start_time = time.time()
    seconds_to_record = 10
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
    fps = 6.0
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('UnknownPerson.mp4', fourcc, fps, (width, height))

    while (int(time.time() - start_time) < seconds_to_record):
        ret, frame = cap.read()
        if ret == True:
            out.write(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    out.release()
    cap.release()
    cv2.destroyAllWindows()

#Runner method for the deetection and classification algorithim
def run_face_detection(input_video, kfaces, frame_number, names):
    face_locations = []
    face_encodings = []
    face_names = []
    num_recording = 0
    #While the video stream is on
    while True:
        ret, frame = input_video.read()
        frame_number += 1
        #If the stream is false, break out of it
        if not ret:
            break
        #This is the conversion between rgb and bgr
        rgb_frame = frame[:, :, ::-1]
        #This passes in the locations of the faces
        face_locations = face_recognition.face_locations(rgb_frame, model = "hog")
        #This sets up the face encoding section from the  image stream
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        #This sets up an array of the face names present from the video stream
        face_names = []
        #Runs while there is a face encoding in the list
        for face_encoding in face_encodings:
            #Compares the current face_encoding object with thee set of known faces to find a match
            match = face_recognition.compare_faces(kfaces, face_encoding, tolerance = 0.4)

            #Annotates the images with the names
            name = None
            iterator = 0
            for result in match:
                if result:
                    name = names[iterator]
                else:
                    iterator += 1
                    continue

            #Addes the name of the face to the name of the faces
            face_names.append(name)
        #This sets up the boxes and draws around the images
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            if not name:
                for (x,y,w,h) in face_locations: 
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    #This sets up the rectangle around the face in green filled
                    cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    if num_recording < 1:
                        #print("Recording Video of Unknown Person(s)")
                        threading.Thread(target = recordVideo).start()                        
                        num_recording += 1 
            else:
                #This sets up the rectangle around thee face in green
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                #This sets up the rectangle around the face in green filled
                cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 255, 0), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                #
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
        #print("Writing frame {}".format(frame_number))
        cv2.imshow('frame', frame)

        #This exits the video feed when we hit esc
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            input_video.release()
            cv2.destroyAllWindows()

#Main runner
def main():
    input_video = cv2.VideoCapture(0)
    frame_number = 0
    known_faces = []
    names = []
    kf = set_up(known_faces)
    list_of_names = get_names(names)
    run_face_detection(input_video, kf, frame_number, list_of_names)

main()