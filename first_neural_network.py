weight = 0.1

"""
This is the basic Neural network:
takes an input and multiplies it by the weight, 
which in this example is 0.1.
We are then given a prediction 0.85
"""
def neural_network(input, weight):
    prediction = input * weight
    return prediction


"""
This is how to use the neural network.
"""
number_of_toes = [8.5, 9.5, 9, 10] # the dataset
input = number_of_toes[0] # singluar input from the dataset
pred = neural_network(input, weight) # get a prediction from the singlar piece of data
print(pred)
