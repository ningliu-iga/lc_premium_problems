from typing import List
import collections


# use a dictionary to count the number of occurrence of each number, if the count==2, don't need to increment any more
# each operation is O(1) time, O(n) space
class FirstUnique1:
    def __init__(self, nums: List[int]):
        self.count = collections.defaultdict(int)
        self.nums = collections.deque()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while self.nums and self.count[self.nums[0]] > 1:
            self.nums.popleft()
        return self.nums[0] if self.nums else -1

    def add(self, value: int) -> None:
        if self.count[value] > 1: return
        if self.count[value] == 1:
            self.count[value] += 1
            return
        self.count[value] += 1
        self.nums.append(value)
        return


# using doubly linked list, where head and tail are dummy nodes. use a map to record the key-node pair.
# use a set to record non-unique numbers.
# each operation is O(1) time, O(n) space
class FirstUnique:
    def __init__(self, nums: List[int]):
        self.head, self.tail = ListNode(0), ListNode(0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.key2node = {}
        self.non_unique_nums = set()
        for num in nums: self.add(num)

    def showFirstUnique(self) -> int:
        if self.key2node: return self.head.next.val
        return -1

    def add(self, value: int) -> None:
        if value in self.non_unique_nums: return
        if value not in self.key2node:
            node = ListNode(value)
            self.key2node[value] = node
            self.add_to_tail(node)
        else:
            to_del_node = self.key2node[value]
            # need to del the element in map first then del node, otherwise will cause NPE (null pointer exception)
            del self.key2node[value]  # same as self.key2node.pop(value)
            self.del_node(to_del_node)
            self.non_unique_nums.add(value)

    def add_to_tail(self, node):
        predecessor = self.tail.prev
        predecessor.next, node.prev = node, predecessor
        node.next, self.tail.prev = self.tail, node

    def del_node(self, node):
        predecessor, successor = node.prev, node.next
        predecessor.next, successor.prev = successor, predecessor
        node.prev, node.next = None, None  # need to set prev and next to None when deleting a node


class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


if __name__ == '__main__':
    firstUnique = FirstUnique([2, 3, 5])
    out = []
    out.append(firstUnique.showFirstUnique())
    firstUnique.add(5)
    out.append(firstUnique.showFirstUnique())
    firstUnique.add(2)
    out.append(firstUnique.showFirstUnique())
    firstUnique.add(3)
    out.append(firstUnique.showFirstUnique())

    expect = [2, 2, 3, -1]
    if expect == out:
        print('Accepted')
    else:
        print('Wrong')
        print(out)
