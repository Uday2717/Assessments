class Student:
    def __init__(self,roll_no,fname,lname,contactnumber,subject,marks,fees):
        self.roll_no = roll_no
        self.fname = fname
        self.lname = lname
        self.contactnumber = contactnumber
        self.subject = subject
        self.marks = marks
        self.fees = fees

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self,roll_no,fname,lname,contactnumber,subject,marks,fees):
        student = Student(roll_no,fname,lname,contactnumber,subject,marks,fees)
        self.students.append(student)

    def display_students(self):
        print("Student List:")
        for student in self.students:
            print(f"Name: {student.fname}, Roll No: {student.roll_no}, Grade: {student.grade}")

    def update_student_grade(self, roll_no, new_grade):
        for student in self.students:
            if student.roll_no == roll_no:
                student.grade = new_grade
                print(f"Grade updated for {student.fname} (Roll No: {student.roll_no})")

    def delete_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print(f"Deleted student with Roll No: {roll_no}")
                return
        print(f"Student with Roll No: {roll_no} not found")

def main():
    student_system = StudentManagementSystem()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student Grade")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            roll_no = input("Enter student roll number: ")
            fname = input("Enter student FirstName: ")
            lname = input("Enter student LastName: ")
            contactnumber = int(input("Enter Contact Number: "))
            subject = input("Enter A Subject: ")
            marks = input("Enter student Marks: ")
            fees = input("Enter Student Fees:")
            student_system.add_student(roll_no,fname,lname,contactnumber,subject,marks,fees)
            print("Student added successfully!")

        elif choice == '2':
            student_system.display_students()

        elif choice == '3':
            roll_no = input("Enter roll number of student to update grade: ")
            new_grade = input("Enter new grade: ")
            student_system.update_student_grade(roll_no, new_grade)

        elif choice == '4':
            roll_no = input("Enter roll number of student to delete: ")
            student_system.delete_student(roll_no)

        elif choice == '5':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
