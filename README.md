## Overview
This Python script allows you to merge multiple `.JPG` images into a single PDF document. Each image is resized to fit an A4 page (210x297 mm) while maintaining its original aspect ratio, and it is centered on the page for a professional layout.

## Features
- Automatically resizes images to fit within an A4 page (210x297 mm).
- Maintains the aspect ratio of images to prevent distortion.
- Centers each image on the PDF page.
- Supports `.JPG` format for images.

## Requirements
- Python 3.x
- FPDF library
- Pillow library (for handling image dimensions)

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/mbrychczynski/Image-to-PDF-Converter.git
    ```
2. Navigate to the project directory:
    ```bash
    cd image-to-pdf-converter
    ```
3. Install the required dependencies:
    ```bash
    python3 -m pip install --upgrade Pillow
    ```

## Usage

1. Place all the `.JPG` images you want to merge into a folder named `IMGs_to_merge`.
2. Run the script:
    ```bash
    python merge_images_to_pdf.py
    ```
3. The resulting PDF will be saved in the `PDF_result` folder as `result.pdf`.

## Code Explanation

- **Image Dimension Conversion**: The script converts image dimensions from pixels to millimeters, based on the default 72 DPI (dots per inch) assumed by the FPDF library.
- **Scaling and Centering**: Images are scaled down proportionally to fit within the A4 dimensions while keeping their aspect ratio intact, and they are centered on the page.

## Contributing

Feel free to fork this project and submit pull requests for any improvements or new features!

## License

This project is licensed under the MIT License.