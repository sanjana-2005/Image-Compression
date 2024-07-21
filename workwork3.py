import heapq
import os
from collections import defaultdict
from PIL import Image
import matplotlib.pyplot as plt
MAX_TREE_HT = 256
class MinHeapNode:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None
def read_image_data(input_filename):
    with open(input_filename, 'rb') as f:
        return bytearray(f.read())
def write_image_data(output_filename, data):
    with open(output_filename, 'wb') as f:
        f.write(data)
def build_huffman_tree(data):
    frequency = defaultdict(int)
    for byte in data:
        frequency[byte] += 1
    min_heap = [[weight, [byte, ""]] for byte, weight in frequency.items()]
    heapq.heapify(min_heap)
    
    while len(min_heap) > 1:
        left = heapq.heappop(min_heap)
        right = heapq.heappop(min_heap)
        
        for pair in left[1:]:
            pair[1] = '0' + pair[1]
        for pair in right[1:]:
            pair[1] = '1' + pair[1]
        
        heapq.heappush(min_heap, [left[0] + right[0]] + left[1:] + right[1:])
    
    return min_heap[0][1:]
def encode_data(data, codes):
    encoded_data = ""
    sample_data = ""  # Variable to store the sample data
    for byte in data:
        encoded_data += codes[byte] 
        sample_data += bin(byte)[2:].zfill(8)  # Convert byte to binary and append to sample data
    
    return encoded_data, sample_data

def compress_image(input_filename, output_filename):
    image_data = read_image_data(input_filename)
    codebook = {} 
    compressed_data = bytearray() 

    # Print dimensions of the original image
    original_image = Image.open(input_filename)
    width, height = original_image.size
    print("Original Image Dimensions:", f"{width} x {height}")

    # Resize the image to make the dimensions smaller
    resized_image = original_image.resize((width // 2, height // 2))  # Resize dimensions by half
    resized_width, resized_height = resized_image.size
    print("Resized Image Dimensions:", f"{resized_width} x {resized_height}")

    # Build Huffman tree and get codes
    huffman_tree = build_huffman_tree(image_data)
    for byte, code in huffman_tree:
        codebook[byte] = code

    # Encode the data using Huffman codes
    encoded_data, sample_data = encode_data(image_data, codebook)

    # Print summary of encoded data
    print("\nEncoded Data Summary:")
    print("Total Bytes Before Compression:", len(image_data))
    print("Total Bytes After Compression:", len(encoded_data) // 8)  # Convert bits to bytes
    compression_ratio = (len(encoded_data) / 8) / len(image_data) * 100  # Compression ratio in percentage
    print("Compression Ratio:", f"{compression_ratio:.2f}%")
    print("Sample Data Before Huffman Coding:", sample_data[:50])  # Print only the first 50 characters

    # Write the codebook to the output file
    with open(output_filename + ".codebook", 'w') as f:
        for byte, code in huffman_tree:
            f.write(f"{byte}: {code}\n")

    # Convert encoded data to bytes
    for i in range(0, len(encoded_data), 8):
        byte = encoded_data[i:i+8]
        compressed_data.append(int(byte, 2))

    # Save the resized image as JPEG
    resized_image.save(output_filename + ".jpg")

    # Print dimensions and size of the compressed image
    compressed_size = os.path.getsize(output_filename + ".jpg")
    
    print("\nCompressed Image Summary:")
    print("Dimensions:", f"{resized_width} x {resized_height}")
    print("Size:", compressed_size, "bytes")


def show_image(filename, grayscale=False):
    img = Image.open(filename)
    if grayscale:
        img = img.convert('L')  # Convert to grayscale
    plt.imshow(img, cmap='gray' if grayscale else None)
    plt.axis('off')  # Hide axes
    plt.show()

if __name__ == "__main__":
    input_filename = r"C:\Users\shalu\Downloads\land.jpg"
    output_filename = r"C:\Users\shalu\Downloads\gray.jpeg"

    # Compress the image
    compress_image(input_filename, "compressed.bin")

    # Decompress the compressed data
    #decompress_image("compressed.bin", output_filename)

    # Show the original and decompressed images in grayscale
    show_image(input_filename, grayscale=True)
    #show_image(output_filename, grayscale=True)
