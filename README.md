# Architectural Design Optimization Tool - Image Processing Pipeline for Classifying Building Layouts

## Overview

This project is an image processing pipeline designed to accurately classify bitmap images of building layouts by extracting key features. It is a web-based application built with Flask that allows users to upload an image of a yellow bit map, which is then processed to calculate several key metrics, including:

- **Length** (in cm)
- **Width** (in cm)
- **Area** (in cm²)
- **Shape Ratio** (Width/Length)
- **Complexity**

The processed image and its metrics are displayed back to the user in a visually appealing user interface.

## Features
- **Feature Extraction:** Extracts key features from building layout images using image processing techniques.
- **Color Thresholding:** Identifies key regions in the layout by segmenting the image based on color intensity.
- **Vertex Counting:** Determines the complexity of building layouts by counting the number of significant vertices.
- **Contour Detection:** Detects and analyzes the shapes and structures within the building layout.
- **K-means Clustering:** Groups layouts into similar families based on extracted features, allowing for efficient classification.

![image](https://github.com/user-attachments/assets/e0e38089-a3d9-4124-b3ff-62ee7626ad9d)

---

## Demo Video

Here’s a video demonstration of how the tool works:



https://github.com/user-attachments/assets/fdf83bba-f5f9-4dfc-a8c2-8a335d6ab055

)

---

## Features

- Upload images directly through the web interface.
- Process the image to extract metrics related to the object's shape and dimensions.
- Display processed images alongside their metrics.
- Responsive design, working across desktop and mobile devices.
  
## Technologies Used

- **Python (Flask)**: For the web server and backend logic.
- **OpenCV**: For image processing and yellow object detection.
- **HTML/CSS**: For the frontend, including a modern and responsive UI.

## Future Improvements

- Implement deep learning-based classification for improved accuracy.

- Add support for additional feature extraction methods.

- Optimize performance for large-scale datasets.

---

## Workflow

### Image Preprocessing:

- Convert the image to grayscale.

- Apply Gaussian blurring to reduce noise.

- Use adaptive thresholding to highlight key structures.

### Feature Extraction:

- Detect contours and extract their properties.

- Count vertices using polygon approximation.

- Perform color segmentation to identify key regions.

### Clustering & Classification:

- Use K-means clustering to group layouts into distinct families.

- Assign labels to images based on extracted feature similarities.

---

## Installation and Setup

### Prerequisites
Ensure that you have the following dependencies installed:
- Python 3.x
- OpenCV
- NumPy
- Matplotlib
- Scikit-learn

### Clone the Repository
```bash
pip install opencv-python numpy matplotlib scikit-learn
git clone https://github.com/your-username/flask-image-analysis-tool.git
cd flask-image-analysis-tool
