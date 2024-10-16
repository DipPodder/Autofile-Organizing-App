def detect_file_type(file_path):
    # Define a dictionary of file extensions and their corresponding types
    file_types = {
        ".jpg": "Image",
        ".jpeg": "Image",
        ".png": "Image",
        ".gif": "Image",
        ".pdf": "Document",
        ".doc": "Document",
        ".docx": "Document",
        ".txt": "Document",
        ".mp4": "Video",
        ".mov": "Video",
        ".avi": "Video",
        ".mp3": "Audio",
        ".wav": "Audio",
        ".aac": "Audio"
    }

    # Get the file extension
    extension = file_path.split('.')[-1].lower()
    if extension.startswith('.'):
        extension = '.' + extension

    # Determine the file type based on the extension
    file_type = file_types.get(extension, "Unknown file type")
    print(f"Detected file type: {file_type}")

