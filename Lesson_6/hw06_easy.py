'''
Задача-1: Написать класс, например, Worker, который должен содержать информацию
о работнике (ФИО, оклад, надбавка за напряженность).
Создать экземпляр класса и передать конкретные данные (примеры ФИО, должности,
оклад и надбавки). Оклад и надбавку передать в виде строки.
На основе строки создать атрибут income, который реализовать в виде словаря
и инкапуслировать. Словарь income должен содержать информацию об окладе и надбавке.
Применить к экземпляру
класса метод __dict__ и проверить какой будет результат применения этого метода.
А комментариях к заданию написать тип результата на русском языке.
'''
'''
class Worker:
    def __init__(self, name, profession, salary, add):
        self.name = name
        self.profession = profession
        self._income = {'salary': salary, 'add': add}



worker1 = Worker('Михайлов Евгений Владиславович', 'слесарь', 30000, 5000)

print(worker1.__dict__)
# тип - словарь
'''
'''
Задача-2: Продолжить работу над задачей 1. Создать на основе класса Worker класс
Position (реализовать наследование). Добавить классу уникальный атрибут -
% премии к зарплате (от суммы оклада).
Создать метод расчета зарплаты с учетом только премии.
Реализовать обращение к этому атриубуту, как к свойству.
Проверить работу всей структуры на реальных данных, вывести результаты.
'''
'''
class Worker:
    def __init__(self, name, profession, salary, add):
        self.name = name
        self.profession = profession
        self._income = {'salary': salary, 'add': add}

class Position(Worker):
    def __init__(self, name, profession, salary, add, premium):
        Worker.__init__(self, name, profession, salary, add)
        self.premium = premium

    @property
    def salary_with_prem(self):
        return(self._income['salary'] + self._income['salary'] * (self.premium/100))


position = Position('Михайлов Евгений Владиславович', 'слесарь', 30000, 5000, 10)

print(position.salary_with_prem)
'''
'''
Задача-3: Продолжить работу над задачей 2.  Реализовать полиморфизм
использования знака + в методах 1) вывода полного имени работника и возраста
2) вычисления общего дохода работника с учетом надбавки .
Проверить работу всей структуры на реальных данных, вывести результаты.
'''
class Worker:
    def __init__(self, name, surname, profession, salary, add):
        self.name = name
        self.surname = surname
        self.profession = profession
        self._income = {'salary': salary, 'add': add}

class Position(Worker):
    def __init__(self, name, surname, profession, salary, add, premium):
        Worker.__init__(self, name, surname, profession, salary, add)
        self.premium = premium

    @property
    def salary_with_prem(self):
        self.sal_w_p = self._income['salary'] + self._income['salary'] * (self.premium/100)
        return self.sal_w_p

    def salary_with_add(self):
        self.salary_with_add = self.sal_w_p + self.add
        return self.salary_with_add

    def get_full_name(self):
        return self.name + ' ' + self.surname


position = Position('Евгений Владиславович', 'Михайлов', 'слесарь', 30000, 5000, 10)

print(position.salary_with_add)
print(position.salary_with_prem)
print(position.get_full_name)


