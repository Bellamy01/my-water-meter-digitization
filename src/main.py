# # Import required packages
# import cv2
# import pytesseract
 
# # Mention the installed location of Tesseract-OCR in your system
# pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR'
 
# # Read image from which text needs to be extracted
# img = cv2.imread("E:\WORK\Y3\embedded\my-water-meter-digitization\data\input\image.png")
 
# # Preprocessing the image starts
 
# # Convert the image to gray scale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# # Performing OTSU threshold
# ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
 
# # Specify structure shape and kernel size. 
# # Kernel size increases or decreases the area 
# # of the rectangle to be detected.
# # A smaller value like (10, 10) will detect 
# # each word instead of a sentence.
# rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
 
# # Applying dilation on the threshold image
# dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
 
# # Finding contours
# contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, 
#                                                  cv2.CHAIN_APPROX_NONE)
 
# # Creating a copy of image
# im2 = img.copy()
 
# # Looping through the identified contours
# # Then rectangular part is cropped and passed on
# # to pytesseract for extracting text from it
# # Extracted text is then printed to the console
# for cnt in contours:
#     x, y, w, h = cv2.boundingRect(cnt)
     
#     # Drawing a rectangle on copied image
#     rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
     
#     # Cropping the text block for giving input to OCR
#     cropped = im2[y:y + h, x:x + w]
     
#   # Apply OCR on the cropped image
#     text = pytesseract.image_to_string(cropped)
     
#     # Print the text
#     print(text)


# Import the necessary libraries 
import cv2 
import pytesseract 
import numpy as np
 
# If you're on windows, you will need to point pytesseract to the path 
# where you installed Tesseract 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR' 

# Use OpenCV to read the image 
# replace 'test.png' with your image file 
img = cv2.imread('E:\WORK\Y3\embedded\my-water-meter-digitization\data\input\image.png') 

# Convert the image to gray scale 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# Use Gaussian blur to remove noise 
blur = cv2.GaussianBlur(gray, (5,5), 0) 

# Use adaptive thresholding to convert the image to binary 
# ADAPTIVE_THRESH_GAUSSIAN_C: threshold value is the weighted sum of 
# neighbourhood values where weights are a gaussian window. 
# BLOCK Size - It decides the size of neighbourhood area. 
# C - It is just a constant which is subtracted from the mean or weighted 
# mean calculated. 
bin_img = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
 
# Perform dilation and erosion to remove some noise 
kernel = np.ones((1, 1), np.uint8) 
img = cv2.dilate(bin_img, kernel, iterations=1) 
img = cv2.erode(img, kernel, iterations=1) 

# Use pytesseract to convert the image data to text 
text = pytesseract.image_to_string(img) 

# Print the text 
print(text)