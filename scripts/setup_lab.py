import os

TEST_DIR = "test_files"

def setup_lab():
    os.makedirs(TEST_DIR, exist_ok=True)

    files = {
        "file1.txt": "This is sample data",
        "file2.txt": "More test data",
    }

    for name, content in files.items():
        with open(os.path.join(TEST_DIR, name), "w") as f:
            f.write(content)

    # Create canary file
    with open(os.path.join(TEST_DIR, ".canary"), "w") as f:
        f.write("DO NOT TOUCH")

    print("[SETUP COMPLETE] Lab ready")

if __name__ == "__main__":
    setup_lab()