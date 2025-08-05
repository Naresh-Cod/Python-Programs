import tkinter as tk

# Function to update label text
def update_text():
    entered_text = entry.get()
    label.config(text=f"Hello, {entered_text}!")

# Create main window
root = tk.Tk()
root.title("Simple Tkinter Program")
root.geometry("300x200")

# Create a label
label = tk.Label(root, text="Enter your name:", font=("Arial", 12))
label.pack(pady=10)

# Create an entry field
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

# Create a button
button = tk.Button(root, text="Greet", command=update_text, font=("Arial", 12))
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
