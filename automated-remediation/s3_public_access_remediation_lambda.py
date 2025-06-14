import boto3
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    """
    Lambda function to automatically remediate S3 buckets with public access.
    It identifies the bucket from the event and ensures public access blocks are enabled.
    """
    logger.info(f"Received event: {event}")

    try:
        # This Lambda is typically triggered by an AWS Config rule or CloudWatch Event
        # that detects non-compliance. The event structure will vary.
        # For this exercise, let's assume the bucket name is directly passed or
        # can be extracted from a common Config Rule event structure.

        # --- Scenario 1: Directly passing bucket name for testing/demonstration ---
        # If the event directly contains 'bucket_name' for simpler testing
        if 'bucket_name' in event:
            bucket_name = event['bucket_name']
            logger.info(f"Processing bucket: {bucket_name} from direct event.")
        # --- Scenario 2: Extracting from AWS Config Rule Event ---
        # A common AWS Config Rule event for S3 public access will look like this:
        # event['detail']['requestParameters']['bucketName'] for PutBucketAcl, etc.
        # Or for Config Rule evaluations: event['detail']['newEvaluationResult']['evaluationResultIdentifier']['resourceDetails']['resourceId']
        elif 'detail' in event and 'requestParameters' in event['detail'] and 'bucketName' in event['detail']['requestParameters']:
            bucket_name = event['detail']['requestParameters']['bucketName']
            logger.info(f"Processing bucket: {bucket_name} from CloudTrail/Config event.")
        elif 'detail' in event and 'resourceId' in event['detail'] and 'resourceType' in event['detail'] and event['detail']['resourceType'] == 'AWS::S3::Bucket':
            bucket_name = event['detail']['resourceId']
            logger.info(f"Processing bucket: {bucket_name} from generic Config event.")
        else:
            logger.error("Could not determine bucket name from event.")
            return {
                'statusCode': 400,
                'body': 'Could not determine bucket name from event.'
            }

        logger.info(f"Attempting to ensure public access block for bucket: {bucket_name}")

        # Ensure Public Access Block is enabled for the bucket
        # This operation will prevent new public ACLs, policies, and block existing ones.
        s3_client.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': True,
                'IgnorePublicAcls': True,
                'BlockPublicPolicy': True,
                'RestrictPublicBuckets': True
            }
        )
        logger.info(f"Successfully applied Public Access Block to bucket: {bucket_name}")

        return {
            'statusCode': 200,
            'body': f'Successfully remediated S3 bucket: {bucket_name} - Public Access Block enabled.'
        }

    except s3_client.exceptions.NoSuchBucket as e:
        logger.error(f"Bucket {bucket_name} does not exist: {e}")
        return {
            'statusCode': 404,
            'body': f'Bucket {bucket_name} not found.'
        }
    except Exception as e:
        logger.error(f"Error remediating S3 public access for {bucket_name}: {e}")
        return {
            'statusCode': 500,
            'body': f'Error remediating S3 bucket {bucket_name}. Error: {str(e)}'
        }