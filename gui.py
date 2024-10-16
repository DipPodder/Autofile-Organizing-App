import tkinter as tk
from tkinter import filedialog
from fileorganizer import organize_files

#decorator
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function : {func.__name__} finished execution.")
        return result
    return wrapper

@log_function_call
def browse_folder():
    path = filedialog.askdirectory()
    
    if path:
        organize_files(path)
        
@log_function_call
def create_gui():
    root = tk.Tk()
    root.title("File Organizer")
    root.geometry("400x300")
    root.minsize(400,300)
    
    # Center the window
    window_width = 400
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    browse_button = tk.Button(root,text="Browse Folder", command= browse_folder)
    browse_button.pack(pady=20, padx=20, expand=True)
    
    root.mainloop()
    
if __name__ == "__main__":
    print("Starting GUI...")  
    create_gui()