import pickle
from huffman_encoding import HuffmanEncoding

class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.huffman = HuffmanEncoding()

    def compress(self, output_path):
        with open(self.file_path, 'r') as file:
            text = file.read()

        encoded_text = self.huffman.encode(text)
        
        # Store both encoded text and encodings
        with open(output_path, 'wb') as compressed_file:
            data = {
                "encoded_text": encoded_text,
                "encodings": self.huffman.encodings
            }
            pickle.dump(data, compressed_file)

    def decompress(self, compressed_file_path, output_path):
        with open(compressed_file_path, 'rb') as compressed_file:
            data = pickle.load(compressed_file)
        
        encoded_text = data["encoded_text"]
        self.huffman.encodings = data["encodings"]
        
        decoded_text = self.huffman.decode(encoded_text)

        with open(output_path, 'w') as output_file:
            output_file.write(decoded_text)
