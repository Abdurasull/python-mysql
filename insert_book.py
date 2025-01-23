import mysql.connector
from pprint import pprint
def insert_book(cursor, title, author, published_year, genre, price):
    cursor.execute(f"""insert into Books(title, author, published_year, genre, price)
                        values ("{title}", "{author}", {published_year}, "{genre}", {price}); 
                   """)
    print("Maluot muvoffaqqiyatli qo`shildi!\n")