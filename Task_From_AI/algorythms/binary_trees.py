class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Задача: Maximum Depth of Binary Tree (Максимальная глубина дерева)
LeetCode №104
"""
def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    # 2. Рекурсивно вызываем функцию для левого и правого ребенка
    left_height = maxDepth(root.left)
    right_height = maxDepth(root.right)

    return 1 + max(left_height, right_height)


# Вспомогательная функция для вывода дерева (упрощенный BFS)
def tree_to_list(root: TreeNode):
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
        # Убираем лишние None в конце для красоты
        while result and result[-1] is None:
            result.pop()
    return result


"""Инверсия дерева (Invert Binary Tree)
LeetCode №226"""

def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root


# Собираем дерево снизу вверх
# Левая ветка
n1 = TreeNode(1)
n3 = TreeNode(3)
n2 = TreeNode(2, left=n1, right=n3)

# Правая ветка
n6 = TreeNode(6)
n9 = TreeNode(9)
n7 = TreeNode(7, left=n6, right=n9)

# Корень
root = TreeNode(4, left=n2, right=n7)
print("До инверсии:   ", tree_to_list(root))

inverted_root = invertTree(root)

print("После инверсии:", tree_to_list(inverted_root))
# Ожидаемый вывод: [4, 7, 2, 9, 6, 3, 1]


"""
Same Tree (LeetCode №100"""


def isSimmetric(root: TreeNode) -> bool:
    if not root:
        return True

    def isMirror(t1, t2):
        # 1. Если оба узла пустые — они зеркальны
        if not t1 and not t2:
            return True
        # 2. Если один пустой или значения не равны — не зеркальны
        if t1.val != t2.val or not t1 or not t2:
            return False
        return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

    return isMirror(root.left, root.right)

# решение лит кода
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         if not p and not q:
#             return True
#         if not p or not q or p.val != q.val:
        #     return False
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
