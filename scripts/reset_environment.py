import os

TEST_DIR = "test_files"

def reset_environment():
    for file in os.listdir(TEST_DIR):
        path = os.path.join(TEST_DIR, file)

        # Remove encrypted files and ransom notes
        if file.endswith(".locked") or file == "README_RESTORE.txt":
            os.remove(path)
            print(f"[REMOVED] {file}")

    print("[RESET COMPLETE] Environment clean")

if __name__ == "__main__":
    reset_environment()