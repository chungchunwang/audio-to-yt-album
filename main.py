# Importing required libraries
from moviepy.editor import *
from pydub import AudioSegment
import os
import tkinter as tk
from tkinter import filedialog

# Function to create video from audio and image


def create_video(audio_path, image_path, output_path):
    # Get audio duration
    audio = AudioSegment.from_file(audio_path, format="m4a")
    duration = len(audio) / 1000.0  # Convert to seconds

    # Load image and set the duration
    img_clip = ImageSequenceClip([image_path], fps=24)
    img_clip = img_clip.set_duration(duration)

    # Load audio
    audio = AudioFileClip(audio_path)

    # Set audio to video
    video = img_clip.set_audio(audio)

    # Write to file
    video.write_videofile(output_path, codec="libx264")






# Function to open file dialog and get file path
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

# Function to trigger video creation
# Updated function to trigger video creation with output folder
def generate_videos():
    audio_folder = folder_entry.get()
    album_cover = file_entry.get()
    output_folder = output_folder_entry.get()
    
    for filename in os.listdir(audio_folder):
        if filename.endswith(".m4a"):
            audio_file_path = os.path.join(audio_folder, filename)
            output_video_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.mp4")
            create_video(audio_file_path, album_cover, output_video_path)
    
    status_label.config(text="Video(s) generated successfully.")

# Initialize Tkinter window (continued from previous code)
root = tk.Tk()
root.title("Audio to Video Converter")

# Audio Folder selection
folder_label = tk.Label(root, text="Select Audio Folder:")
folder_label.pack()
folder_entry = tk.Entry(root, width=50)
folder_entry.pack()
# Function to open directory dialog and get folder path for audio folder
def browse_audio_folder():
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)
folder_button = tk.Button(root, text="Browse", command=browse_audio_folder)
folder_button.pack()

# Album Cover File selection
file_label = tk.Label(root, text="Select Album Cover:")
file_label.pack()
file_entry = tk.Entry(root, width=50)
file_entry.pack()
file_button = tk.Button(root, text="Browse", command=browse_file)
file_button.pack()

# Output Folder selection
output_folder_label = tk.Label(root, text="Select Output Folder:")
output_folder_label.pack()
output_folder_entry = tk.Entry(root, width=50)
output_folder_entry.pack()
# Function to open directory dialog and get folder path for output folder
def browse_output_folder():
    folder_path = filedialog.askdirectory()
    output_folder_entry.delete(0, tk.END)
    output_folder_entry.insert(0, folder_path)
output_folder_button = tk.Button(root, text="Browse", command=browse_output_folder)
output_folder_button.pack()

# Generate button
generate_button = tk.Button(root, text="Generate Video(s)", command=generate_videos)
generate_button.pack()

# Status label
status_label = tk.Label(root, text="")
status_label.pack()

# Run the Tkinter event loop
root.mainloop()




# Directory where .m4a files are stored
# audio_folder = "/path/to/audio/folder"

# # Path to the album cover image
# album_cover = "/path/to/album_cover.jpg"

# # Loop through the files in the directory
# for filename in os.listdir(audio_folder):
#     if filename.endswith(".m4a"):
#         audio_file_path = os.path.join(audio_folder, filename)

#         # Define the output video path
#         output_video_path = os.path.join(
#             audio_folder, f"{os.path.splitext(filename)[0]}.mp4")

#         # Create video
#         create_video(audio_file_path, album_cover, output_video_path)

