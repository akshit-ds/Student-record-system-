# Mini project

# Student record system


stu = {}

while True:
    print("<!-- STUDENT RECORD SYSTEM -->")
    print("1. Add student ")
    print("2. Update marks ")
    print("3.search elment ")
    print("4. Delete element ")
    print("5.Display all records ")
    print("6. EXIT ")
    
    Choice = int(input("Enter your choice "))

    if Choice == 1 :
        name = input("ENter your name ")
        marks = int(input("ENter the marks "))
        stu[name]=marks
        print("Student add sucessfully ")
    elif Choice == 2:
        name = input("ENter your name ")
        if name in stu:
                marks = int(input("ENter the marks "))
                stu[name]=marks
                print("Marks updated")
        else :
             print("student not found ")
    elif Choice == 3:
        name = input("ENter your name ")
        if name in stu:
            print("marks", stu[name])
        else:
            print("Student not found")
             
    elif Choice == 4:
        name = input("ENter your name ")
        if name in stu:
            del stu[name]
            print("student record delte ")
        else:
            print("student not found")
    elif Choice == 5:
        if len(stu) ==0:
            print("no students found ")
        else:
            print("\n Students records ")
            for name,marks in stu.items():
                print(name,":",marks)
    elif Choice == 6:
        print("program break ")
        break
    else:
        print("Invalid program")
             
         
