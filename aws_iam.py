import json
import boto3
from botocore.exceptions import ClientError

 # defining function for creating IAM User
def create_iam_user(user_name):
    try:
        iam_client = boto3.client('iam')
        response = iam_client.create_user(UserName=user_name)
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists")
            return False
        else:
            print("Unexpected error: %s" % e)
            return False
    return response


# function for listing all IAM users
def list_iam_users():
    try:
        iam_client = boto3.client('iam')
        paginator = iam_client.get_paginator('list_users')
        for response in paginator.paginate():
            #print(response["Users"])
            for user in response["Users"]:
                print("User name: ",user["UserName"])
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists")
        else:
            print("Unexpected error: %s" % e)


#function for upading IAM user
def update_iam_user(existing_user_name, new_user_name):
    try:
        iam_client = boto3.client('iam')
        iam_client.update_user(UserName=existing_user_name,
                            NewUserName=new_user_name)
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists")
        else:
            print("Unexpected error: %s" % e)

#function for creating IAM policy
def create_iam_policy(policy_name, policy_json):
    try:
        iam_client = boto3.client('iam')
        iam_client.create_policy(
            PolicyName=policy_name,
            PolicyDocument=json.dumps(policy_json)
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists")
            return False
        else:
            print("Unexpected error: %s" % e)
            return False
    return True

#function for attaching IAM policy to user
def attach_custom_iam_policy_with_user(policy_name, user_name):
    try:
        sts = boto3.client('sts')
        account_id = sts.get_caller_identity()['Account']
        policy_arn = f'arn:aws:iam::{account_id}:policy/{policy_name}'
        iam_client = boto3.client('iam')
        iam_client.attach_user_policy(
            UserName=user_name,
            PolicyArn=policy_arn
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists")
        else:
            print("Unexpected error: %s" % e)

# attaching AWS managed IAM policy
def attach_managed_iam_policy_with_user(policy_name, user_name):
    try:
        sts = boto3.client('sts')
        policy_arn = f'arn:aws:iam::aws:policy/{policy_name}'
        iam_client = boto3.client('iam')
        iam_client.attach_user_policy(
            UserName=user_name,
            PolicyArn=policy_arn
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists")
        else:
            print("Unexpected error: %s" % e)

#function for detaching IAM policy from user
def detach_custom_iam_policy_with_user(policy_name, user_name):
    try:
        sts = boto3.client('sts')
        account_id = sts.get_caller_identity()['Account']
        policy_arn = f'arn:aws:iam::{account_id}:policy/{policy_name}'
        iam_client = boto3.client('iam')
        iam_client.detach_user_policy(
            UserName=user_name,
            PolicyArn=policy_arn
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists")
        else:
            print("Unexpected error: %s" % e)


# detaching AWS managed IAM policy
def detach_managed_iam_policy_with_user(policy_name, user_name):
    try:
        sts = boto3.client('sts')
        policy_arn = f'arn:aws:iam::aws:policy/{policy_name}'
        iam_client = boto3.client('iam')
        iam_client.detach_user_policy(
            UserName=user_name,
            PolicyArn=policy_arn
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists")
        else:
            print("Unexpected error: %s" % e)


#function for deleting IAM User
def delete_iam_user(user_name):
    try:
        iam_client = boto3.client('iam')
        response = iam_client.delete_user(UserName=user_name)
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists")
            return False
        else:
            print("Unexpected error: %s" % e)
            return False
    return response

#=============================================================================================================

#listing all Iam users 
#list_iam_users()
user_name = ["namchandJ", "luckysingh", "nageshKumar", "Khubchand"]

# #creating a Iam User 
# for i in user_name:
#     responseObject = create_iam_user(i)
#     print(responseObject)


# # upading IAM user
#update_iam_user("virendraK", "Khubchand")
#list_iam_users()

# # creating IAM policy
custom_policy_json = {
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Action": [
                "ec2:*"
            ],
            "Resource": "*"
        }]
    }
#create_iam_policy("majha_policy_ultimate_policy", custom_policy_json)

# attaching our custom IAM policy to user
#attach_custom_iam_policy_with_user("majha_policy_ultimate_policy", "Khubchand")

# # attaching AWS managed IAM policy
#attach_managed_iam_policy_with_user("AdministratorAccess", "nageshKumar")

# #function for detaching IAM policy from user
# detach_custom_iam_policy_with_user("majha_policy_ultimate_policy", "Khubchand")

# detaching AWS managed IAM policy
#detach_managed_iam_policy_with_user("AdministratorAccess", "nageshKumar")

# #function for deleting IAM User
# for i in user_name:
#     responseObject = delete_iam_user(i)
#     print(responseObject)
