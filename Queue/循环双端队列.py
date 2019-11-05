# coding: utf-8

'''641. 设计循环双端队列
设计实现双端队列。
你的实现需要支持以下操作：

MyCircularDeque(k)：构造函数,双端队列的大小为k。
insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true。
insertLast()：将一个元素添加到双端队列尾部。如果操作成功返回 true。
deleteFront()：从双端队列头部删除一个元素。 如果操作成功返回 true。
deleteLast()：从双端队列尾部删除一个元素。如果操作成功返回 true。
getFront()：从双端队列头部获得一个元素。如果双端队列为空，返回 -1。
getRear()：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1。
isEmpty()：检查双端队列是否为空。
isFull()：检查双端队列是否满了。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-circular-deque
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Node:

    def __init__(self, data, _next=None):
        self.data = data
        self.next = _next


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.head = None
        self.rear = None
        self.max_length = k
        self.length = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.length == self.max_length:
            return False
        new_item = Node(value, self.head)
        self.head = new_item
        if not self.rear:
            self.rear = new_item
        self.length += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.length == self.max_length:
            return False
        new_item = Node(value)
        if self.rear:
            self.rear.next = new_item
        self.rear = new_item
        if not self.length:
            self.head = new_item
        self.length += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.length:
            self.head = self.head.next
            self.length -= 1
            if not self.length:
                self.rear = None
            return True
        return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.length:
            if self.length == 1:
                self.head, self.rear, self.length = None, None, 0
                return True
            # 一个指针域的话，时间复杂度是On
            p = self.head
            # print(self.max_length, self.length, self.head)
            pre_item = Node(-1)
            while p.next:
                pre_item, p = p, p.next
            pre_item.next = None
            self.rear = pre_item
            self.length -= 1
            return True
        return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.length:
            return self.head.data
        return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.length:
            return self.rear.data
        return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.length == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.length == self.max_length

    def print_queue(self):
        result = []
        p = self.head
        while p:
            result.append(p.data)
            p = p.next
        return result

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
