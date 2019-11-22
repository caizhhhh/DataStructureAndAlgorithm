# coding: utf-8
'''快排。
我的实现有点丑，底部注释有更优雅的版本'''


def quick_sort(data_list, left, right):
    '''left、right分别为list的左右边index。
    原地排序，函数返回None'''
    if right > left:
        low, high = left + 1, right
        low_stop = high_stop = False
        middle_value = data_list[left]
        while low <= high and high >= left and low <= right:
            if not low_stop and data_list[low] > middle_value:
                low_stop = True
            if not high_stop and data_list[high] < middle_value:
                high_stop = True
            if low_stop and high_stop:
                data_list[low], data_list[high] = data_list[high], data_list[low]
                low_stop = high_stop = False
            if not low_stop:
                low += 1
            if not high_stop:
                high -= 1

        data_list[left], data_list[high] = data_list[high], data_list[left]
        quick_sort(data_list, left, high-1)
        quick_sort(data_list, high+1, right)


# lst = [20, 3, 88, 10, 22, 12, 9, 8, 100, 99, 88, 0]
# quick_sort(lst, 0, len(lst)-1)
# print(lst)


'''
def quickSort(array, left, right):
    if left < right:
        q = partition(array, left, right)
        quickSort(array, left, q-1)
        quickSort(array, q+1, right)


def partition(array, left, right):
    key = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] <= key:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[right] = array[right], array[i+1]

    return i + 1


lst = [20, 3, 88, 10, 22, 12, 9, 8, 100, 99, 88, 0]
quickSort(lst, 0, len(lst)-1)
print(lst)
'''
