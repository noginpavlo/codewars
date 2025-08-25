import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

logger = logging.getLogger()
logger.setLevel(logging.INFO)


@dataclass
class APIData:

    endpoint: str = ""
    headers: dict[str, int] = field(default_factory=dict)
    session: bool | None = None


class BaseConnector(ABC):

    @abstractmethod
    def connect(self, api_data: APIData) -> bool: ...


class BaseFetcher(ABC):

    @abstractmethod
    def fetch(self, path: str) -> dict: ...


class BaseProcessor(ABC):

    @abstractmethod
    def multiply(self, values: list[int]) -> list[int]: ...


class Connector(BaseConnector):
    def connect(self, api_data: APIData):
        if api_data.session is None:
            api_data.session = True
        return api_data.session


class Fetcher(BaseFetcher):
    def fetch(self, path: str) -> dict:
        if path == "/ok":
            return {"data": 123}
        if path == "/error":
            raise ValueError
        return {}


class Processor(BaseProcessor):

    def __init__(self, factor: int) -> None:
        self._factor = factor

    def multiply(self, values: list[int]) -> list[int]:
        return [value * self._factor if value % 2 == 0 else value for value in values]


class Service:

    def __init__(self, fetcher: BaseFetcher, processor: BaseProcessor) -> None:
        self.fetcher = fetcher
        self.processor = processor
        self.cache: dict = {}

    def run(self, path: str) -> list[int]:
        if path in self.cache:
            return self.cache[path]
        data = self.fetcher.fetch(path)
        processed = self.processor.multiply(list(data.values()))
        self.cache[path] = processed
        return processed


if __name__ == "__main__":

    fetcher1 = Fetcher()
    processor1 = Processor(2)

    s = Service(fetcher1, processor1)
    try:
        print(s.run("/ok"))
    except ValueError:
        logger.exception("ValueError occurred")

    try:
        print(s.run("/error"))
    except ValueError:
        logger.exception("ValueError occurred")

    try:
        print(s.run("/ok"))
    except ValueError:
        logger.exception("ValueError occurred")
