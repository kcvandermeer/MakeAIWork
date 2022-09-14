import math
import random as rd 

# Requirements

# Create neural net to distinguish O-s from X-es


# Define symbols
symbolVecs = {'O': (1, 0), 'X': (0, 1)}
symbolChars = dict ((value, key) for key, value in symbolVecs.items ())

# Define datasets for training

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


#define testsets for testing

# testSet = (
#     ((
#         (0, 1, 1),
#         (1, 0, 1),
#         (1, 1, 0)
#     ), 'O'),
#     ((
#         (1, 0, 1),
#         (1, 0, 1),
#         (1, 1, 0)
#     ), 'O'),
#     ((
#         (1, 0, 1),
#         (0, 0, 0),
#         (1, 0, 1)
#     ), 'O'),
#     ((
#         (0, 1, 0),
#         (1, 0, 1),
#         (0, 1, 0)
#     ), 'O'),
#     ((
#         (1, 0, 0),
#         (1, 1, 1),
#         (0, 0, 1)
#     ), 'X'),
#     ((
#         (0, 0, 1),
#         (1, 1, 1),
#         (1, 0, 0)
#     ), 'X'),
#     ((
#         (0, 0, 0),
#         (1, 1, 1),
#         (0, 0, 0)
#     ), 'X'),
#     ((
#         (1, 0, 0),
#         (1, 1, 0),
#         (1, 0, 0)
#     ), 'X')
# )      


#design classes 'Node' & 'Link'

class Node:
    def __init__ (self, value, inLinks):
        self.value = None  # ingevoerde waarde is namelijk 0 of 1
        self.inLinks = []
        
        self.x1 = Node( , 0) 
        self.x2 = Node( , 0)
        self.x3 = Node( , 0)
        self.x4 = Node( , 0)
        self.x5 = Node( , 0)  # x5 is zeer waarschijnlijk de meest invloedrijke of bepalende inputnode
        self.x6 = Node( , 0)
        self.x7 = Node( , 0)
        self.x8 = Node( , 0)
        self.x9 = Node( , 0)  
        self.y1 = Node( , 9)
        self.y2 = Node( , 9)

class Link:
    def __init__(self, weight, inputNode, outputNode):
        self.weight = weight
        self.inputNode = inputNode
        self.outputNode = outputNode
        
        
        
        self.l1 = Link(1, x1, y1)
        self.l2 = Link(1, x2, y1)
        self.l3 = Link(1, x3, y1)
        self.l4 = Link(1, x4, y1)
        self.l5 = Link(1, x5, y1)
        self.l6 = Link(1, x6, y1)
        self.l7 = Link(1, x7, y1)
        self.l8 = Link(1, x8, y1)
        self.l9 = Link(1, x9, y1)
        self.l10 = Link(1, x1, y2)
        self.l11 = Link(1, x2, y2)
        self.l12 = Link(1, x3, y2)
        self.l13 = Link(1, x4, y2)
        self.l14 = Link(1, x5, y2)
        self.l15 = Link(1, x6, y2)
        self.l16 = Link(1, x7, y2)
        self.l17 = Link(1, x8, y2)
        self.l18 = Link(1, x9, y2)
    

#design Softmax function (to calculate the possibility on X or O) and Loss/Cost function,  which are both not dependent on classes
#Softmax = e ^ (x - max(x)) / sum(e^(x - max(x))

def softmax:
    math.exp() / math.exp()

#Loss function = mean squared error = MSE = (1/n) * Σ (actual – prediction)2

def MSE:
    (1/4) * (yactual - yprediction)2