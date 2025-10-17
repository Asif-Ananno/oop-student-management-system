from services.student_services import add_student, view_student, update_student,delete_student

def main_menu():
    while True:
        print("\n Student Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting the system........")
            break
        else:
            print("Invalid input")
        
if __name__=="__main__":
    main_menu()
