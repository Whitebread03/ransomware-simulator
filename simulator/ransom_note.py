import os
from datetime import datetime

TEST_DIR = "test_file"

def create_ransom_note():
    note_content = f"""
============================
 FILES ENCRYPTED (SIMULATION)
=============================

Your files have been encyrpted as part of a cybersecurity simulation.

This is NOT real ransomware
1. Run decryptor.py
2. Use the provided key file (key.key)

Timestamp: {datetime.now()}
============================
"""
    
    note_path = os.path.join(TEST_DIR, "README_RESTORE.txt")

    with open(note_path, "w") as f:
        f.write(note_content)

    print("[INFO] Ransom note created")

if __name__ == "__main__":
    create_ransom_note()