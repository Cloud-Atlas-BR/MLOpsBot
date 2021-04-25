#!/bin/bash

while getopts r:a:c:g:t:k:s: flag
do
    case "${flag}" in
        r) repository=${OPTARG};;
        a) account=${OPTARG};;
        c) context=${OPTARG};;
        g) region=${OPTARG};;
        t) test=${OPTARG};;
        k) key=${OPTARG};;
        s) secret=${OPTARG};;
    esac
done

if [ $test == True ]
then
    docker build --build-arg ACCESS_KEY=${key} --build-arg SECRET_ACCESS=${secret} --build-arg REGION=${region} -t ${repository} ${context}
    docker run -d -p 9000:8080 ${repository}
    pip install pytest
    pytest
fi

if [ -z $test ]
then
    docker build -t ${repository} ${context}
    aws ecr describe-repositories --repository-names ${repository} || aws ecr create-repository --repository-name ${repository}
    aws ecr get-login-password --region ${region} | docker login --username AWS --password-stdin ${account}.dkr.ecr.${region}.amazonaws.com
    docker tag ${repository}:latest ${account}.dkr.ecr.${region}.amazonaws.com/${repository}:latest
    docker push ${account}.dkr.ecr.${region}.amazonaws.com/${repository}:latest
else
    echo "Push Skipped"
fi