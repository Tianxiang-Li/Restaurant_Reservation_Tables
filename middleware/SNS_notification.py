import json

def publish_notification(sns_client, sns_topic, json_message):
    res =sns_client.publish(
        TopicArn = sns_topic,
        Message = json.dumps(json_message, indent=2),
        Subject = "Something Happend"
    )

    print("publish_notification response = ",
          json.dumps(res, indent=2))
