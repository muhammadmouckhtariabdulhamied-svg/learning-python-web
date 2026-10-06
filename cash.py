
prices ={"banana": 133, "apple": 7, "orange": 9.5 ,}
item = input("Enter your item ").lower()

if item in prices:
    print(f"{item} is {prices[item]}")
else:
    print("item not available now")
import tkinter as tk
from tkinter import messagebox


   