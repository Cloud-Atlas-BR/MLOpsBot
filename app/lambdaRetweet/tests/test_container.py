import requests
import json


def test_post():

    msg = json.dumps({"Records": [{"messageId": "aa3c92aa-b97d-4024-b01f-b9d0ba89c135", "body": "{\"Records\":[{\"eventVersion\":\"2.1\",\"eventSource\":\"aws:s3\",\"awsRegion\":\"us-east-1\",\"eventTime\":\"2021-04-25T18:31:01.221Z\",\"eventName\":\"ObjectCreated:Put\",\"userIdentity\":{\"principalId\":\"AWS:AROA44HHEXASRK4VIL3SB:mlops-bot-tweets\"},\"requestParameters\":{\"sourceIPAddress\":\"44.192.88.161\"},\"responseElements\":{\"x-amz-request-id\":\"VR93HE8QPM3JTA8G\"},\"s3\":{\"s3SchemaVersion\":\"1.0\",\"configurationId\":\"5319166b-5927-40d4-bbf1-f1c5746f6bd2\",\"bucket\":{\"name\":\"mlops-bot-buckets3-1raofixybwfd6\",\"ownerIdentity\":{\"principalId\":\"A1FV7ZV9PVIRFA\"},\"arn\":\"arn:aws:s3:::mlops-bot-buckets3-1raofixybwfd6\"},\"object\":{\"key\":\"tweets/1385573647549558789.json\"}}}]}"}]})
    url = "http://localhost:9000/2015-03-31/functions/function/invocations"
    r = requests.post(url, data=msg)
    print(r.status_code)
    assert r.text == '{"statusCode": 200}'
