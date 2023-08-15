# Extra Classes for leetcode python


# Singly linked list
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def push(self, val):
        cur = self

        while cur.next:
            cur = cur.next

        cur.next = ListNode(val=val)

    def print(self):
        cur = self

        print("ListNode: ")

        valList = []

        while cur:
            valList.append(cur.val)
            cur = cur.next

        print(" -> ".join([str(i) for i in valList]))

    def from_list(arr: list):
        if len(arr) < 1:
            return None

        head = ListNode(arr[0])

        cur = head

        for val in arr[1:]:
            cur.next = ListNode(val)
            cur = cur.next

        return head

    def concat(ln1, ln2):
        cur = ln1
        while cur.next:
            cur = cur.next

        cur.next = ln2


if __name__ == '__main__':
    fooo = ListNode.from_list([1, 2, 3])
    fooo.push(4)
    fooo.print()
