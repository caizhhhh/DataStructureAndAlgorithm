# coding: utf-8


def selection_sort(data_list):
    '''各个元素为int的无序list，冒泡排序后返回升序排列的list'''
    length = len(data_list)
    while length >= 2:
        the_max_ind = 0
        for index in range(1, length):
            if data_list[index] > data_list[the_max_ind]:
                the_max_ind = index
        data_list[the_max_ind], data_list[length-1] = data_list[length-1], data_list[the_max_ind]
        length -= 1
    return data_list


# lst = [2, 3, 1, 10, 12, 9]
# print(selection_sort(lst))
