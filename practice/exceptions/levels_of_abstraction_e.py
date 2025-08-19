"""
This code exemplifies bad separation of consenrnes that violates SRP.
The code it bad. Comments explain why.
"""


class FileProcessor:
    MAX_RETRIES = 3

    def __init__(self, file_path):  # missing type hinting everywhere
        self.file_path = file_path
        self.file = None

    def process_file(self):  # this method is doing too much. Too many except blocks
        try:
            self.open_file()
            data = self.read_file()
            processed = self.transform_data(data)
            self.save_file(processed)
        except FileNotFoundError as e:  # unnecessary alias e. Not used after
            print(f"File not found: {self.file_path}")
            raise
        except ValueError as e:  # unnecessary alias e. Not used after
            print(f"Invalid data in file: {self.file_path}")
            raise
        except Exception as e:
            print("Something went wrong")  # this does not include e. not clear what is the problem
            raise

    def open_file(self):
        for i in range(self.MAX_RETRIES):
            try:
                self.file = open(self.file_path, "r")
                break  # this brakes the flow, will except be executed at all?
            except FileNotFoundError as e:  # this exception controls logic flow
                print(f"Attempt {i+1} failed, retrying...")
        else:
            raise FileNotFoundError(
                f"Could not open file {self.file_path} after {self.MAX_RETRIES} retries"
            )

    def read_file(self):
        return self.file.read()

    def transform_data(self, data):  # type hinting is missing
        # Let's say it expects only numeric lines
        return [int(line) for line in data.split("\n")]

    def save_file(self, data):  # type hinting
        with open("output.txt", "w") as f:
            f.write(str(data))
