# Import the SDK
import boto3
import botocore

class S3Manager():
    def __init__(self):
        self.BUCKET_NAME = 'polylog'
        self.session = boto3.Session(
            aws_access_key_id='ASIAWDSRHSOT6XMS4S5F',
            aws_secret_access_key = 'bkL/4wn60AT2pcpVsuw+xOyY3k9lRWjap2PdONTq',
            aws_session_token = 'FwoGZXIvYXdzEFMaDKUz1HsLmYPH4zM3jyLQAUqSNszsryVe1mOdyMVo+/54FRKx1QZc8QYXCV13j27bqZjIsGUvfAf/mavX80+aKyvHLpAxC1hGfJolJ4bc1uzN97hzXoKFRZ497+9VsB9WeAGNx5H3dpH9gxSA151kIfKabiZpe2XzSMKteJGawXrpILRcd7JfplcefRXiu0re+Mkv7d05e/L6YLZAhIXkZjvfZIAhq81oKXxROm6EJLpX/a3uNLKgIqF+tzK5wNEVuXXYY7rWswBGeED9/rhhjWG9xu2gE667hXWoOzqY6gQoot6O8QUyLVUf/cegvHStwrDigxKFWAjbWuiE3LcvTZhnJYZ7T2ZqhxLI7JxmFlv0JHqo2w=='
        )
        self.s3 = self.session.resource('s3')
        self.s3_client = self.session.client('s3')


    # Download file from s3
    # s3_key: path in s3, excluding bucket name
    # local_file: name of the file once it's downloaded
    # path: path of parent folder where file will be downloaded
    def download(self, s3_key, path):
        local_file = s3_key.split('/')[-1]
        local_file = path + "/" + local_file
        try:
            self.s3.Bucket(self.BUCKET_NAME).download_file(s3_key, local_file)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
            else:
                raise

    # Upload file to s3
    # object_key: path on s3 after bucket name
    def upload(self, source_file, s3_path):
        s3_path = s3_path + '/' + source_file
        try:
            self.s3.Bucket(self.BUCKET_NAME).upload_file(source_file, s3_path)
        except Exception as e:
            print(e)

    def listBucketObjects(self):
        try:
            response = self.s3_client.list_objects_v2(Bucket=self.BUCKET_NAME)
        except Exception as e:
            print(e)
            return None

        if response['KeyCount'] > 0:
            keys = []
            for file in response['Contents']:
                keys.append(file['Key'])
            return keys

        return None

    def containsKey(self, key):
        keys = self.listBucketObjects()
        if key in keys:
            return True
        return False


KEY =  'hackatown2020/images/example.jpg' # replace with your object key
local = 'test.txt'

s3 = S3Manager()
s3.download(KEY, ".")
# s3.upload(local, 'hackatown2020')
# print(s3.listBucketObjects())
print(s3.containsKey('hackatown2020/images/example.jpg'))



# response = s3.list_buckets()

# Output the bucket names
# print('Existing buckets:')
# for bucket in response['Buckets']:
#     print(f'  {bucket["Name"]}')


# object_key = 'test.txt'
#
# print('Uploading some data to {} with key: {}'.format(
#     myBucket, object_key))
# s3.put_object(Bucket=myBucket, Key=object_key, Body=b'Hello World!')

