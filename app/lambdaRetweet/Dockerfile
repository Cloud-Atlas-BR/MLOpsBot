FROM amazon/aws-lambda-python:3.8

ARG ACCESS_KEY
ARG SECRET_ACCESS
ARG REGION

ENV AWS_ACCESS_KEY_ID=$ACCESS_KEY
ENV AWS_SECRET_ACCESS_KEY=$SECRET_ACCESS
ENV AWS_DEFAULT_REGION=$REGION

COPY app/requirements.txt requirements.txt

# Install python dependences
RUN pip install -U pip
RUN pip install -r requirements.txt

# Copy function code
COPY app/ ./

CMD [ "app.handler" ]


# curl -H "Content-Type: application/json" -d @app/lambdaRetweet/tests/msg.json -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" 