```mermaid

classDiagram

&#x20;   class Notification {

&#x20;       <<abstract>>

&#x20;       +send(recipient, message, priority)

&#x20;   }



&#x20;   class NotificationCreator {

&#x20;       <<abstract>>

&#x20;       +create\_notification() Notification

&#x20;       +deliver(recipient, message, priority)

&#x20;   }



&#x20;   class EmailNotification {

&#x20;       -host: str

&#x20;       -port: int

&#x20;       +send()

&#x20;   }



&#x20;   class SMSNotification {

&#x20;       -api\_key: str

&#x20;       -url: str

&#x20;       +send()

&#x20;   }



&#x20;   class PushNotification {

&#x20;       -token: str

&#x20;       -url: str

&#x20;       +send()

&#x20;   }



&#x20;   class EmailNotificationCreator {

&#x20;       -host, port

&#x20;       +create\_notification() EmailNotification

&#x20;   }



&#x20;   class SMSNotificationCreator {

&#x20;       -api\_key, url

&#x20;       +create\_notification() SMSNotification

&#x20;   }



&#x20;   class PushNotificationCreator {

&#x20;       -token, url

&#x20;       +create\_notification() PushNotification

&#x20;   }



&#x20;   Notification <|-- EmailNotification

&#x20;   Notification <|-- SMSNotification

&#x20;   Notification <|-- PushNotification



&#x20;   NotificationCreator <|-- EmailNotificationCreator

&#x20;   NotificationCreator <|-- SMSNotificationCreator

&#x20;   NotificationCreator <|-- PushNotificationCreator



&#x20;   EmailNotificationCreator ..> EmailNotification : creates

&#x20;   SMSNotificationCreator ..> SMSNotification : creates

&#x20;   PushNotificationCreator ..> PushNotification : creates

```

