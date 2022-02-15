from PIL import Image
import math
import numpy as np
from sympy import *

theta_deg = 60
theta_rad = theta_deg * math.pi / 180
output_dir = './outputs/'

# r = receivers, u = x casters, v = y casters
def convert_result_to_images(r, u, v):
    im1_arr = np.zeros(r.shape)
    im2_arr = np.zeros(r.shape)
    im3_arr = np.zeros(r.shape)
    
    for i in range(r.shape[0]):
        for j in range(r.shape[1]):
            im1_arr[i, j] = calculate_pixel_image1(im1_arr, r, u, i, j)
            im2_arr[i, j] = calculate_pixel_image2(im2_arr, r, u, i, j)
            im3_arr[i, j] = calculate_pixel_image3(im3_arr, r, v, i, j)

    convert_array_to_image(im1_arr, "1")
    convert_array_to_image(im2_arr, "2")
    convert_array_to_image(im3_arr, "3")
    
def calculate_pixel_image1(im1_arr, r, u, i, j):
    h = u[i, j] - r[i, j]
    shadowed_area = tan(theta_rad) * h
    im1_arr[i, j] = (1 - shadowed_area) * 255
    assert im1_arr[i, j] <= 255
    return im1_arr[i, j]

def calculate_pixel_image2(im2_arr, r, u, i, j):
    h = u[i, j + 1] - r[i, j]
    shadowed_area = tan(theta_rad) * h
    im2_arr[i, j] = (1 - shadowed_area) * 255
    assert im2_arr[i, j] <= 255
    return im2_arr[i, j]

def calculate_pixel_image3(im3_arr, r, v, i, j):
    h = v[i, j] - r[i, j]
    shadowed_area = tan(theta_rad) * h
    im3_arr[i, j] = (1 - shadowed_area) * 255
    assert im3_arr[i, j] <= 255
    return im3_arr[i, j]

def convert_array_to_image(image_arr, image_num):
    image = Image.fromarray(image_arr.astype(np.uint8))
    output_file_name = 'image' + image_num + '.png'
    image.save(output_dir + output_file_name)
    