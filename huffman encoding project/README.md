

# Huffman Encoding Project

## Overview
This project implements a complete end-to-end Huffman Encoding algorithm for file compression and decompression. Huffman encoding is a lossless compression technique that assigns variable-length codes to characters based on their frequency in the input data. The more frequently a character appears, the shorter its binary representation, resulting in efficient data compression.

## Project Structure
```
HuffmanCompression/
├── main.py                   # Main script to run the project
├── huffman_encoding.py       # Core Huffman encoding and decoding logic
├── file_handler.py           # Utility functions for file reading and writing
├── tests/
│   ├── test_huffman.py       # Unit tests for Huffman encoding functions
│   └── test_file_compression.py # Unit tests for file compression and decompression
├── data/
│   ├── sample.txt            # Sample text file for testing compression
│   └── compressed.huff       # Output compressed binary file
└── README.md                 # Project documentation
```

## Features
- **Huffman Tree Construction**: Creates a binary tree where the path to each leaf node represents the binary code for a character.
- **Encoding**: Generates Huffman-encoded binary data from the input text.
- **Decoding**: Reconstructs the original text from the binary data using the Huffman tree.
- **File Compression**: Compresses input files and outputs a binary file.
- **File Decompression**: Decompresses the binary file back to the original text format.

## How to Run the Project
1. **Clone the Repository**: Clone this project to your local machine.
   ```bash
   git clone <repository_url>
   cd HuffmanCompression
   ```

2. **Run the Main Script**:
   ```bash
   python main.py
   ```

3. **Check File Sizes**:
   Use the `os` module to print the sizes of the original and compressed files:
   ```python
   import os
   original_size = os.path.getsize('data/sample.txt')
   compressed_size = os.path.getsize('data/compressed.huff')
   print(f"Original Size: {original_size} bytes")
   print(f"Compressed Size: {compressed_size} bytes")
   ```

## Example
- **Input**: A text file containing `hello how are you`.
- **Compressed Output**: A binary file representing the Huffman-encoded data.
- **Compression Analysis**: The script prints the original and compressed file sizes, along with the compression ratio.

## Limitations
- **Small File Performance**: For small text files, the compression might result in a larger output due to metadata overhead.
- **Optimization**: Best suited for larger files with repetitive patterns.

## Future Enhancements
- Implement better metadata handling for smaller files.
- Add more compression strategies for better adaptability.

