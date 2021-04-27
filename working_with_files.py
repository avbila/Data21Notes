# notes:
# squares = [i * i for i in range(10)]

def open_and_print_file(file):
    try:
        # opened_file = open(file, "r")
        # file_line_list = opened_file.readlines()
        # print(file_line_list)
        # for line in file_line_list:
        #     print(line.strip('\n'))
        #
        # opened_file.close()
        # or
        with open(file, "r") as opened_file:
            for line in opened_file:
                print(line.rstrip('\n'))

    except FileNotFoundError as errmsg:
        print("File not found")
        print(errmsg)  # to print message that would normally be shown
        raise  # to print messages in red
    # finally:
    #     print("Execution complete")  # will always be printed


def writing_to_file(file, order_item):
    try:
        with open(file, 'a') as opened_file:
            opened_file.write(order_item+"\n")
    except FileNotFoundError:
        print("file cannot be found")


def writing_list_to_file(file, order_list):
    # other way : [opened_file.write(item + '\n') for item in list]
    try:
        with open(file, 'a') as opened_file:
            for item in order_list:
                opened_file.write(item+"\n")
    except FileNotFoundError:
        print("file cannot be found")


# for position, line in enumerate(a_file):  [this is used to index each line so you can select specific lines in a
# text file. use if function to match with the desired line number]
# or
# with open("order.txt") as my_file:
#     print(list(my_file)[-2])

# open_and_print_file("order.txt")
# # writing_to_file("order.txt","Cabbage")
# #writing_list_to_file("order.txt", ["Chicken", "socks", "Bread"])
# open_and_print_file("order.txt")
#-------------------------------------------------------------------------------