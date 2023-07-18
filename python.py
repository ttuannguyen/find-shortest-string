input = ['aaa', 'a', 'bb', 'ccc']

def find(input):

    size = len(input)
    for i in range(size):
        inx_of_min = i
        temp = input[i]
        for j in range(i+1, size):
            print(i, j)

    # min = 1
    # for st in input:
    #     print(len(st))

find(input)