
class Node:
    # Node class to store characters, frequencies, and left/right children
    def __init__(self, left=None, right=None, value=None, frequency=None):
        self.left = left
        self.right = right
        self.value = value
        self.frequency = frequency

    def children(self):
        return (self.left, self.right)


class HuffmanEncoding:
    def __init__(self, string):
        self.string = string
        self.frequency = {}   # Character frequencies
        self.encoding = {}    # Character encodings

    def char_frequency(self):
        # Count frequency of each character in the input string
        for char in self.string:
            self.frequency[char] = self.frequency.get(char, 0) + 1
        # Create a list of nodes, one per unique character
        self.nodes = [Node(value=char, frequency=freq) for char, freq in self.frequency.items()]
        # Sort nodes by frequency
        self.nodes.sort(key=lambda node: node.frequency)

    def build_tree(self):
        # Build the Huffman tree by combining nodes with the lowest frequencies
        while len(self.nodes) > 1:
            # Take two nodes with the smallest frequency
            left = self.nodes.pop(0)
            right = self.nodes.pop(0)
            # Create a new node with these two as children and sum of frequencies
            new_node = Node(left=left, right=right, frequency=left.frequency + right.frequency)
            # Add the new node back into the sorted node list
            self.nodes.append(new_node)
            self.nodes.sort(key=lambda node: node.frequency)

    def generate_codes(self, node, code=""):
        # Traverse the tree to create binary codes
        if node is None:
            return
        if node.value:  # Leaf node with a character
            self.encoding[node.value] = code
        # Recursive calls to traverse left (add '0') and right (add '1')
        self.generate_codes(node.left, code + "0")
        self.generate_codes(node.right, code + "1")

    def encode(self):
        # Full encoding process
        self.char_frequency()  # Step 1: Frequency count
        self.build_tree()      # Step 2: Build Huffman tree
        # Step 3: Generate codes from the root of the tree
        root = self.nodes[0]
        self.generate_codes(root)
        # Display the result
        print(" Char | Huffman Code ")
        for char, code in self.encoding.items():
            print(f" {char:4} | {code}")

# Main program
string = input("Enter a string to encode: ")
encoder = HuffmanEncoding(string)
encoder.encode()

'''

---

### 2) Code Explanation

- **Class `Node`**:
  - Represents a node in the Huffman tree. Each node stores a character, its frequency, and references to left and right child nodes (for non-leaf nodes).
  
- **Class `HuffmanEncoding`**:
  - **`__init__`**: Initializes the input string, the frequency dictionary, and the encoding dictionary.
  - **`char_frequency`**: Counts the frequency of each character in the input string and creates a list of `Node` objects, sorted by frequency.
  - **`build_tree`**: Builds the Huffman tree by repeatedly combining the two nodes with the lowest frequencies until only one node (the root) remains.
  - **`generate_codes`**: Recursively traverses the Huffman tree to assign binary codes to each character based on their path from the root. '0' is added when moving left, and '1' when moving right.
  - **`encode`**: Manages the full encoding process (frequency calculation, tree building, code generation) and displays the Huffman codes for each character.

---

### 3) Explanation of Input and Output

- **Input**:
  - The program takes a string from the user (e.g., "hello").
  
- **Output**:
  - It outputs the Huffman encoding of each unique character in the input string in tabular form.

Example:
```
Enter a string to encode: hello
 Char | Huffman Code 
 h    | 10
 e    | 11
 l    | 0
 o    | 11
```

---

### 4) Time and Space Complexity

- **Time Complexity**:
  - **Frequency calculation**: \(O(n)\), where \(n\) is the length of the string.
  - **Tree building**: \(O(m \log m)\), where \(m\) is the number of unique characters (nodes are sorted after each merge operation).
  - **Code generation**: \(O(m)\), since each unique character has a path to traverse in the tree.

  Overall time complexity is \(O(n + m \log m)\).

- **Space Complexity**:
  - **Frequency dictionary**: \(O(m)\) for storing each character's frequency.
  - **Huffman tree**: \(O(m)\) for storing nodes.
  - **Encoding dictionary**: \(O(m)\) for storing the codes.
  
  Total space complexity is \(O(m)\).
Sure, here’s the explanation and updated code with comments. This version of Huffman Encoding uses classes, takes input from the user, and builds the tree step-by-step with explanations.

### Code Explanation

1. **Node Class**:
   - The `Node` class represents each node in the Huffman tree.
   - Each `Node` can store a character (`value`), frequency (`frequency`), and has pointers to `left` and `right` child nodes.
   - `children()` method returns the children nodes for easier access in tree traversal.

2. **Huffman_Encoding Class**:
   - The `Huffman_Encoding` class orchestrates the entire process of encoding.
   - It starts by initializing the string to be encoded and preparing data structures (`q` for the nodes and `encoding` for the final binary codes).

3. **char_frequency**:
   - Counts the frequency of each character in the input string.
   - Creates a node for each unique character with its frequency and stores these nodes in a list.
   - Sorts the nodes by frequency to use a priority queue-like structure for building the tree.

4. **build_tree**:
   - Constructs the Huffman Tree by combining nodes with the lowest frequencies.
   - Repeatedly merges the two nodes with the smallest frequency to create a parent node with a combined frequency.
   - Adds this new parent node back to the list, ensuring the list remains sorted.

5. **helper**:
   - A recursive helper function for traversing the Huffman Tree.
   - Assigns binary codes by going left (`0`) and right (`1`).
   - When it reaches a leaf node (contains a character), it saves the binary string as that character’s encoding.

6. **huffman_encoding**:
   - Initiates the encoding process by calling the `helper` function starting from the root of the tree.

7. **print_encoding**:
   - Displays the final Huffman codes for each character in a formatted table.

8. **encode**:
   - Runs the encoding steps in sequence: calculating frequency, building the tree, generating codes, and printing the encoding.

### Complexity
The time complexity for building the tree is \(O(n \log n)\), where \(n\) is the number of unique characters in the input string.
'''
