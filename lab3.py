import tkinter as tk
from tkinter import filedialog
import os
from datetime import datetime
import random

class FileDateChangerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Зміна дати файлу")
        
        self.path = None
        
        self.label = tk.Label(root, text="Виберіть файл:")
        self.label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        
        self.select_button = tk.Button(root, text="Оберіть файл", command=self.select_file)
        self.select_button.grid(row=0, column=1, padx=10, pady=5)
        
        self.date_label = tk.Label(root, text="Введіть нову дату:")
        self.date_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        self.year_label = tk.Label(root, text="Рік:")
        self.year_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        
        self.year_var = tk.StringVar()
        self.year_var.set(random.randint(1990, 2024))  # випадковий рік за замовчуванням
        self.year_entry = tk.OptionMenu(root, self.year_var, *range(1990, 2025))
        self.year_entry.grid(row=2, column=1, padx=10, pady=5)
        
        self.month_label = tk.Label(root, text="Місяць:")
        self.month_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        
        self.month_var = tk.StringVar()
        self.month_var.set(random.randint(1, 12))  # випадковий місяць за замовчуванням
        self.month_entry = tk.OptionMenu(root, self.month_var, *range(1, 13))
        self.month_entry.grid(row=3, column=1, padx=10, pady=5)
        
        self.day_label = tk.Label(root, text="День:")
        self.day_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        
        self.day_var = tk.StringVar()
        self.day_var.set(random.randint(1, 31))  # випадковий день за замовчуванням
        self.day_entry = tk.OptionMenu(root, self.day_var, *range(1, 32))
        self.day_entry.grid(row=4, column=1, padx=10, pady=5)
        
        self.change_button = tk.Button(root, text="Змінити дату", command=self.change_date)
        self.change_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        
    def select_file(self):
        self.path = filedialog.askopenfilename()
        
    def change_date(self):
        if self.path is None:
            tk.messagebox.showerror("Помилка", "Будь ласка, виберіть файл.")
            return
        
        try:
            year = int(self.year_var.get())
            month = int(self.month_var.get())
            day = int(self.day_var.get())
            new_date = datetime(year, month, day)
            os.utime(self.path, (new_date.timestamp(), new_date.timestamp()))
            tk.messagebox.showinfo("Успіх", "Дата файлу успішно змінена.")
        except Exception as e:
            tk.messagebox.showerror("Помилка", f"Помилка при зміні дати файлу: {e}")

root = tk.Tk()
app = FileDateChangerApp(root)
root.mainloop()
