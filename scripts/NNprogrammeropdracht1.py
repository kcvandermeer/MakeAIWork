import math
import random as rd 

# Requirements

# Create neural net to distinguish O-s from X-es


# Define symbols
symbolVecs = {'O': (1, 0), 'X': (0, 1)}
symbolChars = dict ((value, key) for key, value in symbolVecs.items ())

# Define datasets for training & testing

trainingSet = (
    ((
        (1, 1, 1),
        (1, 0, 1),
        (1, 1, 1)
    ), 'O'),
    ((
        (0, 1, 0),
        (1, 0, 1),
        (0, 1, 0)
    ), 'O'),
    ((
        (0, 1, 0),
        (1, 1, 1),
        (0, 1, 0)
    ), 'X'),
    ((
        (1, 0, 1),
        (0, 1, 0),
        (1, 0, 1)
    ), 'X')
)

testSet = (
    ((
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0)
    ), 'O'),
    ((
        (1, 0, 1),
        (1, 0, 1),
        (1, 1, 0)
    ), 'O'),
    ((
        (1, 0, 1),
        (0, 0, 0),
        (1, 0, 1)
    ), 'O'),
    ((
        (0, 1, 0),
        (1, 0, 1),
        (0, 1, 0)
    ), 'O'),
    ((
        (1, 0, 0),
        (1, 1, 1),
        (0, 0, 1)
    ), 'X'),
    ((
        (0, 0, 1),
        (1, 1, 1),
        (1, 0, 0)
    ), 'X'),
    ((
        (0, 0, 0),
        (1, 1, 1),
        (0, 0, 0)
    ), 'X'),
    ((
        (1, 0, 0),
        (1, 1, 0),
        (1, 0, 0)
    ), 'X')
)      


#design classes 'Node' & 'Link'

class Node:
    def __init__ (self, value, inLinks):
        self.value = None
        self.inLinks = []
        
        self.x1 = Node( , 0) 
        self.x2 = Node( , 0)
        self.x3 = Node( , 0)
        self.x4 = Node( , 0)
        self.x5 = Node( , 0)
        self.x6 = Node( , 0)
        self.x7 = Node( , 0)
        self.x8 = Node( , 0)
        self.x9 = Node( , 0)  
        self.y1 = Node( , 9)
        self.y2 = Node( , 9)

class Link:
    def __init__(self, weight, inputNode, outputNode):
        self.weight = 1
        self.inputNode = inputNode
        self.outputNode = outputNode
        
        
        
        self.l1 = Link()
        self.l2 = Link()
        
    

#design Softmax function and Loss/Cost function  #Loss function = mean squared error = MSE = (1/n) * Σ (actual – prediction)2

def softmax:
    math.exp()

def MSE:
    (1/4) * ()2