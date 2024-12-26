import tkinter as tk
from tkinter import messagebox


def on_click():
    messagebox.showinfo("название окошка", "Произошел тык")

root = tk.Tk()
root.title("Демонстрация Tkinter")
root.geometry("400x200")

label = tk.Label(root, text="мега-приложение", font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(root, text="Тыкни", font=("Arial", 12), command=on_click)
button.pack(pady=10)

if __name__ == "__main__":
    root.mainloop()
