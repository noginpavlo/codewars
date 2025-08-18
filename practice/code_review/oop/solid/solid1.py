from abc import ABC, abstractmethod

"""
Fixing the problematic non-solid code to make it solid.
"""


class BaseReport(ABC):
    """
    Interface for Report class. Ensures existing title and data properties.
    Important for correct dependency injetion.
    """

    @property
    @abstractmethod
    def title(self) -> str: ...

    @property
    @abstractmethod
    def data(self) -> list: ...


class BaseGenerateReport(ABC):

    @abstractmethod
    def generate(self, report: BaseReport) -> str: ...


class Report(BaseReport):
    """Stores the data and title."""

    def __init__(self, title: str, data: list):
        self._title = title
        self._data = data

    @property
    def title(self) -> str:
        return self._title

    @property
    def data(self) -> list:
        return self._data


class GenerateReport:
    """Generates reports"""

    def generate(self, report: BaseReport) -> str:
        report_str = f"*** {report.title} ***\n"
        for line in report.data:
            report_str += f"- {line}\n"
        return report_str


class SaveToFile:
    """Saves to file the data"""

    def __init__(self, generator: BaseGenerateReport) -> None:
        self.generator = generator

    def save_to_file(self, report: BaseReport, filename: str):
        with open(filename, "w") as f:
            f.write(self.generator.generate(report))
        print(f"Report saved to {filename}")


class EmailSender:
    """Sends emails"""

    def __init__(self, generator: BaseGenerateReport) -> None:
        self.generator = generator

    def send_email(self, report: BaseReport, recipient: str) -> None:
        print(f"Sending report to {recipient}...")
        print(self.generator.generate(report))


class ExportJson:
    """Exports data to json"""

    def export_json(self, report: BaseReport) -> dict:
        return {"title": report.title, "data": report.data}
