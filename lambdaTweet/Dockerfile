FROM python:3.8.8-slim-buster

# Define function directory
ARG FUNCTION_DIR="/function/"

# Install aws-lambda-cpp build dependencies
RUN apt-get update && \
  apt-get install -y \
  g++ \
  make \
  cmake \
  unzip \
  wget \
  libcurl4-openssl-dev

# Create function directory
WORKDIR ${FUNCTION_DIR}

# Install the runtime interface client
RUN pip install \
        --target ${FUNCTION_DIR} \
        awslambdaric

RUN wget https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie -P /usr/local/bin/

COPY app/requirements.txt ${FUNCTION_DIR}/requirements.txt

# Install python dependences
RUN pip install \
        --target ${FUNCTION_DIR} \
        -r requirements.txt

# Copy function code
COPY app/* ${FUNCTION_DIR}

RUN chmod +x entry.sh
RUN chmod +x /usr/local/bin/aws-lambda-rie

ENTRYPOINT [ "./entry.sh" ]
CMD [ "app.handler" ]    