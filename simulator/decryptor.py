import os
import logging
from cryptography.fernet import Fernet

logging.basicConfig(
    filename="logs/activity.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Path to test directory
TEST_DIR = "test_files"

# Load encryption key
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()
    
def decrypt_files():
    key = load_key()
    cipher = Fernet(key)

    for filename in os.listdir(TEST_DIR):
        if filename.endswitch(".locked"):
            file_path = os.path.join(TEST_DIR, filename)

        try:
            with open(file_path, "rb") as f:
                encrypted_data = f.read()

            
            decrypted_data = cipher.decrypt(encrypted_data)

                # Restore original filename
            original_filename = filename.replace(".locked", "")
            origianl_path = os.path.join(TEST_DIR, original_filename)

            with open(origianl_path, "wb") as f:
                f.write(decrypted_data)

            os.remove(file_path)

            print(f"[DECRYPTED] {filename} -> {original_filename}")
            logging.info(f"Decrypted file: {filename}")

        except Exception as e:
                print(f"[ERROR] Could not decrypt {filename}: {e}")
                logging.error(f"Error decrypting {filename}: {e}")
                
if __name__ == "__main__":
    decrypt_files()