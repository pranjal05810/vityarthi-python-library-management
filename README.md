Library Management System

1.Project Title

Library Management System

2.Project Overview

I made this Library Management System as my project for the Vityarthi Python Essential Course.

I chose this project because students often need to check whether a book is available, search for a particular book, or know when an issued book has to be returned. Doing these things manually can take extra time and may also create unnecessary crowd at the library counter.

This project is a simple Python program that helps with these basic tasks. It allows the user to view books, search for a book, check its availability, issue a book and return it.

I have also added a due date for issued books. If a book is returned after the due date, the program calculates the fine according to the number of late days.

For the sample data, I have included books from Coding, Engineering Mathematics, Physics and Environmental Studies.


3.Objectives

The main objectives of this project are:

- To make some basic library activities easier.
- To help students find books more quickly.
- To check whether a book is available or already issued.
- To keep track of issued books.
- To show the due date of an issued book.
- To calculate a fine if a book is returned late.
- To reduce unnecessary waiting and crowd at the library counter.
- To apply the Python concepts learned during the course to a practical problem.


4.Features

* View Books

The user can see the books available in the library.

* Search Book

The user can search for a particular book from the library collection.

* Check Availability

The program shows whether a book is available or has already been issued.

* Issue Book

If the required book is available, the user can issue it.

* Due Date

After issuing a book, the program provides a due date for returning it.

* Due Date Reminder

The user can check the due date of an issued book so that the book can be returned on time.

* Return Book

The user can return an issued book. After returning it, the book becomes available again.

* Fine Calculation

If a book is returned after its due date, the program calculates the fine based on the number of late days.

For example:

    Late days = 3
    Fine per day = ₹10

    Total fine = 3 × ₹10
               = ₹30

* Menu-Based Program

The different operations are available through a simple menu. The user can select an option according to what they want to do.

* Book Categories

The sample books used in the project are related to:

- Coding
- Engineering Mathematics
- Physics
- Environmental Studies


5.Technologies and Concepts Used

Technology

- Python
- GitHub
- VS Code / Google Colab

Python Concepts

I used the basic Python concepts that I learned during the course, such as:

- Variables
- Lists
- Dictionaries
- Functions
- `if-else`
- `for` loop
- `while` loop
- User input
- Strings
- Basic calculations
- Date handling

The main purpose was to understand how these concepts can be combined to make a small working application.

6.Project Files

The project repository contains the following files:

    Library-Management-System/
    │
    ├── README.md
    ├── statement.md
    ├── library_management.py
    └── screenshots/

Files in the Project

README.md  
Contains information about the project, its features and instructions.

statement.md
Contains the problem statement, scope, target users and high-level features.

library_management.py  
Contains the main Python code of the project.

screenshots  
Contains screenshots of the program while testing different features.


7.Installation and Running the Project

Step 1: Install Python

First, Python should be installed on the computer.

To check whether Python is already installed, open Command Prompt or Terminal and type:

    python --version

If Python is installed correctly, its version will be displayed.



Step 2: Download the Project

Download the project from the GitHub repository.

Step 3: Open the Project Folder

After downloading the project, open its folder.

The main Python file is:

    library_management.py



Step 4: Open Terminal

Open Command Prompt or Terminal in the project folder.

If using VS Code, the terminal can be opened from:

    Terminal → New Terminal

Step 5: Run the Program

Type the following command:

    python library_management.py

Press Enter

The Library Management System menu should now appear.

8. Instructions for Testing

The project can be tested by selecting the different options shown in the program menu.

Test 1: Display Books

1. Run the Python program.
2. Select the option to display books.
3. Check the books shown on the screen.

Expected result:  
The program should display the books stored in the library.

Test 2: Search for a Book

1. Select the search option.
2. Enter the name of a book.
3. Check the result.

Expected result: 
If the book exists, its details should be displayed.

If it does not exist, the program should display a suitable message.

Test 3: Check Book Availability

1. Select the availability option.
2. Enter the required book information.

Expected result:
The program should tell whether the book is available or already issued.

Test 4: Issue a Book

1.Select the issue-book option.
2.Enter the required details.
3.Select an available book.

Expected result:
The book should be issued successfully and its due date should be shown.

Test 5: Check Due Date

1.Issue a book.
2.Select the option for checking the issued book or due date.

Expected result: 
The program should display the due date of the book.

Test 6: Return a Book on Time

1. Select the return-book option.
2. Enter the required details.
3. Return the book on or before the due date.

Expected result:  
The book should be returned successfully and no late fine should be charged.

Test 7: Return a Book Late

1.Select the return-book option.
2.Enter a return date after the due date.
3.Check the result.

Expected result: 
The program should calculate the number of late days and display the fine.

Example:

Due Date: 30 September
Return Date: 3 October

Late Days: 3
Fine per day: ₹10
Total Fine: ₹30

Test 8: Invalid Input

1. Start the program.
2. Enter an option that is not present in the menu.

Expected result:  
The program should display an appropriate message instead of stopping suddenly.


9. Screenshots

Screenshots of the project are included in the screenshots folder.

The screenshots show the working of different parts of the program, such as:

* Main menu
* List of books
* Book search
* Book availability
* Book issue
* Due date
* Book return
* Fine calculation

These screenshots are included as proof of testing and to show the output of the project.

10. Book Categories

The project contains sample books from four main categories:

Coding, Python, Programming, Data Structures
Engineering Mathematics ,Calculus, Algebra, Mathematics 
Physics , Mechanics, Optics, Engineering Physics
Environmental Studies ,Ecology, Environment, Sustainability


