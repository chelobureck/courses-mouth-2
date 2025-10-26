import sqlite3

def create_tables():
    engine.execute("""
        CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    author TEXT,
                    publication_year INTEGER,
                    genre TEXT,
                    number_of_pages INTEGER,
                    number_of_copies INTEGER,
                    deleted INTEGER DEFAULT 0
                )
    """)
    engine.execute("""
        CREATE TABLE IF NOT EXISTS books_archive (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    author TEXT,
                    publication_year INTEGER,
                    genre TEXT,
                    number_of_pages INTEGER,
                    number_of_copies INTEGER
                )
    """)


def insert_books(books: list[list]):
    try:
        if len(books) >= 10:
            for book in books:
                engine.execute("""
                            INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
                            VALUES (?, ?, ?, ?, ?, ?)
                        """, (book[0], book[1], book[2], book[3], book[4], book[5]))
                engine.commit()
        else:
            raise ValueError("Слишком мало книг для добавления в базу данных")
    except:
        print("Проверьте передаваемые данные книг")


def delete_book(book_name: str):
    try:
        engine.execute("""
                DELETE FROM books
                WHERE name = ?
            """, (book_name,))
        engine.commit()
    except:
        print("призошла ошибка при удалении")


def soft_delete(book_id: int):
    try:
        result = engine.execute("""
                SELECT name, author 
                FROM books 
                WHERE id = ?
            """, (book_id,)).fetchone()
        
        book_name, book_author = result
        
        engine.execute("""
            INSERT INTO books_archive (name, author, publication_year, genre, number_of_pages, number_of_copies)
            SELECT name, author, publication_year, genre, number_of_pages, number_of_copies
            FROM books
            WHERE id = ? AND NOT EXISTS (
                        SELECT 1 FROM books_archive 
                        WHERE name = ? AND author = ?
                        )
            
        """, (book_id, book_name, book_author))
        engine.execute("""
            UPDATE books SET
                deleted = deleted + 1
            WHERE id = ?
        """, (book_id,))
        engine.commit()
    except:
        print("произошла ошибка при мягком удалении")


def hard_delete(books_id: int):
    try:
        engine.execute("""
            DELETE FROM books WHERE id = ? AND deleted > 0
        """)
        engine.commit()
    except:
        print("произошла ошибка при жетском удалении")


books_list = [
            ["Garry Potter", "J.K. Rowling", 1997, "Fantasy", 223, 5],
            ["The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 310, 3],
            ["1984", "George Orwell", 1949, "Dystopian", 328, 4],
            ["To Kill a Mockingbird", "Harper Lee", 1960, "Fiction", 281, 2],
            ["Pride and Prejudice", "Jane Austen", 1813, "Romance", 279, 6],
            ["The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction", 180, 7],
            ["Moby Dick", "Herman Melville", 1851, "Adventure", 635, 1],
            ["War and Peace", "Leo Tolstoy", 1869, "Historical", 1225, 2],
            ["The Catcher in the Rye", "J.D. Salinger", 1951, "Fiction", 214, 4],
            ["The Lord of the Rings", "J.R.R. Tolkien", 1954, "Fantasy", 1178, 3]
            ]



if __name__ == "__main__":
    engine = sqlite3.connect("database.db")
    create_tables()
    insert_books(books_list)
    delete_book("Pride and Prejudice")
    soft_delete(4)
    soft_delete(7)
    hard_delete(4)
    hard_delete(3)

    engine.close()