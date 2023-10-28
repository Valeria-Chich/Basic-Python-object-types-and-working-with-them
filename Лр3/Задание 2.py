def find_common_participants(str_1, str_2, separate=","):# TODO Напишите функцию find_common_participants
    communis_list = []
    str_1_new = separate.join(list(str_1.split("|")))
    str_2_new = separate.join(list(str_2.split("|")))
    list_1 = str_1_new.split(separate)
    list_2 = str_2_new.split(separate)
    for people in list_1:
        if people in list_2:
            communis_list.append(people)
    return communis_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print("Список общих участнико:",find_common_participants(participants_first_group, participants_second_group))
print("Список общих участнико:",find_common_participants(participants_first_group, participants_second_group, separate=";"))# TODO Провеьте работу функции с разделителем отличным от запятой
