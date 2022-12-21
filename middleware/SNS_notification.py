import json
import os
import boto3

ACCESS_ID = 'AKIARKPHZ57NF3RREITN'
ACCESS_KEY = 'UIGpae17i9VjS2AcrmNPssAqbSkEjsynVKLsCize'

def publish_notification(request, response):
    sns_topic_arn = "arn:aws:sns:us-east-2:091217326042:TableUpdate"
    sns_client = boto3.client('sns',
                              region_name='us-east-2',
                              aws_access_key_id=ACCESS_ID,
                              aws_secret_access_key=ACCESS_KEY)
    #if request.method in ['PUT', 'POST', 'DELETE']:
    msg = {
        "URL": request.url,
        "Method": request.method,
        "Response": response
    }
    #msg = "{\n \"test\": \"From SNS_notification.py\" \n}"
    res = sns_client.publish(
        TopicArn=sns_topic_arn,
        Message=msg,
    )
    print("publish_notification response = ",
          json.dumps(res, indent=2))

#publish_notification(1, 1)