import numpy as np

#sizes = [1000000, 1500000, 2000000, 2500000, 3000000, 10000000]
sizes = [1000000, 1500000, 2000000, 2500000]

for i in range(len(sizes)):
    
    size = sizes[i]
    array = np.random.choice(size*5, size-1, replace=False) + 1

    with open("sm_input_" + str(i+1) + ".txt", 'w') as fout:
        for k in range(array.size):
            fout.write(str(array[k]) + ' ')

        fout.write('\n')