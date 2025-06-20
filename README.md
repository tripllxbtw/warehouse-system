# 📦 Warehouse Management System

**Warehouse Management System** is a simple desktop application written in Python with a graphical user interface (GUI). It helps you manage your warehouse: add products, update quantities, search for products, and delete them. All data is saved to a JSON file for persistent storage.

---

## 🚀 Features

✅ Add new products  
✅ View all products  
✅ Search for a product by name  
✅ Update product quantity  
✅ Delete a product  
✅ Save data to `warehouse_gui.json`  
✅ GUI built with **Tkinter**  
✅ Prebuilt **.exe file** for easy use on Windows

---

## 🗂️ Where data is stored

All data is automatically saved to:
```
/home/tripllex/Documents/warehouse_gui.json
```

If you run the `.exe` version — the JSON file will be created in the same folder as the `.exe`.

---

## ⚙️ How to run the project

### ✅ 1. Python version (source code)

- Make sure you have **Python 3** installed.
- No extra dependencies required — all are built-in.
- Run the script:
  ```bash
  python warehouse_gui.py
  ```

### ✅ 2. EXE version (Windows)

- In the `dist` folder, you will find `warehouse_gui.exe`.
- Double-click to run — no Python installation needed.
- All data will be saved in the same folder as the `.exe`.

---

## 🖼️ GUI Example

![screenshot]([(https://imgur.com/a/rkN5swZ))  

---

## 💡 Technologies

- Python 3
- Tkinter
- JSON
- PyInstaller (to build the `.exe`)

---

## ⚡ How to build your own `.exe`

If you want to build the `.exe` yourself:
```bash
pip install pyinstaller
pyinstaller --onefile --noconsole warehouse_gui.py
```

After building, the file will appear in the `dist/` folder.

---

## 📝 Author

> Program by **tripllxbtw**
