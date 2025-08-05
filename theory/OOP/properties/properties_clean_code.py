"""
Read getter_setter.py first. This is one more practice example with additional stuff.
"""


class Coordinates:
    """
    Class accepts latitude and longitude values but the must be defined within particular range
    (from -90 to 90)
    """

    def __init__(self, lat: float, long: float) -> None:  # None return is typical for __init__
        self._latitude = self._longitude = 0.0  # ensures that _latitude and _longitude exist anyway
        self.latitude = lat
        self.longitude = long

    @property
    def latitude(self) -> float:
        return self._latitude

    @latitude.setter
    def latitude(self, lat_value: float) -> None:
        if lat_value not in range(-90, 90 + 1):
            raise ValueError(f"{lat_value} is not in valid latitude range")
        self._latitude = lat_value

    @property
    def longitude(self) -> float:
        return self._longitude

    @longitude.setter
    def longitude(self, long_value: float) -> None:
        if long_value not in range(-90, 91 + 1):
            raise ValueError(f"{long_value} is not in valid longitude range")
        self._longitude = long_value
