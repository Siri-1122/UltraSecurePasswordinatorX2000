import random
import tkinter as tk

letters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
numbers = "1234567890"
characters = "!@#$%^&*()"
pw = []

def passwordinator():
    pw.clear()  
    n = 0
    while n <= 20:
        a = random.choice([letters, numbers, characters])
        if a == letters:
            pw.append(a[random.randint(0,51)])
        elif a == numbers:
            pw.append(a[random.randint(0,9)])
        else:
            pw.append(a[random.randint(0,9)])
        n += 1
    password = ''.join(pw)
    password_label.config(text=f"The PASSWORDINATOR Suggests: {password}")

window = tk.Tk()
window.title("UltraSecurePasswordinatorX2000")
window.geometry("400x200")

title_label = tk.Label(window, text="Password Generator", font=("Helvetica", 16))
title_label.pack(pady=10)

generate_button = tk.Button(window, text="Generate Password", command=passwordinator, font=("Helvetica", 12))
generate_button.pack(pady=10)

password_label = tk.Label(window, text="Your password will appear here...", font=("Helvetica", 12))
password_label.pack(pady=10)

window.mainloop()
