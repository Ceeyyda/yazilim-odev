# notifier.py

class NotificationManager:
    def __init__(self):
        self.email_host = "smtp.gmail.com"
        self.email_port = 587
        self.sms_api_key = "ABC123"
        self.sms_url = "https://sms-api.example.com/send"
        self.push_token = "PUSH_TOKEN_XYZ"
        self.push_url = "https://push.example.com/notify"
        self.log = []

    def send(self, notification_type, recipient, message, priority="normal"):
        if notification_type == "email":
            if priority == "urgent":
                subject = "🚨 ACİL: " + message[:30]
            else:
                subject = "Bildirim: " + message[:30]
            print(f"[EMAIL] {self.email_host}:{self.email_port} → {recipient}")
            print(f"  Konu: {subject}")
            print(f"  Mesaj: {message}")
            self.log.append(f"email:{recipient}:{message}")

        elif notification_type == "sms":
            if len(message) > 160:
                message = message[:157] + "..."
            if priority == "urgent":
                message = "ACİL! " + message
            print(f"[SMS] API:{self.sms_api_key} → {recipient}")
            print(f"  Mesaj: {message}")
            self.log.append(f"sms:{recipient}:{message}")

        elif notification_type == "push":
            payload = {
                "token": self.push_token,
                "to": recipient,
                "body": message,
                "sound": "alert" if priority == "urgent" else "default"
            }
            print(f"[PUSH] {self.push_url} → {recipient}")
            print(f"  Payload: {payload}")
            self.log.append(f"push:{recipient}:{message}")

        else:
            print(f"HATA: Bilinmeyen bildirim tipi: {notification_type}")

    def send_bulk(self, notification_type, recipients, message, priority="normal"):
        for recipient in recipients:
            self.send(notification_type, recipient, message, priority)

    def get_log(self):
        return self.log


if __name__ == "__main__":
    manager = NotificationManager()
    manager.send("email", "ali@example.com", "Siparişiniz hazır!", priority="normal")
    manager.send("sms", "+905001234567", "Siparişiniz kargoya verildi.", priority="urgent")
    manager.send("push", "device_token_abc", "Yeni bir mesajınız var.", priority="normal")
    manager.send_bulk("email", ["a@x.com", "b@x.com"], "Kampanya başladı!")
    manager.send("whatsapp", "someone", "test")  # hata durumu