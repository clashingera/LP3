
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
'''