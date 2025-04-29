import random
import tkinter as tk

letters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
numbers = "1234567890"
characters = "!@#$%^&*()"
runes = "ᚿᛂᚡᛂᚱ ᚵᚮᚿᚿᛆ ᚵᛁᚡᛂ ᚤᚮᚢ ᚢᛔ, ᚿᛂᚡᛂᚱ ᚵᚮᚿᚿᛆ ᛚᛂᛐ ᚤᚮᚢ ᛑᚮᚡᚿᛖᚠᛖᚱ ᚷᚩᚾᚾᚪ ᚷᛁᚠᛖ ᛁᚩᚢ ᚢᛈ, ᚾᛖᚠᛖᚱ ᚷᚩᚾᚾᚪ ᛚᛖᛏ ᛁᚩᚢ ᛞᚩᚹᚾ"
pw = []

def passwordinator():
    pw.clear()
    n = 0
    try:
        length = int(length_entry.get())
    except ValueError:
        password_label.config(text="Enter a valid number, dummy.")
        return
    while n <= length:
        a = random.choice([letters, numbers, characters, runes])
        if a == letters:
            pw.append(a[random.randint(0,51)])
        elif a == numbers:
            pw.append(a[random.randint(0,9)])
        elif a == runes:
            pw.append(a[random.randint(0, len(runes))])
        else:
            pw.append(a[random.randint(0,9)])
        n += 1
    password = ''.join(pw)
    password_label.config(text=f"The PASSWORDINATOR Suggests:\n{password}")

def clipboard():
    window.clipboard_clear()
    window.clipboard_append(password_label.cget("text").replace("The PASSWORDINATOR Suggests:\n", ""))
    window.update()  
    copy_label.config(text="Password copied! Now don't go writing it down everywhere.") 

window = tk.Tk()
window.title("UltraSecurePasswordinatorX2000")
window.geometry("500x300")
window.configure(bg="#2E2E2E")  

title_label = tk.Label(window, text="Passwordinator", font=("Comic Sans", 18), fg="#FFFFFF", bg="#2E2E2E")
title_label.pack(pady=10)

length_entry = tk.Entry(window, font=("Comic Sans", 14))
length_entry.pack(pady=5)
length_entry.insert(0, "20")  

generate_button = tk.Button(window, text="Passwordinate", command=passwordinator, font=("Comic Sans", 12), bg="#4E4E4E", fg="#FFFFFF")
generate_button.pack(pady=10)

password_label = tk.Label(window, text="Your password will appear here...", font=("Comic Sans", 12), fg="#FFFFFF", bg="#2E2E2E")
password_label.pack(pady=10)

copy_button = tk.Button(window, text="Copy This Abomination", command=clipboard, font=("Comic Sans", 12), bg="#4E4E4E", fg="#FFFFFF")
copy_button.pack(pady=5)

copy_label = tk.Label(window, text="", font=("Comic Sans", 10), fg="#00FF00", bg="#2E2E2E")
copy_label.pack()

window.mainloop()
