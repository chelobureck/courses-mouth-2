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

def get_all_students(conn):
    res = conn.execute("SELECT * FROM students")
    return res.fetchall()

def get_all_name_students(conn):
    res = conn.execute("SELECT id, name FROM students")
    return res.fetchall()

def get_name_students(conn, student_id: int):
    res = conn.execute("SELECT name FROM students WHERE id = ?", (student_id, ))
    return res.fetchall()

def get_student(conn):
    res = conn.execute("SELECT * FROM students ORDER BY name")
    return res.fetchall()

def change_student(conn, student_id, age):
    conn.execute("UPDATE students SET age = ? WHERE id = ?", (age, student_id))
    conn.commit()

def change_id(conn, student_id, new_id):
    conn.execute("UPDATE students SET id = ? WHERE id = ?", (new_id, student_id))
    conn.commit()

if __name__ == "__main__":
    conn = sqlite3.connect("database.db")
    create_tables(conn)
    # add_students(conn, 'Maksat', 19, 'Bishkek')
    # add_students(conn, 'Rayana', 19, 'Tokmok')
    # add_students(conn, 'Nurbeck', 18, 'Osh')
    # del_table(conn)
    # del_student(conn=conn, student_id=4)
    # print(get_all_students(conn))
    # print(type(get_all_students(conn)))
    # print(get_all_name_students(conn))
    # print(type(get_all_name_students(conn)))
    # print(get_name_students(conn, 2))
    # print(type(get_name_students(conn, 2)))
    # change_student(conn, 2, 23)
    change_id(conn, 2, 1)
    print(get_student(conn))


    conn.close()