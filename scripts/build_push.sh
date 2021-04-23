#!/bin/bash

while getopts r:a:c:g: flag
do
    case "${flag}" in
        r) repository=${OPTARG};;
        a) account=${OPTARG};;
        c) context=${OPTARG};;
        g) region=${OPTARG};;
    esac
done

aws ecr describe-repositories --repository-names ${repository} || aws ecr create-repository --repository-name ${repository}
aws ecr get-login-password --region ${region} | docker login --username AWS --password-stdin ${account}.dkr.ecr.${region}.amazonaws.com
docker build -t ${repository} context
docker tag ${repository}:latest ${account}.dkr.ecr.${region}.amazonaws.com/${repository}:latest
docker push ${account}.dkr.ecr.${region}.amazonaws.com/${repository}:latest