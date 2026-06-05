def read_file():
    try:
        with open("sample.txt", "r") as file:
            for line in file:
                print(line.strip())

    except FileNotFoundError:
        print("Error: sample.txt was not found.")

read_file()
