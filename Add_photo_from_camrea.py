import os

import cv2
import tkinter as tk
from tkinter import Button
from PIL import Image, ImageTk

take_photo=False
def open_camera(id,iteration,name):
    # Open the camera
    cap = cv2.VideoCapture(0)
    photo_counter = 0

    def capture_photo():
        nonlocal photo_counter
        # Capture a frame
        ret, frame = cap.read()
        if ret:
            # Save the captured image
            cv2.imwrite(f'CameraPhotos/{name}/captured_photo{photo_counter + 1}_{id}.jpg', frame)
            print(f"Photo {photo_counter + 1} saved")
            photo_counter += 1
            # Close the Tkinter window after 5 photos
            if photo_counter >= 5:
                root.destroy()
    def show_frame():
        # Get a frame from the camera
        ret, frame = cap.read()
        if ret:
            # Convert the frame to a format Tkinter can display
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)
        lmain.after(10, show_frame)

    # Create the main window
    root = tk.Tk()
    root.title("Camera Capture")

    # Create a label to display the camera feed
    lmain = tk.Label(root)
    lmain.pack()

    # Create a button to capture the photo
    capture_button = Button(root, text="Capture Photo", command=capture_photo)
    capture_button.pack()

    # Start the camera feed
    show_frame()

    # Start the Tkinter event loop
    root.mainloop()

    # Release the camera when the window is closed
    cap.release()


# Run the function to open the camera
#open_camera(1,1,"Ahmed")


def OnClickAddFromCamera():
        #import Add_photo_from_camrea
        id = 449
        name = "Nagib Test"
        create_folder(f'CameraPhotos/{name}')
        #for i in range(1, 6):
        open_camera(id,0,name)

def create_folder(path):
        try:
            # Create the directory, including any necessary intermediate directories
            os.makedirs(path, exist_ok=True)
            print(f"Folder '{path}' created successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

#OnClickAddFromCamera()