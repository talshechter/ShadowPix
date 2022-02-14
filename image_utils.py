import cv2
import numpy as np
import math

def load_global_images(images_paths, size):
    images = []
    for path in images_paths:
        image = cv2.imread(path)
        image = preprocess_image(image, size)
        images.append(image)
    return images

def load_images(img1_path, img2_path, img3_path, size):
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)
    img3 = cv2.imread(img3_path)
    img1 = preprocess_image(img1, size)
    img2 = preprocess_image(img2, size)
    img3 = preprocess_image(img3, size)
    return img1, img2, img3


def preprocess_image(img: np.ndarray, size) -> np.ndarray:
    """Preprocess the input image to fit the algorithm expected input:
        1. crop the image to symetrics shape.
        2. rescale to size*size pixels.
        3. change image to gray scale in range [0, 1].
    """
    height = img.shape[0]
    width = img.shape[1]
    crop_size = abs((height - width)/2)
    if height > width:
        img = img[math.ceil(crop_size):-math.floor(crop_size), :]
    if width > height:
        img = img[:, math.ceil(crop_size):-math.floor(crop_size)]
    new_image = cv2.resize(img, (size, size))
    gray_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
    return gray_image/255  # pixel value is between [0,1]