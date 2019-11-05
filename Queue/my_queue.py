# coding: utf-8


class Node:

    def __init__(self, data, _next=None):
        self.data = data
        self.next = _next


class Queue:

    def __init__(self):
        self.head = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if not self.rear:
            self.head = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.head:
            item = self.head
            self.head = self.head.next
            if self.rear == item:
                self.rear = None
            return item.data
        return None

    def is_empty(self):
        return self.head is None

    def length(self):
        p = self.head
        count = 0
        while p:
            count += 1
            p = p.next
        return count

    def print_queue(self):
        p = self.head
        print_list = []
        while p:
            print_list.append(p.data)
            p = p.next
        return print_list


# q = Queue()
# print(q.is_empty())
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print(q.is_empty())
# print(q.length())
# print(q.print_queue())
# print(q.dequeue())
# print(q.is_empty())
# print(q.length())
# print(q.print_queue())
