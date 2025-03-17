# 🍩 Donut Recipe Calculator

## 📌 Introduction

The **Donut Recipe Calculator** is a Python-based GUI application that calculates ingredient quantities for making donuts based on user input. The user enters the number of donuts to be made, and the app provides a list of required ingredients, adjusting for normal and cold weather conditions.

## 📜 Table of Contents

- [Introduction](#-introduction)  
- [Features](#-features)  
- [Installation](#-installation)  
- [Usage](#-usage)  
- [Dependencies](#-dependencies)  
- [Configuration](#-configuration)  
- [Example](#-example)  
- [Troubleshooting](#-troubleshooting)  
- [Contributors](#-contributors)  
- [License](#-license)  

## ✨ Features

- **Graphical User Interface (GUI)** built with **Tkinter**  
- Dynamically calculates ingredient amounts based on user input  
- Supports two weather conditions: **Normal** and **Cold**  
- Saves the ingredient list to `ingredientes.txt`  
- **Print functionality** (Windows-specific, currently commented out)  
- Simple and lightweight application  

## 💾 Installation

### Prerequisites

Ensure you have **Python 3.x** installed on your system.

### Steps

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/donut-dough-calculator.git
   cd donut-dough-calculator
   ```

2. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the application:
   ```sh
   python app.py
   ```

## 🚀 Usage

1. Enter the number of donuts you want to make in the input box.  
2. Click on:
   - **"Normal Weather"** for standard ingredient calculations.  
   - **"Cold Weather"** to adjust yeast quantity for colder conditions.  
3. View the calculated ingredients in the text box.  
4. Click **"Print File"** to print the `ingredientes.txt` file (Windows only).  
5. Click **"Delete"** to clear the ingredient list.  

## 📦 Dependencies

This project uses the following Python libraries:

- `tkinter` (built-in with Python)  
- `Pillow` (for handling images)  
- `time` (built-in)  
- `pathlib` (built-in)  

To install dependencies manually, run:

```sh
pip install pillow
```

## ⚙️ Configuration

The default ingredient list is stored in the Python dictionary:

```python
ingredients = {
    'Harina': 35.2564,
    'Margarina': 1.839,
    'Manteca': 1.839,
    'Huevo': 5.288,
    'Azucar': 5.64312,
    'Agua': 12.7,
    'Sal': 0.29,
    'Levadura': 0.3522
}
```

For **cold weather**, the yeast (`Levadura`) is reduced by 30%.

## 📌 Example

If the user enters `10` donuts, the output might look like:

```
Receta de donas para 10 donas
Clima: Normal     Hora: 12:30:45 | 17/03/25
---------------------------------
Harina: 352.564
Margarina: 18.39
Manteca: 18.39
Huevo: 52.88
Azucar: 56.4312
Agua: 127.0
Sal: 2.9
Levadura: 3.522
```

## ❗ Troubleshooting

- **Issue:** App doesn't open  
  **Solution:** Ensure you have installed all dependencies using `pip install pillow`.  

- **Issue:** Image not found  
  **Solution:** Ensure `donut.png` is in the same directory as `app.py`.  

- **Issue:** Print function doesn't work  
  **Solution:** The `win32print` module is required for printing on Windows. Install it using:  
  ```sh
  pip install pywin32
  ```

## 👥 Contributors

- Anthony Kummerfeldt- **Developer**  

## 📜 License

This project is licensed under the **MIT License**.  
