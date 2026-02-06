import cv2
import numpy as np

class SharpenProcessor:
    def __init__(self):
        pass

    def apply_sharpen(self, img):
        """
        Sharpen image using a custom kernel
        """
        if img is None:
            return None

        # Định nghĩa kernel làm sắc nét (tăng cường trung tâm, giảm xung quanh)
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])

        # Áp dụng bộ lọc 2D
        return cv2.filter2D(img, -1, kernel)