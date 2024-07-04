import numpy as np
from math import cos, pi

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from random import randint as rnd


class Model(nn.Module):
    def __init__(self, in_features=4, h1=32, h2=32, h3=32, out_features=1):
        super().__init__()
        self.fc1 = nn.Linear(in_features, h1)
        self.fc2 = nn.Linear(h1, h2)
        self.fc3 = nn.Linear(h2, h3)
        self.out = nn.Linear(h3, out_features)
    
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.out(x)

        return x


torch.manual_seed(69)

model = nn.Sequential(nn.Linear(16, 32),
                      nn.ReLU(),
                      nn.Linear(32,32),
                      nn.ReLU(),
                      nn.Linear(32,32),
                      nn.ReLU(),
                      nn.Linear(32,1),
                      nn.ReLU())

print(model)


loss_fn = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr = 0.0001)




file = open("prefect_solutions_12.txt", "r")
file = file.read().split("\n")

data = []

def conservative_func(n):
    return 1 / (1+n)

def modified_func(n):
    return 1 / (1 + n**0.37)

def light_slope_func(n):
    return cos(pi/2 - pi/(2*(1 + 0.56 * n ** 0.37)))

for i in file:
    tmp = i.split(":")
    #print(tmp[1])
    data.append([np.array(list(map(int,tmp[0].split())))/15, light_slope_func(int(tmp[1]))])



test_batch_size = 1000

test_data = []

for i in range(test_batch_size):
    k = rnd(0,len(data)-1)
    test_data.append(data[k])
    del data[k]

X = []
Y = []
X_test = []
Y_test = []

for i in data:
    X.append(i[0])
    Y.append(i[1])

for i in test_data:
    X_test.append(i[0])
    Y_test.append(i[1])


#print(f"X: {X.dtype}")
#print(f"Y: {Y}")
#print(f"X_test: {X_test}")
#print(f"Y_test: {Y_test}")

X = torch.tensor(X)
Y = torch.tensor(Y)
X_test = torch.tensor(X_test)
Y_test = torch.tensor(Y_test)

print(f"X: {X.dtype}")

X = X.to(torch.float32)
Y = Y.to(torch.float32)
X_test = X_test.to(torch.float32)
Y_test = Y_test.to(torch.float32)

n_epochs = 100

for epoch in range(n_epochs):
    for i in range(len(X)):
        y_pred = model(X[i])
        loss = loss_fn(y_pred, Y[i])
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print(f"Finished epoch {epoch}, latest loss {loss}")

with torch.no_grad():
    y_pred = model(X_test)
accuracy = np.sqrt((y_pred - Y_test)**2).mean()
print(f"Accuracy {accuracy}")
