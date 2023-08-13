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
        # DP: mem contains two axis, mem[i][j] shows whether nums[i:j] is valid or not
        mem = [[False] * (len(nums) + 1) for _ in range(len(nums) + 1)]

        # Fill up base case first
        # for i in range(len(mem)):
        #     for j in range(len(mem)):
        #         if 2 <= j - i <= 3:
        #             mem[i][j] |= all(elem == nums[i] for elem in nums[i:j])
        #             mem[i][j] |= all(
        #                 nums[k] - nums[k - 1] == 1
        #                 for k in range(i + 1, j)) if j - i == 3 else False

        for i in range(len(mem)):
            if i < len(mem) - 2:
                mem[i][i + 2] = all(elem == nums[i] for elem in nums[i:i + 2])

            if i < len(mem) - 3:
                mem[i][i + 3] = all(elem == nums[i] for elem in nums[i:i + 3])
                mem[i][i + 3] |= nums[i + 2] - nums[i + 1] == nums[
                    i + 1] - nums[i] == 1

        for i in range(len(mem)):
            for j in range(i + 3, len(mem)):
                if i > j:
                    continue
                elif 2 <= j - i <= 3:
                    pass
                else:
                    mem[i][j] = (mem[i][j - 2]
                                 and mem[j - 2][j]) or (mem[i][j - 3]
                                                        and mem[j - 3][j])

        # Returns mem[0][-1]
        # print(nums)

        # print("i", end="")
        # [print(f"{i:6}", end="") for i in range(len(mem))]
        # print()

        # for k, i in enumerate(mem):
        #     print(k, end=" ")
        #     for j in i:
        #         print(f"{str(j):6}", end="")
        #     print()

        return mem[0][-1]

    # Main function
    def main(self):
        arr = [348054, 7876, 34051]
        print(self.validPartition(arr))


solution = Solution()
solution.main()
