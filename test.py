import boto3
from pprint import pprint
import json

s3_client = boto3.client('s3')
bucket_name = 'data-eng-resources'


bucket_contents = s3_client.list_objects_v2(Bucket=bucket_name,
                                            Prefix='Data21')
for key_name in bucket_contents['Contents']:
    print(key_name['Key'])
print("\nPrinting to json\n")
json_file_to_write = {"Name": "Andrei",
                      "Pets": ["dog", "cat"]}
s3_client.put_object(
    Body=json.dumps(json_file_to_write),
    Bucket=bucket_name,
    Key='Data21/Andrei.json'
)

s3_object = s3_client.get_object(
    Bucket=bucket_name,
    Key='Data21/Andrei.json'
)
contents = s3_object['Body'].read()
contents_dict = json.loads(contents)
pprint(contents_dict)

bucket_contents = s3_client.list_objects_v2(Bucket=bucket_name,
                                            Prefix='Data21')
for key_name in bucket_contents['Contents']:
    print(key_name['Key'])


s3_client.delete_object(
    Bucket=bucket_name,
    Key="Data21/Andrei.json"
)

print("\nChecking to see if file deleted.\n")
bucket_contents = s3_client.list_objects_v2(Bucket=bucket_name,
                                            Prefix='Data21')
for key_name in bucket_contents['Contents']:
    print(key_name['Key'])
