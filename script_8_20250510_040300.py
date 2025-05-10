# Personal coding practice
# Problem: Find a stack using divide and conquer.

```python
def find_stack(arr):
    def divconquer(arr, low, high):
        if low == high:
            return arr[low]
        mid = (low + high) // 2
        left_max = divconquer(arr, low, mid)
        right_max = divconquer(arr, mid + 1, high)
        return max(left_max, right_max)
    
    if not arr:
        return None
    return divconquer(arr, 0, len(arr) - 1)
```