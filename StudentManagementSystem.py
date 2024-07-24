students = {}


def add_student():
    student_id=int(input("Enter Student Id :"))
    if student_id in students:
        print("Student ID already exists!")
        print("**********************************")
        return False
    else:
        student_fname=input("Enter Student First Name :")
        student_lname=input("Enter Studnet Last Name :")
        student_contact=input("Enter Contact Number :")
        subject=input("Enter a subject:")
        marks=int(input("Enter marks :"))
        fees=int(input("Enter fees : "))
        student[student_id]={
            "first_name":student_fname,
            "last_name":student_lname,
            "contact":student_contact,
            "subjects":{
                subject:{
                    "marks":marks,
                    "fees":fees
                    }
                }
            }
        print("Student added successfully")
        print("***********************************")


def remove(student_id):
    if student_id in students:
        del students[student_id]
        print("Student removed successfully")
        print("************************************")
    else:
        print("Student ID Not Found")
        print("************************************")

def specific_student(student_id):
    if student_id in students:
        student_info=students[students[student_id]]
        student_data={
            "student_id":student_id,
            "first_name":student_info["first_name"],
            "last_name":student_info["last_name"],
            "contact":student_info["contact"],
            "subjects":student_info["subjects"]
            }
        print("Student Details:")
        print(student_data)
        print("**********************************")
    else:
        print("Student ID Not Found")
        print("**************************************")


def view_all_students():
    if not students:
        print("No students registered yet")
        print("**************************************")
    else:
        for student_id,student_info in students.items():
            student_data={
                "student_id":student_id,
                "first_name":student_info["first_name"],
                "last_name":student_info["last_name"],
                "contact":student_info["contact"],
                "subjects":student_info["subjects"]
            }
            print(atudent_data)

def counseller():
    while True:
        print("1. Add Student")
        print("2. Remove Student")
        print("3. View All Students")
        print("4. View Specific Student")
        print("5. Exit")
        print("**************************************")
        choice = int(input("Enter Your Choice:"))
        print("**************************************")
        if choice == 1:
            add_student()
        elif choice == 2:
            student_id = int(input("Enter Student ID To Remove:"))
            remove(student_id)
        elif choice == 3:
            view_all_students()
        elif choice == 4:
            student_id = int(input("Enter Student ID To View Details:"))
            specific_student(student_id)
        elif choice == 5:
            break
        else:
            print("Invalid Choice!")


def student_faculty(student_id):
    if student_id in students:
        subject = input("Enter Subject:")
        marks = int(input("Enter Marks:"))
        students[student_id]["subjects"][subject]={
            "marks":marks
        }
        print("Marks Added Successfully!")
        print("**************************************")
    else:
            print("Student ID Not Found!")
            print("**************************************")


def faculty():
    while True:
        print("1. Add Marks To Student")
        print("2. View All Students")
        print("3. Exit")
        print("**************************************")
        choice = int(input("Choice What You Want:"))
        print("**************************************")

        if choice == 1:
            student_id = int(input("Enter Student ID To Add Marks:"))
            student_faculty(student_id)
        elif choice == 2:
            view_all_students()
        else:
            print("Invalid Choice!")
            print("**************************************")
            break


while True:
    print("Press 1 For Counseller")
    print("Press 2 For Faculty")
    print("Press 3 For Student")
    print("**************************************")
    role = int(input("Enter Your Role:"))
    print("**************************************")
    if role == 1:
        counseller()
    elif role == 2:
        faculty()
    elif role == 3:
        student_id = int(input("Enter Student ID To View Details:"))
        specific_student(student_id)
    else:
        print("Invalid Role!")
        print("**************************************")
        break
    
            
        
