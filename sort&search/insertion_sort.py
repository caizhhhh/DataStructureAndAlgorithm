# coding: utf-8


def insertion_sort(data_list):
    for index in range(1, len(data_list)):
        current_item = data_list[index]
        position = index
        while position > 0 and current_item < data_list[position-1]:
            data_list[position] = data_list[position-1]
            position -= 1

        data_list[position] = current_item

    return data_list


lst = [2, 3, 1, 10, 12, 9]
print(insertion_sort(lst))
