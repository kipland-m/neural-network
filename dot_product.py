import numpy as np
#vector
inputs = [1, 2, 3, 2.5]

#matrix of vectors
weights = [[0.2, 0.8 , -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

# how do we multiply this vector times this matrix of vectors?
# we do this using the dot products.

biases = [2, 3, 0.5]

   
output = np.dot(weights, inputs) + biases

print(output)

