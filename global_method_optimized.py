from image_utils import load_global_images
import torch
import numpy as np

def heightfield_to_image_init(image_size, radius):
    """wrapper for the heighfield to image function."""
    def heightfield_to_image(heightfield):
        """calculates the effective shaddow on every pixel and converts the heightfield to image."""
        image = torch.zeros((image_size, image_size))
        for i in range(image_size):
            for j in range(image_size):
                max_effective_shaddow_on_j = 0
                for k in range(1, radius+1):
                    if j+k >= image_size:
                        break
                    pixel_effective_shaddow_on_j = heightfield[i, j+k] - k
                    if pixel_effective_shaddow_on_j > max_effective_shaddow_on_j:
                        max_effective_shaddow_on_j = pixel_effective_shaddow_on_j
                image[i, j] = max_effective_shaddow_on_j - heightfield[i, j]
        return image
    return heightfield_to_image


def compute_loss(images, heightfield, heightfield_to_image):
    loss = 0
    for i in range(4):
        current_image = images[i, :, :]
        tmp_heightfield = heightfield
        for j in range(i):
            tmp_heightfield = torch.rot90(tmp_heightfield)
        result_image = heightfield_to_image(tmp_heightfield)
        loss += torch.nn.MSELoss()(result_image, current_image)
    return loss


def main():
    img1_path = 'global_images/img1.jpg'
    img2_path = 'global_images/img2.png'
    img3_path = 'global_images/img3.png'
    img4_path = 'global_images/img4.png'
    size = 50
    radius = 10
    num_iterations = 1000
    images = load_global_images([img1_path, img2_path, img3_path, img4_path], size)
    device=torch.device('cpu')
    tensor_images = torch.stack([torch.from_numpy(image).to(device) for image in images]).float()
    tensor_images.requires_grad = False
    heightfield = torch.rand([size, size], requires_grad=True, device=device).float()
    optimizer = torch.optim.Adam([heightfield], lr=0.001)
    loss_trace = []
    heightfield_to_image = heightfield_to_image_init(size, radius)
    loss_trace = []
    for i in range(num_iterations):
        optimizer.zero_grad()
        loss = compute_loss(tensor_images, heightfield, heightfield_to_image)
        loss.backward()
        optimizer.step()
        if i%100==0:
            loss_trace.append(loss)
            print(loss)
    print(loss_trace)


if __name__ == '__main__':
    main()