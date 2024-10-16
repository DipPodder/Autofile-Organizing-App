import os

def validate_path(func):
    def wrapper(path, *args, **kwargs):
        if not os.path.exists(path):
            print(f"Error: The path '{path}' does not exist.")
            return
        return func(path, *args, **kwargs)
    return wrapper
