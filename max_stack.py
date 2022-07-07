from typing import List

# similar to 155. Min Stack, we append x and the current max as a tuple to the stack.
# each operation is amortized O(1)
class MaxStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curr_max = self.peekMax()
        if not curr_max or x > curr_max: curr_max = x
        self.s.append((x, curr_max))

    def pop(self):
        """
        :rtype: int
        """
        return self.s.pop()[0] if self.s else None

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1][0] if self.s else None

    def peekMax(self):
        """
        :rtype: int
        """
        return self.s[-1][1] if self.s else None

    def popMax(self):
        """
        :rtype: int
        """
        curr_max = self.peekMax()
        s2 = []
        while self.top() != curr_max:
            s2.append(self.s.pop()[0])
        self.s.pop()
        while s2:
            self.push(s2.pop())
        return curr_max


if __name__ == '__main__':
    stack = MaxStack()
    out = []
    stack.push(5)
    stack.push(1)
    stack.push(5)
    out += stack.top(),
    out += stack.popMax(),
    out += stack.top(),
    out += stack.peekMax(),
    out += stack.pop(),
    out += stack.top(),

    expect = [5,5,1,5,1,5]
    if expect == out:
        print('Accepted')
    else:
        print('Wrong')
        print(out)
