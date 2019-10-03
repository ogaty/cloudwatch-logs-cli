import sys
import json
import pprint
import boto3
from boto3.session import Session

if len(sys.argv) < 4:
    print("python3 get-event.py profile groupName streamName")
    exit(-1)

profile = sys.argv[1]
session = Session(profile_name=profile)
client = session.client('logs')

logGroupName = sys.argv[2]
logStreamName = sys.argv[3]


response = client.get_log_events(
    logGroupName=logGroupName,
    logStreamName=logStreamName,
    startFromHead=True
)

for key in response["events"]:
    print(key["message"])
