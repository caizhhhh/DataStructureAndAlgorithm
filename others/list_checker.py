# coding: utf-8

import timeit


def test1():
	lst = []
	for i in range(1000):
		lst = lst + [i]


def test2():
	lst = []
	for i in range(1000):
		lst.append(i)


def test3():
	lst = [x for x in range(1000)]


def test4():
	lst = list(range(1000))


t1 = timeit.timeit("test1()", "from __main__ import test1", number=1000)
t2 = timeit.timeit("test2()", "from __main__ import test2", number=1000)
t3 = timeit.timeit("test3()", "from __main__ import test3", number=1000)
t4 = timeit.timeit("test4()", "from __main__ import test4", number=1000)

print('t1 cost time {}'.format(t1))
print('t2 cost time {}'.format(t2))
print('t3 cost time {}'.format(t3))
print('t4 cost time {}'.format(t4))


'''
the result:
t1 cost time 1.3350609
t2 cost time 0.08810650000000009
t3 cost time 0.03256999999999999
t4 cost time 0.014445800000000064
'''


# def test5():
#     lst = [list(range(100)), list(range(100)), list(range(100)), list(range(100)), list(range(100)), list(range(100)), list(range(100))]
#     return [y for x in lst for y in x]
#
#
# def test6():
#     lst = [list(range(100)), list(range(100)), list(range(100)), list(range(100)), list(range(100)), list(range(100)), list(range(100))]
#     # res = lst[0]
#     res = []
#     for index in range(0, len(lst)):
#         res.extend(lst[index])
#     return res
#
#
# t5 = timeit.timeit("test5()", "from __main__ import test5", number=1000)
# t6 = timeit.timeit("test6()", "from __main__ import test6", number=1000)
# print('t5 cost time {}'.format(t5))
# print('t6 cost time {}'.format(t6))
