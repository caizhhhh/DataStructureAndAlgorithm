# coding: utf-8
'''
栈是一种特殊的表，数据只能从栈顶（top）插入，称做压入（push）,也只能从栈顶删除，称为弹出（pop）。其特点是后进先出（LIFO）

操作：
is_empty():返回布尔值
length():返回栈内元素个数
push(item):压入元素到栈顶
pop():弹出栈顶的元素
get_top():查看栈顶的元素
get_items():从栈底到栈顶依次打印栈内元素
'''


class NoDataError(Exception):
	pass


class Stack:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def length(self):
		return len(self.items)

	def push(self, item):
		self.items.append(item)

	def pop(self):
		if self.is_empty():
			raise NoDataError
		return self.items.pop()

	def get_top(self):
		if self.is_empty():
			raise NoDataError
		return self.items[-1]

	def get_items(self):
		return self.items
