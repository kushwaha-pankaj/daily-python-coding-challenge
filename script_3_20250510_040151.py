# Personal coding practice
# Problem: Check a queue using DFS.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def dfs_search_in_queue(node, target):
    stack = [node]
    while stack:
        current = stack.pop()
        if current.value == target:
            return True
        for child in reversed(current.children):
            stack.append(child)
    return False
```