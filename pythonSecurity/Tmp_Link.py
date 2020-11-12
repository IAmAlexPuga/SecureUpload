import boto3
from botocore.exceptions import ClientError
from typing import Optional

#Must update the .aws/credentials with aws student session token every time!
#Remeber for demo
def create_presigned_url(bucket_name: str, object_name: str, expiration=5000) -> Optional[str]:
    #Grab current session
    s3_client = boto3.session.Session().client('s3')

    try:
        #Attempts to generate a presigned url given the above parameters
        response = s3_client.generate_presigned_url('get_object',Params={'Bucket': bucket_name,'Key': object_name},ExpiresIn=expiration)
    except ClientError as e:
        print(e)
        return None
    return response


# function that calls above function to create presigned url
def generate_presigned_url(item):
    bucket_name = "uploads-project"
    bucket_resource_url = "bidden.jpg" #"https://s3.us-east-1.amazonaws.com/" + bucket_name + "/" + item
    url = create_presigned_url(bucket_name,bucket_resource_url)
    return {
        'url': url
    }

# Need to link this to django. As of now it works 
link = generate_presigned_url(name ="bidden.jpg")

print(link)

s3 = boto3.resource("s3")

for b in s3.buckets.all():
    print(b.name)