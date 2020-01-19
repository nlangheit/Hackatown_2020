import os
from datetime import date, datetime
from typing import List

from flask import Request
from werkzeug import local
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

    def create_garbage_location(self, request: Request):
        filename, file_extension = os.path.splitext(str(request.files.get("image").filename)) # .params[<form element name with file>].filename
        file_extension = file_extension if file_extension else ""
        bucket_key: str = self.storage_service.upload(request.files.get("image").read(), extension=file_extension)
        garbage_location: GarbageLocation = GarbageLocation(
            location_name=request.form.get("location_name"),
            latitude=request.form.get("latitude"),
            longitude=request.form.get("longitude"),
            date=datetime.now(),
            image_url=bucket_key,
            pollution_level=request.form.get("pollution_level")
        )
        self.session.add(garbage_location)
        self.session.commit()

    def get_garbage_by_id(self, garbage_id: int) -> dict:
        return (
            self.session
                .query(GarbageLocation)
                .get(garbage_id)
        ).as_dict()

    def get_all_garbages(self): #  -> List[GarbageLocation]:
        garbages: List[GarbageLocation] = (
            self.session
            .query(GarbageLocation)
            .all()
        )
        liste  = {"garbages": [c.as_dict() for c in garbages]}
        return liste

    def download_location(self, request):
        # save image to s3, get URL
        # create GarbageLocation object with said URL
        # add object to database
        # storage_service: S3Manager = S3Manager()
        # storage_service.
        key: str = "hackatown2020/images/example.jpg"
        self.storage_service.download(key, ".")
