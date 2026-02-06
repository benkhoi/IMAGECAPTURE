import cv2

class MedianProcessor:
    def __init__(self):
        pass

    def apply_median_filter(self, img, kernel_size=5):
        """
        Apply Median filtering to reduce salt-and-pepper noise
        """
        if img is None:
            return None
        
        # kernel_size phải là số lẻ (3, 5, 7...)
        return cv2.medianBlur(img, kernel_size)

    