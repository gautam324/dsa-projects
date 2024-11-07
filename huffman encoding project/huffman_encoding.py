import heapq
from collections import Counter, defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanEncoding:
    def __init__(self):
        self.encodings = {}
        self.decoding_tree = None

    def _build_tree(self, frequency):
        heap = [Node(char, freq) for char, freq in frequency.items()]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            node1 = heapq.heappop(heap)
            node2 = heapq.heappop(heap)
            merged = Node(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            heapq.heappush(heap, merged)

        return heap[0]  # Root of Huffman tree

    def _generate_encodings(self, node, path=""):
        if node is None:
            return
        if node.char is not None:
            self.encodings[node.char] = path
            return
        self._generate_encodings(node.left, path + "0")
        self._generate_encodings(node.right, path + "1")

    def encode(self, text):
        frequency = Counter(text)
        root = self._build_tree(frequency)
        self._generate_encodings(root)
        self.decoding_tree = root

        encoded_text = ''.join(self.encodings[char] for char in text)
        return encoded_text

    def decode(self, encoded_text):
        decoded_text = []
        current = self.decoding_tree
        for bit in encoded_text:
            current = current.left if bit == '0' else current.right
            if current.char is not None:
                decoded_text.append(current.char)
                current = self.decoding_tree

        return ''.join(decoded_text)
