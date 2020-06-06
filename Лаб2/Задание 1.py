# 1.В словаре хранится информация о клиентах парикмахерской, 
# ключ - фамилия/имя клиента, значение - список строк формата: дата_услуга_стоимость.
clients = {
    # Фамилия/Имя       Дата       Услуга    Стоимость
   'Иванников': [['11.11.2018', 'Стрижка', '600']],
    'Ломакин': [['13.13.2013', 'Стрижка', '500']],
    'Куприянова': [['19.10.2007', 'Покраска волос', '600']] 

}

# добавление и удаление клиента
# добавление и удаление значений списка
def add_client(key):
    if key in clients:
        if clients[key] == None:
            clients[key] = []
        else:
            clients[key].append([date])
    else:
        clients[key] = []


def delete_client(key, value=None):
    if value:
        if value in clients[key]:
            clients[key] = []
        else:
            print(f'Здесь нет {value} для клиента')
    else:
        try:
            clients.pop(key)
        except:
            print(f'Здесь нет {key} для клиента\n')


# 2.Найти по фамилии
# дата последнего обращения find_date
# количество потраченных денег find_spended_money
# самый давний клиент find_oldest
# самый частый клиент find_frequent 
# самый богатый find_richest

def compare_dates(date1, date2, predicat=False):
    if predicat:
        if date1[2] > date2[2]:
            return True
        elif date1[2] == date2[2] and date1[1] > date2[1]:
            return True
        else:
            return False
    else:
        if date1[2] > date2[2]:
            return date1
        elif date1[2] == date2[2] and date1[1] > date2[1]:
            return date1
        else:
            return date2
        


def find_date(key):
    if clients[key]:
        newest_date = [19, 10 ,2000]
        for value in clients[key]:
            current_date = [int(x) for x in value[0].split('.')]
            newest_date = compare_dates(current_date, newest_date)
            newest_date = str(newest_date).replace('[','').replace(']', '').replace(', ', '.')
        print(f"Новая дата для {key}  {newest_date}")
    


def find_spended_money(key):
    money = 0
    for value in clients[key]:
        money += int(value[2])
    print(f'Сумма за {key} составляют {money} rub')



def find_oldest():
    oldest_date = [19, 10 ,2050]
    oldest_client = ''
    for client in clients:
        for value in clients[client]: 
            current_date = [int(x) for x in value[0].split('.')]
            if compare_dates(oldest_date, current_date, predicat=True):
                oldest_date = current_date
                oldest_client = client
    print(f"Самый старый клиент {oldest_client}, самая старая дата {str(oldest_date).replace('[','').replace(']', '').replace(', ', '.')}")
    


def find_frequent():
    count = 0
    frequent = ''
    for client in clients:
        if len(clients[client]) > count:
            count = len(clients[client])
            frequent = client
    print(f'Самый частый клиент  {frequent}')


def find_richest():
    count = 0
    richest = ''
    for client in clients:
        current_count = 0
        for value in clients[client]:
            if int(value[2]) > current_count:
                current_count += int(value[2])
        if current_count > count:
            count = current_count
            richest = client
    print(f'самый богатый клиент {richest} потраченные деньги  {count}')


print("Добаление и удаление\n"
        "1.Добавить клиента\n" \
        "2.Добавить клиенту значение\n" \
        "3.Удалить клиента\n" \
        "4.Удалить по значению\n" \
        "Поиск по фамилии\n" \
        "5.Дата последнего обращения\n" \
        "6.Количество потраченных денег\n" \
        "7.Самый давний клиент\n" \
        "8.Самый частый клиент\n" \
        "9.Самый богатый клиент\n" \
       )
while True:
    try:
        user_input = int(input('-> '))
        if user_input == 1:
            add_client(input('Введите клиента\n'))
        elif user_input == 2:
            add_client(input('Введите клиента\n'),input('Введите дату\n'),input('Введите услугу\n'),input('Введите цену\n'))
        elif user_input == 3:
            delete_client(input('Введите клиента\n'))
        elif user_input == 4:
            delete_client(input('Введите клиента\n'),input('Введите значение\n'))
        elif user_input == 5:
            find_date(input('Введите клиента\n'))
        elif user_input == 6:
            find_spended_money(input('Введите клиента\n'))
        elif user_input == 7:
            find_oldest()
        elif user_input == 8:
            find_frequent()
        elif user_input == 9:
            find_richest()
            break
        else:
            print('Ошибка')
        [print(f"{key} {clients[key]}") for key in clients]
    except Exception as e:
        print(e)


