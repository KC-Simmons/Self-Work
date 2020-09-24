import numpy as np 

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




class CopyNN(object):
    def __init__(self, NumIL, NumHL, NumOL, weightsHL, weightsOL, biasHL, biasOL):
        self.NumIL = NumIL
        self.NumHL = NumHL
        self.NumOL = NumOL
        self.weightsHL = weightsHL
        self.weightsOL = weightsOL
        self.biasHL = biasHL
        self.biasOL = biasOL

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
        self.biasHL = self.biasHL + np.sum(hidden_gradients


        




NeuralNetwork = NN(2,5,1)
ffinputtest = np.array([[1,0,1,0],[0,1,1,0]])
targets = np.array([1,1,0,0])
print(NeuralNetwork.feedforward(ffinputtest))
for i in range(10000):
    NeuralNetwork.train(ffinputtest, targets)

print(NeuralNetwork.feedforward(ffinputtest))
ffinputreal = np.array([[1],[1]])
print(NeuralNetwork.feedforward(ffinputreal))


##ffinput for feedforward alg are read by array

