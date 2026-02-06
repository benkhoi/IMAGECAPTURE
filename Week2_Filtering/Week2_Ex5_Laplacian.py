import cv2
import numpy as np

class LaplacianProcessor:
    def __init__(self):
        pass

    def apply_laplacian(self, img):
        """
        Detect edges using Laplacian operator
        """
        if img is None:
            return None

        # 1. Chuyển sang ảnh xám
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 2. Áp dụng Laplacian. Dùng CV_64F để tránh mất mát dữ liệu cạnh âm
        laplacian_64f = cv2.Laplacian(gray, cv2.CV_64F)

        # 3. Chuyển về dạng ảnh hiển thị được (uint8)
        abs_laplacian = np.absolute(laplacian_64f)
        return np.uint8(abs_laplacian)