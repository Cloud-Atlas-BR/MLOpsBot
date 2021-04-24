 #!/bin/bash 
 
pip install boto3
shopt -s expand_aliases
alias setblahblahenva="eval $(python scripts/digest.py)"
setblahblahenva