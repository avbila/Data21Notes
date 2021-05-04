

def prob_18():
    path = []
    with open("prob_18.txt", "r") as file:
        for line in file:
            path.append(line.replace('\n','').split(' '))
    temp_row = []
    for row_number in range(len(path)):
        path[row_number] = [int(i) for i in path[row_number]]

    index = 0
    sum = 0
    next_row = 0

    for row in path:
        sum += row[index]
        next_row += 1
        if next_row != len(path):
            if path[next_row][index] < path[next_row][index+1]:
                index += 1
    print(sum)


def prob_29():
    a_min = 2
    a_max = 100
    b_min = 2
    b_max = 100

    numbers = []

    for a in range(a_min,a_max+1):
        for b in range(b_min,b_max+1):
            numbers.append(a**b)

    print(len(set(numbers)))



prob_29()