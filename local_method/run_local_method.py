from local_method import *
from local_results_to_images_converter import convert_result_to_images

def run():
    print("Running local method...")
    img1_path = 'local_images/final-im1.jpg'
    img2_path =  'local_images/final-im2.jpg'
    img3_path = 'local_images/final-im3.jpg'
    r, u, v = main_local_method(img1_path, img2_path, img3_path)
    print("Finished running the algorithm, converting results to images")
    convert_result_to_images(r, u, v)
    print("Done. Output images saved in \"outputs\" directory")
    
if __name__ == '__main__':
    run()