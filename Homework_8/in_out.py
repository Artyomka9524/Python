def append_data(name_file, data):
    with open(name_file, 'a') as file:
        file.write(f"{data},")


def get_info(name_file):
    with open(name_file, 'r', encoding="UTF-8") as file:
        info = file.read().split(",")
    return info
