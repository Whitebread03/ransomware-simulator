import os
import time

expected_size = 24

def get_expected_size(folder):
    canary_path = os.path.join(folder, ".canary")
    return os.path.getsize(canary_path)

def check_mass_modification(folder, threshold=10):
    files = os.listdir(folder)
    if len(files) > threshold:
        return True
    return False

def detect_canary_trigger(folder):
    canary_path = os.path.join(folder, ".canary.locked")

    # If the canary was encrypted/renamed -> trigger alert
    if not os.path.exists(canary_path):
        return True
    
    expected_size = get_expected_size(folder)

    if os.path.getsize(canary_path) != expected_size:
        return True
    return False