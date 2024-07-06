import os
import shutil
import tkinter as tk
from tkinter import filedialog

def select_and_save_image(destination_folder, iteration, id):
    # Create a root window and hide it
    root = tk.Tk()
    root.withdraw()

    # Open file dialog to select an image
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")]
    )

    # Check if a file was selected
    if file_path:
        # Get the file extension
        _, file_extension = os.path.splitext(file_path)

        # Create the new filename
        new_file_name = f"Photo{iteration}_{id}{file_extension}"

        # Ensure the destination folder exists
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Create the destination path
        destination_path = os.path.join(destination_folder, new_file_name)

        # Copy the selected image to the destination folder with the new name
        shutil.copy(file_path, destination_path)

        print(f"Image saved to {destination_path}")
    else:
        print("No file selected")

# Example usage:
# select_and_save_image("CameraPhotos/JohnDoe", 1, "12345")
