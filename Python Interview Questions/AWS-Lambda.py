import json
import boto3
import uuid

# Initialize S3 client
s3 = boto3.client('s3')

# Define your S3 bucket name
BUCKET_NAME = "loan-default-bucket"

def lambda_handler(event, context):
    try:
        # Parse request body (Assuming JSON format)
        body = json.loads(event['body'])
        data = body.get("data", "No Data Provided")

        # Generate a unique file name
        file_name = f"data_{uuid.uuid4()}.txt"

        # Upload data to S3
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=data
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Data uploaded successfully!", "file": file_name})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
