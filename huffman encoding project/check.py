import os

# Define a function to get file size in bytes
def get_file_size(file_path):
    return os.path.getsize(file_path)
# File paths
original_file = r'C:\Users\gauta\Desktop\huffman encoding project\data\sample.txt'
compressed_file = r'C:\Users\gauta\Desktop\huffman encoding project\data\compressed.bin'

# Get file sizes
original_size = get_file_size(original_file)
compressed_size = get_file_size(compressed_file)

# Calculate size difference
size_difference = original_size - compressed_size
compression_ratio = (compressed_size / original_size) * 100

# Print results
print(f"Original File Size: {original_size} bytes")
print(f"Compressed File Size: {compressed_size} bytes")
print(f"Size Reduction: {size_difference} bytes")
print(f"Compression Ratio: {compression_ratio:.2f}% of original size")
