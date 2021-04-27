import csv
# import pandas as pd
# data = pd.read_csv("user_details.csv")
# print(data)

with open("user_details.csv") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")

    # for row in csvreader:
    #     print(row[-1])

    # #to skip first line:
    # iterable_csv = iter(csvreader)
    # next(iterable_csv)
    # for row in iterable_csv:
    #     print(row)
    # Creating an ETL Pipeline:

def get_csv_file(csv_name):
    with open("user_details.csv") as csv_file:
        csvreader = csv.reader(csv_file, delimiter=",")
        ans = list(csvreader)
    return ans

def transform_user_details(csv_name):
    #only save name and  email addresss:
    new_list_list = []

    for row in csv_name:
        new_row = [row[1], row[2], row[-1]]
        new_list_list.append(new_row)

    return new_list_list

def create_new_csv_file(old_details="user_details.csv", new_file_name = "new_details.csv"):
    new_details =transform_user_details(get_csv_file(old_details))

    with open(new_file_name,'w') as new_file:
        csv_writer = csv.writer(new_file, lineterminator='\n')
        csv_writer.writerows(new_details)


create_new_csv_file()
