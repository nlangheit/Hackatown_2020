from typing import List

from sqlalchemy.orm import Session

from db_model import GarbageLocation
from s3.s3manager import S3Manager

"""
    def __init__(
            self,
            location_name,
            latitude,
            longitude,
            date,
            image_url,
            pollution_level
    ):
"""

class GarbageLocationService:
    def __init__(self, session: Session):
        self.storage_service: S3Manager = S3Manager()
        self.session: Session = session

    def create_garbage_location(self, request):
        # save image to s3, get URL
        # self.storage_service.upload(".")
        # create GarbageLocation object with said URL
        # add object to database
        # self.storage_service.upload()
        ...

    def get_garbage_by_id(self, garbage_id: int) -> GarbageLocation:
        return (
            self.session
                .query(GarbageLocation)
                .get(123)
        )

    def get_all_garbages(self): #  -> List[GarbageLocation]:
        garbages: List[GarbageLocation] = (
            self.session
            .query(GarbageLocation)
            .all()
        )
        liste  = {"garbages": [c.as_dict() for c in garbages]}
        # liste: list = [x.as_dict() for x in garbages]
        return liste

    def download_location(self, request):
        # save image to s3, get URL
        # create GarbageLocation object with said URL
        # add object to database
        # storage_service: S3Manager = S3Manager()
        # storage_service.
        key: str = "hackatown2020/images/example.jpg"
        self.storage_service.download(key, ".")
