# ---------------------------------------------------------
# QR Code Generator Application
# Developed for Biox Systems
# This program generates a QR code from a URL input
# ---------------------------------------------------------

# Import qrcode library
import qrcode

# Ask user to enter URL
url = input("Enter the URL to generate QR Code: ")

# Create QR Code object
qr = qrcode.QRCode(
    version=1,                  # Controls size of QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,                # Size of each box in pixels
    border=4                    # Thickness of border
)

# Add data to QR code
qr.add_data(url)

# Generate QR code
qr.make(fit=True)

# Create image
img = qr.make_image(fill_color="black", back_color="white")

# Save image
img.save("generated_qrcode.png")

# Success message
print("QR Code generated successfully!")
print("Image saved as generated_qrcode.png")
