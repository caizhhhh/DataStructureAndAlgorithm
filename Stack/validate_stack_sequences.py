# coding: utf-8


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def get_top(self):
        return self.items[-1]


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # if len(pushed) != len(popped):
        # 	return False
        stack = Stack()
        index = 0
        for item in pushed:
            stack.push(item)
            while not stack.is_empty() and popped[index] == stack.get_top():
                stack.pop()
                index += 1

        return stack.is_empty()
