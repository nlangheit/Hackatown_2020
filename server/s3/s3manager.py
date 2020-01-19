import boto3
import botocore
import uuid


class S3Manager:
    def __init__(self):
        self.BUCKET_NAME = 'polylog'
        self.PATH = 'hackatown/images/'
        self.session = boto3.Session(
            aws_access_key_id='ASIAWDSRHSOTZ6NTXJCQ',
            aws_secret_access_key = 'iPZnue+CKc5PSbaPcfqiVkIaZ8IAT4bzHKAnfMWk',
            aws_session_token = 'FwoGZXIvYXdzEFYaDNDvRp45NxYqobk0hSLQARk4fu5roK4KcAzUOdADCe4jvbX9HEUhglWHQwvdQ9S3aWrdk0Kmp44oeYhflxlHGbwNkA4CT8U27L7ogLvf3/nzYP/9p5sMP4vA3hcdunirONiEXSgIxYySzvdwCHOEik39Ob0QWtCifx5q9PZJLwIoItVSPp2Un9M+NM4XrselADxvEIncGdw8RwqZAWOvets/8e5yNLknWZCycUBk7YMxtpY52t1oPL9kkaCfCp9eZ1NlKlA1zcxvIk7U3GB5zLLL3yASXv7RYxUw5e641cIo8ruP8QUyLbnQ9TAdMasCgallw6sQ4oupkR3dsynihgAPcJFshw8Kw25U+t25CLDqNFI0qA=='
        )
        self.s3 = self.session.resource('s3')
        self.s3_client = self.session.client('s3')

    def download(self, s3_key, path):
        """
            Download file from s3
            s3_key: path in s3, excluding bucket name
            local_file: name of the file once it's downloaded
            path: path of parent folder where file will be downloaded
        """
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
    def upload(self, source_file):
        s3_path = self.PATH + uuid.uuid1().hex
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

#
# KEY = 'hackatown2020/images/example.jpg' # replace with your object key
# local = 'test.txt'
#
# s3 = S3Manager()
# s3.upload('dylan.jpg')
# s3.download(KEY, ".")
# print(s3.containsKey('hackatown2020/images/example.jpg'))
