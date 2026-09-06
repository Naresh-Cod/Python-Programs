import tkinter as tk

# window
root = tk.Tk()
root.title("Meri Pehli App")
root.geometry("400x300")

# label
title_label = tk.Label(root, text="Aapka naam kya hai?", font=("Arial", 14))
title_label.pack(pady=10) #pack()

#Text input box
name_input = tk.Entry(root, font=("Arial", 12), width=20)
name_input.pack(pady=10)

# Function and Button
def show_greeting():
    user_name = name_input.get() 
    result_label.config(text=f"Hello, {user_name}! Welcome to Tkinter.")

# Button
greet_button = tk.Button(root, text="Click Me", command=show_greeting, bg="blue", fg="white", font=("Arial", 12))
greet_button.pack(pady=10)

# Result
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="green")
result_label.pack(pady=20)

# loop run
root.mainloop()