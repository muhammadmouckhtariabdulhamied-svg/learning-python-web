import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

def show_date():
    selected_date = cal.get_date()
    date_label.config(text=f"Selected Date: {selected_date}")

root = tk.Tk()
root.title("Digital Calendar")
root.geometry("500x400")

cal = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
cal.pack(pady=20)

date_label = ttk.Label(root, text="")
date_label.pack(pady=10)

btn = ttk.Button(root, text="Show Date", font=("Calibri", 12), command=show_date)
btn.pack(pady=10)

root.mainloop()