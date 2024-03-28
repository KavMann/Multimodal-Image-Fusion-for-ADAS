import os
import cv2
import numpy as np
# import matplotlib.pyplot as plt
from vggfusion import fuse

def fuse_images(ir_folder, rgb_folder, destination_folder):
    # Get sorted list of filenames in each folder
    ir_images = sorted(os.listdir(ir_folder))
    rgb_images = sorted(os.listdir(rgb_folder))

    # Iterate over the images in both folders
    for ir_image_file, rgb_image_file in zip(ir_images, rgb_images):
        # Construct full paths for IR and RGB images
        ir_image_path = os.path.join(ir_folder, ir_image_file)
        rgb_image_path = os.path.join(rgb_folder, rgb_image_file)

        # Load images
        ir_image = cv2.imread(ir_image_path, cv2.IMREAD_GRAYSCALE)
        rgb_image = cv2.imread(rgb_image_path)

        # Fuse images
        fused_image = fuse(ir_image, rgb_image)

        # Normalize the pixel values to [0, 255]
        fused_image = (fused_image - np.min(fused_image)) / (np.max(fused_image) - np.min(fused_image)) * 255

        # Convert to unsigned 8-bit integer format
        fused_image = fused_image.astype(np.uint8)

        # Save fused image to destination folder
        fused_image_name = f"fused_{os.path.basename(ir_image_path)}"
        fused_image_path = os.path.join(destination_folder, fused_image_name)
        cv2.imwrite(fused_image_path, fused_image)
        print(f"Fused image saved at: {fused_image_path}")

        # # Display images for debugging
        # fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        # axes[0].imshow(ir_image, cmap='gray')
        # axes[0].set_title('IR Image')
        # axes[0].axis('off')
        # axes[1].imshow(rgb_image)
        # axes[1].set_title('RGB Image')
        # axes[1].axis('off')
        # axes[2].imshow(fused_image, cmap='gray')
        # axes[2].set_title('Fused Image')
        # axes[2].axis('off')
        # plt.show()

# Example usage:
for i in range(1,10):
    ir_folder = f'../images/processed/formatted/set-{i}/ir'
    rgb_folder = f'../images/processed/formatted/set-{i}/rgb'
    destination_folder = '../images/processed/formatted/set-{i}/fused'
    fuse_images(ir_folder, rgb_folder, destination_folder)