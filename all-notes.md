# ŞİFRELEME

**ASİMETRİK ŞİFRELEME**

- Her kullanıcının public ve private anahtarı var.
- Biri diğerine veri şifrelerken diğerinin public keyini kullanarak şifreliyor. 
- Gelen veriyi ise herbir kullanıcı kendi private anahtarı ile çözebiliyor.
- Private anahtarlar sayesinde şifrelere ulaşılamıyor.

**SİMETRİK ŞİFRELEME**

- Şifreleme ve çözme için aynı key kullanılır.
- Public key şifrelemesinden daha hızlı.
- Anahtarların çok iyi korunması gerekli.
- Anahtar paylaşımlarında güvenli bir kanal kullanılmalı.


**AES ŞİFRELEME YÖNTEMİ**

Simetrik şifreleme yöntemini kullanır.(Gönderici ve alıcı aynı anahtara sahip.)

128 , 192, 256 bit anahtar çeşidi bulunur.192 ve 256 bit anahtarlar çok gizli bilgiler için kullanılır.

Aes 4x4 state matrisi üzerinde çalışır.

    Şifreleme algoritması genel olarak 4 temel işlemden oluşmaktadır.
      - Subbytes ,byte değiştirir
      - Shiftrows ,satırları kaydırır 
      - Mixcolumns , sütunları kaydırır
      - AddRoundKey , her bir roundda anahtar ekler .
  
- Mesajı bloklara bölüyor ve o blocklar üzerinden şifreleme yapıyor (block cipher).

- Her roundda yeni bir anahtar üretilir ve o anahtar o roundda kullanılır.

- 128 bit anahtar için 10 round yapılır.

- Bu işlemler sonrası mesaj şifrelenmiş olur . 

Algoritma detayları için :

https://github.com/ricmoo/pyaes/tree/master/pyaes
https://www.youtube.com/watch?v=gP4PqVGudtg
http://bilgisayarkavramlari.sadievrenseker.com/2009/06/03/aes-ve-rijndeal-sifreleme/
https://github.com/ricmoo/pyaes/tree/master/pyaes

**Avantajları**

- Hızlı
- Güvenli (Anahtarın brute-force ile kırılması 128 bitlik anahtar için yaklaşık 2^128 mertebesinde işlem gerektiriyor , günümüzde evrenin yaşından daha uzun bir süre  )
- Donanım ve yazılıma uygun
- 

**Dezavanatajları**



**RSA ŞİFRELEME YÖNTEMİ**

- Asimetrik şifreleme yöntemini kullanır.(Gönderici ve alıcı ayrı ayrı kendilerie ait public ve private anahtarlara sahip)
- Metni şifrelerken çarpanlara ayırma metodundan yararlanır.
- Hem göndericinin hem alıcının public ve private keyleri var.
- Public ve private keyler birbirlerine matematiksel olarak bağlılar.
- Gönderici ile alıcı birbirlerinin public keylerini birbirlerine gönderirler.
- Gönderici alıcının public keyi ile şifreleme yapar.
- Alıcı public key ile şifrelenmiş mesajı kendi private keyi ile çözer.Alıcının private keyi olmadan şifrelenmiş mesaj çözülemez.
- Böylece simetrik şifrelemedeki anahtar paylaşmadan dolayı olabilecek zaafiyet önlenmiş olur.

Algoritması : https://www.geeksforgeeks.org/rsa-algorithm-cryptography/ or http://bilgisayarkavramlari.sadievrenseker.com/2008/03/19/rsa/

**Dezavantajları**

- Her kullanıcı private anahtarı ile gizlenmiş metinleri tek bir anahtarla çözebilir , bu durum anahtar kaybolması veya başka birinin eline geçmesi durumunda sıkıntılara yol açar.
- n kullanıcı için n-1 şifre gerekli
