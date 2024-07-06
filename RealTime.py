import tensorflow as tf
import cv2
import numpy as np
from PIL import Image
from tensorflow.keras.applications.inception_v3 import preprocess_input
import os
import time
import re
import SQLServerDoWork
import datetime
names_negative_list = []
pos_list_own_images = np.array([])
neg_list_own_images = np.array([])
positive = []
negative = []
positive_distance_list = []
names_positive_list = []
negative1=[]

threshold = 1.5
pos_sum = 0
neg_sum = 0
encoder = tf.keras.models.load_model('mobilenetv2_ourdata_lfw_without_aug_3.h5')
def FaceYacta():


    def read_our_image(path):
        print(path)
        image = cv2.imread(path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = np.array(Image.fromarray(image).resize((128, 128)))

        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.08, minNeighbors=5)
        try:
            x, y, w, h = faces[0]
            face_img = image[y:y + h, x:x + w]
            face_img = np.array(Image.fromarray(face_img).resize((128, 128)))

        except:
            face_img = image

        return face_img

    def read_Anchor(image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = np.array(Image.fromarray(image).resize((128, 128)))

        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.08, minNeighbors=5)
        try:
            x, y, w, h = faces[0]
            face_img = image[y:y + h, x:x + w]
            face_img = np.array(Image.fromarray(face_img).resize((128, 128)))
        except:
            face_img = image

        return face_img



    def my_model():
        name="Lesa Mt3mlsh"
        global names_negative_list
        global negative
        global negative1
        our_images_path = '10 Shot'
        folders = os.listdir(our_images_path)
        for folder in folders:
            folder_path = os.path.join(our_images_path, folder)
            print("folder  ", folder_path)
            for filename in os.listdir(folder_path):
                negative_path = os.path.join(folder_path, filename)
                names_negative_list = np.append(names_negative_list, filename)
                image = read_our_image(negative_path)
                image = np.expand_dims(image, axis=0)
                image = np.array(image)
                image = preprocess_input(image)
                negative.append(image)

        for i in range (len(negative)):
            negative1.append(encoder.predict(negative[i]))

    def DoWork(face_img):
        negative_distance_list = []
        global names_negative_list
        global neg_list_own_images
        global neg_sum
        distances = []
        final_names_avg = []
        global negative1
        anchor = []
        anchor.append(read_Anchor(face_img))
        anchor = np.array(anchor)
        anchor = preprocess_input(anchor)
        tensor1 = encoder.predict(anchor)
        max_counter = 0

        for i in negative1:
            tensor3=i
            neg_distance = np.sum(np.square(tensor1 - tensor3), axis=-1)
            negative_distance_list = np.append(negative_distance_list, neg_distance)
            neg_prediction = np.where(neg_distance <= threshold, 0, 1)
            neg_list_own_images = np.append(neg_list_own_images, neg_prediction)
        for i in range(len(negative_distance_list)):
            neg_sum += negative_distance_list[i]
            if (i + 1) % 5 == 0:
                neg_avg = neg_sum / 5
                distances = np.append(distances, neg_avg)
                final_names_avg = np.append(final_names_avg, names_negative_list[i])
                neg_sum = 0

        min_distance_avg = min(distances)
        for i in range(len(distances)):
            if min_distance_avg == distances[i]:
                min_name = final_names_avg[i]
                break

        print(final_names_avg)
        print(distances)
        print(min_distance_avg)
        if min_distance_avg>threshold:
            return "unknown"
        print(min_name)
        return min_name



    # Initialize Haar Cascade for face detection
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    if face_cascade.empty():
        print("Error: Could not load Haar Cascade Classifier.")
        exit()

    # Initialize the camera
    cap = cv2.VideoCapture(0)

    my_model()

    # Flag to indicate if a photo has been captured
    photo_captured = False


    # Flag to indicate if a face is currently detected
    face_detected = False
    count=0
    faces_list_capturing=[]
    names_list_capturing = []
    Times_list_capturing = []
    paths_list_capturing = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        time.sleep(0.2)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        print(len(faces))
        print('-------')
        if count==0:

            faces_list_capturing=np.append(faces_list_capturing,len(faces))
            if len(faces) > 0:
                count += 1
                # Face detected
                if not face_detected:

                    for (x, y, w, h) in faces:
                            # Preprocess the detected face (resize, normalize, etc.)
                            face_img = frame[y:y+h, x:x+w]
                            student_name=DoWork(face_img)
                            # Display the result on the frame
                            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                            text_box = student_name.split("_")[0]


                            # Input string
                            input_string = text_box

                            # Use regular expression to extract non-numeric part
                            result = re.match("([a-zA-Z]+)", input_string)

                            if result:
                                extracted_string = result.group(1)
                            else:
                                extracted_string = text_box
                            cv2.putText(frame, extracted_string, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

                            # Capture a photo when a face is detected

                            photo_name = f'captured_photo_{count}.jpg'
                            cv2.imwrite(photo_name, frame)
                            if student_name=="unknown":
                                pass
                            else:
                                number = int(student_name.split("_")[1].split(".")[0])
                                if len(names_list_capturing) == 0:
                                    current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                    names_list_capturing = np.append(names_list_capturing, number)
                                    Times_list_capturing = np.append(Times_list_capturing, current_datetime)

                                    paths_list_capturing = np.append(paths_list_capturing, photo_name)
                                else:
                                    if number in names_list_capturing:
                                        pass
                                    else:
                                        names_list_capturing = np.append(names_list_capturing, number)
                                        current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                        Times_list_capturing = np.append(Times_list_capturing, current_datetime)
                                        paths_list_capturing = np.append(paths_list_capturing, photo_name)
                            photo_captured = True
                            #break
            else:
                # No face detected
                face_detected = False
        else:
            #print('hahahah')
            #print(faces_list_capturing)
            if len(faces) > 0 and faces_list_capturing[-1]==0:

                faces_list_capturing = np.append(faces_list_capturing, len(faces))
                count += 1
                # Face detected
                if not face_detected:
                    # Capture a photo when a new face is detected
                    # cv2.imwrite(f'captured_photo_{count}.jpg', frame)
                    # face_detected = True
                    for (x, y, w, h) in faces:
                        # Preprocess the detected face (resize, normalize, etc.)
                        face_img = frame[y:y + h, x:x + w]
                        student_name = DoWork(face_img)
                        # Display the result on the frame
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        text_box = student_name.split("_")[0]
                        # Input string
                        input_string = text_box

                        # Use regular expression to extract non-numeric part
                        result = re.match("([a-zA-Z]+)", input_string)

                        if result:
                            extracted_string = result.group(1)
                        else:
                            extracted_string = text_box
                        cv2.putText(frame, extracted_string, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)



                        # Capture a photo when a face is detected
                        cv2.imwrite(f'captured_photo_{count}.jpg', frame)

                        if student_name == "unknown":
                            pass
                        else:
                            number = int(student_name.split("_")[1].split(".")[0])
                            if len(names_list_capturing) == 0:
                                names_list_capturing = np.append(names_list_capturing, number)
                                current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                Times_list_capturing = np.append(Times_list_capturing, current_datetime)
                                paths_list_capturing = np.append(paths_list_capturing, photo_name)
                            else:
                                if number in names_list_capturing:
                                    pass
                                else:
                                    names_list_capturing = np.append(names_list_capturing, number)
                                    current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                    Times_list_capturing = np.append(Times_list_capturing, current_datetime)
                                    paths_list_capturing = np.append(paths_list_capturing, photo_name)
                        photo_captured = True
                        # break
            else:
                faces_list_capturing = np.append(faces_list_capturing, len(faces))
                # No face detected
                face_detected = False

        # Display the result on the frame
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Display the frame
        cv2.imshow('Face Detection', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    #print(names_list_capturing)

    SQLServerDoWork.AddStudentAttendance(names_list_capturing,Times_list_capturing)
    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

#FaceYacta()