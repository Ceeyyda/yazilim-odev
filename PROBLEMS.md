Kodu incelediğimde gördüğüm birkaç tane sorun var fakat Claude AI ile paylaştığımda benden çok daha fazla sorun gördü. Açıkçası buna fazlasıyla şaşırdım çünkü göremediğim ama çözülmesi gereken bu  kadar sorunun farkında değildim. Claude AI' ya sorduğumda 
Kodun Tasarım Sorunları:

1\. 🔴 God Class — Tek Sınıf Her Şeyi Yapıyor

NotificationManager hem e-posta bağlantı bilgilerini tutuyor, hem SMS API'sini çağırıyor, hem push payload'ı oluşturuyor, hem log yazıyor. Bir sınıfın tek bir sorumluluğu olmalı (Single Responsibility Principle). Şu an bu sınıf değişmesi için 5 farklı sebep var.

Çözüm: Her bildirim tipini ayrı bir sınıfa taşı → Factory Method veya Strategy



2\. 🔴 if-else Zinciri ile Tip Kontrolü (Open/Closed İhlali)

Yeni bir bildirim tipi (WhatsApp, Slack, Teams) eklemek için send() metodunun içine girip yeni bir elif bloku eklemen gerekiyor. Bu, mevcut kodu kırar ve test edilmiş mantığa dokunmak zorunda bırakır.

Çözüm: Her tip için ayrı sınıf → Factory Method veya Strategy Pattern



3\. 🟠 Hard-coded Konfigürasyon

smtp.gmail.com, ABC123, PUSH\_TOKEN\_XYZ değerleri doğrudan sınıfın içine yazılmış. Test ortamında farklı, production'da farklı değer kullanmak imkânsız. Üstelik API key kaynak kodunda görünüyor.

Çözüm: Konfigürasyonu dışarıdan enjekte et → Builder Pattern veya config dosyası



4\. 🟠 Priority Mantığı Her Blokta Tekrar Ediyor

if priority == "urgent" kontrolü email bloğunda, SMS bloğunda, push bloğunda ayrı ayrı yazılmış. Yarın "VIP" gibi yeni bir öncelik tipi eklemek istersen 3 farklı yeri değiştirmen gerekir.

Çözüm: Öncelik mantığını ayrı bir katmana çıkar → Decorator Pattern



5\. 🟠 send\_bulk, send'i Tekrar Çağırıyor — Başka Bir Sorumluluk

Toplu gönderme mantığı send() metodunun üstüne yapıştırılmış. Toplu gönderimde hata yönetimi, retry, paralel işlem gibi ihtiyaçlar ayrı bir kavram — ama şu an hepsi aynı torbada.

Çözüm: → Command Pattern (gönderimi kuyruğa alınabilir bir nesneye dönüştür)



6\. 🟡 Log Mekanizması İlkel ve Sınıfa Gömülü

Log sadece bir string listesi ve sadece bu sınıf yazabiliyor. Yarın dosyaya yazmak, veritabanına kaydetmek veya birden fazla sistemin log'u dinlemesi gerekirse ne olacak?

Çözüm: → Observer Pattern (log, bir gözlemci olarak sisteme bağlanır)



7\. 🟡 Nesne Her Seferinde Yeniden Yaratılabilir

NotificationManager() her yerde new ile oluşturulabilir. Birden fazla instance olursa log'lar ayrı ayrı tutulur, konfigürasyon tutarsızlaşır.

Çözüm: → Singleton Pattern

cevaplarını verdi. Ben de tek bir sınıf içinde bütün işlemin yapıldığını ve bunun işlevsel olmadığı fark etmiştim. Bunun yanında if-else zinciri sebebiyle kodun dinamikliğinin bozulduğunu da görmüştüm fakat diğer sorunlar bana yabancı geldi.

