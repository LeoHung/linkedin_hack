# import ConfigParser
import boto
import io
import os
from boto.s3.key import Key

# config = ConfigParser.ConfigParser()
# config.read("config.ini")

from keys import S3_ACCESS_KEY, S3_SECRET_KEY, S3_BUCKET_NAME
AWS_ACCESS_KEY = S3_ACCESS_KEY
AWS_SECRET_ACCESS_KEY = S3_SECRET_KEY
S3_BUCKET = S3_BUCKET_NAME

def s3_upload(uploaded_file, id):
    s3conn = boto.connect_s3(AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY)
    bucket = s3conn.get_bucket(S3_BUCKET)

    k = Key(bucket)
    k.key = 'id-' + str(id)
    k.content_type = uploaded_file.content_type

    if hasattr(uploaded_file,'temporary_file_path'):
        k.set_contents_from_filename(uploaded_file.temporary_file_path())
    else:
        k.set_contents_from_string(uploaded_file.read())

    k.set_canned_acl('public-read')

    return k.generate_url(expires_in=0, query_auth=False)
