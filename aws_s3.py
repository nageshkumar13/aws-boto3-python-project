import os
import logging
import json
import boto3
from botocore.exceptions import ClientError
from boto3.s3.transfer import TransferConfig
import requests

# defining function for creating bucket
def create_bucket(bucket_name, region=None):
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# defining function listing bucket
def list_buckets( region=None):
    s3_client = boto3.client('s3')
    try:
        if region is not None:
            s3_client = boto3.client('s3', region_name=region)
        response = s3_client.list_buckets()
        print('Existing buckets:')
        for bucket in response['Buckets']:
            print(f'  {bucket["Name"]}')
    except ClientError as e:
        logging.error(e)
        return False
    return True

# defining a function for uploading a file to bucket
def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)

    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


# defining a function for uploading a file object to bucket
def upload_file_object(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        with open(file_name, "rb") as f:
            s3_client.upload_fileobj(f, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# define a function for deleting empty bucket
def delete_empty_bucket(bucket):
    s3_client = boto3.client('s3')
    response = s3_client.delete_bucket(Bucket=bucket)
    print(response)

#function for deleting object from bucket
def delete_object(bucket,object_name):
    s3_client = boto3.client('s3')
    response = s3_client.delete_object(Bucket=bucket,Key=object_name)

#definig function for deleting non empty bucket
def delete_non_empty_bucket(bucket):
    s3_client = s3 = boto3.resource('s3') 
    bucketClient = s3_client.Bucket(bucket)
    bucketClient.objects.all().delete()
    bucketClient.meta.client.delete_bucket(Bucket=bucket)

#function for downloading file from bucket
def download_file(file_name, bucket, object_name):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.download_file(bucket, object_name, file_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


#-------------------------------------------------------------------------------------------------------------

# giving name to the bucket
bucket_name = "boto3-nkpatel"
# specifying region where we want to create the bucket
region_name = "ap-south-1"

# Creating the bucket
#create_bucket(bucket_name, region_name)

# Listing all the buckets in the region
list_buckets(region_name)


# uploading a file called sample_file.txt to the bucket
#upload_file("sample_file.txt", bucket_name, "sample_file.txt")


# uploading a file object to bucket
#upload_file_object("./sample_file_2.txt", bucket_name, "sample_file_2.txt")

#deleting an empty bucket
#delete_empty_bucket(bucket_name)

#deleting object from the bucket 
#delete_object(bucket_name, "sample_file_2.txt")

#deleting a non-empty bucket
#delete_non_empty_bucket(bucket_name)

#downloading file from a bucket
#download_file("sample_file.txt", bucket_name, "sample_file.txt")
