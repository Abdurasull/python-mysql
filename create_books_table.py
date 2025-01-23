from pprint import pprint

def create_books_table(cursor):
    """
    Create a 'books' table in the database if it doesn't exist.
    """
    
    cursor.execute("create database if not exists Library")
    cursor.execute("use Library")
    cursor.execute("""create table if not exists Books(
                    id int auto_increment primary key,
                    title varchar(64) not null,
                    author varchar(64) not null,
                    published_year int not null,
                    genre varchar(64),
                    price int not null
                    );
                   """)
    print("Kutubxona nomli database yaratildi va uni Books nomli table mavjud :) \nMarxamat ma`lumotlar kiriting!\n")