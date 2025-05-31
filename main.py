import hashlib
import tkinter as tk

# create the main window
root = tk.Tk()
root.title("Master Password Manager")
root.geometry("600x400")

# create a label and entry for master password input
label = tk.Label(root, text="Welcome to the Master Password Manager", font=("Arial", 16))
label.grid(row=0, column=0, columnspan=2, pady=20)

# create buttons for creating and verifying master password
create_button = tk.Button(root, text="Create Master Password")
create_button.grid(row=1, column=0, pady=5, padx=5)
verify_button = tk.Button(root, text="Verify Master Password")
verify_button.grid(row=1, column=1, pady=5, padx=5)

# show the entry field when create or verify button is clicked
entry = tk.Entry(root, show="*")
entry.grid_forget()  # Initially hide the entry field
entry_visible = False

def toggle_entry(button_type):
    global entry_visible
    if entry_visible:
        entry.grid_forget()
        entry_visible = False
        entry.delete(0, 'end')  # Clear the entry field
        # Restore buttons
        if button_type == "create":
            verify_button.grid(row=1, column=1, pady=5, padx=5)
        elif button_type == "verify":
            create_button.grid(row=1, column=0, pady=5, padx=5)
        create_button.config(text="Create Master Password", command=lambda: toggle_entry("create"))
        verify_button.config(text="Verify Master Password", command=lambda: toggle_entry("verify"))
    else:
        entry.grid(row=2, column=0, columnspan=2, pady=10)
        entry_visible = True
        if button_type == "create":
            verify_button.grid_forget()
        elif button_type == "verify":
            create_button.grid_forget()
        create_button.config(text="Create", command=create_master_password)
        verify_button.config(text="Verify", command=verify_master_password)

def create_master_password():
    master_password = entry.get()
    hashed_password = hashlib.sha256(master_password.encode()).hexdigest()

    with open("master.txt", "w") as file:
        file.write(hashed_password)
    print("Master password set and saved securely.")
    toggle_entry("create")  # Hide entry after creating

def verify_master_password():
    try:
        with open("master.txt", "r") as file:
            saved_hash = file.read().strip()

        attempt = entry.get()
        attempt_hash = hashlib.sha256(attempt.encode()).hexdigest()

        print("Saved hash:  ", saved_hash)
        print("Attempt hash:", attempt_hash)
        if attempt_hash == saved_hash:
            print("Master password verified successfully.")
            toggle_entry("verify")  # Hide entry after verifying
            return True
        else:
            print("Master password verification failed.")
            toggle_entry("verify")  # Hide entry after verifying
            return False
        
    except FileNotFoundError:
        print("Master password not set yet.")
        return False

# Initial button configuration
create_button.config(command=lambda: toggle_entry("create"))
verify_button.config(command=lambda: toggle_entry("verify"))

root.mainloop()