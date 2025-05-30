import hashlib
import tkinter as tk


root = tk.Tk()
root.title("Master Password Manager")
root.geometry("600x400")


# create a label and entry for master password input
label = tk.Label(root, text="Welcome to the Master Password Manager", font=("Arial", 16))
label.pack(pady=20)

entry_label = tk.Label(root, text="Create your master password:")
entry_label.pack(pady=10)
entry = tk.Entry(root, show='*', width=30)
entry.pack(pady=10)

# create and save a master password
def create_master_password():
    master_password = entry.get()
    hashed_password = hashlib.sha256(master_password.encode()).hexdigest()

    with open("master.txt", "w") as file:
        file.write(hashed_password)
    print("Master password set and saved securely.")

# verify the master password
def verify_master_password():
    try:
        with open("master.txt", "r") as file:
            saved_hash = file.read().strip()

        attempt=input("Enter your master password: ")
        attempt_hash = hashlib.sha256(attempt.encode()).hexdigest()

        print("Saved hash:  ", saved_hash)
        print("Attempt hash:", attempt_hash)
        if attempt_hash == saved_hash:
            print("Master password verified successfully.")
            return True
        else:
            print("Master password verification failed.")
            return False
        
    except FileNotFoundError:
        print("Master password not set yet.")
        return False

# main function to handle user input        
def main():
    while True:
        choice = input("Do you want to (c)reate or (v)erify your master password? (q to quit): ").lower()
        if choice == 'c':
            create_master_password()
        elif choice == 'v':
            if verify_master_password():
                print("Access granted.")
            else:
                print("Access denied.")
        elif choice == 'q':
            break
        else:
            print("Invalid option. Please try again.")


main()
root.mainloop()