import json
import os
import boto3

ACCESS_ID = os.environ['ACCESS_ID']
ACCESS_KEY = os.environ['ACCESS_KEY']


def publish_notification(msg):
    sns_topic_arn = "arn:aws:sns:us-east-2:091217326042:TableUpdate"
    print('Access_id =', ACCESS_ID)
    print('Access_key =', ACCESS_KEY)
    sns_client = boto3.client('sns',
                              region_name='us-east-2',
                              aws_access_key_id=ACCESS_ID,
                              aws_secret_access_key=ACCESS_KEY)
    print("initiated client.")
    res = sns_client.publish(
        TopicArn=sns_topic_arn,
        Message=json.dumps(msg, indent=2),
    )
    print("publish_notification response = ",
          json.dumps(res, indent=2))


def check_publish(request, response):
    if request.method in ['PUT', 'POST', 'DELETE']:
        msg = {
            "URL": request.url,
            "Method": request.method,
            "Response": response.get_data(True)
        }
        print('checking before publish: ')
        print('request method = ' + request.method)
        publish_notification(msg)


"""
m = {
    "URL": "12345",
    "Method": 'GET',
    "Response": "Test Run"
}

publish_notification(m)
#"""