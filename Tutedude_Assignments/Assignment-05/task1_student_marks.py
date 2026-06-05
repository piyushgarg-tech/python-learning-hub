students = {
    "Amit": 85,
    "Pooja": 92,
    "Rahul": 76,
    "Sneha": 89,
    "Arjun": 95
}

name = input("Enter the student's name: ")

if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")
