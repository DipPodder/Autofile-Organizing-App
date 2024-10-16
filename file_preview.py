from PIL import Image
import os

def preview_image(file_path):
    if os.path.exists(file_path):
        try:
            img = Image.open(file_path)
            img.show()
        except Exception as e:
            print(f"Error opening image: {e}")
    else:
        print(f"File not found: {file_path}")
