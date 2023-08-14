# This file is for LeetCode daily challenge for the August 2023.
# Language of the month: Python
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

    # Main function
    def main(self):
        arr = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        print(self.findKthLargest(arr, 4))


solution = Solution()
solution.main()
