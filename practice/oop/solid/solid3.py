from abc import ABC, abstractmethod
from dataclasses import dataclass

"""
Another solid refactor.
"""


@dataclass
class ReportDataHolder:
    """Holds title and data."""

    title: str
    data: list


class BaseReprotGenerator(ABC):
    """Interface for generator of reports"""

    @abstractmethod
    def generate_report(self) -> None: ...


class BaseReportSaver(ABC):
    """Interfadce for repor saver"""

    @abstractmethod
    def save_to_database(self) -> None: ...


class BaseReoprtSender(ABC):
    """Inetface for report sender"""

    @abstractmethod
    def send_report(self, recipient: str) -> None: ...


class PdfReportGenerator(BaseReprotGenerator):
    """Concrete implementation of reort generator that generates PDF"""

    def __init__(self, databank: ReportDataHolder):
        self.databank = databank

    def generate_report(self) -> None:
        print(f"Generating PDF for {self.databank.title}")
        for item in self.databank.data:
            print(f"- {item}")


class ReportSaver(BaseReportSaver):
    """Concrete implementation of report saver that saves report to the db"""

    def __init__(self, databank: ReportDataHolder):
        self.databank = databank

    def save_to_database(self) -> None:
        print(f"Saving report {self.databank.title} to database")


class EmailSender(BaseReoprtSender):
    """Concrete implementation of Email sender."""

    def __init__(self, databank: ReportDataHolder):
        self.databank = databank

    def send_report(self, recipient: str) -> None:
        print(f"Sending report {self.databank.title} to {recipient}")


class ReportManager:
    """Client that handles all the operation related to reports"""

    def generate_report(self, generator: BaseReprotGenerator) -> None:
        generator.generate_report()

    def save_report(self, saver: BaseReportSaver) -> None:
        saver.save_to_database()

    def send_repoort(self, sender: BaseReoprtSender, recipient: str) -> None:
        sender.send_report(recipient)


data = ReportDataHolder("Sales Report", ["item1", "item2", "item3"])
report_generator = PdfReportGenerator(data)
report_saver = ReportSaver(data)
report_sender = EmailSender(data)

manager = ReportManager()
manager.generate_report(report_generator)
manager.save_report(report_saver)
manager.send_repoort(report_sender, "boss@example.com")
