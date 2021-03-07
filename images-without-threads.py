import cv2
import time


# Very heavy and inefficient work
def work(name_image):
    image = cv2.imread(name_image)

    for x in range(3447):
        for y in range(5170):
            pixel = image[x, y]
            pixel_x = 0 if pixel[0] > 50 else 255
            pixel_y = 0 if pixel[1] > 100 else 255
            pixel_z = 0 if pixel[2] > 150 else 255
            image[x, y] = (pixel_x, pixel_y, pixel_z)

    return image


if __name__ == "__main__":
    names = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg"]

    start_time = time.time()

    image_1 = work(names[0])
    image_2 = work(names[1])
    image_3 = work(names[2])
    image_4 = work(names[3])

    end_time = time.time()

    print(f'T = {end_time - start_time}')
