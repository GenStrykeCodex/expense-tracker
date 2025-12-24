# Expense Tracker (CLI) – v1.0

A simple **Command-Line Expense Tracker** built using Python.  
This application allows users to record daily expenses, view all records, and calculate total spending with persistent file storage.

---

## Features

- Add daily expenses with:
  - Date (auto-filled)
  - Category
  - Amount
  - Short description
- View all recorded expenses in a table format
- Calculate total expenses
- Persistent storage using a text file
- Menu-driven and user-friendly CLI
- Input validation for expense amount

---

## Technologies Used

- Python 3
- File handling (`.txt`)
- Lists
- Functions
- Loops and conditionals
- `datetime` module

---

## Project Structure

- `main.py` → Main application logic  
- `expenses.txt` → Stores expense records  

---

## Usage

### Main Menu Options

1. Add an expense
2. View all expenses
3. Check total expenses
4. Exit

### Expense Categories

* Food
* Travel
* Rents
* Utilities
* Other

---

## Expense File Format

Each expense is stored in the following format:


`YYYY-MM-DD,Category,Amount,Note`

Example:

`2025-01-12,Food,250,Lunch`

---

## Concepts Covered

* Persistent data storage
* Menu-driven program design
* Input validation
* Basic financial calculations
* Clean CLI navigation

---

## Future Improvements

* Category-wise expense summary
* Monthly / yearly reports
* Edit or delete expenses
* Custom date input
* GUI version using Tkinter

---

## Version

First release: **v1.0** on **24 December 2025**

---

## Author

Developed by **GenStryke Codex**

---

## License

This project is licensed under the MIT License.

---