import json
import datetime

def lambda_handler(event, context):
    currentDT = datetime.datetime.now()
    print (str(currentDT))
