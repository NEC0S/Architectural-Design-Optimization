# Architectural Design Optimization Tool

## Overview

This project is a web-based application built with Flask that allows users to upload an image of a yellow bit map, which is then processed to calculate several key metrics, including:

- **Length** (in cm)
- **Width** (in cm)
- **Area** (in cm²)
- **Shape Ratio** (Width/Length)
- **Complexity**

The processed image and its metrics are displayed back to the user in a visually appealing user interface.

![UI Screenshot](![image](https://github.com/user-attachments/assets/19f3e47f-d2c2-4115-8dcf-1dbe5df04992)
)

---

## Demo Video

Here’s a video demonstration of how the tool works:

[![Image Analysis Tool Video Demo](video-thumbnail.png)](

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

---

## Installation and Setup

### Prerequisites

To get started with the project, make sure you have the following installed on your machine:

- Python 3.x
- pip (Python package manager)

### Clone the Repository

```bash
git clone https://github.com/your-username/flask-image-analysis-tool.git
cd flask-image-analysis-tool
