import unittest
import os
from file_handler import FileHandler

class TestFileCompression(unittest.TestCase):
    def setUp(self):
        self.file_handler = FileHandler("data/sample.txt")
        with open("data/sample.txt", 'w') as file:
            file.write("Huffman compression is amazing!")

    def test_compression_decompression(self):
        compressed_path = "data/compressed.bin"
        decompressed_path = "data/decompressed.txt"
        
        self.file_handler.compress(compressed_path)
        self.file_handler.decompress(compressed_path, decompressed_path)

        with open("data/sample.txt", 'r') as original_file, open(decompressed_path, 'r') as decompressed_file:
            self.assertEqual(original_file.read(), decompressed_file.read())

    def tearDown(self):
        os.remove("data/sample.txt")
        os.remove("data/compressed.bin")
        os.remove("data/decompressed.txt")

if __name__ == '__main__':
    unittest.main()
