#!/bin/bash

while getopts r:a:c:g:t: flag
do
    case "${flag}" in
        r) repository=${OPTARG};;
        a) account=${OPTARG};;
        c) context=${OPTARG};;
        g) region=${OPTARG};;
        t) test=${OPTARG};;
    esac
done

docker build -t ${repository} ${context}

if [ -z $test ]
then
    aws ecr describe-repositories --repository-names ${repository} || aws ecr create-repository --repository-name ${repository}
    aws ecr get-login-password --region ${region} | docker login --username AWS --password-stdin ${account}.dkr.ecr.${region}.amazonaws.com
    docker tag ${repository}:latest ${account}.dkr.ecr.${region}.amazonaws.com/${repository}:latest
    docker push ${account}.dkr.ecr.${region}.amazonaws.com/${repository}:latest
else
    echo "Push Skipped"
fi