"""
Pracitce catching bad practices when exception handling.
The following code is bad. Explain why using comments.
"""


# this exception exists merely to control logic flow. can be removed
class StopProcessing(Exception):
    pass


class InvoiceProcessor:
    def __init__(self, invoices):  # missing type hinting
        self.invoices = invoices

    def run(self):
        try:
            self._validate()
            self._calculate_totals()
            self._save_results()
        except StopProcessing:  # this exposes internal details braking encapsulation
            print("Processing stopped.")
        except Exception:  # too general. Overwrites exceptions' context
            print("An error occurred while processing invoices.")

    def _validate(self):
        if not self.invoices:
            # controles logic flow. can use return False instead
            raise StopProcessing("No invoices provided.")
        if not isinstance(self.invoices, list):
            raise Exception(
                "Invoices must be a list."
            )  # not truly exceptional case. Expected. Return False

    def _calculate_totals(self):
        total = 0
        for invoice in self.invoices:
            total += invoice["amount"]  # invoices is list. Treated like dict
        self.total = total

    def _save_results(self):
        try:
            with open("totals.txt", "w") as f:
                f.write(f"Total: {self.total}")
        except:  # except is too general, it does not tell what is the problem
            print(
                "Could not save results."
            )  # just return False and handle on higher level of abstraction
