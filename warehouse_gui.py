import os
import json
import tkinter as tk
from tkinter import simpledialog, messagebox

# Путь к JSON-файлу для хранения данных
DATA_FILE = "/home/tripllex/Документы/warehouse_gui.json" #You can change this path to your desired location
warehouse = {}

# Загрузка данных из JSON
def load_data():
    global warehouse
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            warehouse = json.load(f)
    else:
        warehouse = {}

# Сохранение данных в JSON
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(warehouse, f, indent=4)
    messagebox.showinfo("Saved", "Data saved successfully!")

# Добавление продукта
def add_product():
    name = simpledialog.askstring("Input", "Enter product name:")
    quantity = simpledialog.askinteger("Input", "Enter quantity:")
    category = simpledialog.askstring("Input", "Enter category:")

    if not name or not quantity or not category:
        messagebox.showwarning("Warning", "All fields are required!")
        return

    if name in warehouse:
        warehouse[name]['quantity'] += quantity
    else:
        warehouse[name] = {
            "quantity": quantity,
            "category": category
        }

    messagebox.showinfo("Success", f"Product '{name}' added.")

# Показать все товары
def show_products():
    if not warehouse:
        messagebox.showinfo("Empty", "Warehouse is empty.")
        return
    text = ""
    for name, info in warehouse.items():
        text += f"{name} - Quantity: {info['quantity']}, Category: {info['category']}\n"
    messagebox.showinfo("Products", text)

# Обновление количества
def update_quantity():
    name = simpledialog.askstring("Update", "Enter product name to update:")
    if name not in warehouse:
        messagebox.showwarning("Error", f"Product '{name}' not found.")
        return
    quantity = simpledialog.askinteger("Update", f"Enter new quantity for '{name}':")
    warehouse[name]['quantity'] = quantity
    messagebox.showinfo("Updated", f"Quantity of '{name}' updated.")

# Удаление продукта
def delete_products():
    name = simpledialog.askstring("Delete", "Enter product name to delete:")
    if name in warehouse:
        del warehouse[name]
        messagebox.showinfo("Deleted", f"Product '{name}' deleted.")
    else:
        messagebox.showwarning("Error", f"Product '{name}' not found.")

# Поиск продукта
def search_products():
    name = simpledialog.askstring("Search", "Enter product name to search:")
    if name in warehouse:
        info = warehouse[name]
        messagebox.showinfo("Found", f"{name} - Quantity: {info['quantity']}, Category: {info['category']}")
    else:
        messagebox.showwarning("Not Found", f"Product '{name}' not found.")

# Интерфейс
root = tk.Tk()
root.title("Warehouse Management System")
root.geometry("600x700")

tk.Button(root, text="Add Product", width=40, font=("Arial", 16), command=add_product).pack(pady=5)
tk.Button(root, text="Show All Products", width=40, font=("Arial", 16), command=show_products).pack(pady=5)
tk.Button(root, text="Update Quantity", width=40, font=("Arial", 16), command=update_quantity).pack(pady=5)
tk.Button(root, text="Delete Product", width=40, font=("Arial", 16), command=delete_products).pack(pady=5)
tk.Button(root, text="Search Product", width=40, font=("Arial", 16), command=search_products).pack(pady=5)
tk.Button(root, text="Save Data", width=40, font=("Arial", 16), command=save_data).pack(pady=5)
tk.Button(root, text="Exit", width=40, font=("Arial", 16), command=root.destroy).pack(pady=20)

tk.Label(root, text="Program by tripllxbtw", font=("Arial", 12)).pack(pady=70)

# Загрузка данных при запуске
load_data()

root.mainloop()
