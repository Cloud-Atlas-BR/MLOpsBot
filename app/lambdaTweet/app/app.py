import json
import boto3
import tweepy
from src.secrets_manager import get_secret
from botocore.config import Config

# Create interface with services
s3 = boto3.client("s3")
ssm = boto3.client("ssm", config=Config(region_name='us-east-1'))

# Get twitter secrets
secrets = get_secret()

# Define a autenticação
auth = tweepy.OAuthHandler(secrets["CONSUMER_KEY"], secrets["CONSUMER_SECRET"])
auth.set_access_token(secrets["ACCESS_TOKEN"], secrets["ACCESS_TOKEN_SECRET"])

# Instancia o cliente do Twitter
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


def handler(event, context):

    ssm_name = "/CloudAtlas/MLOpsBot/Bucket"
    bucket_name = ssm.get_parameter(Name=ssm_name)["Parameter"]["Value"]

    results = api.search(q="-kiiara -bitcoin (#MLOps) -filter:retweets",
                         result_type="recent",
                         count=50)

    tweets = results["statuses"]

    for tweet in tweets:
        print(tweet)
        s3.put_object(Bucket=bucket_name,
                      Body=json.dumps(tweet).encode('utf-8'),
                      Key="tweets/" + tweet['id_str'] + ".json")

    return {'statusCode': 200}
