from math import floor


def calculate_percentage(num, percent):
    return floor((num/100) * percent)
salarys = []
amount_payables = []
with open('input.txt', 'r') as file:
    for line in file:
        salary = int(line)
        # !!!Если зарплата меньше МРОТ то выдаст ошибку!!!
        MINIMUM_WAGE = 13_130
        if salary > MINIMUM_WAGE:
            PENSION_TAX = calculate_percentage(salary, 6)
            
            tax = calculate_percentage((salary - MINIMUM_WAGE - PENSION_TAX), 13) + calculate_percentage(salary, 1)
            # !!!Вводим процент от зарплаты, который пойдет как премия!!!
            award_percent = int(input(f'Введите процент вознаграждения для {salary} зарплаты: '))
            award = calculate_percentage(salary, award_percent)
            amount_payable = salary - tax + award
            salarys.append(salary)
            amount_payables.append(amount_payable)
            print(f'Сумма к оплате составляет {amount_payable} рублей\n')
        else:
            print(f'Ошибка - зарплаты {salary} < MROT {MINIMUM_WAGE}\n')

with open('output.txt', 'w') as file:
    for s, a in zip(salarys, amount_payables):
        file.write(f'Зарплата {s} Сумма к оплате: {a}\n')
