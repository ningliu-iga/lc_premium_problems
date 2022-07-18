from typing import List


# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:


class Solution:
    # use a for loop to search for potential candidate: if the current candidate knows i, then the current candidate is
    # not the celebrity and i is the possible celebrity. once we decide the possible candidate, anybody before him
    # cannot be the celebrity bc the "anybody" is passed either bc he knows somebody (which becomes the new candidate)
    # or somebody don't know him. Anybody after the possible candidate cannot be the celebrity bc the current candidate
    # doesnt know him. The next step is to check the people before and after him to make sure the candidate meets
    # celebrity criterion.
    # O(n) time, O(1) space
    def findCelebrity(self, n: int, graph) -> int:
        candidate = 0
        for i in range(1, n):
            if graph[candidate][i] == 1:
                candidate = i
        for i in range(n):
            if i < candidate and (graph[i][candidate] == 0 or graph[candidate][i] == 1):
                return -1
            if i > candidate and graph[i][candidate] == 0:
                return -1
        return candidate


if __name__ == '__main__':
    graph1 = [[1, 1, 0], [0, 1, 0], [1, 1, 1]]
    graph2 = [[1, 0, 1], [1, 1, 0], [0, 1, 1]]
    out = list(map(Solution().findCelebrity, [len(graph1), len(graph2)], [graph1, graph2]))

    expect = [1, -1]
    if expect == out:
        print('Accepted')
    else:
        print('Wrong')
        print(out)
