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



# def mat2vec(mat):
#     vec = []
    
#     rows = len(mat)
    
#     for row in range(0, rows):
#         cols = len(mat[row])
#         for col in range(0, cols):
#             vec.append(mat[row][col])
#     return vec

# v1 = mat2vec(mat1)
# v2 = mat2vec(mat2)
# v3 = mat2vec(mat3)
# v4 = mat2vec(mat4)



#design classes 'Node' & 'Link'

class Node:
    def __init__ (self, value, inLinks):
        self.value = None  # ingevoerde waarde is namelijk 0 of 1 - value komt uit de vector
        self.inLinks = []
        
      
  # design nodes as objects      

# self.x1 = Node( , 0) 
# self.x2 = Node( , 0)
# self.x3 = Node( , 0)
 # self.x4 = Node( , 0)
# self.x5 = Node( , 0)  # x5 is zeer waarschijnlijk de meest invloedrijke of bepalende inputnode
# self.x6 = Node( , 0)
# self.x7 = Node( , 0)
# self.x8 = Node( , 0)
# self.x9 = Node( , 0)  
# self.y1 = Node( , 9)
# self.y2 = Node( , 9)


class Link:
    def __init__(self, weightO, weightX, inputNode, outputNode):
        self.weightO = weightO
        self.weightX = weightX
        self.inputNode = inputNode
        self.outputNode = outputNode
        
        
 # design links as objects

# self.l1 = Link(weightO[0], weightX[], x1, y1)
# self.l2 = Link(weightO[1], weightX[], x2, y1)
# self.l3 = Link(weightO[2], weightX[], x3, y1)
# self.l4 = Link(weightO[3], weightX[], x4, y1)
# self.l5 = Link(weightO[4], weightX[], x5, y1)
# self.l6 = Link(weightO[5], weightX[], x6, y1)
# self.l7 = Link(weightO[6], weightX[], x7, y1)
# self.l8 = Link(weightO[7], weightX[], x8, y1)
# self.l9 = Link(weightO[8], weightX[], x9, y1)
# self.l10 = Link(weightO[], weightX[0], x1, y2)
# self.l11 = Link(weightO[], weightX[1], x2, y2)
# self.l12 = Link(weightO[], weightX[2], x3, y2)
# self.l13 = Link(weightO[], weightX[3], x4, y2)
# self.l14 = Link(weightO[], weightX[4], x5, y2)
# self.l15 = Link(weightO[], weightX[5], x6, y2)
# self.l16 = Link(weightO[], weightX[6], x7, y2)
# self.l17 = Link(weightO[], weightX[7], x8, y2)
# self.l18 = Link(weightO[], weightX[8], x9, y2)


weightO = [1, 1, 1, 1, 1, 1, 1, 1, 1]
weightX = [1, 1, 1, 1, 1, 1, 1, 1, 1]

v1 = [1,1,1,1,0,1,1,1,1]
v2 = [0,1,0,1,0,1,0,1,0]
v3 = [0,1,0,1,1,1,0,1,0]
v4 = [1,0,1,0,1,0,1,0,1]

#design function to multiply trainingset with weights

# def input2output:

#  v (9x1 vector) * weights(1x9 vector)



def multiplier(v1, weightO, weightX):
    c = []
    f = []
    c = sum([a * b for a, b in zip(v1, weightO)])
    f = sum([d * e for d, e in zip(v1, weightX)])
    return c, f 
    


print(multiplier(v1, weightO, weightX))

output = multiplier(v1, weightO, weightO)
outputO = print(output[0])
outputX = print(output[1])

#design Softmax function (to calculate the possibility on X or O)  and Loss/Cost function,  which are both not dependent on classes


#Softmax = e ^ (x - max(x)) / sum(e ^ (x - max(x))

# def softmax:
#     math.exp() / math.exp()

#Loss function = Cost function = mean squared error = MSE = (1/n) * Σ (actual – prediction)2

# def MSE:
#     (1/4) * (yactual - yprediction)2
    












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
