#инициализация  класса нейронной сети
import numpy
import scipy


class NeuralNetwork:
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        #задать количество узлов во входном, скрытых, и выходном слоях
        # и задать скорость обучения
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        self.lr = learningrate

        self.activation_function = lambda x:scipy.special.expit(x)

        self.wih = (numpy.random.rand(self.hnodes, self.inodes) - 0.5)
         # создадим матрицу весов W - скрытый - входной
        self.who = (numpy.random.rand(self.onodes, self.hnodes) - 0.5)
        # W выходной слой - скрытые слои
        pass

        #функция активации
    def train():
        # W  - обычно так обозначаются веса
       
        
        # numpy.random.rand(строки, колонки)
        #  numpy.random.rand(3,3) - 0.5
        pass
    def query():
        # превращаем список входных значений в двумерный массив

        inputs = numpy.array(inputs_list, ndmin = 2).T
        # расчитать входящие сигналы для скрытого слоя
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_outputs)
        pass

inputnodes = 3
hiddennodes = 3
outputnodes = 3
learningrate = 0.3

n_mnist = NeuralNetwork(inputnodes, hiddennodes, outputnodes, learningrate)
print(n_mnist)
