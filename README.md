# PDF Signer Project

A professional solution for digitally signing PDF documents with QR codes. This application allows you to securely sign your PDF documents, upload them to an FTP server, and add a QR code that verifies the document's authenticity.

## Features

- 🎯 User-friendly graphical interface
- 📄 PDF document processing
- 🔒 Secure FTP uploading
- 📱 QR code generation
- ✍️ Digital signature integration
- 🔍 Document tracking capability

## Requirements

To run the program, you need:

- Python 3.x
- Required Python libraries:
  - tkinter (for GUI)
  - ftplib (for FTP operations)
  - qrcode (for QR code generation)
  - PyPDF2 (for PDF processing)
  - fpdf (for PDF creation)

## Installation

1. Install Python on your computer (if not already installed):
   - For Windows: [Python.org](https://www.python.org/downloads/)
   - For Linux: `sudo apt-get install python3`

2. Install required libraries:
```bash
pip install tkinter qrcode PyPDF2 fpdf2
```

## Usage

1. Start the program:
```bash
python upload.py
```

2. Click the "Select PDF File" button in the window

3. Choose the PDF file you want to sign

4. The program will automatically:
   - Upload the document to the FTP server
   - Generate a QR code
   - Add the signature and QR code to the document
   - Save the new signed document with a "signed_" prefix

## Technical Details

- FTP Server: ftpupload.net
- Upload destination: https://greenproject.rf.gd/upload/
- QR code size: 30x30 pixels
- Signature text: Two-line format
- Supported format: PDF

## Security

- All FTP operations are conducted over encrypted channels
- Documents are stored securely on the server
- QR codes are generated with unique identifiers

## Troubleshooting

If you encounter any of these issues:

1. "PDF file can't be found" error:
   - Verify the file exists
   - Check for special characters in the filename

2. FTP error:
   - Check your internet connection
   - Verify firewall settings

3. QR code error:
   - Ensure sufficient disk space
   - Check permissions for temporary file deletion

## Contact

For any issues or suggestions:
- Email: rufat@example.com
- GitHub: github.com/rufat
- Website: greenproject.rf.gd

## License

This project is licensed under the MIT License. See the LICENSE file for details.
