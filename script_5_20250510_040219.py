# Personal coding practice
# Problem: Concatenate a trie using DFS.

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

def concatenate_trie(root):
    result = []

    stack = [(root, '')]

    while stack:
        node, path = stack.pop()

        if node.end_of_word:
            result.append(path)

        for char, child_node in node.children.items():
            stack.append((child_node, path + char))

    return ''.join(result)
```