import cv2
import numpy as np

class ErosionProcessor:
    def __init__(self):
        pass

    def apply_erosion(self, img, kernel_size=5):
        """
        Apply Morphological Erosion (thường dùng để loại bỏ nhiễu trắng nhỏ)
        """
        if img is None:
            return None

        # Tạo kernel (structuring element) hình vuông toàn số 1
        kernel = np.ones((kernel_size, kernel_size), np.uint8)

        # Thực hiện bào mòn (iterations=1 là làm 1 lần)
        return cv2.erode(img, kernel, iterations=1)