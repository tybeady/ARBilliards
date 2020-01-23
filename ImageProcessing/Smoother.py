import cv2
import numpy as np

def Smooth(im):

    # smooth the image with alternative closing and opening
    # with an enlarging kernel
    morph = im.copy()

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
    morph = cv2.morphologyEx(morph, cv2.MORPH_CLOSE, kernel)
    morph = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))

    # take morphological gradient
    gradient_image = cv2.morphologyEx(morph, cv2.MORPH_GRADIENT, kernel)

    # split the gradient image into channels
    image_channels = np.split(np.asarray(gradient_image), 3, axis=2)

    channel_height, channel_width, _ = image_channels[0].shape

    # apply Otsu threshold to each channel
    for i in range(0, 3):
        _, image_channels[i] = cv2.threshold(~image_channels[i], 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
        image_channels[i] = np.reshape(image_channels[i], newshape=(channel_height, channel_width, 1))

    # merge the channels
    image_channels = np.concatenate((image_channels[0], image_channels[1], image_channels[2]), axis=2)

    # save the denoised image
    return image_channels


def Edges(im):

    grey_image = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    kernel_size = 3
    blur_gray = cv2.GaussianBlur(grey_image,(kernel_size, kernel_size),0)
    low_threshold = 50
    high_threshold = 125
    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)
    return edges
