import cv2
import numpy as np

class SobelXProcessor:
    def __init__(self):
        pass

    def apply_sobel_x(self, img):
        """
        Detect vertical edges using Sobel X
        """
        if img is None:
            return None

        # 1. Chuyển sang ảnh xám để tính toán gradient tốt hơn
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 2. Tính Sobel X. Dùng CV_64F để giữ giá trị âm (đạo hàm âm)
        sobelx_64f = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)

        # 3. Chuyển giá trị tuyệt đối và về lại dạng unsigned 8-bit để hiển thị
        abs_sobelx = np.absolute(sobelx_64f)
        sobelx_8u = np.uint8(abs_sobelx)

        return sobelx_8u