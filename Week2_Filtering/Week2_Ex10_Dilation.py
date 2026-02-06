import cv2
import numpy as np

class DilationProcessor:
    def __init__(self):
        pass

    def apply_dilation(self, img, kernel_size=5):
        """
        Apply Morphological Dilation (thường dùng để lấp đầy lỗ đen nhỏ)
        """
        if img is None:
            return None

        # Tạo kernel hình vuông
        kernel = np.ones((kernel_size, kernel_size), np.uint8)

        # Thực hiện giãn nở
        return cv2.dilate(img, kernel, iterations=1)