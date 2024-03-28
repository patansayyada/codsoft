import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    num_special = int(special_entry.get())
    num_numbers = int(numbers_entry.get())
    num_upper = int(upper_entry.get())
    
    if length < num_special + num_numbers + num_upper:
        messagebox.showerror("Error", "The specified length is too short for the requested characters.")
        return
    
    special_characters = string.punctuation
    numbers = string.digits
    upper_case_letters = string.ascii_uppercase
    lower_case_letters = string.ascii_lowercase

    required_special = ''.join(random.choice(special_characters) for _ in range(num_special))
    required_numbers = ''.join(random.choice(numbers) for _ in range(num_numbers))
    required_upper = ''.join(random.choice(upper_case_letters) for _ in range(num_upper))
    
    remaining_length = length - (num_special + num_numbers + num_upper)
    remaining_characters = ''.join(random.choice(lower_case_letters) for _ in range(remaining_length))

    password = required_special + required_numbers + required_upper + remaining_characters
    password = ''.join(random.sample(password, len(password))) # Shuffle the characters to make it more random
    
    result_label.config(text="Generated Password: " + password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create labels and entry fields
tk.Label(root, text="Length:").grid(row=0, column=0, sticky="e")
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

tk.Label(root, text="Special Symbols:").grid(row=1, column=0, sticky="e")
special_entry = tk.Entry(root)
special_entry.grid(row=1, column=1)

tk.Label(root, text="Numbers:").grid(row=2, column=0, sticky="e")
numbers_entry = tk.Entry(root)
numbers_entry.grid(row=2, column=1)

tk.Label(root, text="Capital Letters:").grid(row=3, column=0, sticky="e")
upper_entry = tk.Entry(root)
upper_entry.grid(row=3, column=1)

result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2)

# Create generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=5, columnspan=2)

# Run the main event loop
root.mainloop()