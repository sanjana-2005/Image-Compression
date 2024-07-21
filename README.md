# Image Compression
This project focuses on image compression using Huffman coding, a widely employed technique in data compression. The goal is to reduce the storage size of digital images while maintaining visual fidelity. The theoretical foundation involves calculating the frequency of pixel values in the image, building a Huffman tree based on this frequency information, and generating variable-length codes for efficient representation. The implemented algorithm iterates through each pixel in the image, counts the frequency of unique pixel values, and utilizes Huffman coding to create a compact representation of the image. The project also includes features such as displaying image dimensions, calculating compression ratios, and presenting sample data before and after compression. The theoretical framework is implemented in Python, utilizing libraries such as PIL for image processing. The project aims to provide a practical understanding of Huffman coding in image compression and its application to real-world scenarios.

# Work Flow
Reading Original Image: The original image is read using Image.open from the PIL library.
The dimensions of the original image are printed.

Huffman Coding and Compression: Huffman coding is applied to the original image data. The encoded data, compression ratio, and sample data before Huffman coding are printed. The codebook is written to the output file with a ".codebook" extension.

Resizing the Image: The original image is resized to half of its dimensions using the resize method from PIL. The resized dimensions are printed.

Compressed Image Summary: The dimensions and size of the compressed image (resized) are printed.

Decompression: The dimensions and size of the compressed image (resized) are printed.

Displaying Images: The show_image function is called to display the original image.

Saving Resized Image as JPEG: The resized image is saved as a JPEG file with the same name as the output file and ".jpg" extension.

![image](https://github.com/user-attachments/assets/54cf435e-e7c6-4102-a65e-2c69db67b083)

# Output
![image](https://github.com/user-attachments/assets/f11f380d-c147-4ac9-b5be-439498da4e04)
![image](https://github.com/user-attachments/assets/86f3a391-5c0f-4129-bca8-dcae9be03a59)

