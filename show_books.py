from pprint import pprint

def show_all_books(cursor):
    cursor.execute("select * from Books")
    pprint(cursor.fetchall())