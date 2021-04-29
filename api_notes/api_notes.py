import requests
import json
from pprint import pprint

#single piece of information:
post_code_req = requests.get("http://api.postcodes.io/postcodes/se120nb")
print(post_code_req)
print(post_code_req.status_code)  # get the code
print(post_code_req.headers)  # shows information of response
print(post_code_req.content)  # shows data from the server
pprint(post_code_req.json())  # to get it in a dictionary format

# #making multiple requests:
# import json
# from pprint import pprint
#
# json_body = json.dumps({"postcodes":["NE1 4LY", "M45 6GN", "EX165BL"]})
# headers = {"Content-Type": "application/json"}
#
# post_multi_req = requests.post("http://api.postcodes.io/postcodes", headers = headers, data=json_body)
#
# print(post_multi_req.status_code)
# pprint(post_multi_req.json())
