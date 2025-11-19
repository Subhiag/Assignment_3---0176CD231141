
import random
from datetime import datetime

def setup_files():
    files = ["students.txt", "admins.txt", "questions.txt", "results.txt"]
    for f in files:
        try:
            open(f, "x").close()
        except:
            pass
    with open("admins.txt", "r") as f:
        if not f.read().strip():
            with open("admins.txt", "a") as a:
                a.write("admin|admin123\n")
    with open("questions.txt", "r") as f:
        if not f.read().strip():
            add_default_questions()

def add_default_questions():
    questions = [
        ("PYTHON", "What is the correct file extension for Python files?", ".pyt", ".pt", ".py", ".p", "C"),
        ("PYTHON", "Which keyword is used to create a function in Python?", "function", "def", "fun", "define", "B"),
        ("PYTHON", "Which data type is immutable in Python?", "List", "Dictionary", "Set", "Tuple", "D"),
        ("PYTHON", "What is the output of 3 * '2'?", "6", "222", "Error", "None", "B"),
        ("PYTHON", "What is used to handle exceptions in Python?", "try", "accept", "check", "catch", "A"),
        ("PYTHON", "Which symbol is used to start a comment in Python?", "//", "#", "/*", "--", "B"),
        ("PYTHON", "What is the correct way to get input from the user?", "get()", "scan()", "input()", "read()", "C"),
        ("PYTHON", "Which operator is used for floor division?", "/", "//", "%", "", "B"),
        ("PYTHON", "Which module is used to generate random numbers?", "random", "math", "numbers", "statistics", "A"),
        ("PYTHON", "Which keyword is used to import a module in Python?", "include", "import", "using", "require", "B"),

        ("DBMS", "Which key uniquely identifies each record in a table?", "Primary key", "Foreign key", "Candidate key", "Super key", "A"),
        ("DBMS", "Which SQL statement is used to extract data from a database?", "OPEN", "GET", "EXTRACT", "SELECT", "D"),
        ("DBMS", "Which command is used to remove all records from a table?", "DELETE", "REMOVE", "DROP", "TRUNCATE", "D"),
        ("DBMS", "Which command is used to modify data in a database?", "INSERT", "UPDATE", "ALTER", "MODIFY", "B"),
        ("DBMS", "Which of the following is not a DML command?", "INSERT", "UPDATE", "DELETE", "CREATE", "D"),
        ("DBMS", "Which type of key is used to connect two tables?", "Candidate key", "Foreign key", "Primary key", "Alternate key", "B"),
        ("DBMS", "Which constraint ensures that all values in a column are different?", "UNIQUE", "CHECK", "NOT NULL", "DEFAULT", "A"),
        ("DBMS", "Which command is used to create a new table in SQL?", "INSERT", "CREATE", "ALTER", "SELECT", "B"),
        ("DBMS", "Which of the following is used to sort records in SQL?", "SORT BY", "ORDER", "ORDER BY", "GROUP BY", "C"),
        ("DBMS", "Which of the following ensures data accuracy and consistency?", "Data independence", "Data integrity", "Data redundancy", "Data recovery", "B"),

        ("DSA", "Which data structure uses LIFO order?", "Queue", "Stack", "Linked List", "Array", "B"),
        ("DSA", "Which data structure uses FIFO order?", "Stack", "Queue", "Tree", "Graph", "B"),
        ("DSA", "Which algorithm is used for sorting?", "Binary search", "Quick sort", "DFS", "BFS", "B"),
        ("DSA", "Which searching algorithm divides the list into halves?", "Linear search", "Binary search", "Hash search", "Tree search", "B"),
        ("DSA", "Which of the following is a linear data structure?", "Array", "Graph", "Tree", "Hash", "A"),
        ("DSA", "Which operation is used to insert an element in a stack?", "Insert", "Push", "Add", "Enqueue", "B"),
        ("DSA", "Which operation is used to remove an element from a queue?", "Pop", "Dequeue", "Delete", "Remove", "B"),
        ("DSA", "Which traversal prints the nodes of a tree level by level?", "Preorder", "Inorder", "Postorder", "Level order", "D"),
        ("DSA", "Which sorting algorithm repeatedly selects the smallest element?", "Bubble sort", "Selection sort", "Merge sort", "Quick sort", "B"),
        ("DSA", "Which data structure is used for recursion?", "Array", "Stack", "Queue", "Linked list", "B")
    ]
    with open("questions.txt", "a") as f:
        for q in questions:
            f.write("|".join(q) + "\n")

