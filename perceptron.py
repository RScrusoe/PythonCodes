import numpy as np
from matplotlib import pyplot as plt 
import csv

# np.random.seed(10)
slope = 0.3
intercept = -0.1
epochs = 5

def data_load(file):
    f = open(file)
    r = csv.reader(f)
    d = {}
    for i in r:
        i[0] = int(i[0])
        if i[0] not in d:
            d[i[0]] = []
            d[i[0]].append([float(i[1]),float(i[2])])
        else:
            d[i[0]].append([float(i[1]),float(i[2])])
    f.close()
    return d
# d = data_load('datapoints.csv')

def line_function(x):
    return slope*x + intercept


def random_data_points(n,xl,xh,yl,yh):
    l = []
    for i in range(n):
        x = np.random.uniform(xl,xh)
        y = np.random.uniform(yl,yh)
        lineY = line_function(x)
        if y >= lineY:
            label = +1
        else:
            label = -1
        l.append([label,x,y])
    return l

xy_data = random_data_points(100,-1,1,-1,1)


class Perceptron():
    n = 3
    weights = []
    learning_rate = 0.1
    bias = 1

    def __init__(self,n):
        n = n
        for i in range(self.n):
            self.weights.append(np.random.uniform(-1,1))

    def guess(self,inputs):
        all_sum = 0
        for i in range(self.n):
            all_sum += inputs[i]*self.weights[i] 
        return np.sign(all_sum)

    def train(self,inp,target):
        guess = self.guess(inp)
        error = target - guess
        for i in range(self.n):
            self.weights[i] += (error * inp[i] * self.learning_rate)


    def draw_trained_line(self):
        x1 = -1
        x2 = 1
        y1 = -1*(self.weights[2]/self.weights[1]) -1*(self.weights[0]/self.weights[1])*(x1)
        y2 = -1*(self.weights[2]/self.weights[1]) -1*(self.weights[0]/self.weights[1])*(x2) 
        print(-1*(self.weights[0]/self.weights[1]),-1*(self.weights[2]/self.weights[1]))
        plt.plot([x1,x2],[y1,y2],ls='dashed',c='r')


p = Perceptron(3)

#setting axes
plt.axis([-1,1,-1,1])

# Plotting Acrual line 
plt.plot([-1,1],[line_function(-1),line_function(1)],ls='solid')


# Training for Epochs
# For each epoch: Train, check score
# For last epoch plot accordingly
for epoch in range(epochs):
    result = 0
    for i in xy_data:
        inp = i[1:] + [1]
        out = p.train(inp,i[0])
    for i in xy_data:
        inp = i[1:] + [1]
        guess = p.guess(inp)
        if guess == i[0]:
            result += 1

    if epoch == (epochs - 1):
        result = 0
        for i in xy_data:
            inp = i[1:] + [1]
            guess = p.guess(inp)   
            if i[0] == 1:
                m = '*'
            else:
                m = 'o'
            if guess == i[0]:
                result += 1
                c = 'g'
            else:
                c = 'r'
            plt.scatter(i[1],i[2],marker=m,c = c)
            # plt.pause(0.0001)
    print(result)


p.draw_trained_line()
plt.show()


# print(p.weights)