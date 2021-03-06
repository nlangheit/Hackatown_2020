import boto3
import botocore
import uuid


class S3Manager:
    def __init__(self):
        self.BUCKET_NAME = 'polylog'
        self.PATH = 'hackatown/images/'
        self.OBJECT_URL = 'https://polylog.s3.amazonaws.com/'
        self.session = boto3.Session(
            aws_access_key_id='ASIAWDSRHSOTQYIZEJVF',
            aws_secret_access_key = 'OiNAmN2vUGrryxticB4cmj5hfXfVGcJi2PpHTbaF',
            aws_session_token = 'FwoGZXIvYXdzEGEaDAUMLDDqRki4zcND1SLQAXF4bqqn/B7cjnnmOy4OVPohQhE4dcYnaXLa26xPNbybQ3exyirRwWhzC2yngbPEnSrlBmNylQ52lqF6fqKd/lD9qvCleuT2a/Pv/aLCw0R6Re3r4BuFyY/PnF5FvbNcmrRZ/gL752B8HGUoRg5YOoVoT4jDm0L4QknnhFzBB2Bc8FpOJY2MKWF8ccyy36adAr+3oJjooioL5LcyoChww5OqQB+70zHgr41uzSs+Yy5OrrAhvtjoNcnjhHbmSnGOyI2+eW+Uk0XLhD7owb43u9sojPSR8QUyLZLr42XJZXHRP4T/06iqOjA0oFzliZ6l0YMhb4gI+XHHF31E676y8ilhdg+/Mg==')
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
