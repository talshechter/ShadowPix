import numpy as np
import math
import cv2

def local_method(img1: np.ndarray, img2: np.ndarray, img3: np.ndarray, size=50, tetha = 60):  
    """Implementation of the local method algorithm."""
    u = np.zeros((size, size+1))
    v = np.zeros((size, size))
    r = np.zeros((size, size))
    rad_tetha = math.radians(tetha)
    s = 1 / math.tan(rad_tetha)
    for col in range(size):
        for row in range(size):
        # equation (2) in the paper
            u[row, col+1] = u[row, col] + s*(img2[row, col] - img1[row, col])

    for row in range(size-1):
        max_diff = 0
        for col in range(size-1):
        # equation (3) in the paper.
            diff_satisfy_condition_i = u[row][col] + s * (img1[row, col] + img1[row+1, col] - img3[row+1, col]) - u[row+1, col]
            if max_diff < diff_satisfy_condition_i:
                max_diff = diff_satisfy_condition_i
        u[row+1, :] += max_diff
    # get r, v from u based on equations (1) in the paper.
    r = u[:, : size] - s * img1
    v = r + s * img3
    return r, u, v


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


def main_local_method(img1_path, img2_path, img3_path):
    size = 50
    img1, img2, img3 = load_images(img1_path, img2_path, img3_path, size)
    r, u, v = local_method(img1, img2, img3)
    return r, u, v

if __name__ == '__main__':
    img1_path = 'local_images/final-im1.jpg'
    img2_path =  'local_images/final-im2.jpg'
    img3_path = 'local_images/final-im3.jpg'
    main_local_method(img1_path, img2_path, img3_path)
