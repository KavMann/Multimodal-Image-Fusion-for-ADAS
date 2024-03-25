from PIL import Image
import os

# Path to the directory containing the images
input_folder_rgb = '/content/Set-1/RGB'
# Path to the directory where resized images will be saved
output_folder_rgb = '/content/Fusion-Results/Resize-RGB'
# Desired width and height for the resized images
desired_width_rgb = 436
desired_height_rgb = 520

for filename in os.listdir(input_folder):
    # Check if the file is an image
    if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
        # Open the image file
        with Image.open(os.path.join(input_folder, filename)) as img:
            # Resize the image while maintaining the aspect ratio
            img.thumbnail((desired_width, desired_height))
            # Save the resized image to the output folder
            img.save(os.path.join(output_folder, filename))

print("RGB images resized and saved successfully.")

# Path to the directory containing the images
input_folder_ir = '/content/Images/IR'
# Path to the directory where resized images will be saved
output_folder_ir = '/content/Fusion-Results/Resize-IR'
# Desired width and height for the resized images
desired_width_ir = 440
desired_height_ir = 350

for filename in os.listdir(input_folder):
    # Check if the file is an image
    if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
        # Open the image file
        with Image.open(os.path.join(input_folder, filename)) as img:
            # Resize the image while maintaining the aspect ratio
            img.thumbnail((desired_width, desired_height))
            # Save the resized image to the output folder
            img.save(os.path.join(output_folder, filename))

print("Images resized and saved successfully.")

# Path to the directory containing the images
input_folder = '/content/Fusion-Results/Resize-RGB'
# Path to the directory where cropped images will be saved
output_folder = '/content/Fusion-Results/Cropped-RGB'
# Define crop margins (top, bottom, left, right)
crop_margins = (21, 59, 32, 54)

# Loop through all the files in the input folder
for filename in os.listdir(input_folder):
    # Check if the file is an image
    if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
        # Open the image file
        with Image.open(os.path.join(input_folder, filename)) as img:
            # Crop the image using the specified margins
            cropped_img = img.crop((crop_margins[2], crop_margins[0], img.width - crop_margins[3], img.height - crop_margins[1]))
            # Save the cropped image to the output folder
            cropped_img.save(os.path.join(output_folder, filename))

print("Images cropped and saved successfully.")

