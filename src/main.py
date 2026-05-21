from notifications.email import EmailNotificationCreator
from notifications.sms import SMSNotificationCreator
from notifications.push import PushNotificationCreator

email_creator = EmailNotificationCreator(host="smtp.gmail.com", port=587)
sms_creator = SMSNotificationCreator(api_key="ABC123", url="https://sms-api.example.com")
push_creator = PushNotificationCreator(token="PUSH_TOKEN_XYZ", url="https://push.example.com")

email_creator.deliver("ali@example.com", "Siparişiniz hazır!")
sms_creator.deliver("+905001234567", "Kargoya verildi.", priority="urgent")
push_creator.deliver("device_abc", "Yeni mesajınız var.")