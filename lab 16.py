# Feed Forward Neural Network

import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Input values
x1 = 1
x2 = 1

# Weights
w1 = 1
w2 = 1

# Bias
bias = -1.5

# Calculate weighted sum
z = (x1 * w1) + (x2 * w2) + bias

# Activation function
output = sigmoid(z)

print("Input:", x1, x2)
print("Output:", round(output, 2))

if output >= 0.5:
    print("Prediction: 1")
else:
    print("Prediction: 0")
