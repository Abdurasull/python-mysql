from pprint import pprint
def search_books_by_author_or_genre(cursor, search_type, search_value):
    cursor.execute(f"select {search_type}, id, author from Books where {search_type} = '{search_value}'")
    result = cursor.fetchall()
    # for i in result:
    #     print(f"")
    for i in result:
        print(f"{search_type}: {i[0]}\n id: {i[1]}\n {}")