import face_recognition
import cv2
from PIL import Image
import glob


#This is arrays for the locations of the faces, encodings and the names associated with the faces
#This is for the the frames in the video stream to make sure every element in the video stream is run

#Setting up a video capture stream

def populate_images(image_objects):

    filenames = [img for img in glob.glob("images/*.jpg")]
    filenames.sort() # ADD THIS LINE
    for img in filenames: #assuming jpg
        print(img)
        im = face_recognition.load_image_file(img)
        image_objects.append(im)
    return image_objects



def set_up(faces):
    image_objects = []
    image_objects = populate_images(image_objects)

    face_encodings = []

    for image in image_objects:
        face_encodings.append(face_recognition.face_encodings(image)[0])

    faces = face_encodings
    

    return faces


def run_face_detection(input_video, kfaces, frame_number):
    face_locations = []
    face_encodings = []
    face_names = []
    print(kfaces)
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
            match = face_recognition.compare_faces(kfaces, face_encoding, tolerance=0.5)

            #Annotates the images with the names
            name = None
            if match[0]:
                name = "Vishnu"
            elif match[1]:
                name = "Bhavesh"
            elif match[2]:
                name = "Pablo"
            elif match[3]:
                name = "Sumeet"

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


        print("Writing frame {}".format(frame_number))
        cv2.imshow('frame', frame)

        #This exits the video feed when we hit esc
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            input_video.release()
            cv2.destroyAllWindows()
    
def _main_():
    input_video = cv2.VideoCapture(0)
    frame_number = 0
    known_faces = []
    kf = set_up(known_faces)
    run_face_detection(input_video, kf, frame_number)










