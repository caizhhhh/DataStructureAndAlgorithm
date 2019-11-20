# coding: utf-8


def merge_sort(data_list):
    '''归并排序，先分裂，再归并并排序'''
    # 递归基本结束条件
    if len(data_list) > 1:
        mid_index = len(data_list) // 2
        left, right = data_list[:mid_index], data_list[mid_index:]
        left = merge_sort(left)
        right = merge_sort(right)

        # 合并
        merge_list = []
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merge_list.append(left[i])
                i += 1
            else:
                merge_list.append(right[j])
                j += 1
            k += 1

        merge_list.extend(left[i:] if i < len(left) else right[j:])
        return merge_list
    return data_list

# lst = [2, 3, 1, 10, 12, 9, 8, 100, 99, 88, 0]
# print(merge_sort(lst))