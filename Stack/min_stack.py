# coding: utf-8
'''
155.最小栈
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

    push(x) -- 将元素 x 推入栈中。
    pop() -- 删除栈顶的元素。
    top() -- 获取栈顶元素。
    getMin() -- 检索栈中的最小元素。

示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-stack
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.is_empty = True

    def push(self, x: int) -> None:
        '''先压入最小值，再压入x'''
        self.items.append(x if self.is_empty else (x if x < self.items[-2] else self.items[-2]))
        self.items.append(x)
        if self.is_empty:
            self.is_empty = False

    def pop(self) -> None:
        self.items.pop()
        self.items.pop()
        if not self.items:
            self.is_empty = True

    def top(self) -> int:
        if self.items:
            return self.items[-1]

    def getMin(self) -> int:
        if not self.is_empty:
            return self.items[-2]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
