import unittest
from huffman_encoding import HuffmanEncoding

class TestHuffmanEncoding(unittest.TestCase):
    def test_encoding_decoding(self):
        huffman = HuffmanEncoding()
        text = "hello world"
        encoded_text = huffman.encode(text)
        decoded_text = huffman.decode(encoded_text)
        self.assertEqual(text, decoded_text)

if __name__ == '__main__':
    unittest.main()
