numbers_dictionary = {}
#starting_string = [1,3,2]
starting_string = [6,4,12,1,20,0,16]
# nums = starting_string

for i in range(len(starting_string)-1):
    numbers_dictionary[starting_string[i]] = i+1
prev_num = starting_string[-1]
index = len(starting_string)+1
stopping_index = 30000000

while index <= stopping_index:

    # Numbers not previously used:
    if prev_num not in numbers_dictionary.keys():
        cur_num = 0
    # Numbers previously used:
    else:
        cur_num = index - 1 - numbers_dictionary[prev_num]

    numbers_dictionary[prev_num] = index - 1
    prev_num = cur_num
    # nums.append(cur_num)
    index += 1

print(cur_num)