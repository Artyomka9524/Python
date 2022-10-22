import ui
from answers import *


def button_click():
    ui.print_data("Вы можете: \n1. Вывести всю информацию\n2. Добавить информацию \n3. Поиск по ID")
    user_answer = ui.input_data("Введите цифру: ")
    print()
    if user_answer == "1":
        print_all()
    elif user_answer == "2":
        add_data()
    elif user_answer == "3":
        search_data()