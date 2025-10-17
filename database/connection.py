import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",  # or your root password
        database="student_management",
        cursorclass=pymysql.cursors.DictCursor
    )
