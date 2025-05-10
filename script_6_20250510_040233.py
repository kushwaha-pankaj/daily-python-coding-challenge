# Personal coding practice
# Problem: Count a stack using BFS.

```python
def count_stack_bfs(stack):
    def bfs(stack):
        count = 0
        stack_temp = []
        while stack:
            node = stack.pop()
            count += 1
            for child in node.get('children', []):
                stack_temp.append(child)
        return count, stack_temp

    total_count = 0
    while stack:
        count, new_stack = bfs(stack)
        total_count += count
        stack = new_stack

    return total_count
```