import os.path
import pathlib
from fpdf import FPDF
from PIL import Image

A4_WIDTH = 210
A4_HEIGHT = 297
DIR_PATH = "./PDF_result"

files = [f for f in pathlib.Path().glob("./IMGs_to_merge/*.JPG")]
files.sort()

pdf = FPDF(orientation="P", format="A4")

for file in files:
    pdf.add_page()

    # Open the image to get its dimensions
    image = Image.open(file)
    img_width, img_height = image.size

    # Convert image dimensions from pixels to mm at 72 DPI (default for FPDF)
    # - Images are in pixels, but PDF pages are in millimeters.
    # - 25.4 is used to convert inches to mm (since 1 inch = 25.4 mm).
    # - We divide by 72 because FPDF assumes images are at 72 DPI.
    # - This converts image size from pixels to mm, so it can be properly scaled to fit the PDF page.
    img_width_mm = img_width * 25.4 / 72
    img_height_mm = img_height * 25.4 / 72

    # Calculate scaling to fit the image within A4
    # - A4 page dimensions are 210x297 mm.
    # - width_ratio: how much we need to shrink the image width to fit the page.
    # - height_ratio: how much we need to shrink the image height to fit the page.
    # - We take the smaller scaling ratio (min) to ensure the image fits within both the width and height.
    width_ratio = A4_WIDTH / img_width_mm
    height_ratio = A4_HEIGHT / img_height_mm
    scale = min(width_ratio, height_ratio)

    # Calculate new width and height to maintain the aspect ratio
    # - We multiply the original image dimensions by the scale factor
    #   to ensure the image size is proportionally reduced.
    new_width = img_width_mm * scale
    new_height = img_height_mm * scale

    # Center the image on the A4 page
    # - After resizing, we calculate the offset to center the image.
    # - x_offset: amount of space to leave on the left and right to center the image horizontally.
    # - y_offset: amount of space to leave on the top and bottom to center the image vertically.
    x_offset = (A4_WIDTH - new_width) / 2
    y_offset = (A4_HEIGHT - new_height) / 2

    # Add the image to the PDF
    pdf.image(str(file), x_offset, y_offset, new_width, new_height)

if not os.path.exists("./PDF_result"):
    os.makedirs(DIR_PATH)

pdf.output(f"{DIR_PATH}/result.pdf", "F")