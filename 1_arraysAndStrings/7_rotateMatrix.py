"""
1.7 Rotate Matrix: Gien an image represented by N x N matrix, where each pixel in the image 
is represented by an integer, wrie a method to rotate the image by 90 degreees.
Can you do this in place?
"""


# To be implemented
def rotateMatrix(arr):
	for i in range(len(arr)):
		for j in range(len(arr[i])):



			0 1 1            0 0 0         0,1 -> 1,2      0,2 -> 2,2      2,1 -> 1,0
			0 0 0            1 0 1
			0 1 0            0 0 1