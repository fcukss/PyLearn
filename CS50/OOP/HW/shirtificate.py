from fpdf import FPDF
from PIL import Image

# Constants
PDF_WIDTH = 210
PDF_HEIGHT = 297
SHIRT_IMAGE = "shirtificate.png"  # Make sure this file exists in the same directory

# Prompt for user's name
name = input("Name: ")

# Create PDF
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

# Set title text
pdf.set_font("Helvetica", "B", 44)
pdf.cell(0, 40, "CS50 Shirtificate", ln=True, align="C")

# Get image dimensions and position it
with Image.open(SHIRT_IMAGE) as img:
    img_width, img_height = img.size
    aspect_ratio = img_height / img_width
    target_width = 150 * 1.3 # in mm
    target_height = target_width * aspect_ratio
    x_position = (PDF_WIDTH - target_width) / 2
    y_position = 60
    pdf.image(SHIRT_IMAGE, x=x_position, y=y_position, w=target_width)

# Overlay name on shirt
pdf.set_font("Helvetica", size=22)
pdf.set_text_color(255, 255, 255)
pdf.set_xy(0, y_position + 45)
pdf.cell(0, 10, f"{name} took CS50", align="C")

# Output to file
pdf.output("shirtificate.pdf")




