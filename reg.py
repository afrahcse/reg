import tkinter as tk
from tkinter import messagebox

def register():
    username = entry_username.get()
    password = entry_password.get()
    email = entry_email.get()
    
    # Simple validation
    if username and password and email:
        messagebox.showinfo("Success", f"Registration Successful!\nUsername: {username}\nEmail: {email}")
    else:
        messagebox.showwarning("Error", "All fields are required!")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create labels and text boxes
label_username = tk.Label(root, text="Username:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Password:")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

label_email = tk.Label(root, text="Email:")
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()

# Create a register button
register_button = tk.Button(root, text="Register", command=register)
register_button.pack()

# Run the application
root.mainloop()
