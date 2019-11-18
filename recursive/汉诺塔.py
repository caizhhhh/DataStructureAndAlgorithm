# coding: utf-8
'''
汉诺塔问题请网上搜
'''


def hannota(height, start_pole, middle_pole, des_pole):
    # 结束条件
    if height >= 1:
        hannota(height-1, start_pole, des_pole, middle_pole)
        move(height, start_pole, des_pole)
        hannota(height-1, middle_pole, start_pole, des_pole)


def move(height, start_pole, des_pole):
    print('The disk{} moved from {} to {}'.format(height, start_pole, des_pole))


# hannota(4, '#1', '#2', '#3')



