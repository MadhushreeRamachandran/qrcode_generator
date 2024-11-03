# Enhanced QR Code Generator

A simple and intuitive QR code generator built with Python and Tkinter. This application allows users to create QR codes with customizable settings such as size, border, and colors.

## Features

- **Generate QR Codes**: Enter a URL or text and generate a QR code instantly.
- **Customization Options**: Adjust box size, border size, fill color, and background color.
- **Preview**: See a preview of the generated QR code before saving.
- **Save QR Code**: Save the generated QR code as a PNG file.

## Requirements

To run this project, you need:

- Python 3.x
- Required Python packages:
  - `qrcode`
  - `Pillow`
  - `tkinter`

You can install the required packages using pip:

```bash
pip install qrcode[pil] Pillow
```

## Usage

1. **Clone the Repository**: Begin by cloning the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/enhanced-qr-code-generator.git
    cd enhanced-qr-code-generator
    ```

2. **Run the Application**: Launch the QR code generator by executing:
    ```bash
    python qr_code_generator.py
    ```

3. **Input Data**:
   - In the designated field, enter the URL or text you want the QR code to represent. This is your primary input.

4. **Customize QR Code**:
   - **Box Size**: Adjust the box size by entering a numeric value. This controls how large each individual module (box) of the QR code will be.
   - **Border Size**: Specify the border size, which will determine the thickness of the white border around the QR code.
   - **Color Selection**:
     - Click the **Select Fill Color** button to choose a color for the QR code itself.
     - Click the **Select Background Color** button to set the background color of the QR code.

5. **Generate and Preview**:
   - Click the **Generate QR Code** button to create the QR code. The generated QR code will be displayed in the preview section of the application.

6. **Save the QR Code**:
   - To save your QR code, click the **Save QR Code** button. A dialog will appear for you to choose the location and name of your saved file. The QR code will be saved as a PNG image.
