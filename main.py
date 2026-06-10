import csv

FILE = "data.csv"

def add_application():
    company = input("Company: ")
    role = input("Role: ")
    status = input("Status: ")
    date = input("Interview Date: ")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([company, role, status, date])

    print("Application added successfully!")

def view_applications():
    try:
        with open(FILE, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No applications found.")

while True:
    print("\n1. Add Application")
    print("2. View Applications")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_application()

    elif choice == "2":
        view_applications()

    elif choice == "3":
        break

    else:
        print("Invalid choice")
