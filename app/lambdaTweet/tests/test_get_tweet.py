import requests


def test_post():

    msg = "{}"
    url = "http://localhost:9000/2015-03-31/functions/function/invocations"
    r = requests.post(url, data=msg)
    print(r.status_code)
    assert r.text == '{"statusCode": 200}'
