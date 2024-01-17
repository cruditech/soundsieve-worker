import os
import boto3

def dummy_function(message):
    print("Received message:", message)

def poll_sqs(queue_url, session):
    sqs = session.client('sqs')
    while True:
        response = sqs.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=1,
            WaitTimeSeconds=20
        )
        if 'Messages' in response:
            for message in response['Messages']:
                dummy_function(message['Body'])
                sqs.delete_message(
                    QueueUrl=queue_url,
                    ReceiptHandle=message['ReceiptHandle']
                )

if __name__ == '__main__':
    session = boto3.Session(
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
        region_name='us-east-1'
    )
    queue_url = 'https://sqs.us-east-1.amazonaws.com/106022474758/SieveQueue'
    poll_sqs(queue_url, session)
