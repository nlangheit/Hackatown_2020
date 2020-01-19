

class GarbageLocation:
    def __init__(
            self,
            location_name,
            latitude,
            longitude,
            date,
            image_url,
            pollution_level
    ):
        self.location_name: str = location_name
        self.latitude : int = latitude
        self.longitude : int = longitude
        self.date : str = date
        self.image_url : str = image_url
        self.pollution_level : int = pollution_level
