# img2text
We will be taking Images from the User and Generate Descriptions of those Images.

# Image to Text Annotation using Google Gemini

This project is a web-based Image to Text Annotation tool built using **Streamlit** and **Google Gemini**. The application allows users to upload an image, provide an optional input prompt, and get text annotations based on the content of the image using the Gemini AI model.

## Features

- Upload an image (jpg, jpeg, png formats supported)
- Provide an optional prompt for context or leave it blank
- Generate text annotations using Google Gemini's `gemini-1.5-flash` model
- Display the uploaded image with a generated response on the same page

## Project Structure


## Installation

To run this project locally, follow these steps:

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/image-to-text-annotation-gemini.git
cd image-to-text-annotation-gemini

python -m venv venv
source venv/bin/activate   # On Windows, use: venv\Scripts\activate

Usage
Input Prompt: You can optionally enter a prompt to provide more context for the image annotation.
Upload Image: Upload an image file in one of the supported formats (jpg, jpeg, png).
Submit: Click the "Submit" button to receive the text annotation based on the image content and optional prompt.
The image and response will be displayed on the same page.

Dependencies
Streamlit: For building the interactive web app
Google Generative AI: For using the Gemini AI model to annotate images
PIL (Pillow): For handling image uploads and display
dotenv: For loading environment variables from the .env file
Future Improvements
Add support for additional image formats.
Expand functionality to allow multiple image uploads and batch processing.
Integrate more advanced controls for fine-tuning the AI model’s behavior.
