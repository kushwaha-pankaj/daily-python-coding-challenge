# Personal coding practice
# Problem: Calculate a linked list using sliding window.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sliding_window_linked_list(head, k):
    if not head or k <= 0:
        return []

    current = head
    stack = []
    result = []

    while current:
        stack.append(current.val)
        if len(stack) > k:
            stack.pop(0)
        if len(stack) == k:
            result.append(stack[:])
        current = current.next
        
    return result
```