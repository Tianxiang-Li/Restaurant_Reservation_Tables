import json
import boto3


def publish_notification(json_message):
    sns_topic_arn = "arn:aws:sns:us-east-2:091217326042:TableUpdate"
    sns_client = boto3.client(
        'sns',
        region_name='us-east-2',
    )
    #msg = json.dumps(json_message, indent=2)
    msg = "{\n \"test\": \"From SNS_notification.py\" \n}"
    res = sns_client.publish(
        TopicArn=sns_topic_arn,
        Message=msg,
    )
    print("publish_notification response = ",
          json.dumps(res, indent=2))
