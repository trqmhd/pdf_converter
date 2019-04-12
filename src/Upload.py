import boto
import os
import boto3
from boto.s3.key import Key

#aws credential
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

client = boto3.client('s3')

bucket_name = 'cloud-automation' #s3 bucket name


conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
bucket = conn.get_bucket(bucket_name)

k = Key(bucket)
bucket_list = bucket.list()


rootdir = '/Users/trqmhd/PycharmProjects/Microservices/output' #  triggered folder/files to upload
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        local_path = os.path.join( subdir, file)
        relative_path = os.path.relpath(local_path, rootdir)
        s3_path = os.path.join(relative_path)
        print ('Searching "%s" in "%s"' % (s3_path, bucket_name))


        try:
            client.head_object(Bucket=bucket_name, Key=s3_path)
            print ("Path found on S3! Skipping %s..." % s3_path)

        # try:
            # client.delete_object(Bucket=bucket, Key=s3_path)
        # except:
            # print "Unable to delete %s..." % s3_path
        except:
            print ("Uploading %s..." % s3_path)
            client.upload_file(local_path, bucket_name, s3_path)










