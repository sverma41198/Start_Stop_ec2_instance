import boto3
region='ap-south-1'
client = boto3.client('ec2',region_name=region)

def lambda_handler(event,context):
        instances = get_instances_with_tag('ec2_start', 'true')
        #prints IDs of started instances
        if instances:
             client.start_instances(InstanceIds=instances)
             print(f"Stopped EC2 instances: {instances}")

#functions to get instanceID with "ec2_start:true" tag            
def get_instances_with_tag(tag_name, tag_value):
    response = client.describe_instances(Filters=[{'Name': f'tag:{tag_name}', 'Values': [tag_value]}])
    instances = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]
    return instances