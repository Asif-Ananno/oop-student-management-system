from models.person import Person
from database.connection import get_connection

class Student(Person):
    def __init__(self,name,email,phone,department,id=None):
        super().__init__(name,email,phone)
        self.id = id
        self.department = department

    def display_info(self):
        print(f"ID:{self.id} , Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Dept: {self.department}")

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO students (name,email,phone,department) values (%s,%s,%s,%s)"
        cursor.execute(sql,(self.name,self.email,self.phone,self.department))
        conn.commit()
        self.id = cursor.lastrowid
        conn.close()

    @staticmethod
    
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")

        # Fetch all rows (already dicts)
        students = cursor.fetchall()

        conn.close()
        return students
    @staticmethod
    def get_by_id(student_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id=%s",(student_id,))
        row = cursor.fetchone()
        conn.close()
        return row
    
    def update(self):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "UPDATE students SET name=%s, email=%s, phone=%s, department=%s WHERE id=%s" 
        cursor.execute(sql,(self.name,self.email,self.phone,self.department,self.id))
        conn.commit()
        conn.close()
    
    @staticmethod
    def delete(student_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id=%s",(student_id,))
        conn.commit()
        conn.close()
