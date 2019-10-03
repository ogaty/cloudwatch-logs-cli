import sys
import json
import datetime
import boto3
from boto3.session import Session

if len(sys.argv) < 3:
    print("python3 list-events.py profile groupName")
    exit(-1)

profile = sys.argv[1]
session = Session(profile_name=profile)
client = session.client('logs')

response = client.describe_log_streams(
    logGroupName=sys.argv[2],
    orderBy='LastEventTime',
    descending=True,
)

for key in response["logStreams"]:
    print(datetime.datetime.fromtimestamp(key["creationTime"] / 1000).strftime('%Y-%m-%d %H:%M:%S') + " " + key["logStreamName"])
