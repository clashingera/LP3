def recur(n):
    # Base case: if n is 0 or 1, return n
    if n <= 1:
        return n
    # Recursive case: sum of previous two Fibonacci numbers
    return recur(n - 1) + recur(n - 2)

def iterative(n):
    # Initialize first two Fibonacci numbers
    a, b = 0, 1
    print(a, end=" ")  # Print first Fibonacci number
    if n > 1:
        print(b, end=" ")  # Print second Fibonacci number
    
    # Iteratively print each Fibonacci number up to nth number
    for _ in range(2, n):
        a, b = b, a + b
        print(b, end=" ")
    print()  # For a newline after the sequence

if __name__ == "__main__":
    # Get user input
    num = int(input("Enter the nth number for series: "))
    
    # Check if the input is valid
    if num <= 0:
        print("Please enter a positive integer")
    else:
        print("Fibonacci sequence with recursion:")
        # Print Fibonacci sequence using recursion
        for i in range(num):
            print(recur(i), end=" ")
        print()  # For a newline after the sequence
        
        print("Fibonacci series with Iteration:")
        # Print Fibonacci sequence using iteration
        iterative(num)
'''
This code demonstrates two methods to generate and display the Fibonacci sequence up to the nth number using recursion and iteration.

### Key Points:
1. **Recursion** is a programming technique where a function calls itself to solve a problem. Here, the function `recur()` calls itself to calculate the nth Fibonacci number by breaking it down into smaller sub-problems.
2. **Iteration** involves using loops to repeat a sequence of instructions until a condition is met. The function `iterative()` uses a `for` loop to compute the Fibonacci sequence iteratively.

### Code Explanation:

- **Fibonacci Sequence**: Each number in the sequence is the sum of the two preceding numbers, starting with 0 and 1. The sequence starts as: 0, 1, 1, 2, 3, 5, 8, and so on.

- **Recursive Function `recur(n)`**:
    - **Base Case**: If `n` is 0 or 1, return `n` (because the first two Fibonacci numbers are 0 and 1).
    - **Recursive Case**: For values greater than 1, the function returns the sum of the previous two Fibonacci numbers: `recur(n - 1) + recur(n - 2)`.
    - The recursive function is called within a loop in `main`, printing each Fibonacci number up to `num`.

- **Iterative Function `iterative(n)`**:
    - **Initialization**: Starts with the first two Fibonacci numbers, `a = 0` and `b = 1`.
    - **Loop**: For each number from 2 up to `n`, it:
        1. Prints the next number in the sequence.
        2. Updates `a` and `b` so that `b` becomes the sum of `a` and `b` (new Fibonacci number).
    - This method is more efficient than recursion for large `n` because it avoids redundant calculations.

- **User Input**: The program prompts the user to enter the nth number, validating if `num` is positive. Then it prints both the recursive and iterative Fibonacci sequences up to the nth number.

### Recursion vs. Iteration:
- **Recursion** is simple to write but can be slower and use more memory due to repeated calls.
- **Iteration** is generally faster and uses less memory because it doesn't involve function call overhead.



### Time and Space Complexity Analysis

The code implements the Fibonacci sequence in two ways: using recursion and using iteration. Let's analyze the time and space complexity of each.

---

#### 1. **Recursive Fibonacci Function (`recur`)**

The recursive function calculates the \( n \)-th Fibonacci number by repeatedly calling itself to find the sum of the two previous Fibonacci numbers.

- **Time Complexity**:
  - The time complexity of the recursive Fibonacci function is **O(2^n)**.
  - This is because each call to `recur(n)` results in two additional recursive calls: `recur(n-1)` and `recur(n-2)`.
  - This exponential growth leads to a large number of redundant calculations, making it inefficient for large values of \( n \).

- **Space Complexity**:
  - The space complexity of the recursive function is **O(n)**.
  - This is due to the **call stack** used by recursive calls, which can grow up to \( n \) calls deep.
  - In the worst case, the maximum depth of the recursion stack is \( n \).

---

#### 2. **Iterative Fibonacci Function (`iterative`)**

The iterative approach calculates the Fibonacci sequence up to the \( n \)-th number without recursion, instead using a loop.

- **Time Complexity**:
  - The time complexity of the iterative function is **O(n)**.
  - This is because there is a single `for` loop that iterates up to \( n \) times to compute each Fibonacci number.

- **Space Complexity**:
  - The space complexity of the iterative function is **O(1)**.
  - Only a fixed amount of space is used for the two variables (`a` and `b`) to store consecutive Fibonacci numbers.
  - This makes it a much more space-efficient approach compared to the recursive method.

'''
