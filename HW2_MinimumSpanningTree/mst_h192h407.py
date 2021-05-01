import numpy as np
import sys

# Declearing Martix and its size
M = np.array([], dtype=int)
n = 0

# Declearing sorted vetex edges
V = []


# set class for make, union, find operations
class set:
    prev_node = {}

    # Make set for vertex N
    def make_set(self, N):
        for i in range(N):
            self.prev_node[i] = i

    # Find set
    def find_set(self, vertex):
        if self.prev_node[vertex] == vertex:
            return vertex
        # recursively find the root
        return self.find_set(self.prev_node[vertex])

    # Union two vertex
    def union(self, vertex1, vertex2):
        root1 = self.find_set(vertex1)
        root2 = self.find_set(vertex2)

        self.prev_node[root1] = root2


# define file reading function
def read_file(file_name):
    global M, n
    with open(file_name) as f:
        # read the rest lines as proposal preference
        for line in f:
            char = line.strip('\n ').split(' ')
            char = [int(a) for a in char]
            M = np.append(M, char)
    n = int(np.sqrt(M.shape[0]))  # get the size of matrix
    M = M.reshape(n, n)  # reshape the array to be 2d


# Get and sort all vertex
def vertex(M):
    for i in range(n):
        for j in range(n):
            # if the weight is not 0, then add to list and sort by weight asending
            if M[i, j] != 0:
                V.append((i, j))
    V.sort(key=lambda x: M[x[0], x[1]]) 


# Start implementating Kruskal's Algorithm
def Kruskal(matrix):
    A = list()  # a list contains answers
    s = set()
    s.make_set(n)  # make set
    for (u, v) in V:
        a = s.find_set(u)
        b = s.find_set(v)
        if a != b:
            A.append((u, v))
            s.union(u, v)
    return A


def main():
    read_file(sys.argv[1])
    vertex(M)
    answer = Kruskal(M)
    for a in answer:
        print(f"{a[0]} {a[1]}")


if __name__ == '__main__':
    main()
