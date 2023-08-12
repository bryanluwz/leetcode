# https://leetcode.com/problems/find-latest-group-of-size-m/
def findLatestStep(arr: list[int], m: int) -> int:
    if len(arr) == m:
        return m

    binary_string = [0] * (len(arr) + 2)
    latest_step = -1

    for index, i in enumerate(arr):
        # i would be the index of the '1', since binary string is 1-indexed
        # left and right are just left and right of the '1'
        left = binary_string[i - 1]
        right = binary_string[i + 1]

        if left == m or right == m:
            latest_step = index

        # Keep track of the size of the grouping
        binary_string[i - left] = binary_string[i + right] = left + right + 1

    return latest_step


if __name__ == '__main__':
    print(findLatestStep([1, 2], 2))
