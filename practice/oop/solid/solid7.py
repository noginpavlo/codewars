"""
Some more solid stuff.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class Parameters:
    """Dataclass that holds city, units and headers information."""

    city: str | None = None
    units: str = "metric"
    headers: dict = field(default_factory=dict)


@dataclass
class Cacher:
    """Dataclass that caches city information."""

    cache: dict = field(default_factory=dict)


class BaseWeatherFetcher(ABC):
    """Interface for WeatherFetcher."""

    @abstractmethod
    def fetch_weather(self) -> dict: ...


class City(ABC):

    @staticmethod
    def meets_conditions(city_name: str | None) -> dict:
        return {"city": "Unknown", "temp": 20, "condition": "Unknown"}


class LondonCity(City):

    @staticmethod
    def meets_conditions(city_name: str | None):
        if city_name == "London":
            return {"city": "London", "temp": 15, "condition": "Cloudy"}


class ParisCity(City):

    @staticmethod
    def meets_conditions(city_name: str | None):
        if city_name == "Paris":
            return {"city": "Paris", "temp": 18, "condition": "Sunny"}


class UnknownCity(City):

    @staticmethod
    def meets_conditions(city_name: str | None):
        return {"city": "Unknown", "temp": 20, "condition": "Unknown"}


class CityResolver:

    def __init__(self, params: Parameters):
        self._params = params

    def match_city(self):

        for cls in City.__subclasses__():
            if cls.meets_conditions(self._params.city):
                data = cls.meets_conditions(self._params.city)
                return data

        return {"city": "Unknown", "temp": 20, "condition": "Unknown"}



class WeatherFetcher(BaseWeatherFetcher):

    def __init__(self, cacher: Cacher):
        self._cacher = cacher

    def fetch_weather(self) -> dict:
        if self._params.city in self._cacher.cache:
            return self._cacher.cache[self._params.city]

                self._cacher.cache[self._params.city] = data
                return {}


class WeatherPrinter:

    def __init__(self, fetcher: BaseWeatherFetcher, params: Parameters, cacher: Cacher):
        self._fetcher = fetcher
        self._params = params
        self._cacher = cacher

    def print_weather(self) -> None:
        data = self._fetcher.fetch_weather()
        print(
            f"City: {self._params.city}, Temp: {data['temp']}°C, Condition: {data['condition']}"
        )


if __name__ == "__main__":

    param_settings1 = Parameters()
    cacher1 = Cacher()
    fetcher1 = WeatherFetcher(cacher1, param_settings1)
    weather_printer = WeatherPrinter(fetcher1, param_settings1, cacher1)

    param_settings1.city = "Paris"
    weather_printer.print_weather()
