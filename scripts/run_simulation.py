import os

def run_full_simulation():
    os.system("python simulator/encryptor.py")
    os.system("python simulator/ransom_note.py")
    os.system("python simulator/decryptor.py")

if __name__ == "__main__":
    run_full_simulation()