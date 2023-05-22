inputs = [1, 2, 3, 4]

weights = [[0.3, 0.8, 0.7, 0.5],
           [0.2, 0.3, 0.4, 0.1],
           [0.4, 0.9, 0.3, 0]]

baises = [4, 3, 2]

output_neuron = []

for weight, baise in zip(weights, baises):
    output = 0
    for w, i in zip(weight, inputs):
        output += w*i
    output += baise
    output_neuron.append(output)
    
print(output_neuron)