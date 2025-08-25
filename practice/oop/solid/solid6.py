import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


@dataclass
class FileData:
    lines: list[str] = field(default_factory=list)


@dataclass
class Cache:
    data: dict[str, list[str]] = field(default_factory=dict)


class BaseProcessor(ABC):
    @abstractmethod
    def process_data(self, data: list[str]) -> list[str]: ...


class UpperEvenProcessor(BaseProcessor):
    def process_data(self, data: list[str]) -> list[str]:
        return [x.strip().upper() if i % 2 == 0 else x.strip() for i, x in enumerate(data)]


class BaseFileReader(ABC):
    @abstractmethod
    def read(self, path: str) -> FileData: ...


class FileReader(BaseFileReader):
    def read(self, path: str) -> FileData:
        file_data = FileData()
        if Path(path).exists():
            with open(path, "r", encoding="utf-8") as f:
                file_data.lines = f.readlines()
        return file_data


class Loader:
    def __init__(self, reader: BaseFileReader, processor: BaseProcessor, cache: Cache):
        self.reader = reader
        self.processor = processor
        self.cache = cache

    def load_file(self, path: str) -> list[str]:
        if path in self.cache.data:
            return self.cache.data[path]

        file_data = self.reader.read(path)
        processed_lines = self.processor.process_data(file_data.lines)
        self.cache.data[path] = processed_lines
        return processed_lines


class Printer:
    def print_file(self, file_data: FileData) -> None:
        if file_data.lines:
            for line in file_data.lines:
                print(line, end="")  # lines already have newline
        else:
            logger.info("File is empty or not found.")
            raise FileNotFoundError("No lines to print.")


if __name__ == "__main__":

    PATH = "example.txt"

    reader = FileReader()
    processor = UpperEvenProcessor()
    cache = Cache()
    loader = Loader(reader, processor, cache)

    processed_lines = loader.load_file(PATH)
    file_data = FileData(processed_lines)
    printer = Printer()
    printer.print_file(file_data)
