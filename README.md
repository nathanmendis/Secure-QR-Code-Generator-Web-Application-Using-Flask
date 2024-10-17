
# QR Code Encryption and Decryption App

This is a Flask-based web application that allows users to encrypt a URL, generate a QR code from the encrypted data, and later decrypt the encrypted link by scanning the QR code. 

## Features

- **URL Encryption**: Encrypt a URL using a unique encryption key generated with the `cryptography.fernet` library.
- **QR Code Generation**: Generates a QR code from the encrypted URL.
- **QR Code Download**: Allows users to download the generated QR code.
- **QR Code Decryption**: Decrypts a URL by scanning the QR code and providing the encryption key.
- **File Upload for Decryption**: Accepts uploaded QR code images for decryption.

## Technologies Used

- **Flask**: Backend framework to handle routing and rendering templates.
- **Cryptography**: For encrypting and decrypting URLs using Fernet encryption.
- **qrcode**: To generate QR codes from encrypted data.
- **OpenCV**: To scan and decode QR codes from uploaded images.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/qr-code-encryption-app.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```

4. Access the application on your browser:
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure

```
.
├── app.py              # Main Flask application
├── templates
│   ├── index.html      # HTML page for URL encryption and QR generation
│   └── decrypt.html    # HTML page for QR decryption
├── static
│   └── encrypted_qr.png # Stores generated QR codes (default file)
├── uploads             # Stores uploaded QR code images for decryption
└── README.md           # This file
```

## Usage

### Encrypt a URL
1. Navigate to the homepage.
2. Enter a URL in the input field and click "Encrypt and Generate QR Code".
3. The app will generate and display a QR code along with an encryption key.
4. Download the QR code for future use and securely store the encryption key.

### Decrypt a URL
1. Navigate to the "Decrypt" page.
2. Upload the QR code file.
3. Enter the encryption key provided during encryption.
4. The app will display the decrypted URL if the key is correct.

## Security Considerations

- Ensure the encryption key is stored safely by the user since it's necessary for decryption.
- Always use **HTTPS** when deploying to production to ensure secure transmission of keys and data.
- Implement limits on file uploads to avoid potential abuse.

## License

This project is licensed under the MIT License.
