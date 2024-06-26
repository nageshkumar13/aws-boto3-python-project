import os
import boto3
import json_operations 
import json
from aws_ec2 import ec2_client


# getting the public IP of instance
def get_public_ip(instance_id):
    reservations = ec2_client.describe_instances(InstanceIds=[instance_id]).get("Reservations")

    for reservation in reservations:
        for instance in reservation['Instances']:
            print(instance.get("PublicIpAddress"))


# getting the private IP of instance
def get_private_ip(instance_id):
    reservations = ec2_client.describe_instances(InstanceIds=[instance_id]).get("Reservations")

    for reservation in reservations:
        for instance in reservation['Instances']:
            print(instance.get("PrivateIpAddress"))


# getting all running instances
def get_running_instances():
    reservations = ec2_client.describe_instances(Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running"],
        }
    ]).get("Reservations")
        
    for reservation in reservations:
        for instance in reservation["Instances"]:
            instance_id   = instance["InstanceId"]
            instance_type = instance["InstanceType"]
            public_ip     = instance["PublicIpAddress"]
            private_ip    = instance["PrivateIpAddress"]
            print(f"{instance_id}, {instance_type}, {public_ip}, {private_ip}")

# reboot instance
def reboot_instance(instance_id):
    response = ec2_client.reboot_instances(InstanceIds=[instance_id])
    print(response)


# stop instance
def stop_instance(instance_id):
    response = ec2_client.stop_instances(InstanceIds=[instance_id])
    print(response)


# start instance
def start_instance(instance_id):
    response = ec2_client.start_instances(InstanceIds=[instance_id])
    print(response)


# terminate instance
def terminate_instance(instance_id):
    response = ec2_client.terminate_instances(InstanceIds=[instance_id])
    print(response)
    ec2_data["ec2_instance_ids"].remove(instance_id)




# Replace the value of instance-id & run the code you will get 
# the public & private IP of an EC2 instance

#get_public_ip("i-03ad9e67e7936f84d")

#get_private_ip("i-03ad9e67e7936f84d")


# Run the below code & you will get the instance id, instance type, and public & private IP addresses of 
# all the running instances

get_running_instances()


# Reboot, Stop, Start & Terminate the instance

#reboot_instance("i-03ad9e67e7936f84d") #<instance-id>

#stop_instance("i-03ad9e67e7936f84d")

#start_instance("i-03ad9e67e7936f84d")

#terminate_instance("i-03ad9e67e7936f84d") #<instance-id>
