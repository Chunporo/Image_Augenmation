import imgaug.augmenters as iaa
import imageio.v2 as imageio
import os
from matplotlib import pyplot as plt
import cv2
# Define augmentation sequence
seq = iaa.Sequential([
    iaa.Crop(percent=(0, 0.1)), # crop images from each side by 0 to 16px (randomly chosen
    iaa.Fliplr(p=0.5), # flip the image horizontally
    iaa.Flipud(p=0.5), # flip the image vertically
    iaa.Affine(rotate=(-180, 180)), # rotate the image 
    iaa.GaussianBlur(sigma=(0, 3.0)), # apply gaussian blur with a sigma between 0 and 3.0
    # Strengthen or weaken the contrast in each image.
    iaa.LinearContrast((0.75, 1.5)),
    # Add gaussian noise.
    # For 50% of all images, we sample the noise once per pixel.
    # For the other 50% of all images, we sample the noise per pixel AND
    # channel. This can change the color (not only brightness) of the
    # pixels.
    iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05*255), per_channel=0.5),
    # Make some images brighter and some darker.
    # In 20% of all cases, we sample the multiplier once per channel,
    # which can end up changing the color of the images.
    iaa.Multiply((0.8, 1.2), per_channel=0.2),
    # Apply affine transformations to each image.
    # Scale/zoom them, translate/move them, rotate them and shear them.
    iaa.AdditiveGaussianNoise(scale=(0, 0.1*255)), # add gaussian noise with a scale between 0 and 0.1*255
], random_order=True)

# Load input image
input_image = imageio.imread("cat.jpg")
plt.imshow(input_image)
plt.show()
# Create output directory if it doesn't exist
if not os.path.exists("output"):
    os.makedirs("output")

# Generate 10 augmented images
for i in range(10):
    # Apply augmentation sequence to input image
    output_image = seq(image=input_image)

    # Save augmented image to output directory
    cv2.imwrite(f"output/output_image_{i}.jpg", output_image)