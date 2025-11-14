from models.teacher import Teacher

def add_teacher():
    print("\n Add new Teacher")
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    department = input("Enter department: ")

    teacher = Teacher(name,email,phone,department)
    teacher.add()
    print(f"Teacher {name} added successfully!")

def view_teachers():
    print("\n All teachers")
    teachers = Teacher.get_all()

    if not teachers:
        print("No teachers found")
        return
    
    for teacher in teachers:
        print(f"ID: {teacher['id']} | Name: {teacher['name']} | Email: {teacher['email']} | Phone: {teacher['phone']} | Department: {teacher['department']}")


def update_teacher():
    print("\n Update Teacher")
    teacher_id = input("Enter Teacher ID: ")

    name = input("Enter New Name: ")
    email = input("Enter New Email: ")
    phone = input("Enter New Phone Number: ")
    department = input("Enter New Department: ")

    teacher = Teacher(name, email, phone, department, teacher_id)
    teacher.update()
    print("Teacher updated successfully!")

def delete_teacher():
    print("\n Delete Teacher")
    teacher_id = input("Enter Teacher ID: ")

    teacher = Teacher("", "", "", "", teacher_id)
    teacher.delete()
    print(" Teacher deleted successfully!")

def teacher_menu():
    while True:
        print("\n=== Teacher Management Menu ===")
        print("1. Add Teacher")
        print("2. View All Teachers")
        print("3. Update Teacher")
        print("4. Delete Teacher")
        print("5. Back to Main Menu")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_teacher()
        elif choice == '2':
            view_teachers()
        elif choice == '3':
            update_teacher()
        elif choice == '4':
            delete_teacher()
        elif choice == '5':
            print("Returning to Main Menu...")
            break
        else:
            print(" Invalid choice! Please enter a number between 1-5.")
