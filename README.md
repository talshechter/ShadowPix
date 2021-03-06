# ShadowPix

This is our final project in the course 3D by Amit Bermano.
We implemented the paper [ShadowPix: Multiple Images from Self Shadowing](https://www.cs.tau.ac.il/~amberman/shadowpixPaper.pdf).
We implemented algorithms that generate ShadowPix of given input images.

## Local Method

- The local method can receive up to 3 images as input.
- The method is based on creating walls that cast shadow and surfaces that receive this shadow.
- Given input images I1, I2, I3, the method computes r, u, v such that:
![Local method - equations](./attachments/local_method_equations.jpg)
- The intuition is that from each direction, the difference between the shadow casters and receivers will result in different input image.

### Example
- Input images:
![Local method - input images](./attachments/local_method_input.jpg)

- Output images:
    - (The generated images from the 3D model we computed, by lighting it from different angles)
![Local method - output images](./attachments/local_method_output.jpg)

### Run The Method
- Perform the following commands
```
cd local_method
python run_local_method.py
```
- The output images will be saved in the "outputs" directory
- In order to run over your images: Add your images to "local_images" directory, and change the name of the images in the file "run_local_method.py".

## Optimized Global Method
- Improvment of the original global method by using torch.optimizer.adam to perform the optimization.
- Can receive up to 4 images as input.
- This method is based on creating heightfield, converting it to mesh, and outputs the computed heightfield as mesh.
- In order to view the results, render the mesh and light it from different directions. (For example, using blender.)

### Example
- Input images and below the output imagesץ
    - (The generated images from the mesh we computed, by rendering the mesh in blender and lighting it from different angles)
![Global method - results](./attachments/global_method_result.jpg)

### Run The Method
- Perform the following commands
```
cd global_method
python global_method_optimized.py
```
- The output mesh will be saved in the "outputs" directory as obj file
- In order to run over your images: Add your images to "global_images" directory, and change the name of the images in the file "global_method_optimized.py".

## Global Method

- The global method can receive up to 4 images as input.
- This method is based in creating heightfield, then converting it to mesh.

### Warning
- The run time of the method is very long 
- It's not guarenteed that it will converge to good results in reasonable time.
![Global method - warning](./attachments/global_method_warning.jpg)

### Run The Method
- Perform the following commands
```
cd global_method
python global_method.py
```
- The output images will be saved in the "outputs" directory
- In order to run over your images: Add your images to "global_images" directory, and change the name of the images in the file "global_method.py".

