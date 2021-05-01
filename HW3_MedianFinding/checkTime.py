'''
Put your .py file in the same folder with Grading.py and test_files folder,
which means your .py file and Grading.py and test_files folder are at the same level.
Change the file name in the main() with your file name.
'''

import sys
import os
import time
import numpy as np
import matplotlib.pyplot as plt

check = False

def read_data(input_file):
    
    file = []
    try:
        lines = input_file.readlines()
        for line in lines:
            temp = list(map(int, line.split(' ')))
            file.append(temp)
    except:
        return file

    return file

def checkTime(executeFile, flag):
    x = [1000000, 1500000, 2000000, 2500000]
    y = []

    try:
        for i in range(len(x)):
            #x.append(i)
            start = time.time()
            execute = f'python3 {executeFile} ./test_files/sm_input_{str(i+1)}.txt > output_{str(i+1)}.txt'
            os.system(execute)
            end = time.time()
            y.append(end - start)
    except:
        print("Fail to generate")

    X = np.array(x) - 1
    Y = np.array(y)

    coefficients = np.polyfit(X, Y, 1)
    reg =  np.polyval(coefficients, X)
    loss1 = 0
    for i in range(len(Y)):
        loss1 += pow(reg[i]-Y[i], 2)
    '''
    plot1 = plt.plot(X, Y, 'o',label='data')
    plot2 = plt.plot(X, reg, 'r',label='fit')
    plt.title('Implementation with first order')
    plt.show()
    '''
    coefficients = np.polyfit(X * np.log(X), Y, 1)
    reg = np.polyval(coefficients, X*np.log(X))
    loss2 = 0
    for i in range(len(Y)):
        loss2 += pow(reg[i]-Y[i], 2)
    '''
    plot1 = plt.plot(X, Y, 'o',label='data')
    plot2 = plt.plot(X, reg, 'r',label='fit')
    plt.title('Implementation with nlogn curve')
    plt.show()
    '''

    print(loss1, loss2)
    if loss1 < loss2:
        print('Your implementation is O(n)')
    else:
        print('Your implementation is O(nlogn)')


def main():
    # put your file name here
    executeFile = "median_h192h407.py"
    isLinear = checkTime(executeFile, check)


if __name__=="__main__":
    main()
