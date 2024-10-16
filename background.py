import time
from datetime import datetime

def background_task(path):
    while True:
        current_time = datetime.now()
        # Check if the current minute is 0 (the start of the hour)
        if current_time.minute == 0:
            print(f"Running organize_files at {current_time}")
            organize_files(path)
            # Wait for an hour before the next execution
            time.sleep(3600)
        else:
            # Sleep for a minute before checking again
            time.sleep(60)
