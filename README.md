**Image Description with Step-by-Step Instructions**

**Description:**

This Flask application leverages Google GenerativeAI to analyze images and generate detailed, step-by-step instructions for each image. Users can upload up to four images at a time, and the application will provide textual descriptions for each image.

**Features:**

Image upload functionality using Flask-CORS for cross-origin requests.

Error handling for invalid image formats and upload quantity.

Integration with Google GenerativeAI's gemini-1.5-flash model for generating image descriptions.

Clear and informative API responses, including success messages and error details.



**Prerequisites:**

Install dependencies:

`pip install requirements.txt`

**Run the application:**

Run the application from the command line:
`python app.py`

**Upload images:**

Test Images are in Testcases folder.

**Website**

Users visit the web page and select image files (PNG format only) using the "Choose Image" button.

The JavaScript code handles image selection and sends the selected images in a POST request to the Flask application's /upload endpoint.

The Flask application processes the images.

The descriptions are sent back to the web page as a JSON response.

The JavaScript code parses the JSON response and displays the descriptions for each uploaded image in the designated area of the UI.

**Testing**

Place various test images (in PNG format) in a separate folder (e.g., test_images).

Follow the usage instructions to upload and view generated descriptions.

**File Structure**

project_root/


├── sever.py (Flask application code)

├── requirements.txt (dependencies)

├── index.html (HTML UI)

├── script.js (JavaScript code)

├── style.css (CSS styles)

├── tests/

│   ├── testcase.csv (test cases data)  # Move test data to tests folder

│   └── TC-01 (Test Images TC-01 to TC-03)

└── Readme.md
 
