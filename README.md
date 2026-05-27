# QR Code Generator Using Python

## Project Overview

This project is a QR Code Generator application developed using Python. The application allows users to enter a website URL and automatically generates a QR code image. The generated QR code can be scanned using a smartphone camera or QR scanner application to open the corresponding website link.

QR (Quick Response) codes are widely used for storing website links, contact information, payment details, and other digital data in a machine-readable format.

---

## Features

- Generate QR code from a URL
- Save QR code as an image file (.png)
- Simple and user-friendly interface
- Fast QR code generation
- Easily scannable output

---

## Technologies Used

- Python
- qrcode Library
- Pillow Library
- Visual Studio Code
- GitHub

---

## Project Structure

```text
QR_Code_Generator/
│
├── qr_generator.py
├── requirements.txt
├── generated_qrcode.png
└── README.md
```

---

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/QR-Code-Generator.git
```

### Step 2: Navigate to Project Folder

```bash
cd QR-Code-Generator
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## Required Dependencies

The project uses the following libraries:

```txt
qrcode
pillow
```

You can also install manually:

```bash
pip install qrcode[pil]
```

---

## How to Run the Project

Run the following command:

```bash
python qr_generator.py
```

---

## Example Input

```text
Enter the URL to generate QR Code:
https://github.com/
```

---

## Example Output

```text
QR Code generated successfully!
Image saved as generated_qrcode.png
```

A QR code image file will be generated and saved in the project folder.

---

## Working Process

1. User enters a website URL.
2. The qrcode library processes the input.
3. A QR code image is generated.
4. The QR code is saved as a PNG file.
5. A success message is displayed.

---

## Output

The application generates a QR code image (`generated_qrcode.png`) that can be scanned using any smartphone camera or QR scanner app to open the website link.

---

## Future Improvements

- Add GUI support using Tkinter
- Allow users to customize QR code colors
- Generate QR codes for text, phone numbers, and email addresses
- Add logo embedding inside QR codes

---

## Conclusion

This project demonstrates the practical implementation of Python libraries for QR code generation. It helps in understanding Python programming concepts such as user input, file handling, image generation, and external library integration.

---

## Author

Yasir Salman Shaikh

---

## License

This project is developed for educational purposes.
