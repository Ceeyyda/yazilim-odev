from .base import Notification, NotificationCreator

class SMSNotification(Notification):
    def __init__(self, api_key: str, url: str):
        self.api_key = api_key
        self.url = url

    def send(self, recipient: str, message: str, priority: str = "normal") -> None:
        if len(message) > 160:
            message = message[:157] + "..."
        if priority == "urgent":
            message = "ACİL! " + message
        print(f"[SMS] API:{self.api_key} → {recipient}")
        print(f"  Mesaj: {message}")


class SMSNotificationCreator(NotificationCreator):
    def __init__(self, api_key: str, url: str):
        self.api_key = api_key
        self.url = url

    def create_notification(self) -> SMSNotification:
        return SMSNotification(self.api_key, self.url)