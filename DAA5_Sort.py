
import random

class QuickSort:
    def __init__(self, array):
        self.array = array

    # Deterministic partition method
    def partition(self, low, high):
        pivot = self.array[high]  # last element as pivot
        i = low - 1  # pointer for the right position of pivot

        for j in range(low, high):
            if self.array[j] <= pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
        
        # Place pivot in its correct position
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        return i + 1

    # Randomized partition method
    def partition_random(self, low, high):
        pivot_index = random.randint(low, high)
        # Swap the randomly chosen pivot with the high element
        self.array[pivot_index], self.array[high] = self.array[high], self.array[pivot_index]
        return self.partition(low, high)

    # Deterministic QuickSort
    def quicksort_deterministic(self, low, high):
        if low < high:
            pivot_index = self.partition(low, high)
            self.quicksort_deterministic(low, pivot_index - 1)
            self.quicksort_deterministic(pivot_index + 1, high)

    # Randomized QuickSort
    def quicksort_randomized(self, low, high):
        if low < high:
            pivot_index = self.partition_random(low, high)
            self.quicksort_randomized(low, pivot_index - 1)
            self.quicksort_randomized(pivot_index + 1, high)

# Main program
while True:
    print("Press Ctrl+C to exit...")
    array = [int(x) for x in input("Enter array: ").split()]
    
    print("\nDeterministic QuickSort:")
    sorter_d = QuickSort(array.copy())
    sorter_d.quicksort_deterministic(0, len(array) - 1)
    print(sorter_d.array)
    
    print("\nRandomized QuickSort:")
    sorter_r = QuickSort(array.copy())
    sorter_r.quicksort_randomized(0, len(array) - 1)
    print(sorter_r.array)
    
'''```


### 2) Code Explanation

- **Class `QuickSort`**: Manages the sorting logic and array state.

- **`__init__`**: Initializes the array for sorting.

- **`partition` (deterministic)**:
  - Chooses the last element as the pivot.
  - Rearranges the array such that elements less than or equal to the pivot are on the left, and greater elements are on the right.
  - Returns the index where the pivot is finally positioned.

- **`partition_random` (randomized)**:
  - Selects a random pivot index and swaps it with the last element before calling the `partition` function. This introduces randomness into the pivot choice.

- **`quicksort_deterministic`**:
  - Recursively applies the deterministic partitioning on the subarrays until the array is sorted.

- **`quicksort_randomized`**:
  - Uses the randomized partitioning approach for sorting by selecting a random pivot each time.

- **Main Program**:
  - Takes a list of integers from the user, then sorts and prints it using both deterministic and randomized quicksort methods.

---

### 3) Explanation of Input and Output

- **Input**:
  - A sequence of integers entered by the user to be sorted (e.g., `3 1 4 1 5 9`).
  
- **Output**:
  - Two sorted arrays, one sorted with the deterministic QuickSort method and the other with the randomized QuickSort method.

Example:
```
Enter array: 3 1 4 1 5 9
Deterministic QuickSort:
[1, 1, 3, 4, 5, 9]

Randomized QuickSort:
[1, 1, 3, 4, 5, 9]
```

---

### 4) Time and Space Complexity

- **Time Complexity**:
  - **Average case**: \(O(n \log n)\) for both variants.
  - **Worst case (Deterministic)**: \(O(n^2)\) if the pivot choice is poor, leading to highly unbalanced partitions. For example, if the list is already sorted and the last element is always chosen as the pivot.
  - **Worst case (Randomized)**: \(O(n \log n)\) on average due to the randomized pivot reducing the likelihood of poor partitioning.

- **Space Complexity**: 
  - \(O(\log n)\) for both variants due to the recursion stack.
-'''
