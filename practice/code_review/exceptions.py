"""
This is a practice aimed to catch bad code when exception handling.

The following code is bad. To mark bad practices use comments!
"""


class TerminateEarly(Exception):
    pass


class ReportGenerator:
    def __init__(self, data_source):
        self.data_source = data_source

    def generate(self):
        try:
            self._connect()
            self._fetch_data()
            self._format_report()
            self._save_report()
        except TerminateEarly:
            # this throws away the real reason why the exception occurred
            # "No data source provided."
            # this also shows the high-level module internal details logic, violates encapsulation
            print("Report generation stopped early.")
        except Exception as e:
            print("Unexpected error occurred:", e)

    def _connect(self):
        if not self.data_source:
            raise TerminateEarly(
                "No data source provided."
            )  # controles logic flow. Not just informative
        print(f"Connected to {self.data_source}")

    def _fetch_data(self):
        # Pretend fetching data
        if self.data_source == "offline":
            raise Exception("Data source is offline.")
        # defaults the data after raising exception. The data will not be accessible by high level module
        self.data = ["Alice", " Bob", "  Charlie "]

    def _format_report(self):
        for i in range(len(self.data)):
            self.data[i] = self.data[i].strip().title()

    def _save_report(self):
        try:
            with open("report.txt", "w") as f:
                for line in self.data:
                    f.write(line + "\n")
        except:  # too general error. Does not show the real reason why it stopped. Can be anything. Not informative
            print("Error while saving report.")
