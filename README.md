# 🧮 Calculator App using Python (Tkinter)

A simple GUI calculator built using Python's built-in `tkinter` module. This app performs basic arithmetic operations and demonstrates a modular, problem-solving approach to building Python GUI applications.

---

## 🚀 Features

- User-friendly GUI
- Supports basic operations: `+`, `−`, `×`, `÷`
- Entry field to input expressions
- `=` button to evaluate result
- `C` button to clear input
- Basic error handling (e.g. divide by zero)

---

## 📌 Problem-Solving Framework Used

### 🔶 1. Understand the Problem
- Goal: Build a calculator for basic math operations
- Interface: Graphical (not console-based)
- Input: User clicks buttons to form expressions
- Output: Result shown in display field

---

### 🔶 2. Define Core Features
- Input via on-screen buttons
- Display evaluated result
- Clear button to reset input
- Error handling for invalid expressions

---

### 🔶 3. Decide Interface
- Chosen: **GUI** using `tkinter`
- Alternative: Console version using `input()` (not used here)

---

### 🔶 4. Sketch UI / Wireframe
- Top: Display field (Entry)
- Grid of buttons: Numbers (0–9), Operators (`+`, `-`, `*`, `/`)
- Bottom row: Clear (`C`) and Equal (`=`)

---

### 🔶 5. Design Architecture
- **UI**: Main window, layout using Frames and Buttons
- **Logic**: Functions for click handling, evaluation, clear
- **Error Handling**: Wrap evaluation in try/except

---

### 🔶 6. Implement in Layers
1. Create window and layout
2. Add display field
3. Add number/operator buttons
4. Add button functions
5. Implement evaluation logic
6. Add clear button
7. Style the UI

---

### 🔶 7. Test Edge Cases
- `Divide by zero`: Shows "Error"
- `Multiple operations`: Handles well via `eval()`
- `Invalid input`: Caught using try/except

---

### 🔶 8. Improvisation
- Modularized code using functions
- Easy to extend with scientific functions
- Optional: Add keyboard support or expression history

---

## 🛠️ Technologies Used

- Python 3.x
- Tkinter (built-in GUI toolkit)

---

## 🧪 How to Run

1. Clone this repository or copy the code.
2. Run the Python file:

```bash
python calculator.py
