import shutil
import os
import SQLServerDoWork

def generate_valid_filename(filename):
    # Replace invalid characters with underscores
    valid_chars = "-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(c if c in valid_chars else '_' for c in filename)


def copy_video_to_folder(video_path, destination_folder, new_filename,time):
    # Check if the source video exists
    if not os.path.exists(video_path):
        print(f"Error: The video file '{video_path}' does not exist.")
        return

    # Check if the destination folder exists, if not, create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    try:
        # Generate a valid filename for the destination file
        new_filename = generate_valid_filename(new_filename)
        SQLServerDoWork.Add_Violence_Incidences(time,new_filename)
        # Build the destination path with the new filename
        destination_path = os.path.join(destination_folder, new_filename)

        # Copy the video file to the destination folder with the new filename
        shutil.copyfile(video_path, destination_path)

        print(f"Video '{video_path}' copied to '{destination_folder}' as '{new_filename}' successfully.")
    except Exception as e:
        print(f"Error: {e}")


# Example usage:
# source_video_path = "my_videos/video_1.mp4"
# destination_folder = "Violence_Incidences"
# new_filename = "2024-04-14 20:46:55.mp4"
# copy_video_to_folder(source_video_path, destination_folder, new_filename)



    
