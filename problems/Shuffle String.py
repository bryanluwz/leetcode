# https://leetcode.com/problems/shuffle-string/
def restoreString(s: str, indices: list[int]) -> str:
    restored_string = [''] * len(indices)

    for ori_index, restored_index in enumerate(indices):
        restored_string[restored_index] = s[ori_index]

    return ''.join(restored_string)


if __name__ == '__main__':
    print(restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
