# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in
# 100

# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]

def un_list(num):
    return [l for l in range(20, num + 1) if l % 20 == 0 or l % 21 == 0]

print(un_list(int(input("Введите N: "))))    

