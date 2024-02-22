import numpy as np
import math
import matplotlib.pyplot as plt


x = np.array([61,62,63,65,65,68,69,70,72,75])
y = np.array([105,120,120,160,120,145,175,160,185,210])

theta0 = np.random.randint(-50,50)
theta1 = np.random.randint(-50,50)
alpha = 0.1
iter = 10000000

n = len(x)
#using unit vector to move more carefully
for i in range(iter):
    dtheta0 = dtheta1 = 0
    for j in range(n):
        dZ = y[j] - theta0 - theta1 * x[j]
        dtheta1 -= dZ * x[j]
        dtheta0 -= dZ
    
    if i % 10000 == 0:
        l = 0
        y_predictions = np.array([])
        for j in range(len(x)):
            new_value = theta1*x[j] + theta0
            y_predictions = np.append(y_predictions, new_value)
            l += (y[j] - new_value)**2
        plt.clf()
        plt.scatter(x, y)
        plt.plot(x, y_predictions, c='red')
        plt.title(f'loss:{(1/(2*n) * l):.5f}')
        plt.pause(0.00001)
        print(f'{theta1:.3f},{theta0:.3f},loss={(1/(2*n) * l):.5f}')

    l = math.sqrt(dtheta0 ** 2 + dtheta1 ** 2)
    theta1 -= alpha * 1/n * (dtheta1 / l)
    theta0 -= alpha * 1/n * (dtheta0 / l)

