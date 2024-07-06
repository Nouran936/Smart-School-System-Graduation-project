import cv2

def Display_Video(path):
    folder= f"Violence_Incidences\{path}"
    cap = cv2.VideoCapture(folder)
    if not cap.isOpened():
        print("Error: Couldn't open the video file.")
        exit()
    while cap.isOpened():
        ret, frame = cap.read()

        # If 'ret' is False, it means the video has ended
        if not ret:
            break

        # Display the frame
        cv2.imshow('Video', frame)

        # Check for 'q' key to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()
    #print(folder)


#Display_Video("2024-04-14 20_58_32.mp4")