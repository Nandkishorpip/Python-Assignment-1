import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(1000, update_time)  # Update every 1000 ms (1 second)

root = tk.Tk()
root.title("Digital Clock")

root.geometry("300x100")
root.configure(bg="black")

label = tk.Label(root, text="", font=("Helvetica", 40), fg="cyan", bg="black")
label.pack(expand=True)

update_time()

root.mainloop()
