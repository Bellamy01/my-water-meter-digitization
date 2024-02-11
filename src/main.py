import cv2
import pytesseract

# Set Tesseract path (adjust if needed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract-OCR\tesseract.exe'

# Read image
img = cv2.imread("E:\WORK\Y3\embedded\my-water-meter-digitization\src\sample.jpg")

# Preprocessing (adjust based on image characteristics)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)  # Optional noise reduction

# Adaptive thresholding for uneven lighting (consider alternatives if needed)
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                              cv2.THRESH_BINARY_INV, 11, 2)

# Find contours of potential text regions
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop through contours and apply OCR
for cnt in contours:
    # Filter contours based on area, aspect ratio, etc. (optional)
    x, y, w, h = cv2.boundingRect(cnt)
    ratio = w / h  # Adjust threshold for your image

    if 2 <= ratio <= 5 and 30 <= w <= 200:  # Example filtering conditions
        cropped = img[y:y + h, x:x + w]

        # Apply additional pre-processing if needed (e.g., deskewing)
        text = pytesseract.image_to_string(cropped, config='--psm 10')  # Use Tesseract config options

        print(text)

# Display processed image (optional)
cv2.imshow("Processed Image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
