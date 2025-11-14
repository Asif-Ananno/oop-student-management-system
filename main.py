from services.student_services import student_menu
from services.teacher_services import teacher_menu

def main_menu():
    while True:
        print("\n===  Student Management System ===")
        print("1. Student Management")
        print("2. Teacher Management")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            student_menu()   
        elif choice == '2':
            teacher_menu()      
        elif choice == '3':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-3.")
       
        
if __name__=="__main__":
    main_menu()
