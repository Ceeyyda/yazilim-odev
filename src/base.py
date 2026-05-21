from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str, priority: str = "normal") -> None:
        pass


class NotificationCreator(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        pass

    def deliver(self, recipient: str, message: str, priority: str = "normal") -> None:
        notification = self.create_notification()
        notification.send(recipient, message, priority)