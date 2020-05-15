# 1.В словаре хранится информация о клиентах парикмахерской, 
# ключ - фамилия/имя клиента, значение - список строк формата: дата_услуга_стоимость.
clients = {
    # Фамилия/Имя       Дата       Услуга    Стоимость
   'Иванников': [['11.11.2018', 'Стрижка', '600']],
    'Ломакин': [['13.13.2013', 'Стрижка', '500']],
    'Куприянова': [['19.10.2007', 'Покраска волос', '600'], ['12.08.2012', 'Подравнивание кончиков', '1200']] 

}

# добавление и удаление клиента
# добавление и удаление значений списка
def add_client(key, value=None):
    if key in clients:
        if clients[key] == None:
            clients[key] = []
        else:
            clients[key].append(value)
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
            print(f'Здесь нет {key} для клиента')


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
    newest_date = [19, 10 ,2000]
    for value in clients[key]:
        current_date = [int(x) for x in value[0].split('.')]
        newest_date = compare_dates(current_date, newest_date)
        newest_date = str(newest_date).replace('[','').replace(']', '').replace(', ', '.')
    print(f"Новая дата для {key}  {newest_date}")



find_date('Иванников')
       
def find_spended_money(key):
    money = 0
    for value in clients[key]:
        money += int(value[2])
    print(f'Сумма за {key} составляют {money} rub')

find_spended_money('Иванников')

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
    
find_oldest()

def find_frequent():
    count = 0
    frequent = ''
    for client in clients:
        if len(clients[client]) > count:
            count = len(clients[client])
            frequent = client
    print(f'Самый частый клиент  {frequent}')

find_frequent()

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

find_richest()
