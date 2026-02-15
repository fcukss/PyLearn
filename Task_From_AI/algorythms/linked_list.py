class ListNode:
    def __init__(self, val =0, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        res = []
        current = self
        while current:
            res.append(str(current.val))
            current = current.next
        return '->'.join(res) + '->'

def reverse_list(head):
    prev = None
    curr= head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

print("До разворота:")
print(node1)

# 2. Разворачиваем
new_head = reverse_list(node1)

print("После разворота:")
print(new_head)


"""
задача: "Заяц и Черепаха" 🐇🐢
Linked List Cycle (LeetCode №141).
"""

def hasCycle(head):
    if not head:
        return False

    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

