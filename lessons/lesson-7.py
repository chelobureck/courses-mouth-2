import sqlite3


def create_tables(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            city TEXT
        )
    """)

def add_students(conn, name: str, age: int, city: str):
    conn.execute("""
    INSERT INTO students (name, age, city)
    VALUES (?, ?, ?)
    """, (name, age, city))
    conn.commit()

def del_table(conn):
    conn.execute("DROP TABLE IF EXISTS students")

def del_student(conn, student_id):
    conn.execute("""DELETE FROM students WHERE id = ?""", (student_id,))
    conn.commit()

if __name__ == "__main__":
    conn = sqlite3.connect("database.db")
    # create_tables(conn)
    # add_students(conn, 'Maksat', 19, 'Bishkek')
    # add_students(conn, 'Rayana', 19, 'Tokmok')
    # add_students(conn, 'Nurbeck', 18, 'Osh')
    # del_table(conn)
    del_student(conn=conn, student_id=2)

    conn.close()