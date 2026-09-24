#Vit bhopal library management systeum

from datetime import datetime, timedelta
FINE_PER_DAY = 5

print("WELCOME TO VIT BHOPAL AB2 LIBRARY")

#list containing dictionaries
library = [{ "id": 101, "title": "Python Programming", "author": "John Zelle", "category": "Coding", "available": True },
            { "id": 102, "title": "Let Us C", "author": "Yashavant Kanetkar", "category": "Coding", "available": True },
              { "id": 103, "title": "Programming in C", "author": "Dennis Ritchie", "category": "Coding", "available": True },
                { "id": 104, "title": "The C Programming Language", "author": "Brian Kernighan", "category": "Coding", "available": True },
                  { "id": 105, "title": "Java Programming", "author": "Herbert Schildt", "category": "Coding", "available": True }, 
                  { "id": 106, "title": "Head First Java", "author": "Kathy Sierra", "category": "Coding", "available": True }, 
                  { "id": 107, "title": "Data Structures Using C", "author": "Reema Thareja", "category": "Coding", "available": True },
                    { "id": 108, "title": "Data Structures and Algorithms", "author": "Narasimha Karumanchi", "category": "Coding", "available": True },
                      { "id": 109, "title": "Introduction to Algorithms", "author": "Thomas H. Cormen", "category": "Coding", "available": True }, 
                      { "id": 110, "title": "Computer Programming", "author": "R. G. Dromey", "category": "Coding", "available": True },
                        { "id": 111, "title": "Learning Python", "author": "Mark Lutz", "category": "Coding", "available": True },
                          { "id": 112, "title": "Automate the Boring Stuff with Python", "author": "Al Sweigart", "category": "Coding", "available": True }, 
                          { "id": 113, "title": "Clean Code", "author": "Robert C. Martin", "category": "Coding", "available": True }, 
                          { "id": 201, "title": "Higher Engineering Mathematics", "author": "B. S. Grewal", "category": "Engineering Mathematics", "available": True }, 
                          { "id": 202, "title": "Engineering Mathematics", "author": "R. K. Jain", "category": "Engineering Mathematics", "available": True }, 
                          { "id": 203, "title": "Advanced Engineering Mathematics", "author": "Erwin Kreyszig", "category": "Engineering Mathematics", "available": True },
                            { "id": 204, "title": "Engineering Mathematics Volume 1", "author": "H. K. Dass", "category": "Engineering Mathematics", "available": True },
                              { "id": 205, "title": "Engineering Mathematics Volume 2", "author": "H. K. Dass", "category": "Engineering Mathematics", "available": True },
                                { "id": 206, "title": "Calculus", "author": "Thomas Finney", "category": "Engineering Mathematics", "available": True },
                                  { "id": 207, "title": "Differential Equations", "author": "S. L. Ross", "category": "Engineering Mathematics", "available": True }, 
                                  { "id": 208, "title": "Linear Algebra", "author": "Gilbert Strang", "category": "Engineering Mathematics", "available": True },
                                    { "id": 209, "title": "Probability and Statistics", "author": "S. C. Gupta", "category": "Engineering Mathematics", "available": True },
                                      { "id": 210, "title": "Numerical Methods", "author": "S. S. Sastry", "category": "Engineering Mathematics", "available": True }, 
                                      { "id": 211, "title": "Discrete Mathematics", "author": "Kenneth Rosen", "category": "Engineering Mathematics", "available": True },
                                        { "id": 212, "title": "Complex Variables", "author": "R. K. Jain", "category": "Engineering Mathematics", "available": True },
                                          { "id": 301, "title": "Concepts of Physics Volume 1", "author": "H. C. Verma", "category": "Physics", "available": True },
                                            { "id": 302, "title": "Concepts of Physics Volume 2", "author": "H. C. Verma", "category": "Physics", "available": True }, 
                                            { "id": 303, "title": "Fundamentals of Physics", "author": "Halliday and Resnick", "category": "Physics", "available": True }, { "id": 304, "title": "University Physics", "author": "Young and Freedman", "category": "Physics", "available": True }, 
                                            { "id": 305, "title": "Engineering Physics", "author": "Gaur and Gupta", "category": "Physics", "available": True }, { "id": 306, "title": "Modern Physics", "author": "Arthur Beiser", "category": "Physics", "available": True }, { "id": 307, "title": "Optics", "author": "Ajoy Ghatak", "category": "Physics", "available": True },
                                              { "id": 308, "title": "Introduction to Electrodynamics", "author": "David J. Griffiths", "category": "Physics", "available": True },
                                                { "id": 309, "title": "Thermal Physics", "author": "Kittel and Kroemer", "category": "Physics", "available": True },
                                                  { "id": 310, "title": "Quantum Physics", "author": "Stephen Gasiorowicz", "category": "Physics", "available": True },
                                                    { "id": 311, "title": "Solid State Physics", "author": "Charles Kittel", "category": "Physics", "available": True },
                                                      { "id": 312, "title": "Classical Mechanics", "author": "John R. Taylor", "category": "Physics", "available": True },
                                                      { "id": 401, "title": "Environmental Studies", "author": "Erach Bharucha", "category": "Environmental Studies", "available": True },
                                                        { "id": 402, "title": "Environmental Science", "author": "Daniel D. Chiras", "category": "Environmental Studies", "available": True },
                                                          { "id": 403, "title": "Environmental Engineering", "author": "Peavy, Rowe and Tchobanoglous", "category": "Environmental Studies", "available": True },
                                                            { "id": 404, "title": "Ecology and Environment", "author": "P. D. Sharma", "category": "Environmental Studies", "available": True }, 
                                                            { "id": 405, "title": "Environmental Pollution", "author": "R. K. Trivedy", "category": "Environmental Studies", "available": True },
                                                              { "id": 406, "title": "Biodiversity Conservation", "author": "K. V. Krishnamurthy", "category": "Environmental Studies", "available": True },
                                                                { "id": 407, "title": "Climate Change", "author": "Andrew Dessler", "category": "Environmental Studies", "available": True },
                                                                  { "id": 408, "title": "Renewable Energy", "author": "Godfrey Boyle", "category": "Environmental Studies", "available": True },
                                                                    { "id": 409, "title": "Environmental Management", "author": "S. P. Mahajan", "category": "Environmental Studies", "available": True },
                                                                      { "id": 410, "title": "Sustainable Development", "author": "M. K. Ghosh", "category": "Environmental Studies", "available": True },
                                                                        { "id": 411, "title": "Water Pollution and Control", "author": "S. P. Mahajan", "category": "Environmental Studies", "available": True },
                                                                          { "id": 412, "title": "Waste Management", "author": "K. Sasikumar", "category": "Environmental Studies", "available": True }, 
                                                                          { "id": 114, "title": "Effective Python", "author": "Brett Slatkin", "category": "Coding", "available": True },
                                                                            { "id": 115, "title": "Python Crash Course", "author": "Eric Matthes", "category": "Coding", "available": True }, 
                                                                            { "id": 116, "title": "Programming Logic", "author": "Joyce Farrell", "category": "Coding", "available": True }, 
                                                                            { "id": 117, "title": "Computer Fundamentals", "author": "P. K. Sinha", "category": "Coding", "available": True },
                                                                              { "id": 118, "title": "Web Technologies", "author": "Uttam K. Roy", "category": "Coding", "available": True },
                                                                                { "id": 119, "title": "Object Oriented Programming", "author": "Robert Lafore", "category": "Coding", "available": True }, 
                                                                                { "id": 120, "title": "Database Management Systems", "author": "Raghu Ramakrishnan", "category": "Coding", "available": True }, 
                                                                                { "id": 121, "title": "Artificial Intelligence", "author": "Stuart Russell", "category": "Coding", "available": True}]

