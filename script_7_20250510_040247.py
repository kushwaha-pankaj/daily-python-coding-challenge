# Personal coding practice
# Problem: Generate a hash table using topological sort.

```python
def topological_sort_with_memoization(graph):
    def dfs(node):
        if node in memo:
            return memo[node]
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
        result.append(node)
        memo[node] = result[:]

    visited = set()
    result = []
    memo = {}
    for node in graph:
        if node not in visited:
            dfs(node)
    return result[::-1]

# Example usage
# graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
# print(topological_sort_with_memoization(graph)) 
```