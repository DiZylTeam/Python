# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной



from random import *
import json


phonebook = {}

def save():
    with open("phonebook.json", 'w', encoding="utf-8") as fh:
        fh.write(json.dumps(phonebook, ensure_ascii=False))




def load():
    with open("phonebook.json", "r", encoding="utf-8") as fh:
        phonebook = json.load(fh)
    return phonebook




def delete():
    name = input('Введите имя контакта для удаления: ')
    load()
    if name in phonebook:  
        del phonebook[name]
    save()
    print("Контакт успешно удалён!")




def change_contact():  
    name = input('Введите имя для редактирования: ')
    load()
    if name in phonebook:  
         phonebook[name] = input("Внесите изменения в контактные данные: ")
    save()
    print("Изменения успешно сохранены!")




while True:
    command = input("Введите команду: ")
    if command == "/add":
        name = input("Имя контакта: ")
        number1 = input("Введите 1-й номер телефона: ")
        number2 = input("Введите 2-й номер телефона: ")
        birthday = input("Дата рождения: ")
        email = input("Введите email: ")
        phonebook[name] = {"phone_numbers": [number1, number2], "birthday": birthday, "email": email}
        print("Контакт сохранен")
    elif command == "/all":
        print("Список всех контактов")
        print(phonebook)
    elif command == "/find":
        name = input("Введите имя для поиска: ")
        if name in phonebook:
            print(name, phonebook[name])
    elif command == "/save":
        save()
        print("Контакт сохранен")
    elif command == "/load":
        phonebook = load()
        print("Загрузка прошла успешно!")
    elif command == "/del":
        delete()
    elif command == "/change":
        change_contact()
        