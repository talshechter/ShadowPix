import numpy as np
import cv2
from scipy.signal import convolve2d
from image_utils import load_global_images

w_g=1.5
w_s=0.001
OPTIMIZATION_STEPS = 10000000
SIZE=50


class GlobalMethod:
    def __init__(self, images, size, radius=10):
        self.size = size
        self.images = images
        self.radius = radius
        self.w_g = w_g
        self.w_s = w_s
        self.temp = 1
        self.temp_diff = self.temp / (OPTIMIZATION_STEPS)
        self.heightfield = np.zeros([self.size, self.size])
        self.binary_images = np.ones([4, size, size])
        self.loss = np.inf
        self.gp_images = np.asarray([self.g_conv(self.p_conv(image)) for image in self.images])

    def calculate_loss(self, binary_images):
        loss = 0
        for i in range(4):
            current_binary_image = binary_images[i]
            p_image = self.p_conv(current_binary_image)
            gp_image = self.g_conv(p_image)
            loss+= self.mse(p_image, self.images[i])
            loss+= self.w_g * self.mse(gp_image, self.gp_images[i])
        loss += 0 #self.w_s * self.mse(g_conv(self.heightfield), np.zeros(self.heightfield.shape))
        return loss
      
    def g_conv(self, image, kernel_size=3):
        kx = np.asarray([[1,0,-1],[2,0,-2],[1,0,-1]])
        ky = np.asarray([[1,2,1] ,[0,0,0], [-1,-2,-1]])
        conv_x = convolve2d(image, kx, mode='same')
        conv_y = convolve2d(image, ky, mode='same')
        return np.sqrt(np.power(conv_x, 2), np.power(conv_y, 2))

    def p_conv(self, image):
        return cv2.blur(image, (3, 3))

    def mse(self, a, b):
      return np.sum((a-b)**2)

    def optimize_simulate_anealing(self):
        loss_trace = []
        for i in range(OPTIMIZATION_STEPS):
            row = np.random.randint(0, self.size)
            col = np.random.randint(0, self.size)
            height_change = np.random.randint(-5, 6)
            self.heightfield[row, col] += height_change
            binary_images = self.calculate_images_from_heightfield()
            new_loss = self.calculate_loss(binary_images)
            loss_diff = self.loss - new_loss
            if loss_diff > 0 or (np.random.random() < np.e ** (loss_diff / self.temp)):
                self.loss = new_loss
                self.binary_images = binary_images
                self.temp -= self.temp_diff
            else:
                self.heightfield[row, col] -= height_change
            if i %100==0:
                loss_trace.append(self.loss)
        with open('global_loss_trace.txt', 'w') as f:
            f.write(str(loss_trace))
   
    def calculate_images_from_heightfield(self):
        images = []
        tmp_heightfield = self.heightfield
        for i in range(4):
            for j in range(i):
                tmp_heightfield = np.rot90(tmp_heightfield)
            image = self.heightfield_to_image(tmp_heightfield)
            images.append(image)
        return np.asarray(images)

    def heightfield_to_image(self, heightfield):
        image = np.zeros((self.size, self.size))
        for j in range(self.size):
            max_effective_shaddow_on_j = np.full((1, self.size), -np.inf)
            for k in range(1, self.radius+1):
                if j+k >= self.size:
                    break
                pixel_effective_shaddow_on_j = heightfield[:, j+k] - k
                max_effective_shaddow_on_j = np.maximum(pixel_effective_shaddow_on_j, max_effective_shaddow_on_j)
                image[:, j] = np.clip(max_effective_shaddow_on_j - heightfield[:, j], 0, 1)
        return image

def main():
    paths = ["global_images/img1.jpg", "global_images/img2.jpg", "global_images/img3.jpg", "global_images/img4.jpg"]
    images = load_global_images(paths, SIZE)
    global_method = GlobalMethod(images, SIZE)
    global_method.optimize_simulate_anealing()
    for i, image in enumerate(global_method.binary_images):
        cv2.imwrite(f"im_{i}.png", image)


if __name__ == '__main__':
    main()