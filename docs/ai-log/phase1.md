\# AI Log — Faz 1: Factory Method



\## Kullandığım AI aracı

Claude (claude.ai)



\---



\## 1. Kod analizi için sorduğum prompt



> "Bu kodda hangi tasarım sorunlarını görüyorsun? Hangi tasarım örüntüleri

> bu sorunları çözebilir? Her sorun için kısa bir açıklama yaz."



\## AI'ın yanıtı (özet)



7 temel sorun tespit etti:

\- God Class: NotificationManager her şeyi tek başına yapıyor (SRP ihlali)

\- if-else tip kontrolü: yeni tip eklemek mevcut kodu kırıyor (OCP ihlali)

\- Hard-coded konfigürasyon: API key ve host bilgileri sınıfa gömülü

\- Priority mantığı tekrarı: urgent kontrolü her blokta ayrı yazılmış

\- Bulk gönderim karmaşası: farklı bir sorumluluk aynı sınıfta

\- İlkel log mekanizması: Observer ile çözülebilir

\- Singleton eksikliği: birden fazla instance sorunu



Çözüm olarak Factory Method, Strategy, Observer, Decorator, Command,

Builder ve Singleton örüntülerini önerdi.



\---



\## 2. Örüntü seçimi için sorduğum prompt



> "Bildirim sistemi için en uygun Creational örüntü hangisi olur,

> Factory Method mu yoksa Builder mı?"



\## AI'ın yanıtı (özet)



Factory Method'un daha uygun olduğunu söyledi çünkü:

\- Her bildirim tipi bağımsız bir nesne

\- Nesne inşası çok adımlı değil, Builder gerekmez

\- Yeni tip eklemek için sadece yeni bir Creator sınıfı yeterli



\---



\## 3. Ben ne uyguladım ve neden?



AI'ın Factory Method önerisini uyguladım. Ancak bazı noktalarda

kendi kararlarımı aldım:



\- AI doğrudan `NotificationFactory` adında tek bir sınıf önerdi.

&#x20; Ben bunun yerine her tip için ayrı Creator sınıfı yazdım çünkü

&#x20; bu daha saf bir Factory Method implementasyonu.



\- `deliver()` metodunu base Creator'a koyma fikrini AI önermedi,

&#x20; ben ekledim. Böylece tüm Creator'lar gönderim mantığını miras alıyor.



\---



\## 4. AI'ın eksik veya yanlış önerdiği şeyler



\- AI başta Singleton'ı da bu fazda uygulamam gerektiğini ima etti.

&#x20; Ancak Singleton bir Creational örüntü olsa da şu an gerçek bir

&#x20; ihtiyaç yok — erken optimizasyon olur. Uygulamadım.



\- AI'ın önerdiği kod yapısında type hint kullanılmamıştı.

&#x20; Ben tüm metodlara type hint ekledim, okunabilirlik arttı.



\---



\## 5. AI olmadan bu faz ne kadar sürerdi?



Muhtemelen 2-3 saat daha uzun sürerdi. Hangi örüntünün uygun olduğunu

araştırmak ve karar vermek zaman alırdı. AI bu kararı hızlandırdı

ama kodu kendim yazdım ve her satırı anladığımdan eminim.

