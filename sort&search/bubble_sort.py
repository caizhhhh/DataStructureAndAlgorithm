# coding: utf-8


def bubble_sort(data_list):
    '''各个元素为int的无序list，冒泡排序后返回升序排列的list'''
    length = len(data_list)
    while length >= 2:
        for index in range(length-1):
            if data_list[index] > data_list[index+1]:
                data_list[index], data_list[index+1] = data_list[index+1], data_list[index]
        length -= 1

    return data_list


# 冒泡排序改进。如果某一轮比对，没有发生一次位置交换，则说明顺序是OK的
def bubble_sort2(data_list):
    '''各个元素为int的无序list，冒泡排序后返回升序排列的list'''
    length = len(data_list)
    while length >= 2:
        is_ok = True
        for index in range(length-1):
            if data_list[index] > data_list[index+1]:
                data_list[index], data_list[index+1] = data_list[index+1], data_list[index]
                is_ok = False
        if is_ok:
            break
        length -= 1

    return data_list

# lst = [1, 2, 9, 3, 10, 12]
# print(bubble_sort(lst))
