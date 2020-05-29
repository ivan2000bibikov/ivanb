import sqlite3


conn = sqlite3.connect('books.db')
c = conn.cursor()
c.execute("DROP TABLE books;")

c.execute("CREATE TABLE books (id int auto_increment primary key, author varchar, title varchar, genre varchar);")
            # Автор    Название       Жанр
lines = [["Вадим Фарг","Лишний игрок", "Фентези"],
         ["Семух Григорий", "S-T-I-K-S. Единственный враг (СИ)", "Боевая фантастика"],
         ["Любой человек", "K-POP мусор", "Правда"],
         ["Толстой", "Война и Мир", " Русская классика"],
         ["Майк Омер", "Внутри убийцы", "Зарубежные детективы"],
         ["Достоевский", "Идиот", "Классика"],
         ["Алексей Губарев", "По кромке удачи. Игра на выживание", "фантастика"],
         ["Дэн Браун", "Происхождение", "Детектив"]]


# !!!Создает новую запись!!!
def create_new_line(author, title, genre):
    c.execute(f"INSERT INTO books (author, title, genre) VALUES('{author}', '{title}', '{genre}');")

def delete_line_by_field(field, value):
    c.execute(f'DELETE FROM books WHERE {field}="{value}"')

def print_data():
    row = c.fetchall()
    for line in row:
        print(*["%-20s" % f'|{x}' for x in line if x])

def get_books(author=None):
    if author:
        c.execute(f'SELECT * FROM books WHERE author="{author}"')
    else:
        c.execute(f'SELECT * FROM books')
    print_data()

def get_4_first_lines():
    c.execute(f'SELECT * FROM books LIMIT 4')
    print_data()

def update_line(field, value, new_value):
    c.execute(f'UPDATE books SET {field}="{new_value}" WHERE {field}="{value}";')
    print_data()

# !!!Цикл проходится по массиву значений и забивает бд данными!!!
for line in lines:
    create_new_line(*line)
    
update_line('title', 'Старушка и топор', 'Преступление и наказание')
sql = """
UPDATE albums 
SET artist = 'John Doe' 
WHERE artist = 'Andy Hunter'
"""



conn.commit()
