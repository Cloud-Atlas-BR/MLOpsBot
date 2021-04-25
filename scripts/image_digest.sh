 #!/bin/bash

while getopts r: flag
do
    case "${flag}" in
        r) repository=${OPTARG};;
    esac
done

sudo apt-get install -y jq
aws ecr describe-images --repository-name ${repository} --image-ids imageTag=latest > output.json
digest=$(jq '.imageDetails[0].imageDigest' output.json)
echo $digest