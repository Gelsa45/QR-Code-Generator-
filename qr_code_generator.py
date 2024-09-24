import qrcode

def generate_qr_code(data, file_name="qr_code.png"):
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,  # Size of the QR Code: 1 is the smallest, up to 40
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # About 7% of errors can be corrected
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # The thickness of the border
    )
    
    # Add the data (URL or text) to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill='black', back_color='white')

    # Save the image to a file
    img.save(file_name)
    print(f"QR code saved as {file_name}")

if __name__ == "__main__":
    # Take input from the user for what the QR code should contain
    data_input = input("Enter the data (URL or text) for the QR code: ")
    file_name = input("Enter the file name to save the QR code (e.g., qr_code.png): ") or "qr_code.png"
    
    generate_qr_code(data_input, file_name)
  
