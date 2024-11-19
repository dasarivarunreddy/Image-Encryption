from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_image(image_path):
    key = load_key()
    fernet = Fernet(key)

    with open(image_path, "rb") as image_file:
        original_image = image_file.read()

    encrypted_image = fernet.encrypt(original_image)

    with open(f"encrypted_{os.path.basename(image_path)}", "wb") as encrypted_file:
        encrypted_file.write(encrypted_image)

    print(f"{image_path} has been encrypted and saved as encrypted_{os.path.basename(image_path)}")

def decrypt_image(encrypted_image_path):
    key = load_key()
    fernet = Fernet(key)

    with open(encrypted_image_path, "rb") as encrypted_file:
        encrypted_image = encrypted_file.read()

    decrypted_image = fernet.decrypt(encrypted_image)

    with open(f"decrypted_{os.path.basename(encrypted_image_path)}", "wb") as decrypted_file:
        decrypted_file.write(decrypted_image)

    print(f"{encrypted_image_path} has been decrypted and saved as decrypted_{os.path.basename(encrypted_image_path)}")

if __name__ == "__main__":
    encrypt_image("example_image.png")  # Replace with your image file
    decrypt_image("encrypted_example_image.png")  # Replace with your encrypted image file
