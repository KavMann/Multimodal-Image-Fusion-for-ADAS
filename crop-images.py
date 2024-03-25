from PIL import Image
import os

# Give set=1-9 and color=RGB/IR
#Resize images
def resize_img(desired_width_rgb,desired_height_rgb,value,color):
    # Path to the directory for RGB
    input_folder = f'../images/processed/Original/Set-{value}/{color}'
    output_folder = f'../images/processed/formatted/set-{value}/{color}'
    try:
        os.makedirs(output_folder)
    except FileExistsError:
        pass

    for filename in os.listdir(input_folder):
        # Check if the file is an image
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Open the image file
            with Image.open(os.path.join(input_folder, filename)) as img:
                # Resize the image while maintaining the aspect ratio
                img.resize((desired_width_rgb, desired_height_rgb))
                # Save the resized image to the output folder
                img.save(os.path.join(output_folder, filename))

    print("Images resized and saved successfully.")

def crop_img(top, bottom, left, right, value, color):
    # Path to the directory containing the images
    input_folder_crop = f'../images/processed/Original/Set-{value}/{color}'
    output_folder_crop = f'../images/processed/formatted/set-{value}/{color}'
    try:
        os.makedirs(output_folder_crop)
    except FileExistsError:
        pass
    
    # Define crop margins (top, bottom, left, right)
    crop_margins = (top, bottom, left, right)
    # Loop through all the files in the input folder
    for filename in os.listdir(input_folder_crop):
        # Check if the file is an image
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Open the image file
            with Image.open(os.path.join(input_folder_crop, filename)) as img:
                # Crop the image using the specified margins
                cropped_img = img.crop((crop_margins[2], crop_margins[0], img.width - crop_margins[3], img.height - crop_margins[1]))
                # Save the cropped image to the output folder
                cropped_img.save(os.path.join(output_folder_crop, filename))

    print("Images cropped and saved successfully.")

# Now run both functions to make sure the images overlap on one another and are of same dimentions. Results added to formatted file for training

