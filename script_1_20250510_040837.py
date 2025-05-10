# Personal coding practice
# Problem: Filter a list using memoization.

```python
def filter_memoized(lst, predicate):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = predicate(x)
        return memo[x]

    return [x for x in lst if helper(x)]
```