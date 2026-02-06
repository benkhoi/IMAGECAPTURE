import cv2

class BilateralProcessor:
    def __init__(self):
        pass

    def apply_bilateral(self, img):
        """
        Apply Bilateral Filter (Smoothing while preserving edges)
        """
        if img is None:
            return None

        # d=9: Đường kính vùng lân cận pixel
        # sigmaColor=75: Độ lệch chuẩn màu (càng lớn càng pha trộn màu xa nhau)
        # sigmaSpace=75: Độ lệch chuẩn không gian (càng lớn càng xét pixel xa)
        return cv2.bilateralFilter(img, 9, 75, 75)