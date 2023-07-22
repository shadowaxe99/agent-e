```python
# cloud_services.py

# Import the necessary libraries for cloud hosting
import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_aws(local_file, bucket, s3_file):
    """
    Upload a file to AWS S3 bucket
    """
    s3 = boto3.client('s3')
    
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

def create_ec2_instance(instance_type, image_id, key_name):
    """
    Create an EC2 instance on AWS
    """
    ec2 = boto3.resource('ec2')
    
    try:
        instance = ec2.create_instances(
            ImageId=image_id,
            InstanceType=instance_type,
            KeyName=key_name,
            MinCount=1,
            MaxCount=1
        )
        print("Instance created successfully")
        return instance[0].id
    except Exception as e:
        print("Error creating instance:", str(e))
        return None

def create_rds_instance(instance_type, engine, username, password):
    """
    Create an RDS instance on AWS
    """
    rds = boto3.client('rds')
    
    try:
        response = rds.create_db_instance(
            DBInstanceIdentifier='my-rds-instance',
            Engine=engine,
            DBInstanceClass=instance_type,
            MasterUsername=username,
            MasterUserPassword=password,
            AllocatedStorage=20
        )
        print("RDS instance created successfully")
        return response['DBInstance']['DBInstanceIdentifier']
    except Exception as e:
        print("Error creating RDS instance:", str(e))
        return None
```
