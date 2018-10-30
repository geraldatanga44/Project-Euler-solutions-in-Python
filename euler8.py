def readfile(filename):  # read information from text file
    text = ''  # store numbers as string
    with open(filename, 'r') as file:  # read from file
        for line in file:
            text += line  # concatenate lines from file
    return text.replace('\n', '')  # replace \n with ""


def adjacent(adj, file):  # adjacent numbers to be multiplied
    string = readfile(file)  # get number string
    index = 0  # index for each number in string
    largest = 0  # largest adjacent product
    while index + adj < len(string):  # adjacent must index must be less than len(str)
        prod = 1  # product set to one
        sub = string[index: index + adj]  # create substring
        for i in sub:
            if int(i) == 0:  # if 0 is found with substring then product is 0
                break  # exit if i is 0
            prod *= int(i)  # cast char to int
        largest = max(prod, largest)  # get largest product
        index += 1  # increment for next adjacent numbers
    return largest  # return largest


print(adjacent(13, 'euler8.txt'))
