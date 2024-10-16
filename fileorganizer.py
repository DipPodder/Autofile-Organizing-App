import os  
import shutil
import json
from validator import validate_path
from logging_handler import log_file_operation
from drag_drop import DragDropApp
from file_type_detection import detect_file_type
from multithreading import organize_in_threads
from background import background_task

# Custom rules function
def load_custom_rules(file_path='rules.json'):
    with open(file_path, 'r') as f:
        return json.load(f)

@validate_path
def organize_files(path):
    # Load custom rules
    rules = load_custom_rules()
    files = os.listdir(path)

    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension.lower() 
        
        # Check if the extension matches any of the rules
        for folder_name, extensions in rules.items():
            if extension in extensions:
                target_directory = os.path.join(path, folder_name)
                try:
                    if not os.path.exists(target_directory):
                        os.makedirs(target_directory)  # Create the folder if it doesn't exist
                    shutil.move(os.path.join(path, file), os.path.join(target_directory, file))
                    print(f"Moved: {file} to {target_directory}")
                    log_file_operation("Moved", file, target_directory)  # Log the operation
                except Exception as e:
                    print(f"Error moving {file}: {e}")
                    log_file_operation("Error", file, f"Error: {e}")  # Log the error
                break 

def get_file_path(path, filename):
    return os.path.join(path, filename)

if __name__ == "__main__":
    path = "F:\\Rag Day"
    organize_files(path)
