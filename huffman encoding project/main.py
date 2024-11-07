from file_handler import FileHandler

if __name__ == "__main__":
    file_path = "data/sample.txt"
    compressed_path = "data/compressed.bin"
    decompressed_path = "data/decompressed.txt"

    file_handler = FileHandler(file_path)
    file_handler.compress(compressed_path)
    file_handler.decompress(compressed_path, decompressed_path)
