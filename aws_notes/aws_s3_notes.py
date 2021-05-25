import boto3
from pprint import pprint
import pandas as pd
import json
import io


s3_client = boto3.client('s3')
print(s3_client)
bucket_name = 'data-eng-resources'
s3_resource = boto3.resource('s3')

# Seeing data:
# # 1) List of buckets:
# bucket_list = s3_client.list_buckets()
# for bucket in bucket_list['Buckets']:
#     pprint(bucket['Name'])
#
# # 2)Get list of objects : list_objects_v2(prints 1000 max)
# bucket_contents = s3_client.list_objects_v2(Bucket=bucket_name,
#                                             Prefix='big-data')  # Prefix to filter "folders"
# pprint(bucket_contents)
# for key_name in bucket_contents['Contents']:
#     print(key_name['Key'])
#
# # 3) Get list of objects : all objects
# bucket = s3_resource.Bucket(bucket_name)
# contents = bucket.objects.all()
# for object in contents:
#  pprint(object.key)


# Retrieve data:
# # 1) json files:
# s3_object = s3_client.get_object(
#     Bucket=bucket_name,
#     Key='python/chatbot-intent.json'
# )
# contents = s3_object['Body'].read()
# contents_dict = json.loads(contents)
# pprint(contents_dict)
#
# # 2) csv files:
# s3_object = s3_client.get_object(
#     Bucket=bucket_name,
#     Key='python/fish-market.csv'
# )
# df = pd.read_csv(s3_object['Body'])
# print(df)


# Load data:
# # 1)json file:
# json_file_to_write = {"Name": "Andrei",
#                       "Pets": ["dog", "cat"]}
#
# # 1.a) uploading a json file:
# with open("andrei-dict.json", "w") as jsonfile:
#     json.dump(json_file_to_write, jsonfile)
#
# s3_client.upload_file(
#     Filename='andrei-dict.json',
#     Bucket=bucket_name,
#     Key='Data21/Andrei.json'
# )
#
# # 1.b) uploading straight into s3:
# s3_client.put_object(
#     Body=json.dumps(json_file_to_write),
#     Bucket=bucket_name,
#     Key='Data21/Put/Andrei.json'  # Name of file
# )
#
# # 2) csv files:
# df = pd.DataFrame([[1, 2, 3, 4, 5], [10, 20, 30, 40, 55]])
#
# # Create buffer:
# str_buffer = io.StringIO()
# df.to_csv(str_buffer)
#
# # then upload by:
# s3_client.put_object(
#     Body=str_buffer.getvalue(),
#     Bucket=bucket_name,
#     Key='Data21/CSV/Andrei.csv'
# )
# # or:
# s3_resource.Object(bucket_name, 'Data21/CSV/Andrei.csv').put(
#     Body=str_buffer.getvalue()
# )