def register_student():
    username = input("Enter username: ").strip()
    with open("students.txt", "r") as f:
        for line in f:
            if line.split("|")[0] == username:
                print("Username already exists.")
                return
    password = input("Enter password: ").strip()
    name = input("Enter full name: ").strip()
    email = input("Enter email: ").strip()
    course = input("Enter course: ").strip()
    year = input("Enter year: ").strip()
    with open("students.txt", "a") as f:
        f.write(f"{username}|{password}|{name}|{email}|{course}|{year}\n")
    print("Registration successful.")

def login_student():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    with open("students.txt", "r") as f:
        for line in f:
            data = line.strip().split("|")
            if data[0] == username and data[1] == password:
                print(f"Welcome, {data[2]}")
                student_menu(username, data[2])
                return
    print("Invalid username or password.")

def student_menu(username, name):
    while True:
        print()
        print("1. Take Quiz")
        print("2. View Results")
        print("3. View Profile")
        print("4. Logout")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            take_quiz(username)
        elif choice == "2":
            view_results(username)
        elif choice == "3":
            show_profile(username)
        elif choice == "4":
            print(f"Logged out, {name}.")
            break
        else:
            print("Invalid choice.")

def show_profile(username):
    with open("students.txt", "r") as f:
        for line in f:
            data = line.strip().split("|")
            if data[0] == username:
                print()
                print("---- Profile ----")
                print(f"Name: {data[2]}")
                print(f"Email: {data[3]}")
                print(f"Course: {data[4]}")
                print(f"Year: {data[5]}")
                return

def take_quiz(username):
    with open("questions.txt", "r") as f:
        questions = [line.strip().split("|") for line in f if line.strip()]
    if len(questions) < 5:
        print("Not enough questions available.")
        return
    quiz = random.sample(questions, 5)
    score = 0
    for i, q in enumerate(quiz, 1):
        print()
        print(f"Q{i}. ({q[0]}) {q[1]}")
        print(f"A. {q[2]}   B. {q[3]}   C. {q[4]}   D. {q[5]}")
        ans = input("Your answer (A/B/C/D): ").strip().upper()
        if ans == q[6]:
            score += 1
    print()
    print(f"Your score: {score}/5")
    with open("results.txt", "a") as f:
        f.write(f"{username}|{score}|5|{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

def view_results(username):
    found = False
    with open("results.txt", "r") as f:
        for line in f:
            data = line.strip().split("|")
            if data[0] == username:
                found = True
                print(f"Score: {data[1]}/{data[2]}   Date: {data[3]}")
    if not found:
        print("No previous results found.")

def login_admin():
    username = input("Enter admin username: ").strip()
    password = input("Enter admin password: ").strip()
    with open("admins.txt", "r") as f:
        for line in f:
            data = line.strip().split("|")
            if data[0] == username and data[1] == password:
                print("Admin login successful.")
                admin_menu()
                return
    print("Invalid admin credentials.")

def admin_menu():
    while True:
        print()
        print("1. Add Question")
        print("2. View All Students")
        print("3. Add New Admin")
        print("4. Logout")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_question()
        elif choice == "2":
            view_students()
        elif choice == "3":
            add_admin()
        elif choice == "4":
            print("Admin logged out.")
            break
        else:
            print("Invalid choice.")

def add_question():
    category = input("Enter category (DSA/DBMS/PYTHON): ").strip()
    question = input("Enter question: ").strip()
    optA = input("Option A: ").strip()
    optB = input("Option B: ").strip()
    optC = input("Option C: ").strip()
    optD = input("Option D: ").strip()
    correct = input("Correct option (A/B/C/D): ").strip().upper()
    with open("questions.txt", "a") as f:
        f.write(f"{category}|{question}|{optA}|{optB}|{optC}|{optD}|{correct}\n")
    print("Question added successfully.")

def view_students():
    with open("students.txt", "r") as f:
        data = [line.strip().split("|") for line in f if line.strip()]
    if not data:
        print("No students registered yet.")
        return
    print()
    print("---- Registered Students ----")
    for s in data:
        print(f"Username: {s[0]} | Name: {s[2]} | Email: {s[3]}")

def add_admin():
    username = input("Enter new admin username: ").strip()
    password = input("Enter new admin password: ").strip()
    with open("admins.txt", "a") as f:
        f.write(f"{username}|{password}\n")
    print("New admin added successfully.")

def main():
    setup_files()
    while True:
        print()
        print("1. Student")
        print("2. Admin")
        print("3. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            print()
            print("1. Register")
            print("2. Login")
            print("3. Back")
            ch = input("Enter choice: ").strip()
            if ch == "1":
                register_student()
            elif ch == "2":
                login_student()
            elif ch == "3":
                continue
            else:
                print("Invalid choice.")
        elif choice == "2":
            login_admin()
        elif choice == "3":
            print("Exiting system.")
            break
        else:
            print("Invalid choice.")

main()


