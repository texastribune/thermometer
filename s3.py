# from datetime import datetime, timedelta
# import gzip
# import StringIO

# from boto.s3.connection import S3Connection, OrdinaryCallingFormat
# from boto.s3.key import Key

import boto3
import json


def push_to_s3(filename, contents):
    # Parameterized for testing.
    # Should this be a setting rather than a hardcoded string?
    s3_bucket = "membership.texastribune.org"
    # Create an S3 client, gives you lowest level access to S3 control
    s3_client = boto3.client(
        "s3",
        #        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        #        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )

    # Write the JSON-formatted SF data to the S3 bucket
    # Future add: Set cache-control in header
    #             Set content-type
    #             Set compression
    s3_client.put_object(
        ACL="public-read",
        Body=json.dumps(contents, indent=2),
        Bucket=s3_bucket,
        Key=filename,
    )
