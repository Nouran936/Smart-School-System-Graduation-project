from tensorflow.keras.models import load_model


def DetectYacta():
    import pygame
    import cv2
    import numpy as np
    import time
    import datetime
    import numpy as np
    import os
    import Copy_Video
    # Specify the height and width to which each video frame will be resized in our dataset.
    IMAGE_HEIGHT , IMAGE_WIDTH = 224, 224
    SEQUENCE_LENGTH = 40
    CLASSES_LIST = ["NonViolence", "Violence"]
    MoBiLSTM_model = load_model('loss 1646.h5')
    # Viomodels/Densenet121 msh run kamel.h5
    # test_videos_directory = 'test_videos'
    # os.makedirs(test_videos_directory, exist_ok=True)
    # output_video_file_path = f'{test_videos_directory}/Output-Test-Video.mp4'

    def predict_video(video_file_path):

        output_directory_vio = f'Violence_Incidences'
        os.makedirs(output_directory, exist_ok=True)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        output_filename_new = os.path.join(output_directory_vio, current_datetime)
        #video_file_path='t1'
        video_reader = cv2.VideoCapture(video_file_path)
        #print(video_reader)
        print(video_file_path)
        print("In Model")

        # Get the width and height of the video.
        original_video_width = int(video_reader.get(cv2.CAP_PROP_FRAME_WIDTH))
        original_video_height = int(video_reader.get(cv2.CAP_PROP_FRAME_HEIGHT))
        #print(original_video_height)
        #print(original_video_width)
        # Declare a list to store video frames we will extract.
        frames_list = []

        # Store the predicted class in the video.
        predicted_class_name = ''

        # Get the number of frames in the video.
        video_frames_count = int(video_reader.get(cv2.CAP_PROP_FRAME_COUNT))
        #print(video_frames_count)
        # Calculate the interval after which frames will be added to the list.
        skip_frames_window = max(int(video_frames_count / SEQUENCE_LENGTH), 1)

        # Iterating the number of times equal to the fixed length of sequence.
        for frame_counter in range(SEQUENCE_LENGTH):

            # Set the current frame position of the video.
            video_reader.set(cv2.CAP_PROP_POS_FRAMES, frame_counter * skip_frames_window)

            success, frame = video_reader.read()
            #print(frame)
            if not success:
                print("break")
                break

            # Resize the Frame to fixed Dimensions.
            resized_frame = cv2.resize(frame, (IMAGE_HEIGHT, IMAGE_WIDTH))

            # Normalize the resized frame.
            normalized_frame = resized_frame / 255

            # Appending the pre-processed frame into the frames list
            frames_list.append(normalized_frame)

        #print(frames_list)
        # Passing the  pre-processed frames to the model and get the predicted probabilities.
        print(np.shape(np.expand_dims(frames_list, axis=0)))
        predicted_labels_probabilities = MoBiLSTM_model.predict(np.expand_dims(frames_list, axis=0))[0]

        # Get the index of class with highest probability.
        predicted_label = np.argmax(predicted_labels_probabilities)

        # Get the class name using the retrieved index.
        predicted_class_name = CLASSES_LIST[predicted_label]
        if predicted_class_name=="Violence":
            pygame.mixer.init()
            pygame.mixer.music.load("blinking-bell-loop-39522.mp3")
            pygame.mixer.music.play()
            # Wait until the music finishes playing
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(20)  # Adjust the number as needed

            # Clean up the mixer when finished
            pygame.mixer.quit()
            Copy_Video.copy_video_to_folder(video_file_path,output_directory_vio,f"{current_datetime}.mp4",current_datetime)

        #else:
            # pygame.mixer.init()
            # pygame.mixer.music.load("NonVio.mp3")
            # pygame.mixer.music.play()
            # # Wait until the music finishes playing
            # while pygame.mixer.music.get_busy():
            #     pygame.time.Clock().tick(20)  # Adjust the number as needed
            #
            # # Clean up the mixer when finished
            # pygame.mixer.quit()

            #playsound('E:/كلية/iot/Testtt/20_3_Try/NonVio.wav')

        # Display the predicted class along with the prediction confidence.
        print(f'Predicted: {predicted_class_name}\nConfidence: {predicted_labels_probabilities[predicted_label]}')
        #print(start_time_Model-time.time())
        video_reader.release()



    # Initialize the camera
    #url= 'http://192.168.1.159:8080/video'
    #cap = cv2.VideoCapture(url)
    cap = cv2.VideoCapture(0)

    output_directory = 'my_videos'
    os.makedirs(output_directory, exist_ok=True)

    # Define the codec
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'XVID' for AVI format
    working= True
    try:
        while True:
            # Define the start time for the 5-second interval
            start_time = time.time()

            # Create a unique timestamp for the video file
            #timestamp = time.strftime("%Y%m%d_%H%M%S")

            # Define the output filename for the video
            output_filename = os.path.join(output_directory, f"video_1.mp4")

            # Create VideoWriter object for the current 5-second interval
            out = cv2.VideoWriter(output_filename, fourcc, 20.0, (640, 480))  # Adjust width and height if needed

            # Capture and write frames for 3 seconds
            while (time.time() - start_time) < 5:
                ret, frame = cap.read()
                if not ret:
                    print("Failed to capture frame.")
                    break

                out.write(frame)
                cv2.imshow('Live Video', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    working=False
                    break
            # Release the VideoWriter for the current 5-second interval
            out.release()
            #cv2.destroyAllWindows()
            if not working:
                return
                break
            # Process the video file through your model
            start_time_model = time.time()
            #output_filename=r"my_videos/2024-04-16 12_45_09.mp4"

            predict_video(output_filename)
            end_time_model = time.time()
            print(f"Time taken by the model prediction: {end_time_model - start_time_model} seconds")

    except KeyboardInterrupt:
        # Release the camera if the user interrupts the program
        cap.release()










#DetectYacta()
