#this neuron on the hidden layers is an input neuron
inputs = [1, 2, 3, 2.5]
weights1 = [0.2, 0.8 , -0.5, 1.0]
bias1 = 2

output = [inputs[0]*weights1[0]+inputs[1]*weights1[1]+inputs[2]*weights1[2]+inputs[3]*weights1[3]+bias1]

print(output)

