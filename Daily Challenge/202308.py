# This file is for LeetCode daily challenge for the August 2023.
# Language of the month: Python
from python_extra_classes import *


# Solution Class
class Solution:

    # 20230810: Search in Rotated Sorted Array II https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
    def search(self, nums: list[int], target: int) -> bool:
        return target in nums

    # 20230811: Coin Change II https://leetcode.com/problems/coin-change-ii/
    def change(self, amount: int, coins: list[int]) -> int:
        # We be using dynamic programming function
        # Either we can use current coin, or dont use current coin
        # Recursive function
        def rec(amount_left: int, current_coin_index: int):
            if amount_left == 0:
                return 1

            if amount_left < 0 or current_coin_index >= len(coins):
                return 0

            # Use current coin
            count_current_coin = rec(amount_left - coins[current_coin_index],
                                     current_coin_index)

            # Use next coin
            count_next_coin = rec(amount_left, current_coin_index + 1)

            return count_current_coin + count_next_coin

        # So recurrence formula is f(amount, current_coin_index) = f(amount - current_coin, current_coin_index) + f(amount, current_coin_index + 1)

        # Top down DP (but some how not working)
        mem = [[0 for _ in range(len(coins))] for _ in range(amount + 1)]
        for i in range(len(coins)):
            mem[0][i] = 1  # Base case

        def top_down(amount_left: int, current_coin_index: int):
            if amount_left == 0:
                return 1
            if amount_left < 0 or current_coin_index >= len(coins):
                return 0

            if mem[amount_left][current_coin_index] != 0:
                return mem[amount_left][current_coin_index]

            mem[amount_left][current_coin_index] = top_down(
                amount_left - coins[current_coin_index],
                current_coin_index) + top_down(amount_left,
                                               current_coin_index + 1)

            return mem[amount_left][current_coin_index]

        # Bottom up DP
        mem = [[0 for _ in range(len(coins))] for _ in range(amount + 1)]
        for i in range(len(coins)):
            mem[0][i] = 1

        for i in range(1, amount + 1):
            for j in range(0, len(coins)):
                if i - coins[j] >= 0:
                    mem[i][j] = mem[i - coins[j]][j]  # Use current coin
                if j >= 1:
                    mem[i][j] += mem[i][j - 1]  # Dont use current coin

        return mem[amount][len(coins) - 1]

    # 20230812: Unique Paths II https://leetcode.com/problems/unique-paths-ii/
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        # Robot on top left, goal on bottom right, obstacle is 1
        # Robot can only move down or right (i.e. index can increase)
        # Recursive function
        def rec(x: int, y: int) -> int:
            if y >= len(obstacleGrid) or x >= len(
                    obstacleGrid[0]) or obstacleGrid[y][x]:
                return 0

            if y == len(obstacleGrid) - 1 and x == len(obstacleGrid[0]) - 1:
                return 1

            return rec(x + 1, y) + rec(x, y + 1)  # Go right + Go down

        # Bottom up
        # mem[y][x] is the unique paths to reach y, x
        mem = [[0 for _ in range(len(obstacleGrid[0]))]
               for _ in range(len(obstacleGrid))]
        mem[0][0] = 1

        for y in range(len(obstacleGrid)):
            for x in range(len(obstacleGrid[0])):
                if obstacleGrid[y][x] == 1:
                    mem[y][x] = 0
                    continue

                if (y == x == 0):
                    continue

                mem[y][x] = 0

                if y - 1 >= 0:
                    mem[y][x] += mem[y - 1][x]
                if x - 1 >= 0:
                    mem[y][x] += mem[y][x - 1]

        return mem[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]

    # 20230813: Check if There is a Valid Partition For The Array https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/
    def validPartition(self, nums: list[int]) -> bool:
        # Use sliding window of size three to scan through array
        mem = [True, False, nums[0] == nums[1] if len(nums) > 1 else False]

        # mem[0] is validity of partition nums[0:i-2]
        # mem[1] is validity of partition nums[0:i-1]
        # mem[2] is validity of partition nums[0:i]

        for i in range(2, len(nums)):
            cur = False

            # Check for two equal elem
            cur |= nums[i] == nums[i - 1] and mem[1]

            # Check for three equal elem
            cur |= nums[i] == nums[i - 1] == nums[i - 2] and mem[0]

            # Check for consec
            cur |= nums[i] - nums[i - 1] == 1 and nums[i - 1] - nums[
                i - 2] == 1 and mem[0]

            # Move window forward
            mem[0], mem[1], mem[2] = mem[1], mem[2], cur

        return mem[2]

    # 20230814: Kth Largest Element in an Array https://leetcode.com/problems/kth-largest-element-in-an-array/
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # IDK man
        nums.sort()
        return nums[-k]

    # 20230815: Partition List https://leetcode.com/problems/partition-list/
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None

        smaller = None
        larger = None

        cur = head
        smaller_tail = None
        larger_tail = None

        while cur:
            if cur.val < x:
                if not smaller:
                    smaller = ListNode(cur.val)
                    smaller_tail = smaller
                else:
                    smaller_tail.next = ListNode(cur.val)
                    smaller_tail = smaller_tail.next
            elif cur.val >= x:
                if not larger:
                    larger = ListNode(cur.val)
                    larger_tail = larger
                else:
                    larger_tail.next = ListNode(cur.val)
                    larger_tail = larger_tail.next
            cur = cur.next

        if smaller_tail:
            smaller_tail.next = larger
            return smaller
        else:
            return larger

    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        window_max = []
        queue = []

        for i in range(len(nums)):
            # Remove previous elem if max is out of window
            while queue and queue[0] <= i - k:
                queue.pop(0)

            # Remove smaller elem if current elem is larger
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            # Add current elem index to queue
            queue.append(i)

            # Add max to window once sliding window is of starting index k - 1, i represents ending index of sliding window
            if i >= k - 1:
                window_max.append(nums[queue[0]])

        return window_max

    # 20230817: 01-Matrix https://leetcode.com/problems/01-matrix/
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        result = [[float('inf') for _ in range(len(mat[0]))]
                  for _ in range(len(mat))]

        # Top left to bottom right
        for y in range(len(mat)):
            for x in range(len(mat[0])):
                if mat[y][x] == 0:
                    result[y][x] = 0
                else:
                    if y - 1 >= 0:
                        result[y][x] = min(result[y][x], result[y - 1][x] + 1)
                    if x - 1 >= 0:
                        result[y][x] = min(result[y][x], result[y][x - 1] + 1)

        # Bottom right to top left
        for y in range(len(mat) - 1, -1, -1):
            for x in range(len(mat[0]) - 1, -1, -1):
                if mat[y][x] == 0:
                    result[y][x] = 0
                else:
                    if y + 1 < len(mat):
                        result[y][x] = min(result[y][x], result[y + 1][x] + 1)
                    if x + 1 < len(mat[0]):
                        result[y][x] = min(result[y][x], result[y][x + 1] + 1)

        return result

    # 20230818: Maximal Network Rank https://leetcode.com/problems/maximal-network-rank/
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        # Calculate degrees
        degrees_list = [0 for _ in range(n)]
        for i in range(n):
            for pairs in roads:
                if i in pairs:
                    degrees_list[i] += 1

        # Find total links for each pair
        network_links = []
        for i in range(n):
            for j in range(i + 1, n):
                network_links.append(degrees_list[i] + degrees_list[j])
                if [i, j] in roads or [j, i] in roads:
                    network_links[-1] -= 1

        return max(network_links)

    # 20230819: Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/
    # OK I didn't solve this myself, I just copied the solution from the solution tab
    def findCriticalAndPseudoCriticalEdges(
            self, n: int, edges: list[list[int]]) -> list[list[int]]:

        class UnionFind:

            def __init__(self, n):
                self.parent = list(range(n))

            def find_parent(self, p):
                if self.parent[p] == p:
                    return p
                self.parent[p] = self.find_parent(self.parent[p])
                return self.parent[p]

            def union(self, u, v):
                pu, pv = self.find_parent(u), self.find_parent(v)
                self.parent[pu] = pv

        def find_mst(n, edges, block, e):
            uf = UnionFind(n)
            weight = 0

            if e != -1:
                weight += edges[e][2]
                uf.union(edges[e][0], edges[e][1])

            for i in range(len(edges)):
                if i == block:
                    continue
                if uf.find_parent(edges[i][0]) == uf.find_parent(edges[i][1]):
                    continue
                uf.union(edges[i][0], edges[i][1])
                weight += edges[i][2]

            for i in range(n):
                if uf.find_parent(i) != uf.find_parent(0):
                    return float('inf')

            return weight

        critical, pseudo_critical = [], []

        for i in range(len(edges)):
            edges[i].append(i)

        edges.sort(key=lambda x: x[2])

        mst_wt = find_mst(n, edges, -1, -1)

        for i in range(len(edges)):
            if mst_wt < find_mst(n, edges, i, -1):
                critical.append(edges[i][3])
            elif mst_wt == find_mst(n, edges, -1, i):
                pseudo_critical.append(edges[i][3])

        return [critical, pseudo_critical]

    # 20230821: Repeated Substring Pattern https://leetcode.com/problems/repeated-substring-pattern/
    def repeatedSubstringPattern(self, s: str) -> bool:
        # from https://assets.leetcode.com/users/images/a42cee30-15be-4992-aa71-07bb8adb669c_1656832963.0830936.jpeg
        return s in (s + s)[1:-1]

    # Main function
    def main(self):
        arr = [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3],
               [3, 4, 3], [1, 4, 6]]
        print(self.findCriticalAndPseudoCriticalEdges(5, arr))


solution = Solution()
solution.main()
