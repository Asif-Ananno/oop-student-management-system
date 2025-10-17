from models.student import Student

def add_student():
    print("\n Add new Student")
    name = input("Enter name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phonenumber: ")
    department = input("Enter department: ")

    student = Student(name,email,phone,department)
    student.save()
    print("Successfully added student")

def view_student():
    students = Student.get_all()
    if not students:
        print("No student found")
        return
    print("\n All students: ")
    for student in students:
        print(f"ID : {student['id']} | Name : {student['name']} | Email: {student['email']} | Phone: {student['phone']} | Department: {student['department']}")
    
def update_student():
    student_id = input("Enter Student ID: ")
    existing = Student.get_by_id(student_id)

    if not existing:
        print("student not found")
        return
    
    name = input(f"Name ({existing['name']}): ") or existing['name']
    email = input(f"Email ({existing['email']}): ") or existing['email']
    phone = input(f"Phone ({existing['phone']}): ") or existing['phone']
    department = input(f"Department ({existing['department']}): ") or existing['department']

    student = Student(name,email,phone,department,id=student_id)
    student.update()

    print("Student Updated Successfully")


def delete_student():
    student_id = input("Enter Student ID: ")
    existing = Student.get_by_id(student_id)

    if not existing:
        print("Student not found")
        return
    
    confirm = input(f"Are you sure you want to delete {existing['name']}? (y/n): ")

    if confirm.lower()=='y':
        Student.delete(student_id)
        print("Student deleted successfully")
    else:
        print("Operation cancelled")

    