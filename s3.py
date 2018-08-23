from datetime import datetime, timedelta
import gzip
import StringIO

from boto.s3.connection import S3Connection, OrdinaryCallingFormat
from boto.s3.key import Key


def push_to_s3(filename=None, contents=None):

    out = StringIO.StringIO()
    with gzip.GzipFile(fileobj=out, mode="w") as f:
        f.write(contents)

    conn = S3Connection(calling_format=OrdinaryCallingFormat())
    bucket = conn.get_bucket('membership.texastribune.org')
    k = Key(bucket)
    k.key = filename
    k.set_contents_from_string(out.getvalue(),
            policy='public-read',
            headers={
                'Cache-Control': 'no-cache',
                'Content-Type': 'application/json',
                'Content-Encoding': 'gzip',
                })
    k.set_acl('public-read')
