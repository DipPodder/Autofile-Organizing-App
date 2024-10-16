import os
import concurrent.futures

def organize_in_threads(path, organize_files_func):
    files = os.listdir(path)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for file in files:
            executor.submit(organize_files_func, os.path.join(path, file))

