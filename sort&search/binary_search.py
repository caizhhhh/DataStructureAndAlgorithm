# coding: utf-8
'''二分查找的前提是有序表；
二分查找的时间复杂度logn'''


def binary_search(data_list, item):
    '''查找item是否在有序表data_list里，返回布尔值'''
    low, high = 0, len(data_list) - 1
    Found = False
    while low <= high and not Found:
        middle = (low + high) // 2  # 区分python2、3的两个除法
        if data_list[middle] == item:
            Found = True
        else:
            if data_list[middle] > item:
                high = middle - 1
            else:
                low = middle + 1
