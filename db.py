from create_books_table import create_books_table
from insert_book import insert_book
from show_books import show_all_books
from search_books_by_author import search_books_by_author_or_genre


import mysql.connector
import login
from pprint import pprint
try:
    connection = mysql.connector.connect(
        host=login.host,
        user=login.user,
        password=login.password,
        port=login.port
    )

    cursor = connection.cursor()

    # 1. MySQL jadvali yaratish
    create_books_table(cursor)

    # 2. Foydalanuvchidan ma'lumot kiritish
    while True:
        title = input("Kitobni nomini kiriting: ")
        author = input("Kitobni authorini kiriting: ")
        published_year = int(input("Kitobni yaratilgan yili: "))
        genre = input("Kitobni janrini kiriting: ")
        price = int(input("kitobni narxini kiriting: "))
        
        insert_book(cursor, title, author, published_year, genre, price)
        x = input("Yana ma`lumot qo`shmoqchi bo`lsangiz 1 ni bosing, aks holda hohlagan bilgini: ")
        if x != '1':
            connection.commit()#malumotni doimiy xotirada saqlab qolish uchun :)
            break

    # 3. Barcha kitoblarni ko'rsatish
    show_all_books(cursor)

    # 4. Ma'lum bir shart bo'yicha qidiruv
    print("author yoki genre ni kiriting")
    search_type = input("Qidiruv turini(yuqoridagilardan biri) kiriting: ")
    search_value = input("Qidiruv turi qiymatini kiriting: ")
    search_books_by_author_or_genre(cursor, search_type, search_value)


    
    


    

    # cursor.execute("create database if not exists educaition")
    # cursor.execute("use educaition")
    # cursor.execute("""create table if not exists talabalar(
    #                 id int auto_increment primary key,
    #                 name varchar(64) not null,
    #                 grade int not null,
    #                 age int not null)
    #                """)
    # cursor.execute("""
    #                 insert into talabalar(name, grade, age)
    #                values 
    #                     ("Abdurasul", 2, 28),("Asror", 2, 16), ("Suxrob", 3, 21), ("Amir", 2, 20), ("Nozim", 3, 20), 
    #                     ("Gulsapsar", 2, 28),("Anora", 2, 16), ("Azizbek", 3, 21), ("Diyorbek", 2, 20), ("Eldor", 3, 20)
    #                 """)
    
    # cursor.execute("select * from talabalar")
    # pprint(cursor.fetchall())
    
except:
    print("xato")