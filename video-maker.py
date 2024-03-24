import cv2
import os

# Directory containing the images
image_folder = './Multimodal-Image-Fusion/images/processed/Original/Set-1/IR'
# Output video file name
video_name = './Multimodal-Image-Fusion/videos/set-1.mp4'


# Get the list of image files in the directory
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]

# Sort the images alphabetically
images.sort()

# Get the dimensions of the first image to set the size of the video
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

# Specify the desired frame rate (fps)
fps = 24

# Initialize the video writer object
video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width,height))

# Loop through the images and write them to the video
for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

# Release the video writer object
video.release()