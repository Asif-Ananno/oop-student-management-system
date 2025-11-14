from database.connection import get_connection
from models.person import Person

class Teacher(Person):
    def __init__(self,name,email,phone,department,id=None):
        super().__init__(name,email,phone)
        self.department = department
        self.id = id
        
    def display_info(self):
        print(f"ID:{self.id} , Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Dept: {self.department}")
    
    def add(self):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO teachers (name,email,phone,department) values (%s, %s, %s, %s)"
        cursor.execute(sql,(self.name,self.email,self.phone,self.department))
        conn.commit()
        conn.close()
    
    def update(self):
        if not self.id:
            print("Teacher Id is required for update")
            return
        conn = get_connection()
        cursor = conn.cursor()
        sql = "UPDATE teachers SET name=%s, email=%s, phone=%s, department=%s WHERE id=%s"
        cursor.execute(sql,(self.name,self.email,self.phone,self.department,self.id))
        conn.commit()
        conn.close()
    
    def delete(self):
        if not self.id:
            print("Teacher ID is required for delete")
            return
        
        conn = get_connection()
        cursor = conn.cursor()
        sql = "DELETE FROM teachers WHERE id=%s"
        cursor.execute(sql,(self.id,))
        conn.commit()
        conn.close()
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM teachers")
        teachers = cursor.fetchall()
        conn.close()
        return teachers

        