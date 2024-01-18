import os
import json

import boto3
from botocore.exceptions import ClientError
from spleeter.separator import Separator

try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    if not (os.environ.get('AWS_ACCESS_KEY_ID') and os.environ.get('AWS_SECRET_ACCESS_KEY')):
        print("dotenv not installed, AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY must be set in environment")
    

def inject_doppler_secrets(session):

    secret_name = "doppler"
    region_name = "us-east-1"

    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # secret = get_secret_value_response['SecretString']
    os.environ = {**os.environ, **get_secret_value_response}

def dummy_function(message):
    print("Received message:", message)
    process_audio(json.loads(message)['target_audio_uri'])

def process_audio(target_audio_uri)
    # Using embedded configuration.
    separator = Separator('spleeter:2stems')

    # Using custom configuration file.
    # separator = Separator('/path/to/config.json')

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
    inject_doppler_secrets(session)
    queue_url = 'https://sqs.us-east-1.amazonaws.com/106022474758/SieveQueue'
    poll_sqs(queue_url, session)
