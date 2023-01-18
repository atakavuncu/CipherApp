# CipherApp
 CipherApp uygulaması, şifreleme ve şifre çözme işlemleri için kullanılan bir USB bellek uygulamasıdır. Temel yapısı itibariyle, cihazda yer alan bir metin belgesini (.txt) şifreleyebilen veya CipherApp kullanılarak şifrelenmiş metin belgesini çözebilen bir güvenlik uygulamasıdır. Bu uygulama USB belleklerin içine kurularak aslında USB belleği, şifrelenmiş metin belgesini okumak için gerekli bir anahtar haline getiriyor.


## Ekran Görüntüleri

![Uygulama Ekran Görüntüsü](https://i.hizliresim.com/9mdawgn.png)     ![Uygulama Ekran Görüntüsü](https://i.hizliresim.com/9ohv5x4.png)     ![Uygulama Ekran Görüntüsü](https://i.hizliresim.com/aa85mxu.png)


## Kullanımı
Uygulama arayüzünde üç adet buton bulunmaktadır. “Dosya Seç” butonu kullanıcıya “.txt” uzantılı dosyaları seçtirmek üzerine tasarlanmıştır. “Şifrele” butonu seçilen dosyayı şifrelemek için kullanılır. Şifreleme fonksiyonu, Fernet kütüphanesi içerisinde bulunan 128-bit anahtarlı AES algoritmasının CBC modu kullanılarak oluşturulmuştur. Şifreleme anahtarı olarak seçilen dosyanın oluşturulma tarihi kullanılmaktadır. Arayüzde yer alan “Şifre Çöz” butonu ise şifrelenen metin belgesinin aynı algoritmalar kullanılarak orijinal haline getirilmesini sağlamaktadır.


## Kullanılan Kütüphaneler
- os
- base64
- Fernet
- hashes
- PBKDF2HMAC
- tkinter
