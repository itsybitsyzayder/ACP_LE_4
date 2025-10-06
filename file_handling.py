# Name: Mendoza, Zhaider M.
# Section: BSIT 2108

# Activity Title: File Handling in Python: Menu-Driven Student Records Management

import os

docpath = os.path.expanduser("~/Documents")

if not os.path.exists(docpath):
    os.makedirs(docpath)

while True:
    print("===== Student Records Menu =====")
    print("1. Register Student")
    print("2. Open Student Record")
    print("3. Exit")
    
    choice = int(input("Enter your choice: "))
    
    print()
    
    if choice == 1:
        print("=== Register Student ===")
        student_number = int(input("Student No.: "))
        student_last_name = input("Last Name: ")
        student_first_name = input("First Name: ")
        student_middle_initial = input("Middle Initial: ")
        student_program = input("Program: ")
        student_age = int(input("Age: "))
        student_gender = input("Gender: ")
        student_birthday = input("Birthday: ")
        student_contact_number = int(input("Contact No.: "))
        
        data = [
            {"Student No.": student_number},
            {"Last Name": student_last_name},
            {"First Name": student_first_name},
            {"Middle Initial": student_middle_initial},
            {"Program": student_program},
            {"Age": student_age},
            {"Gender": student_gender},
            {"Birthday": student_birthday},
            {"Contact No.": student_contact_number}
        ]

        file_path = os.path.join(docpath, f"{student_number}.txt")
        with open(file_path, "w") as f:
            for line in data:
                f.write(str(line) + "\n")

        print(f"✅ Student record saved to: {file_path}")
        print()

    elif choice == 2:
        try:
            print("=== Opening Student Record ===")
        
            student_no = int(input("Enter student number to open student file record: "))
            
            file_path = os.path.join(docpath, f"{student_no}.txt")
            if os.path.exists(file_path):
                with open(file_path, "r") as f:
                    for line in f:
                        print(line.strip())
            else:
                print("❌ Student record not found.")
        
        except FileNotFoundError as e:
            print(f"❌ Student record not found.: {e}")
            
        finally:
            print("Thank you.")
            print()
    
    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
        continue