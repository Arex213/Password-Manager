# 🔐 Master Password Manager

This is a simple Python GUI application for securely creating and verifying a **master password** using the `hashlib` module and the `tkinter` library.

## 📋 Features

- Create and securely store a master password.
- Verify the master password for authentication.
- Passwords are hashed using **SHA-256** before being saved.
- Simple and intuitive graphical interface built with Tkinter.

## 🚀 How It Works

1. **Create Master Password:**
   - Click on **"Create Master Password"**.
   - Enter your desired password and click **"Create"**.
   - The password is hashed and saved to a file named `master.txt`.

2. **Verify Master Password:**
   - Click on **"Verify Master Password"**.
   - Enter the password and click **"Verify"**.
   - The password is hashed and compared with the stored hash in `master.txt`.

## 🔧 Requirements

- Python 3.x
- No external libraries required. Uses built-in modules:
  - `tkinter` for GUI
  - `hashlib` for password hashing

## 📦 Installation & Running

1. Clone or download the repository.
2. Run the Python script:

```bash
python password_manager.py
```

> Ensure that the file is named `password_manager.py` or any other name you prefer.

## 🔐 Security Note

- This application **only stores the hashed password**, not the raw password itself.
- For a production-grade password manager, consider using proper encryption libraries, secure storage mechanisms, and password salting.