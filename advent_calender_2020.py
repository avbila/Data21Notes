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


def day_4():  # needs part 2
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


# Day 5:
class Day_5_problem:

    def __init__(self):
        self.columns = []
        self.rows = []
        self.row_values = []
        self.column_values = []
        self.max_id = 0
        self.passenger_tickets=[]
        self.missing_row = 0
        self.missing_column = 0

    def get_input(self, file_name="AdventCalenderFiles/day_5.txt"):
        with open(file_name, 'r') as input_file:
            for line in input_file:
                self.passenger_tickets.append(line)

    def get_rows(self):
        for passenger in self.passenger_tickets:
            self.rows.append(passenger[:7])

    def get_columns(self):
        for passenger in self.passenger_tickets:
            self.columns.append(passenger[-4:-1])

    def get_row_values(self):
        for passenger in self.rows:
            row_numbers = [i for i in range(0, 128)]
            for partition in passenger:
                if len(row_numbers) == 2 and partition == "F":
                    self.row_values.append(row_numbers[0])
                elif len(row_numbers) == 2 and partition == "B":
                    self.row_values.append(row_numbers[1])
                elif partition == "F":
                    row_numbers = row_numbers[0:int(len(row_numbers)/2)]
                else:
                    row_numbers = row_numbers[int(len(row_numbers)/2):]

    def get_column_values(self):
        for passenger in self.columns:
            column_numbers = [i for i in range(0, 8)]
            for partition in passenger:
                if len(column_numbers) == 2 and partition == "L":
                    self.column_values.append(column_numbers[0])
                elif len(column_numbers) == 2 and partition == "R":
                    self.column_values.append(column_numbers[1])
                elif partition == "L":
                    column_numbers = column_numbers[0:int(len(column_numbers)/2)]
                else:
                    column_numbers = column_numbers[int(len(column_numbers)/2):]

    def find_biggest_id(self):
        for index in range(len(self.row_values)):
            id = (8 * self.row_values[index]) + self.column_values[index]
            if id > self.max_id:
                self.max_id = id

    def get_highest_id(self):
        return self.max_id

    def find_missing_row(self):
        for row_number in range(1, 127):
            if self.row_values.count(row_number) == 7:
                self.missing_row = row_number

    def find_missing_column(self):
        column_numbers = [i for i in range(0,8)]
        for index in range(len(self.column_values)):
            if self.row_values[index] == self.missing_row:
                column_numbers.remove(self.column_values[index])
        self.missing_column = column_numbers[0]

    def find_missing_id(self):
        return (self.missing_row * 8) + self.missing_column

    # test = Day_5_problem()
    # test.get_input()
    # test.get_rows()
    # test.get_columns()
    # test.get_row_values()
    # test.get_column_values()
    # test.find_biggest_id()
    # print(test.get_highest_id())
    # test.find_missing_row()
    # test.find_missing_column()
    # print(test.find_missing_id())


# Day 6:
class Day_6_problem:

    def __init__(self):
        self.group_data = []
        self.sum_count_1 = 0
        self.sum_count_2 = 0

    def get_input_file(self, file_name="AdventCalenderFiles/day_6.txt"):
        data = []
        with open(file_name, 'r') as input_file:
            for line in input_file:
                data.append(line)

        group_info = []
        for line in data :
            if line == "\n":
                self.group_data.append(group_info)
                group_info = []
            else:
                group_info.append(line.replace("\n", ""))
        self.group_data.append(group_info)

    def get_sum_count_part_1(self):
        for group in self.group_data:
            yes_ans = ""
            for ans in group:
                yes_ans += ans
            yes_ans = set(list(yes_ans))
            self.sum_count_1 += len(yes_ans)

    def get_sum_count_part_2(self):
        for group in self.group_data:
            similar_ans = set(group[0])
            if len(group) > 1:
                for i in range(1, len(group)):
                    similar_ans = similar_ans.intersection(set(group[i]))
            self.sum_count_2 += len(similar_ans)

    # test = Day_6_problem()
    # test.get_input_file()
    # test.get_sum_count_part_1()
    # print(test.sum_count_1)
    # test.get_sum_count_part_2()
    # print(test.sum_count_2)


# Day 8:
class Day_8_problem:

    def __init__(self):
        self.code = []
        self.accumulator = 0
        self.jmp_position = []
        self.nop_position = []

    def get_input_file(self, file_name="AdventCalenderFiles/day_8.txt"):
        with open(file_name, 'r') as input_file:
            for line in input_file:
                self.code.append(line.replace("\n", ""))

    def get_cal_accumulator(self):
        index_used =[]
        index = 0
        while True:
            current_code = list(self.code[index].split(" "))
            if index in index_used:
                break
            else:
                index_used.append(index)
                if current_code[0] == "nop":
                    index += 1
                    self.nop_position.append(index)
                elif current_code[0] == "jmp":
                    jump_distance = int(current_code[1])
                    index += jump_distance
                    self.nop_position.append(index)
                elif current_code[0] == "acc":
                    index += 1
                    add_value = int(current_code[1])
                    self.accumulator += add_value

        print(self.accumulator)

    def trouble_shoot_nop(self):
        pass

    def trouble_shoot_jmp(self):
        pass

test = Day_8_problem()
test.get_input_file()
test.get_cal_accumulator()