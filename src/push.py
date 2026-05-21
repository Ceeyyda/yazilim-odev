from .base import Notification, NotificationCreator

class PushNotification(Notification):
    def __init__(self, token: str, url: str):
        self.token = token
        self.url = url

    def send(self, recipient: str, message: str, priority: str = "normal") -> None:
        payload = {
            "token": self.token,
            "to": recipient,
            "body": message,
            "sound": "alert" if priority == "urgent" else "default"
        }
        print(f"[PUSH] {self.url} → {recipient}")
        print(f"  Payload: {payload}")


class PushNotificationCreator(NotificationCreator):
    def __init__(self, token: str, url: str):
        self.token = token
        self.url = url

    def create_notification(self) -> PushNotification:
        return PushNotification(self.token, self.url)