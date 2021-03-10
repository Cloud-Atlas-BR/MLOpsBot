import boto3
import pipes
client = boto3.client("ecr")
details = client.describe_images(repositoryName='mlopsbot/tweets', imageIds=[{'imageTag': 'latest'}])
digest = details["imageDetails"][0]["imageDigest"]
print("export DIGEST_TWEET=%s" % (pipes.quote(str(digest))))