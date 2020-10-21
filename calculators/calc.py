from datetime import datetime

class Calculator:
    def __init__(self, date: datetime, lat: float, lon: float, house_sys: str):
        self.date = date
        self.lat = lat
        self.lon = lon
        self.house_sys = house_sys

    def utc_offset(self):
      return 4
