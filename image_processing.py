
import cv2
import numpy as np

def create_bounding_box(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([15, 100, 100])
    upper_yellow = np.array([45, 255, 255])
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    contours, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(image, [box], 0, (0, 255, 0), 3)
        length = max(rect[1])/10
        width = min(rect[1])/10
    return length, width

def calculate_complexity(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    contours, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    total_complexity = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        total_complexity += area
    return total_complexity

def classify_complexity(complexity):
    if complexity <= 100:
        return "Low"
    elif 100 <= complexity < 250:
        return "Medium"
    else:
        return "High"

def calculate_image_metrics(image_path):
    image = cv2.imread(image_path)
    length, width = create_bounding_box(image)
    area = length * width
    complexity = calculate_complexity(image)
    shape = width / length
    return length, width, area, shape, complexity
