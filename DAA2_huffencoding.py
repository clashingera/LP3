class Node:
    # Node class to store characters and frequencies, as well as left and right child nodes
    def __init__(self, left=None, right=None, value=None, frequency=None):
        self.left = left
        self.right = right
        self.value = value
        self.frequency = frequency
    
    # Helper function to get the children of a node
    def children(self):
        return (self.left, self.right)

class Huffman_Encoding:
    def __init__(self, string):
        self.q = []  # List to store nodes sorted by frequency
        self.string = string
        self.encoding = {}  # Dictionary to store character encodings

    def char_frequency(self):
        # Step 1: Count the frequency of each character in the input string
        count = {}
        for char in self.string:
            if char not in count:
                count[char] = 0
            count[char] += 1

        # Create nodes for each character and store them in a list
        for char, value in count.items():
            node = Node(value=char, frequency=value)
            self.q.append(node)

        # Sort nodes by frequency to maintain priority order
        self.q.sort(key=lambda x: x.frequency)    

    def build_tree(self):
        # Step 2: Build the Huffman tree by combining the lowest frequency nodes
        while len(self.q) > 1:
            # Take the two nodes with the smallest frequency
            n1 = self.q.pop(0)
            n2 = self.q.pop(0)
            # Create a new node with these two nodes as children, frequency is the sum of the two
            node = Node(left=n1, right=n2, frequency=n1.frequency + n2.frequency)
            # Add this new node back into the sorted list
            self.q.append(node)
            self.q.sort(key=lambda x: x.frequency)

    def helper(self, node: Node, binary_str=""):
        # Step 3: Traverse the tree to create binary codes for each character
        if type(node.value) is str:
            # If it's a leaf node (contains a character), store its encoding
            self.encoding[node.value] = binary_str
            return
        # Traverse left with '0' and right with '1'
        left, right = node.children()
        self.helper(node.left, binary_str + "0")
        self.helper(node.right, binary_str + "1")

    def huffman_encoding(self):
        # Start encoding from the root node
        root = self.q[0]
        self.helper(root, "")

    def print_encoding(self):
        # Display the Huffman encoding for each character
        print(' Char | Huffman Code ')
        for char, binary in self.encoding.items():
            print(" %-4r |%12s" % (char, binary))
    
    def encode(self):
        # Full encoding process
        self.char_frequency()  # Step 1: Calculate frequencies and initialize nodes
        self.build_tree()      # Step 2: Build the Huffman Tree
        self.huffman_encoding()  # Step 3: Generate the binary codes
        self.print_encoding()   # Step 4: Print out the result

# Main program to take user input and run Huffman Encoding
string = input("Enter string to be encoded: ")
encode = Huffman_Encoding(string)
encode.encode()
'''
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