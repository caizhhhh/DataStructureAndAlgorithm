# coding: utf-8


'''895. 最大频率栈
实现 FreqStack，模拟类似栈的数据结构的操作的一个类。

FreqStack 有两个函数：

    push(int x)，将整数 x 推入栈中。
    pop()，它移除并返回栈中出现最频繁的元素。
        如果最频繁的元素不只一个，则移除并返回最接近栈顶的元素。



示例：

输入：
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
输出：[null,null,null,null,null,null,null,5,7,5,4]
解释：
执行六次 .push 操作后，栈自底向上为 [5,7,5,7,4,5]。然后：

pop() -> 返回 5，因为 5 是出现频率最高的。
栈变成 [5,7,5,7,4]。

pop() -> 返回 7，因为 5 和 7 都是频率最高的，但 7 最接近栈顶。
栈变成 [5,7,5,4]。

pop() -> 返回 5 。
栈变成 [5,7,4]。

pop() -> 返回 4 。
栈变成 [5,7]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-frequency-stack
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class FreqStack:

    def __init__(self):
        self.items = {}
        self.freq = {}
        self.max_freq = 0

    def push(self, x: int) -> None:
        self.freq[x] = self.freq.get(x, 0) + 1
        if self.items.get(self.freq[x], '') != '':
            self.items[self.freq[x]].append(x)
        else:
            self.items[self.freq[x]] = [x]
        self.max_freq = self.freq[x] if self.freq[x] > self.max_freq else self.max_freq

    def pop(self) -> int:
        item = self.items[self.max_freq].pop()
        if not self.items[self.max_freq]:
            self.max_freq -= 1
        self.freq[item] -= 1
        return item

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()


