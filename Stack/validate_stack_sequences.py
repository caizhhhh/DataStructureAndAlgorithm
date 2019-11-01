# coding: utf-8

from my_stack import Stack


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = Stack()
        index = 0
        for item in pushed:
            stack.push(item)
            while popped and not stack.is_empty() and popped[index] == stack.get_top():
                stack.pop()
                index += 1

        if stack.is_empty():
            return True
        return False

