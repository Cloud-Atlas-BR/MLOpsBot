import json
import boto3
import tweepy
from src.secrets_manager import get_secret

# Create interface with services
s3 = boto3.client("s3")

# Get twitter secrets
secrets = get_secret()

# Define a autenticação
auth = tweepy.OAuthHandler(secrets["CONSUMER_KEY"], secrets["CONSUMER_SECRET"])
auth.set_access_token(secrets["ACCESS_TOKEN"], secrets["ACCESS_TOKEN_SECRET"])

# Instancia o cliente do Twitter
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


def handler(event, context):
    print(event, flush=True)
    for msg in event["Records"]:
        body = json.loads(msg["body"])["Records"][0]
        bucket = body["s3"]["bucket"]["name"]
        key = body["s3"]["object"]["key"]
        tweet = s3.get_object(Bucket=bucket, Key=key)
        content = json.loads(tweet["Body"].read().decode("utf-8"))
        try:
            api.retweet(id=content["id"])
            print(content, flush=True)
        except Exception:
            print("Just done", flush=True)

    return {'statusCode': 200}
