import boto3
import json
import datetime

def lambda_handler(event, context):

    # Initialize a SageMaker client
    sagemaker_client = boto3.client('sagemaker')

    now = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')

    # Define your SageMaker processing job configuration
    processing_job_name = f'test-sai-{now}'
    role = 'arn:aws:iam::801355498549:role/sagemaker-role'
    instance_count = 1
    instance_type = 'ml.t3.medium'

    # Create a processing job
    sagemaker_client.create_processing_job(
        ProcessingResources={
            'ClusterConfig': {
                'InstanceCount': instance_count,
                'InstanceType': instance_type,
                'VolumeSizeInGB': 1
            }
        },
        StoppingCondition={
            'MaxRuntimeInSeconds': 600
        },
        AppSpecification={
            'ImageUri': '801355498549.dkr.ecr.us-east-1.amazonaws.com/test_sai_ecr:latest',
        },
        RoleArn=role,
        ProcessingJobName=processing_job_name,
        Environment={
            'bucket':'test'
        }
    )

    # Wait for the processing job to complete
    sagemaker_client.get_waiter('processing_job_completed_or_stopped').wait(
        ProcessingJobName=processing_job_name
    )

    # Describe the processing job
    response = sagemaker_client.describe_processing_job(ProcessingJobName=processing_job_name)
    status = response['ProcessingJobStatus']
    if status == 'Completed':
        print("Processing job completed successfully.")
    else:
        print(f"Processing job failed with status: {status}")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }