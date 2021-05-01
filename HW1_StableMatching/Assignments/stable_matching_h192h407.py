import sys
# initialize some variable
# men and women will be list of lists, maybe easy to use?
n = 0
men = []
women = []


# define file reading function
def read_file(file_name):
    global men, women, n
    with open(file_name) as f:
        # read the first line of file as number of men and women
        n = int(f.readline())

        # read the rest lines as proposal preference
        temp = []
        for line in f:
            if line.strip():
                char = line.strip('\n')
                char = char.split(',')
                char = [int(a) for a in char]
                temp.append(char)        
    men = temp[:n]  # men's preference are first 10 lists  
    women = temp[-n:]  # women's preference are last 10 lists


# a function check if w prefers m1 over m
def check_prefer_m1_over_m(prefer_list, woman, man, man1):
    index_man = 0
    index_man1 = 0
    for i in range(n):
        if prefer_list[woman-1][i] == man1:
            index_man1 = i
        if prefer_list[woman-1][i] == man:
            index_man = i
    if index_man1 < index_man:
        return True
    else:
        return False


# stable matching agorithem part
def stable_matching():
    # a list sorted by men's id storing paired men and women
    matched = []
    # boolean list track man is free or not
    free_men = [True for i in range(n)]
    # matched women, -1 means not matched, value is the man that engaged with
    matched_women = [-1 for i in range(n)]

    # starts the algorithm
    while True:
        # pick the first free man
        m = 1
        while m < n + 1:
            # if the man is free and have not yet proposed to every woman, then break
            if free_men[m-1] is True and not all(a == -1 for a in men[m-1]):
                break
            m += 1
        # let w to be the highest ranked women in m's list to whom not yet proposed 
        for i in men[m-1]:
            # the woman i in m's list has not been proposed
            if i != -1:
                w = i
                break
        # if woman w is not matched(free), then m, w become engaged
        if matched_women[w-1] == -1:
            matched.append(tuple((m, w)))  # w and m engaged
            free_men[m-1] = False  # the man m become not free
            matched_women[w-1] = m  # the woman w engaged with m
        # if woman w is already engaged with m1
        else:
            m1 = matched_women[w-1]  # the man woman currently matched
            # if m1 is prefered than m for woman w
            if check_prefer_m1_over_m(women, w, m, m1):
                # man m remain free
                pass
            else:
                # delete the old couple (m1, w)
                matched.remove((m1, w))
                matched.append(tuple((m, w)))
                # mark m1 as free and m as not free
                free_men[m1-1] = True
                free_men[m-1] = False
                matched_women[w-1] = m
        # mark the woman in m's list as proposed
        men[m-1] = [-1 if x == w else x for x in men[m-1]]
        # Once all man are not free break the loop
        if all(a is False for a in free_men):
            break
    matched = sorted(matched, key=lambda tup: tup[0])
    # print out result
    for pair in matched:
        print(f"{pair[0]}, {pair[1]}")


def main():
    read_file(sys.argv[1])
    stable_matching()
    

if __name__ == '__main__':
    main()
