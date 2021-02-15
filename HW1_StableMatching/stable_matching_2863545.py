# maybe use for auto run test
file_list = [a for a in range(10, 110, 10)]
# initialize some variable
# men and women will be list of lists, maybe easy to use?
m, w = 0, 0
men = []
women = []


# define file reading function
def read_file():
    global men, women
    with open('./test_files/sm_10.txt') as f:
        # read the first line of file as number of men and women
        m = w = int(f.readline())

        # read the rest lines as proposal preference
        temp = []
        for line in f:
            if line.strip():
                char = line.strip('\n')
                char = char.split(',')
                char = [int(a) for a in char]
                temp.append(char)          
    men = temp[:m]  # men's preference are first 10 lists  
    women = temp[-w:]  # women's preference are last 10 lists


# stable matching agorithem part
def stable_matching():
    matched = []
    # starts the algorithm

    # print out result
    for pair in matched:
        print(f"{pair[0]}, {pair[1]}\n")


def main():
    read_file()
    stable_matching()
    

if __name__ == '__main__':
    main()
