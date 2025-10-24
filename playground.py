from abc import ABC, abstractmethod


class Sender(ABC):
    """Interface"""

    @abstractmethod
    def send(self, receiver: str, message: str) -> None: ...


class EmailMessageSender(Sender):
    """Concrete class that sends messages to receiver."""

    def send(self, receiver: str, message: str) -> None:
        print(f"Message {message} sent to {receiver}")


class SenderStrategy:
    """Orchestrator class that will be called by client."""

    def __init__(self, sender: Sender) -> None:
        self.sender = sender

    def send_message(self, receiver: str, message: str) -> None:
        self.sender.send(receiver, message)


# client
MY_RECEIRVER = "Pavlo"
MY_MESSAGE = "Hey how's it going?"
my_sender = EmailMessageSender()
sndr = SenderStrategy(my_sender)
sndr.send_message(MY_RECEIRVER, MY_MESSAGE)
