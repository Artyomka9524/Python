def print_data(text=''):
    print(f"{text}")


def input_data(text=''):
    return input(f"{text}")


def add_data_pi(id_pes):
    surname = input("surname: ")
    name = input("name: ")
    patronymic = input("patronymic: ")
    phone = input("phone +7 :")
    return f"ID {id_pes} phone: +7 {phone} surname: {surname} name: {name} patronymic: {patronymic}"


def add_data_Salary(id_pes):
    salary = input("salary: ")
    return f"ID {id_pes} {salary}"


def add_data_Department(id_pes):
    department = input("department: ")
    position = input("position: ")
    return f"ID {id_pes} Department {department} Position {position}"
