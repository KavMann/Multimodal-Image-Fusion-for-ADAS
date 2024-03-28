import cv2
import os

# Convert images to video for set 1-9
color = 'fused'
for value in range(1, 10):
    if value ==7:
        continue
    # I/O folder location
    image_folder = f'../Multimodal-Image-Fusion/images/processed/formatted/set-{value}/{color}'
    video_name = f'../Multimodal-Image-Fusion/videos/fused-videos/set-{value}.mp4'

    # Extract the directory path from video_name
    video_directory = os.path.dirname(video_name)

    try:
        os.makedirs(video_directory, exist_ok=True)
        print(f"Directory '{video_directory}' created successfully or already exists.")
    except OSError as e:
        print(f"Error creating directory '{video_directory}': {e}")

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
    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    # Loop through the images and write them to the video
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    # Release the video writer object
    video.release()
