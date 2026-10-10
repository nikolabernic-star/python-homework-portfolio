
id_1 = 4
id_2 = 2
id_3 = 8
id_4 = 5


def fix_number(num):
    if num > 9:
        return num - 9
    else:
        return num



p1 = id_1
p2 = fix_number(id_2 * 2)  # 2 * 2 = 4 -> fix_number(4) = 4
p3 = id_3
p4 = fix_number(id_4 * 2)  # 5 * 2 = 10 -> fix_number(10) = 1


total = p1 + p2 + p3 + p4  # 4 + 4 + 8 + 1 = 17


check_number = (10 - (total % 10)) % 10  # (10 - 7) % 10 = 3



full_id = (str(id_1) + str(id_2) + str(id_3) + str(id_4) + str(check_number))

print(full_id)
