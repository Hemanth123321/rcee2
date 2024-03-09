# deploy.py

import subprocess
import sys

def install_dlib_whl(whl_path):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", whl_path])
        print("dlib installation successful.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dlib: {e}")

if __name__ == "__main__":
    # Specify the path to the dlib.whl file
    dlib_whl_path = "dlib.whl"

    # Install dlib
    install_dlib_whl(dlib_whl_path)
