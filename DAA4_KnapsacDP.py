
### 0-1 Knapsack Problem (Dynamic Programming)

# In the 0-1 Knapsack problem, we can either take an entire item or leave it; fractions aren’t allowed.



#### 1) Simplified Code with Explanation


def knapsack_0_1(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

# Example usage
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
max_value = knapsack_0_1(weights, values, capacity)
print(f"Maximum value in the knapsack: {max_value}")
'''
#### 2) Code Explanation

- **`knapsack_0_1`**:
  - Initializes a 2D `dp` array where `dp[i][w]` represents the maximum value attainable with the first `i` items and a weight capacity `w`.
  - Iterates through each item and weight capacity:
    - If the current item weight is less than or equal to the current capacity, it’s either taken or skipped based on which choice yields a higher value.
    - If it’s greater than the current capacity, it’s skipped.
  - The result is stored in `dp[n][capacity]`, where `n` is the total number of items.

#### 3) Explanation of Input and Output

- **Input**:
  - `weights`: A list of weights of items.
  - `values`: A list of values of items.
  - `capacity`: The maximum weight the knapsack can hold.

- **Output**:
  - The maximum value achievable with the given items and capacity.

Example:
```
Weights = [10, 20, 30]
Values = [60, 100, 120]
Capacity = 50
Output: Maximum value in the knapsack: 220
```

#### 4) Time and Space Complexity

- **Time Complexity**: \(O(n \times C)\), where \(n\) is the number of items and \(C\) is the capacity.
- **Space Complexity**: \(O(n \times C)\) due to the 2D `dp` array.

'''



# ORRRRRRRRRRRRRRRRRRRRRRRRRrr

### 0-1 Knapsack Problem (Branch and Bound)


#### 1) Simplified Code with Explanation


class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound

def bound(node, n, capacity, weights, values):
    if node.weight >= capacity:
        return 0
    profit_bound = node.profit
    j = node.level + 1
    total_weight = node.weight

    while j < n and total_weight + weights[j] <= capacity:
        total_weight += weights[j]
        profit_bound += values[j]
        j += 1

    if j < n:
        profit_bound += (capacity - total_weight) * (values[j] / weights[j])
    return profit_bound

def knapsack_branch_bound(weights, values, capacity):
    n = len(values)
    items = sorted(range(n), key=lambda i: values[i] / weights[i], reverse=True)
    queue = []
    max_profit = 0
    root = Node(-1, 0, 0, 0)
    root.bound = bound(root, n, capacity, weights, values)
    queue.append(root)

    while queue:
        node = queue.pop(0)
        if node.level == n - 1 or node.bound <= max_profit:
            continue
        level = node.level + 1
        next_weight = node.weight + weights[items[level]]
        next_profit = node.profit + values[items[level]]

        if next_weight <= capacity and next_profit > max_profit:
            max_profit = next_profit

        if next_weight <= capacity:
            child = Node(level, next_profit, next_weight, 0)
            child.bound = bound(child, n, capacity, weights, values)
            if child.bound > max_profit:
                queue.append(child)

        child = Node(level, node.profit, node.weight, 0)
        child.bound = bound(child, n, capacity, weights, values)
        if child.bound > max_profit:
            queue.append(child)

    return max_profit

# Example usage
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print("Maximum value:", knapsack_branch_bound(weights, values, capacity))

'''

#### 2) Code Explanation

- **Class `Node`**: Represents a node in the decision tree, storing the level, current profit, current weight, and upper bound.
- **`bound` function**: Calculates the bound on the maximum profit for a node, helping decide whether to explore further.
- **`knapsack_branch_bound`**: Uses a queue to perform breadth-first search on the decision tree. It updates `max_profit` as it encounters nodes with higher achievable profits, pruning nodes with bounds below `max_profit`.

#### 3) Explanation of Input and Output

- **Input**:
  - Same as the 0-1 Knapsack using dynamic programming.
  
- **Output**:
  - The maximum value achievable with the items and capacity.

Example:
```
Weights = [10, 20, 30]
Values = [60, 100, 120]
Capacity = 50
Output: Maximum value: 220
```

#### 4) Time and Space Complexity

- **Time Complexity**: \(O(2^n)\) in the worst case due to the exponential growth of branches, but pruning can reduce it significantly.
- **Space Complexity**: \(O(n)\) for the queue holding nodes at any level.
'''