def create_list_number_random(size):
    from random import randint
    list_number = [randint(1, 100) for _ in range(size)]
    return list_number

def check_input_number(text):
    flag = False
    while flag == False:
        user_number = input(text)
        try:
            float(user_number)
            return int(user_number)
        except ValueError:
            flag == False

def create_list_number_fl_random(size):
    import random
    list_number = [round(random.uniform(0, 20), 2) for _ in range(size)]
    return list_number