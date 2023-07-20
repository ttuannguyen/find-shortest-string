input = ['aaa', 'a', 'bb', 'ccc']

def find(input):

    result = list()
    size = len(input)
    
    # apprach: using selection sort
    for i in range(size):
        inx_of_min = i
        temp = input[i]
        for j in range(i+1, size):
            if len(input[j]) < len(input[inx_of_min]):
                inx_of_min  = j
        input[i] = input[inx_of_min]
        input[inx_of_min] = temp
        result.append(input[i])
    return result[0]

print(find(input))
# print(input)
# print(len('a'))