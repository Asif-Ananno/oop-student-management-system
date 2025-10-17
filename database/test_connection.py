from connection import get_connection

def test_db_connection():
    try:
        conn = get_connection()
        print("Successfully connected to the database")
    except Exception as e:
        print(" Connection failed:", e)
    finally:
        if 'conn' in locals():
            conn.close()
            print(" Connection closed")

if __name__ == "__main__":
    test_db_connection()
