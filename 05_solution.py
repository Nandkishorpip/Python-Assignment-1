import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

# Corrected capitalization of tk.TK to tk.Tk
root = tk.Tk()
root.title("Digital Clock")

clock_label = tk.Label(root, font=("Helvetica", 48), bg="black", fg="cyan")
clock_label.pack(anchor="center", pady=50)

update_time()

root.mainloop()
