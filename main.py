#Mini Project - Student Record System

#variable where all our records will be stored
# 
student_record = {}

while True:

    print(""" <-- STUDENT RECORD SYSTEM -->
    1. Add Record
    2. Update marks
    3. Search Record
    4. Delete Record
    5. Display all records
    6. EXIT""")

    Choice = input("What Action You Want To Perform? (1-6) ")

    # match cases to perform on inputs
    match Choice:
        case "1" :
            name = input("Enter your name ")
            marks = int(input("Enter the marks "))
            student_record[name]=marks
            print("Student Added Sucessfully ")
        case "2" :
            name = input("Enter your name ")
            if name in student_record:
                    marks = int(input("Enter the marks "))
                    student_record[name] = marks
                    print("Marks updated")
            else :
                 print("Student not found ")
        case "3" :
            name = input("Enter your name ")
            if name in student_record:
                
                print(f"{name}:{student_record[name]}")
            else:
                print("Student not found")
        case "4" :
            name = input("Enter your name ")
            if name in student_record:
                del student_record[name]
                print("student record delte ")
            else:
                print("student not found")
        case "5" :
            if len(student_record) == 0:
                print("no students found ")
            else:
                print("\n Students records ")
                for name,marks in student_record.items():
                    
                    print(f"{name}:{marks}")
        case "6" :
            print("EXITED ")
            break

        case _ :
            print("INVALID INPUT")
            continue
