import os
import json
import boto3
import tweepy
from secrets_manager import get_secret
from botocore.config import Config

BUCKET_NAME = "mlops-bot-buckets3-1raofixybwfd6"

# Create interface with services
s3 = boto3.client("s3")
#ssm = boto3.client("ssm", config=Config(region_name = 'us-east-1'))

# Get twitter secrets
secrets = get_secret()

# Define a autenticação
auth = tweepy.OAuthHandler(secrets["CONSUMER_KEY"], secrets["CONSUMER_SECRET"])
auth.set_access_token(secrets["ACCESS_TOKEN"], secrets["ACCESS_TOKEN_SECRET"])

# Instancia o cliente do Twitter
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

def handler(event, context):

    #since_id = ssm.get_parameter(Name="mlops-bot-since-id")["Parameter"]["Value"]

    results = api.search(q="#mlops -filter:retweets", 
                         result_type="recent", 
                         count=50
                        #  , 
                        #  since_id=since_id
                        )

    tweets = results["statuses"]
    #next_since_id = results["search_metadata"]["max_id_str"]

    for tweet in tweets:
        print(tweet)
        s3.put_object(Bucket=BUCKET_NAME,
                    Body=json.dumps(tweet).encode('utf-8'),
                    Key="tweets/"+tweet['id_str']+".json")
    
    #ssm.put_parameter(Name="mlops-bot-since-id", Value=next_since_id, Overwrite=True)

    return {

        'statusCode': 200,
        'body': json.dumps(event)
        
    }
