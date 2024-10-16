import logging

logging.basicConfig(filename='organizer.log', level=logging.INFO)

def log_file_operation(operation, file, dest):
    logging.info(f"{operation}: {file} -> {dest}")