import os
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import tkinter
import tkinter.filedialog as filedialog

def select_file():
    global file_path, file_name
    file_path = filedialog.askopenfilename(filetypes=[("Metin Belgeleri", "*.txt")])
    file_name = os.path.basename(file_path)
    file_label.config(text=file_name)
    encrypt_button.config(state="normal")
    decrypt_button.config(state="normal")

def encryption():
    creation_time = os.path.getctime(file_path)
    salt = str(creation_time).encode()
    password = "my_password".encode()
    kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    with open(file_path, 'rb') as original_file:
        original = original_file.read()
    encrypted = f.encrypt(original)
    with open (file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    result_label.config(text=f"\"{file_name}\" dosyası başarıyla şifrelendi.")

def decryption():
    creation_time = os.path.getctime(file_path)
    salt = str(creation_time).encode()
    password = "my_password".encode()
    kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    with open(file_path, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = f.decrypt(encrypted)
    with open(file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    result_label.config(text=f"\"{file_name}\" dosyası başarıyla çözüldü.")

# Creating GUI
root = tkinter.Tk()
root.title("CipherApp")
root.geometry("300x400")
root.iconbitmap(default='usb.ico')

title_label = tkinter.Label(root, text="CipherApp", font=("Helvetica", 24, "bold"))
title_label.place(relx=0.5, y=70, anchor="center")

file_label = tkinter.Label(root, text="Dosya Seçilmedi", width=20, height=2, relief="sunken")
file_label.place(relx=0.5, y = 150, anchor="center")

# Creating "Dosya Seç" button
select_button = tkinter.Button(root, text="Dosya Seç", command=select_file)
select_button.place(relx=0.5, y = 220, anchor="center")

# Creating "Şifrele / Çöz" button
encrypt_button = tkinter.Button(root, text="Şifrele", command=encryption, state=tkinter.DISABLED)
decrypt_button = tkinter.Button(root, text="Şifre Çöz", command=decryption, state=tkinter.DISABLED)
button_frame = tkinter.Frame(root)
button_frame.pack(pady=20)
encrypt_button.place(relx=0.3, y = 270, anchor="center")
decrypt_button.place(relx=0.7, y = 270, anchor="center")

result_label = tkinter.Label(root)
result_label.place(relx=0.5, y = 320, anchor="center")

root.mainloop()
