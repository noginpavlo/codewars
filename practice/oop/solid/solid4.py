class NotificationSystem:
    def __init__(self, user: str, message: str):
        self.user = user
        self.message = message

    def send_notification(self, method: str) -> None:
        if method == "email":
            print(f"Sending EMAIL to {self.user}: {self.message}")
        elif method == "sms":
            print(f"Sending SMS to {self.user}: {self.message}")
        elif method == "push":
            print(f"Sending PUSH notification to {self.user}: {self.message}")
        else:
            raise ValueError("Unsupported notification method")


class AppClient:
    def notify_user(self, user: str, message: str) -> None:
        system = NotificationSystem(user, message)
        system.send_notification("email")
        system.send_notification("sms")

