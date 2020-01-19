import boto3
import botocore
import uuid


class S3Manager:
    def __init__(self):
        self.BUCKET_NAME = 'polylog'
        self.PATH = 'hackatown/images/'
        self.OBJECT_URL = 'https://polylog.s3.amazonaws.com/'
        self.session = boto3.Session(
            aws_access_key_id='ASIAWDSRHSOT57HQE2VR',
            aws_secret_access_key = 'x02up9GPO9ool7Cp1QNSEoS2ILyAaYRnh/Ip6XJV',
            aws_session_token = 'FwoGZXIvYXdzEFwaDEIBBQ8sgqMkWSPlKiLQAZd9bwPT+7lmRJcVMqlHVShBcHegvx71epnnefky4U8RNWQ+W2Brzw9bSSbeh37jXK9OQxQFfnp86HmFlJfi+YLQKGt1V7eU/3FgFFd+0bnv/3sBqMbjL4Fa5fZWWfT+6HeGshs1vVD6owPHhnmLwfmrICKy25QCTe5k6clIOYGv1cHsG6MK0aFDKlISLMyMStgQDjZFLrAXF2r/wvlp0VKrXNUhllIGMmocahzgjOqB+77DUg+S/2/tT7nPmJfR+BRLiM3CFPI3kB/s6ut2Ct8oh+2Q8QUyLWM1X47DB+0vim4pb1KMHGBAF2n1BTKQdHQkyRbJu6aWZ8sAGdH4nFSdDES7nA=='
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
    def upload(self, file_content, extension: str):
        s3_path = self.PATH + uuid.uuid1().hex + extension
        try:
            # self.s3.Bucket(self.BUCKET_NAME).upload_file(source_file, s3_path)
            self.s3_client.put_object(Bucket=self.BUCKET_NAME, Key=s3_path, Body=file_content)

            return self.OBJECT_URL + s3_path
            # return 'https://polylog.s3.amazonaws.com/' +s3_path
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
                keys.append(self.OBJECT_URL + file['Key'])
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
# print(s3.listBucketObjects())
