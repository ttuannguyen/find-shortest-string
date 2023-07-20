input = ['aaa', 'aa', 'ccc', 'cc', 'b']

def find(input):
    
    shortest = input[0]
    
    for string in input:
        if len(string) < len(shortest):
            shortest = string
    
    return shortest


    # apprach: using selection sort; a bit long
    # size = len(input)
    # for i in range(size):
    #     inx_of_min = i
    #     temp = input[i]
    #     for j in range(i+1, size):
    #         if len(input[j]) < len(input[inx_of_min]):
    #             inx_of_min  = j
    #     input[i] = input[inx_of_min]
    #     input[inx_of_min] = temp
    #     result.append(input[i])
    # return result[0]

find(input)
# print(input)
# print(len('a'))