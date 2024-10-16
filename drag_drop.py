import tkinter as tk
from tkinter import filedialog, messagebox

class DragDropApp:
    def __init__(self, master):
        self.master = master
        master.title("Drag and Drop Organizer")
        master.geometry("400x300")

        # Instructions label
        self.label = tk.Label(master, text="Drag and drop files here or select a folder:")
        self.label.pack(pady=10)

        # Text area for drag-and-drop
        self.text_area = tk.Text(master, height=10, width=50)
        self.text_area.pack(pady=10)

        # Organize button
        self.organize_button = tk.Button(master, text="Organize Files", command=self.organize_files)
        self.organize_button.pack(pady=20)

        # Button to select a folder
        self.select_button = tk.Button(master, text="Select Folder", command=self.select_folder)
        self.select_button.pack(pady=10)

        # Bind the drop event (requires tkinterdnd2)
        # Note: You must install tkinterdnd2 for drag-and-drop support
        # master.bind("<Drop>", self.drop)  # Uncomment if using tkinterdnd2

    def drop(self, event):
        # Get the path from the event (uncomment when using tkinterdnd2)
        path = event.data.strip('{}')  # Remove curly braces
        self.text_area.insert(tk.END, f"{path}\n")  # Insert the path into the text area

    def organize_files(self):
        # Get paths from the text area
        paths = self.text_area.get("1.0", tk.END).strip().splitlines()
        if paths:
            for path in paths:
                try:
                    organize_files(path)  # Call the organize_files function
                except Exception as e:
                    messagebox.showerror("Error", f"Error organizing {path}: {e}")
            messagebox.showinfo("Success", "File organization complete!")
            self.text_area.delete("1.0", tk.END)  # Clear text area after organizing
        else:
            messagebox.showwarning("Input Error", "Please drop files or enter a valid folder path.")

    def select_folder(self):
        # Open a file dialog to select a folder
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.text_area.insert(tk.END, f"{folder_path}\n")  # Insert selected folder path

if __name__ == "__main__":
    root = tk.Tk()
    app = DragDropApp(root)
    root.mainloop()

