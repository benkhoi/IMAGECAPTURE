import cv2

class ThresholdProcessor:
    def __init__(self):
        pass

    def apply_threshold(self, img, thresh_val=127):
        """
        Apply Binary Thresholding
        """
        if img is None:
            return None

        # Thresholding thường yêu cầu ảnh đầu vào là ảnh xám
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Hàm trả về 2 giá trị: (ret, thresholded_image). Ta chỉ lấy cái thứ 2.
        _, binary_img = cv2.threshold(gray, thresh_val, 255, cv2.THRESH_BINARY)

        return binary_img