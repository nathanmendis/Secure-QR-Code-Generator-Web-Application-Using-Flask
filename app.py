from flask import Flask, render_template, request, redirect, url_for, send_file
from cryptography.fernet import Fernet
import qrcode
import cv2
import os

app = Flask(__name__)

# Function to encrypt the link
def encrypt_link(link, key):
    cipher_suite = Fernet(key)
    encrypted_link = cipher_suite.encrypt(link.encode())
    return encrypted_link

# Function to decrypt the link
def decrypt_link(encrypted_link, key):
    cipher_suite = Fernet(key)
    decrypted_link = cipher_suite.decrypt(encrypted_link.encode())
    return decrypted_link.decode()

# Function to generate QR code from encrypted data
def generate_qr_code(data, file_name='encrypted_qr.png'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(f'static/{file_name}')
    return f'static/{file_name}'

# Function to scan and extract data from the uploaded QR code image
def scan_qr_code(file_path):
    img = cv2.imread(file_path)
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(img)
    return data

# Route for the encryption page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        link = request.form['link']
        key = Fernet.generate_key().decode()  # Generate key
        encrypted_link = encrypt_link(link, key).decode()
        qr_file = generate_qr_code(encrypted_link, 'encrypted_qr.png')  # Generate QR Code and save in static folder

        return render_template('index.html', encrypted_link=encrypted_link, key=key, qr_file=qr_file)
    return render_template('index.html')

# Route to download the QR code
@app.route('/download_qr')
def download_qr():
    path = "static/encrypted_qr.png"
    return send_file(path, as_attachment=True)

# Route for the decryption page (with QR code upload)
@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == 'POST':
        key = request.form['key']
        qr_file = request.files['qr_code']
        
        # Save the uploaded file
        file_path = os.path.join('uploads', qr_file.filename)
        qr_file.save(file_path)

        try:
            # Scan the QR code from the uploaded file
            encrypted_data = scan_qr_code(file_path)
            if encrypted_data:
                # Decrypt the data
                decrypted_link = decrypt_link(encrypted_data, key)
                return render_template('decrypt.html', decrypted_link=decrypted_link)
            else:
                error = "Could not decode the QR code."
                return render_template('decrypt.html', error=error)

        except Exception as e:
            error = f"Error during decryption: {e}"
            return render_template('decrypt.html', error=error)

    return render_template('decrypt.html')

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
