from in_out import *
from logger import *
from ui import *


def print_all():
    list_data = get_info("PI.csv.txt")
    list_data += get_info("Salary.csv.txt")
    list_data += get_info("Department.csv.txt")
    for i in list_data:
        print(i)
    info_logger(f'Запрос на вывод информации')


def add_data():
    id_pes = input_data("Введите id: ")

    data_personal = add_data_pi(id_pes)
    append_data("PI.csv.txt", data_personal)
    info_logger(f'Новая запись в таблицу "PI" {data_personal}')

    data_personal = add_data_Salary(id_pes)
    append_data("Salary.csv.txt", data_personal)
    info_logger(f'Новая запись в таблицу "Salary" {data_personal}')

    data_personal = add_data_Department(id_pes)
    append_data("Department.csv.txt", data_personal)
    info_logger(f'Новая запись в таблицу "Department" {data_personal}')

    print_data("\nДанные успешно добавлены.")

def search_data():
    id_pes = input("Введите id: ")
    info_logger(f'Запрос на поиск по ID {id_pes}')

    list_data = get_info("PI.csv.txt")
    list_data += get_info("Salary.csv.txt")
    list_data += get_info("Department.csv.txt")
    count = 0
    for i in list_data:
        if f"ID {id_pes}" in i:
            print(i)
            count += 1
    if count == 0:
        print("Информация не найдена")
