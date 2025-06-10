import boto3
import json
from datetime import datetime

def log_to_s3(bucket_name, filename, input_data, prediction):
    s3 = boto3.client('s3')

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "input": input_data,
        "prediction": prediction
    }

    s3.put_object(
        Bucket=bucket_name,
        Key=f"{filename}_{datetime.now().strftime('%Y%m%d%H%M%S')}.json",
        Body=json.dumps(log_entry),
        ContentType='application/json'
    )