# Function to add a book
def add_book():
    book_id = int(input("Enter Book ID: "))
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    }

    library.append(book)
    print("Book added successfully!")

#function to display all books
def display_book():
    print("\n======VIT BHOPAL LIBRARY BOOKS======")

    if len(library) == 0:
        print("No Books Available.")
    else:
        for book in library:
            print("Book ID:",book["id"])
            print("Title:",book["title"])
            print("Author:",book["author"])

            if book["available"]:
                print("Status:Available")
            else:
                print("Status: Issued")

            print("--------------------------------") 

# Function to search a book
def search_book():
    title = input("Enter book title to search: ")

    found = False

    for book in library:
        if book["title"].lower() == title.lower():
            print("\nBook Found!")
            print("Book ID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])

            if book["available"]:
                print("Status: Available")
            else:
                print("Status: Issued")

            found = True
            break

    if not found:
        print("Book not found.")        

# Function to issue a book
def issue_book():
    book_id = int(input("Enter book ID to issue: "))

    for book in library:
        if book["id"] == book_id:

            if book["available"]:
                book["available"] = False

                issue_date = datetime.now()
                due_date = issue_date + timedelta(days=7)

                book["issue_date"] = issue_date
                book["due_date"] = due_date

                print("\nBook issued successfully!")
                print("Issue Date:", issue_date.strftime("%d-%m-%Y"))
                print("Due Date:", due_date.strftime("%d-%m-%Y"))

            else:
                print("Book is already issued.")

            return

    print("Book not found.")

# Function to return a book
def return_book():
    book_id = int(input("Enter book ID to return: "))

    for book in library:
        if book["id"] == book_id:

            if not book["available"]:

                fine = calculate_fine(book["due_date"])

                book["available"] = True

                print("\nBook returned successfully.")
                print("Final Fine: ₹", fine)

                return

            else:
                print("Book is already available.")

                return

    print("Book not found.")

#Fine Calculation
def calculate_fine(due_date):
    today = datetime.name()

    if today > due_date:
        late_days = (today - due_date).days
        fine = late_days*FINE_PER_DAY

        print("Bool is overdue.")
        print("Late Days:",late_days)
        print("Fine:₹",fine)

        return fine

    else:
        print("Book is returened on time.")
        print("Fine:₹",fine)

        return 0

#Due Due Date Reminder
def due_date_reminder():
    print("\n===== DUE DATE REMINDER =====")

    found = False

    for book in library:

        if not book["available"]:

            found = True

            today = datetime.now()
            due_date = book["due_date"]

            print("\nBook:", book["title"])
            print("Due Date:", due_date.strftime("%d-%m-%Y"))

            if today > due_date:
                late_days = (today - due_date).days
                print("Status: OVERDUE")
                print("Late by:", late_days, "days")

            else:
                remaining_days = (due_date - today).days
                print("Status: Available for return")
                print("Days remaining:", remaining_days)

    if not found:
      print("No books are currently issued.")

# Main program
while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        display_book()

    elif choice == "3":
        search_book()

    elif choice == "4":
        issue_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
      due_date_reminder()

    elif choice == "7":
        print("Thank you for using Library Management System!")
        break
    else:
        print("Invalid choice. Please try again.")      
            
