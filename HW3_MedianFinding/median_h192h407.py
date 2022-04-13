# import necessary modules
import sys

# whatever

def read_file(fileName):
    with open(fileName) as f:
        # read the rest lines as proposal preference
        for line in f:
            char = line.strip('\n ').split(' ')
            char = [int(a) for a in char]
    return char


def median_finding(A):
    if len(A) % 2 == 1:
        print(median_finding_rec(A, len(A) // 2))
    else:
        a1 = median_finding_rec(A, len(A) // 2)
        a2 = 0
        tmp = 0
        for a in A:
            if a > tmp and a < a1:
                a2 = a
                tmp = a1
        print((a1 + a2) * 0.5)
    

# find the ith smallest number
def median_finding_rec(A, i):
    subset = [A[j:j + 5] for j in range(0, len(A), 5)]  # divide the set in to n groups size of 5
    medians = [j[len(j)//2] for j in subset]  # the 3rd number is the median for each gorup of 5
    # median of medians
    x = medians[len(medians)//2]
    k = len([j for j in A if j < x])  # len(left) is the rank of x since A = left-x-right
    if i == k:
        return x
    elif i < k:
        return median_finding_rec([j for j in A if j < x], i)
    elif i > k:
        return median_finding_rec([j for j in A if j > x], i-k-1)


def main():
    A = read_file(sys.argv[1])
    median_finding(A)


if __name__ == '__main__':
    main()
