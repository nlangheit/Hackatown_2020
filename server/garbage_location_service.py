from s3.s3manager import S3Manager


class GarbageLocationService:
    def __init__(self):
        self.storage_manager: S3Manager = S3Manager()

    def create_new_location(self, request):
        # save image to s3, get URL
        # create GarbageLocation object with said URL
        # add object to database
        # storage_service: S3Manager = S3Manager()
        # storage_service.
        ...

    def download_location(self, request):
        # save image to s3, get URL
        # create GarbageLocation object with said URL
        # add object to database
        # storage_service: S3Manager = S3Manager()
        # storage_service.
        key: str = "hackatown2020/images/example.jpg"
        self.storage_manager.download(key, ".")

