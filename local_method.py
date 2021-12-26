from image_utils import *
import numpy as np
import math

def local_method(img1: np.ndarray, img2: np.ndarray, img3: np.ndarray, tetha = 60, size=50):  
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


def main():
    img1_path = 'images/img1.jpg'
    img2_path =  'images/img2.jpg'
    img3_path = 'images/img3.jpg'
    size = 50
    output_file = "output"
    img1, img2, img3 = load_images(img1_path, img2_path, img3_path, size)
    r, u, v = local_method(img1, img2, img3)


if __name__ == '__main__':
    sys.exit(main())
