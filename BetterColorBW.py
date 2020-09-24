import pygame
import math
import random
import numpy as np 

pygame.init()

screenwid = 1000
screenhei = 500
win = pygame.display.set_mode((screenwid,screenhei))
pygame.display.set_caption('Which Color is Better')

run = True
font = pygame.font.SysFont('timesnewroman', 30, True)
ltext = font.render('White',1,(255,255,255))
rtext = font.render('Black',1,(0,0,0))

traindata = []


def gettraindata(traindata, guesstexton):


    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    ffguess = np.array([[(r/255) + 0.01],[(g/255) + 0.01],[(b/255) + 0.01]])
    guess = NeuralNetwork.feedforward(ffguess)
    guesstext = font.render('My Guess is:' + str(guess), 1, (255,255,255))
    win.fill((r,g,b))
    pygame.draw.line(win,(255,255,255), [screenwid/2,0],[screenwid/2, screenhei])
    win.blit(ltext,(screenwid/4, screenhei*0.5))
    win.blit(rtext,((screenwid/4) * 3, screenhei*0.5))
    if guesstexton:
        win.blit(guesstext,((screenwid/2), 0.8*screenhei))
    traindata.append([[(r/255) + 0.01],[(g/255) + 0.01],[(b/255) + 0.01]])
    return traindata



#Activation Function (0,1)
sigmoid = lambda i: (1/(1+np.exp(-i)))
vectorized_sigmoid = np.vectorize(sigmoid)


#Set-up Learning Rate
LR = 0.9


class NN(object):
    def __init__(self, NumIL, NumHL, NumOL):
        self.NumIL = NumIL
        self.NumHL = NumHL
        self.NumOL = NumOL
        #Creates the Weights Matrices
        self.weightsHL = (np.random.rand(NumHL,NumIL)*2)-1
        self.weightsOL = (np.random.rand(NumOL,NumHL)*2)-1
        #Create Bias Matrices
        self.biasHL =((np.random.rand(NumHL,1))*2)-1
        self.biasOL =((np.random.rand(NumOL,1))*2)-1

    def feedforward(self,ffinput):
        hiddenlayer = (self.weightsHL.dot(ffinput)) + self.biasHL
        hiddenlayer = vectorized_sigmoid(hiddenlayer)

        outputlayer = (self.weightsOL.dot(hiddenlayer)) + self.biasOL
        outputlayer = vectorized_sigmoid(outputlayer)
        return outputlayer

        



    def train(self,trinput,answers):
        #Rerun FF code in the train
        hiddenlayer = (self.weightsHL.dot(trinput)) + self.biasHL
        hiddenlayer = vectorized_sigmoid(hiddenlayer)

        outputlayer = (self.weightsOL.dot(hiddenlayer)) + self.biasOL
        outputlayer = vectorized_sigmoid(outputlayer)

        outputs = outputlayer

        #Find the Errors 
        outputserrors = answers - outputs
        weightsOL_t = np.transpose(self.weightsOL)
        hiddenerrors = weightsOL_t.dot(outputserrors)


        hidden_T = np.transpose(hiddenlayer)
        gradients = (LR * outputserrors * outputs * (1 - outputs))
        weight_ho_deltas = gradients.dot(hidden_T)

        self.weightsOL = self.weightsOL + weight_ho_deltas
        self.biasOL = self.biasOL + np.sum(gradients)

        input_T = np.transpose(trinput)
        hidden_gradients = (LR * hiddenerrors * hiddenlayer * (1 - hiddenlayer))
        weight_ih_deltas = hidden_gradients.dot(input_T)

        self.weightsHL = self.weightsHL + weight_ih_deltas
        self.biasHL = self.biasHL + np.sum(hidden_gradients)









initialize = True
trainanswers = []
NeuralNetwork = NN(3,5,1)
guesstexton = True

while run:
    if initialize:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                gettraindata(traindata, guesstexton)
                initialize = False
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            if mousepos[0] <= screenwid/2:
                useranswer = 0
            else:
                useranswer = 1
                
        
            trainanswers.append(useranswer)
            NeuralNetwork.train(traindata[-1],trainanswers[-1])
            traindata = gettraindata(traindata, guesstexton)
        

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            guesstexton = not(guesstexton)

            



    pygame.display.update()
