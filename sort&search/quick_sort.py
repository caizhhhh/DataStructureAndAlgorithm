# coding: utf-8


def quick_sort(data_list):
    # 中值
    middle_value = data_list[0]
    left, right = 1, len(data_list) - 1
    left_stop, right_stop = False, False
    while left < right:
        if not left_stop and data_list[left] > middle_value:
            left_stop = True
            left += 1
        if not right_stop and data_list[right] < middle_value:
            right_stop = True
            right += 1
        if left_stop and right_stop:
            data_list[left], data_list[right] = data_list[right], data_list[left]
            left_stop = right_stop = False


def wtf(data_list):
    pass
