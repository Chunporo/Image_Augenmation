import imgaug.augmenters as iaa
import imageio.v2 as imageio
import os
from matplotlib import pyplot as plt
import cv2

# Define augmentation sequence
seq = iaa.Sequential([
    iaa.Fliplr(0.5),
    iaa.Crop(percent=(0, 0.1)),
    iaa.Sometimes(0.5,
        iaa.GaussianBlur(sigma=(0, 0.5))
    ),
    iaa.LinearContrast((0.75, 1.5)),
    iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05*255), per_channel=0.5),
    iaa.Multiply((0.8, 1.2), per_channel=0.2),
    iaa.Affine(
        scale={"x": (0.8, 1.2), "y": (0.8, 1.2)},
        translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)},
        rotate=(-25, 25),
        shear=(-8, 8)
    ),
    # iaa.Cartoon(blur_ksize=3, segmentation_size=1.0,
    #               saturation=2.0, edge_prevalence=1.0)
], random_order=True)

# Load input image
input_image = imageio.imread("cat.jpg")
plt.imshow(input_image)
plt.show()
# Create output directory if it doesn't exist
if not os.path.exists("output"):
    os.makedirs("output")

# Generate 10 augmented images
for i in range(20):
    # Apply augmentation sequence to input image
    output_image = seq(image=input_image)

    # Save augmented image to output directory
    cv2.imwrite(f"output/output_image_{i}.jpg", output_image)