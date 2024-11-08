
### Fractional Knapsack Problem (Greedy Method)



#### 1) Simplified Code with Explanation


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight  # Value-to-weight ratio

def fractional_knapsack(items, capacity):
    # Sort items by their value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    total_value = 0.0  # Maximum value we can achieve with the given capacity
    for item in items:
        if capacity == 0:  # If the knapsack is full, stop
            break
        if item.weight <= capacity:
            # Take the whole item
            total_value += item.value
            capacity -= item.weight
        else:
            # Take a fraction of the item
            fraction = capacity / item.weight
            total_value += item.value * fraction
            capacity = 0  # Knapsack is now full
    
    return total_value

# Example usage
items = [Item(10, 60), Item(20, 100), Item(30, 120)]
capacity = 50
max_value = fractional_knapsack(items, capacity)
print(f"Maximum value in the knapsack: {max_value}")


'''
#### 2) Code Explanation

- **Class `Item`**: Represents an item with a weight, value, and value-to-weight ratio.
- **`fractional_knapsack`**:
  - Sorts the items by their value-to-weight ratio in descending order to follow the greedy approach.
  - Iterates over the sorted items. If an item fits within the remaining capacity, it’s added entirely. If it doesn’t fit, a fraction of it is added to maximize the value.
  - Stops once the knapsack reaches its capacity.

#### 3) Explanation of Input and Output

- **Input**:
  - A list of items with specific weights and values.
  - The knapsack’s capacity.

- **Output**:
  - The maximum value achievable by the knapsack with fractional items allowed.

Example:
```
Items = [(10, 60), (20, 100), (30, 120)]
Capacity = 50
Output: Maximum value in the knapsack: 240.0
```

#### 4) Time and Space Complexity

- **Time Complexity**: \(O(n \log n)\) due to sorting the items by their ratio.
- **Space Complexity**: \(O(1)\), aside from the input list.

'''
