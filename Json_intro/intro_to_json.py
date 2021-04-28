import json

# pet_data = {
#     "name": "bob",
#     "food": "carrots"
# }
# print(pet_data)

# pet_data_jason_str = json.dumps(pet_data)  # converts json format to str string
# print(pet_data_jason_str)

# #writing a json file:
# with open("new_json_file.json", "w") as jsonfile:
#     json.dump(pet_data,jsonfile)

# #opening a json file:
# with open("new_json_file.json") as jsonfile:
#     pet = json.load(jsonfile)  # creats a dictionary from json file
#
#     print(type(pet))
#     print(pet)

#build a class around json file exchange rate:
class RatesParser:

    def __init__(self, rates_files):
        rates_info = self._open_json_file(rates_files)
        self.base = rates_info["base"]
        self.date = rates_info["date"]
        self.rates = rates_info["rates"]

    def _open_json_file(self, file_name):
        with open(file_name) as rates:
            return json.load(rates)

    # rates_reader = RatesParser("exchange_rates.json")
    # print(rates_reader.base)


