import random
from numpy import interp
def f(x):
    return 0.7*x + 0.1
class Point:
    def __init__(self, width, height, x_,y_,isRandom = True):
        if(isRandom):
            self.width = width
            self.height = height
            self.x =random.uniform(-1,1)
            self.y =random.uniform(-1,1)
            self.label = 0
            if self.y <= f(self.x):
                self.label =1 
            else:
                self.label = -1
            
        else:
            self.width = width
            self.height = height
            self.x =x_
            self.y =y_
            
    def getX(self):
        return interp(self.x, [-1,1],[0, self.width])
    def getY(self):
        return interp(self.y, [-1,1],[self.height, 0])
   
class Perceptron:

    def __init__(self, n, c):
        self.weights = [None] * n
        self.bias = random.uniform(-1,1)
        #Start with random weights
        for i in range(len(self.weights)):
            self.weights[i] = random.uniform(1,-1)
        self.c = c
    #Guess -1 or 1 based on input values
    def feedforward(self, inputs):
        #Sum all values
        sum = 0
        for i in range(len(self.weights)):
            sum += inputs[i]*self.weights[i]
        sum+=self.bias
        #Result is sign of the sum, -1 or 1
        return self.activate(sum)
    
    def activate(self, sum): 
        if (sum > 0): 
            return 1
        elif (sum <0): 
            return -1
    #Function to train the Perceptron
    #Weights are adjusted based on "desired" answer
    def train(self,inputs,desired):
    #Guess the result
        guess = self.feedforward(inputs)
    #Compute the factor for changing the weight based on the error
    #Error = desired output - guessed output
    #Note this can only be 0, -2, or 2
    #Multiply by learning constant
        error = desired - guess
    #Adjust weights based on weightChange * input
        for i in range(len(self.weights)):
            self.weights[i] += self.c * error * inputs[i]
        self.bias += self.c * error     
    def guessY(self,x):
        w0 = self.weights[0]
        w1 = self.weights[1]
        return - (self.bias/w1) - (w0/w1) * x




#The function x*w0+y*w1+bias has an output which is either >=0 or <0. That means we can divide all the points (x, y) into two sets: set1 contains all the points leading to an output >= 0, set2 contains all the points leading to an output <0. Therefore set1 contains all points the perceptron thinks are above the graph and set2 contains all the points the perceptron thinks are below the graph. 
#So when we say "x*w0+y*w1+bias = 0" we get a line equation, on this line there are now all the points leading to output =0. That means that this equation actually describes the dividing line between set1 and set2, therefore divides the points above the graph from the points below the graph (in the perceptron's "opinion").