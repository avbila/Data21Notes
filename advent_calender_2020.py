import numpy as np


def day_15():
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


def day_1(number_of_entries):
    input_file = open('AdventCalenderFiles/day_1.txt', 'r')
    report_entries = []
    for line in input_file:
        separate_line = line.strip()
        report_entries.append(int(separate_line))

    sum_to_search = 2020
    if number_of_entries == 2:
        while True:
            if (sum_to_search - report_entries[0]) in report_entries:
                break
            else:
                report_entries.remove(report_entries[0])

        print(report_entries[0] * (sum_to_search - report_entries[0]))
    elif number_of_entries == 3:
        for i in range(len(report_entries)):
            second_sum_to_search =sum_to_search - report_entries[i]
            for j in range(i+1, len(report_entries)):
                if (second_sum_to_search - report_entries[j]) in report_entries:
                    print(report_entries[i] * report_entries[j] * (second_sum_to_search - report_entries[j]))


def day_2(part):
    #   Separating each line in to its own list:
    input_file = open('AdventCalenderFiles/day_2.txt', 'r')
    individual_entries = []
    for line in input_file:
        separate_line = line.strip()
        line_list = separate_line.split()
        individual_entries.append(line_list)

    # Formatting the lists of each password:
    password_details = []
    for single_entry in individual_entries:
        result = []
        result.append(int(single_entry[0].split("-")[0]))
        result.append(int(single_entry[0].split("-")[1]))
        result.append(single_entry[1][0])
        result.append(single_entry[2])
        password_details.append(result)

    valid_password_count = 0
    if part == 1:
        for password in password_details:
            word_count = password[3].count(password[2])
            if password[0] <= word_count <= password[1]:
                valid_password_count += 1
    elif part == 2:
        for password in password_details:
            if password[3][password[0]-1] == password[2] and password[3][password[1]-1] != password[2]:
                valid_password_count += 1
            elif password[3][password[1]-1] == password[2] and password[3][password[0]-1] != password[2]:
                valid_password_count += 1
    print(valid_password_count)


def day_3():
    input_file = open('AdventCalenderFiles/day_3.txt', 'r')
    map_of_hill = []
    for line in input_file:
        separate_line = line.strip()
        map_of_hill.append(separate_line)

    trees = []
    max_x = len(map_of_hill[0])
    right_donw_list = [[3, 1], [1, 1], [5, 1], [7, 1], [1, 2]]
    for slop in right_donw_list:
        # x goes from left to right
        right_movement =slop[0]
        x = 0
        tree_count = 0
        for level in range(0,len(map_of_hill),slop[1]):
            if map_of_hill[level][x] == "#":
                tree_count += 1
            x += right_movement
            if x >= max_x:
                x -= max_x
        trees.append(tree_count)
    ans = 1
    for number in trees:
        ans = ans*number
    print(ans)

def day_4():
    input_file = open('AdventCalenderFiles/day_4.txt', 'r')
    passengers = []
    person = ''
    for line in input_file:
        if line == "\n":
            passengers.append(person)
            person =''
        else:
            person = person + ' ' + line.strip()
    passengers.append(person)

    valid_identification = 0
    second_valid_identification = 0
    for identification in passengers:
        print(identification)
        if "byr:" in identification and "iyr:" in identification and "eyr:" in identification and\
            "hgt:" in identification and "hcl:" in identification and "ecl:" in identification and\
                "pid:" in identification:
            valid_identification += 1
            # second level validation:
            validity_counter = 0
            # validating birth year
            identification = identification.split(" ")
            for type in identification:
                if "byr:" in type:
                    type = type.replace("byr:", "")
                    if len(type) == 4 and 1920 <= int(type) <= 2002:
                        validity_counter += 1

                if "iyr:" in type:
                    type = type.replace("iyr:", "")
                    if len(type) == 4 and 2010 <= int(type) <= 2020:
                        validity_counter += 1

                if "eyr:" in type:
                    type = type.replace("eyr:", "")
                    if len(type) == 4 and 2020 <= int(type) <= 2030:
                        validity_counter += 1

                if "hgt:" in type:
                    type = type.replace("hgt:", "")
                    if len(type) == 4 and 2020 <= int(type) <= 2030:
                        validity_counter += 1


    print(valid_identification)

day_4()
