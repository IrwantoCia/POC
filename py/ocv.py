import cv2
import numpy as np
import pytesseract

def ocr(image):
    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(image)
    
    # Return the recognized text
    return text

def clear_bank_statement(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply adaptive thresholding to obtain a binary image
    _, threshold = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Perform morphological operations to remove noise and enhance text
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opening = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel, iterations=1)
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    
    # Create a marker image for watershed algorithm
    #dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    #_, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
    #sure_fg = np.uint8(sure_fg)
    
    # Subtract the foreground from the background to obtain the markers
    #unknown = cv2.subtract(sure_bg, sure_fg)
    
    # Apply the watershed algorithm to segment the image
    #_, markers = cv2.connectedComponents(sure_fg)
    #markers += 1
    #markers[unknown == 255] = 0
    #markers = cv2.watershed(image, markers)
    
    # Apply color map to the segmented regions
    #image[markers == -1] = [255, 255, 255]
    
    # Return the cleared image in grayscale
    return opening

def show_image(image):
    resize_image = cv2.resize(image, (1080, 720))                # Resize image
    cv2.imshow('image', resize_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = 'bank.jpg'

image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

k = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], np.uint8)
closing = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, k)
k1 = np.ones((3, 3), np.uint8)
erosion = cv2.erode(closing, k1, iterations = 1)

#dist = cv2.distanceTransform(threshold, cv2.DIST_L2, 5)
#dist = cv2.normalize(dist, dist, 0, 1.0, cv2.NORM_MINMAX)
#dist = (dist * 255).astype("uint8")
#dist = cv2.threshold(dist, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]


show_image(erosion)






