"""
Student Management System

Features:
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Save To File
7. Load From File
8. Exit
"""

import json

students = {}


def add_student():
    roll = input("Roll No: ")
    name = input("Name: ")

    students[roll] = name

    print("Student Added")


def view_students():

    if not students:
        print("No Students Found")
        return

    print("\nStudents:")

    for roll, name in students.items():
        print(f"{roll} -> {name}")


def search_student():
    roll = input("Enter Roll No: ")

    print(
        students.get(
            roll,
            "Student Not Found"
        )
    )


def update_student():
    roll = input("Roll No: ")

    if roll in students:

        new_name = input(
            "New Name: "
        )

        students[roll] = new_name

        print("Updated")

    else:

        print("Student Not Found")


def delete_student():
    roll = input("Roll No: ")

    if roll in students:

        del students[roll]

        print("Deleted")

    else:

        print("Student Not Found")


def save_to_file():

    with open(
        "students.json",
        "w"
    ) as file:

        json.dump(
            students,
            file,
            indent=4
        )

    print(
        "Data Saved Successfully"
    )


def load_from_file():

    global students

    try:

        with open(
            "students.json",
            "r"
        ) as file:

            students = json.load(
                file
            )

        print(
            "Data Loaded Successfully"
        )

    except FileNotFoundError:

        print(
            "No Saved File Found"
        )


while True:

    print("\n===== MENU =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Save To File")
    print("7. Load From File")
    print("8. Exit")

    choice = input(
        "\nEnter Choice: "
    )

    if choice == "1":

        add_student()

    elif choice == "2":

        view_students()

    elif choice == "3":

        search_student()

    elif choice == "4":

        update_student()

    elif choice == "5":

        delete_student()

    elif choice == "6":

        save_to_file()

    elif choice == "7":

        load_from_file()

    elif choice == "8":

        print("Goodbye")
        break

    else:

        print("Invalid Choice")