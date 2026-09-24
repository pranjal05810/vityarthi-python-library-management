# 📚 Library Management System

## 📌 Project Overview

The **Library Management System** is a beginner-level Python project developed as part of the **Vityarthi Python Essentials Course**.

The project is designed to simplify basic library operations such as viewing books, searching for books, adding new books, issuing books, and returning books.

The system uses fundamental Python programming concepts including **lists, dictionaries, functions, conditional statements, loops, and user input**.

---

## 🎯 Objectives

“project aims to reduce unnecessary crowding and waiting time in the library by providing a simple digital system through which students can search for books and check their availability quickly.”

- **Reduce manual record-keeping:** Replace the need to maintain book records manually by storing book information digitally using Python.

- **Make book searching easier:** Allow users to quickly search for a particular book instead of checking through a large number of book records manually.

- **Track book availability:** Clearly show whether a book is available or has already been issued, helping users avoid confusion.

- **Simplify book issuing and returning:** Provide separate options for issuing and returning books so that the status of each book can be updated easily.

- **Improve data organization:** Store book details such as book ID, title, author, and availability in a structured format using Python lists and dictionaries.

- **Reduce human errors:** Use program-based operations to update book records consistently and reduce mistakes that can occur during manual record management.

- **Provide a simple user interface:** Use a menu-driven system so that users can easily select and perform different library operations.

- **Demonstrate a practical use of Python:** Apply basic Python concepts such as functions, loops, conditional statements, lists, and dictionaries to solve a real-world problem.
---

## ✨ Features

The system provides the following features:

### 1. 📖 Display Books
Displays the list of books available in the library along with their details and availability status.

### 2. 🔍 Search Book
Allows the user to search for a book using its title.

### 3. ➕ Add New Book
Allows the user to add a new book by entering its title and author name.

### 4. 📤 Issue Book
Allows a user to issue an available book from the library.

### 5. 📥 Return Book
Allows a user to return a previously issued book.

### 6. 📊 Book Availability
Displays whether a particular book is currently available or issued.

### 7. 📅 **Due Date Reminder**
- 🔔 **Displays the due date** of books currently issued to students.
- 📚 Shows the **book title and due date** clearly.
- ⏰ Checks whether the book is **due or overdue**.
- ⚠️ Displays an **OVERDUE** status when the return date has passed.
- 📆 Shows the **number of days the book is late**.
- 🎯 Helps students **return books on time**.
- 👥 Helps **reduce crowding** by providing quick access to book and due-date information.

### 8. 💰 **Fine Calculation**
- 🔍 Automatically checks whether a book has been **returned late**.
- 📆 Calculates the **number of late days**.
- 💵 Calculates the fine using a **fixed fine amount per day**.
- 🧮 The fine is calculated using:

### 9. ❌ Exit
Allows the user to safely exit the application.

---

## 🛠️ Technologies and Tools Used

### Programming Language
- **Python 3**

### Python Concepts Used
- Variables
- Data Types
- Lists
- Dictionaries
- Functions
- `if-elif-else` statements
- `for` and `while` loops
- User input
- String operations
- Boolean values

### Development Tools
- Visual Studio Code
- GitHub

---

## 📂 Project Structure

```text
Library-Management-System/
│
├── library_management.py
├── README.md
├── statement.md
│
└── screenshots

🚀 Steps to Install & Run the Project
Download or clone the project repository from GitHub.
Make sure Python 3.x is installed on your computer.
Open the project folder in VS Code, IDLE, PyCharm, or Google Colab.
Open the Python file, for example:
library_management.py
Run the Python program.
Follow the menu displayed on the screen and enter the required details.
You can perform operations such as:
📚 View available books
🔍 Search for a book
📖 Issue a book
🔄 Return a book
⏰ Check due-date reminders
💰 Calculate the fine for late returns
The program will display the result directly in the console.
💡 Requirements
Python 3.x
No external libraries are required.
The project uses basic Python concepts such as Lists, Dictionaries, Functions, Conditional Statements, and Loops.
🧪 Instructions for Testing

To test the Library Management System:

▶️ Run the program and check whether the main menu appears correctly.
📚 Select the option to display books and verify that the book list is shown.
🔍 Search for an existing book and confirm that the correct book details are displayed.
❌ Search for a book that does not exist and verify that an appropriate message is displayed.
📖 Issue a book and check whether its availability is updated.
🔄 Return the issued book and verify that it becomes available again.
⏰ Test the due-date reminder using an issued book and check whether the reminder is displayed correctly.
💰 Test the fine calculation by entering a late return and verify that the fine amount is calculated correctly.
🔁 Try different menu options to ensure the program handles user input correctly.
🛑 Test invalid inputs and confirm that the program gives a suitable error message instead of stopping unexpectedly.
