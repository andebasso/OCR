# OCR (Optical Character Recognition) Project

This project implements an OCR (Optical Character Recognition) solution using Python, Tesseract OCR, and a basic GUI (Graphical User Interface) with Tkinter. The software allows the user to select an image from their file system and extract text from it, optimizing the process for different types of text such as hexadecimal, digits, alphabetical, or a mix of all.

## Features

- **Image Selection**: Allows the user to select an image from their file system for text recognition.
- **Image Pre-processing**: Applies image pre-processing techniques to enhance the quality of the text to be recognized, including contrast adjustment and sharpening.
- **Support for Different Text Types**: Offers the option to optimize text recognition for specific formats - hexadecimal, digits, alphabetical, or all.
- **User-friendly GUI**: Utilizes Tkinter for a simple graphical interface, facilitating user interaction.
- **Text Export**: Saves the extracted text in a `.txt` file, in the same directory as the original image.

## Technologies Used

- **Python**: The programming language used to implement the software logic.
- **Tesseract OCR**: An open-source OCR engine used for extracting text from images.
- **Tkinter**: A library for creating the graphical interface.

## Requirements

- Python 3.x
- Python libraries: Pillow, pytesseract, tkinter (typically comes installed with Python).
- Tesseract OCR installed on the system and configured in the system's PATH environment variable.

## Installation

1. **Install Python**: Ensure you have Python 3.x installed on your system.
2. **Install Tesseract OCR**: [Download and install Tesseract OCR](https://github.com/tesseract-ocr/tesseract) following the instructions for your operating system.
3. **Install Python Dependencies**: Run the following command in the terminal to install the necessary libraries:
   ```bash
   pip install Pillow pytesseract

