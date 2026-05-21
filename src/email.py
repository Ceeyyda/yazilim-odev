from .base import Notification, NotificationCreator

class EmailNotification(Notification):
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def send(self, recipient: str, message: str, priority: str = "normal") -> None:
        subject = "🚨 ACİL: " if priority == "urgent" else "Bildirim: "
        subject += message[:30]
        print(f"[EMAIL] {self.host}:{self.port} → {recipient}")
        print(f"  Konu: {subject}")
        print(f"  Mesaj: {message}")


class EmailNotificationCreator(NotificationCreator):
    def __init__(self, host: str = "smtp.gmail.com", port: int = 587):
        self.host = host
        self.port = port

    def create_notification(self) -> EmailNotification:
        return EmailNotification(self.host, self.port)