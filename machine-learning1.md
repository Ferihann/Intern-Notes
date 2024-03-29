**Makine Öğrenmesi Nedir ?**

  Matematiksel ve istatistikler yöntemler kullanarak mevcut verilerden çıkarım yapan bilinmeyene dair tahminlerde bulunan yöntem 
paradigmasıdır.

- **Supervised Learning(Gözetimli Öğrenme)**

  Eğitim verileri üzerinden bir fonksiyon üreten bir makine öğrenmesi tekniğidir. Başka bir deyişle, bu öğrenme tekniğinde girdilerle (işaretlenmiş veri –  labelled data) ile istenen çıktılar arasında eşleme yapan bir fonksiyon üretir. Eğitim verisi hem girdilerden hem çıktılardan oluşur. Fonksiyon, sınıflandırma (classifiction) veya eğri uydurma (regression) algoritmaları ile belirlenebilir.

- **Unsupervised Learning**

Bu yöntemde işaretlenmemiş (unlabelled) veri üzerinden bilinmeyen bir yapıyı tahmin etmek için bir fonksiyon kullanan makine öğrenmesi tekniğidir. Burada girdi verisinin hangi sınıfa ait olduğu belirsizdir.


- **Reinforcement Learning**

    - Makine Öğrenmesi’nde genellikle Markov Karar Süreci adı verilen bir model kullanılıyor. 
  Bu model yapay zekânın önceden bilgilendirilmesine ve yönlendirilmesine dayalı. 
  Kesin bir neden sonuç ilişkisi var. 
    - Pekiştirmeli Öğrenme süreciyse ön bilgi yerine gözlem ve seçimde bulunmak üzerine kurulu. 
  Neden sonuç ilişkisinin nasıl kurulduğu bilgisi yapay zekâya verilmiyor (ya da çok az veriliyor), 
  yapay zekâ kendisi öğreniyor.


![Alt text](https://github.com/Ferihann/Intern-Notes/blob/master/screenshots/Screenshot%20from%202019-07-28%2014-16-04.png)

**Makine Öğrenmesi Algoritmaları**

![Alt text](https://github.com/Ferihann/Intern-Notes/blob/master/screenshots/Screenshot%20from%202019-07-28%2016-43-24.png)

**SUPERVISED LEARNING ALGORITHMS**

- **Lineer Regression**

   ![Alt text](https://github.com/Ferihann/Intern-Notes/blob/master/screenshots/Screenshot%20from%202019-07-28%2019-14-34.png)

  - **Regression line :** Noktaların tamamına en yakın geçen doğru

  Regression ile gerçek değere yakın output tahmin edilmeye çalışılır.
  
 Ordinary least sequeres : 
 
 Yöntem, her nokta ile çizginin korelasyonlu (en yakın) noktası arasındaki mesafelerin karelerinin toplamını dikkate alarak minimum sonucu bulana kadar sürekli olarak birçok çizgi oluşturuyor.

  - **Regression function :**   
     ![Alt text](https://github.com/Ferihann/Intern-Notes/blob/master/screenshots/Screenshot%20from%202019-07-28%2016-56-11.png)

  - **Loss Function(Cost Function , Objective Function) :**

    - ![Alt text](https://github.com/Ferihann/Intern-Notes/blob/master/screenshots/Screenshot%20from%202019-07-28%2018-08-32.png)

    - Hypothesis : Bizim regresyon fonksiyonumuz
    - Cost Function : Hipotezimizin ne kadar doğru sonuç verdiğini hesaplar.

    - Amacımız cost fonksiyonunun değerini en aza indirgemek bunun için de gradient descend algoritmasını kullanacağız.

 **Linear Regression with Multiple Variable**

 - **Feature Scaling** , fonksiyonda kullanacağımız featurelar benzer aralıklarda olmalı .Bunu yaparken de mean normalization
    yönteminden faydalanabiliriz .
    
    - Mean Normalization : 
    
      ![](https://github.com/Ferihann/Intern-Notes/blob/master/screenshots/Screenshot%20from%202019-07-28%2019-33-31.png)
      
    - **Gradient Descend Algorithm** 

      - ![](https://github.com/Ferihann/Intern-Notes/blob/master/screenshots/Screenshot%20from%202019-07-28%2018-15-20.png)
   
      - Cost fonksiyonunun theataya göre kısmi türevi alınır.Burdaki amaç türev ile adım adım fonksiyonun en küçük noktasını bulmaya 
  çalışmaktır.θ'yı konverge olana kadar günceller.(Minimumu bulur.)
      - Fonksiyon konverge ettiği noktada en küçük değerini alır.
      - Alpha (α) : öğrenme oranı , α çok küçük olursa θ fonksiyonun başlangıç noktasından yavaşça iner. Eğer α çok büyük olursa da 
  θ hiç konverge olmayabilir . Bu durumda algoritma başarısız olmuş olur.

      - ![](https://github.com/Ferihann/Intern-Notes/blob/master/screenshots/Screenshot%20from%202019-07-28%2018-23-40.png)

      - ![](https://github.com/Ferihann/Intern-Notes/blob/master/screenshots/Screenshot%20from%202019-07-28%2019-17-53.png)


- Birden fazla tahminleyici (predictor) değişken kullanarak tahminlemeye çalışılır.
- **Polynomial Regression:**  Veriler arası ilişki her zaman doğrusal olmayabilir. Optimum ilişkiyi bulmak için bir eğri gerekebilir. Tıpkı polinom fonksiyonlarında olduğu gibi bu yöntemde de bir terimin karesi veya küpü(veya terimin üssü herhangi bir sayı olabilir) alınarak doğrusal olmayan bir regresyon modeli oluşturulmak istenebilir. Bu gibi durumlarda kullanılabilen bir algoritmadır.









Kaynakça : 

https://www.e-adys.com/makine_ogrenmesi/hangisini-secmeliyim-supervised-ve-unsupervised-learning/

https://www.kizgibikodla.com/news/yeni-baslayanlar-icin-adan-zye-makine-ogrenmesi/

https://medium.com/@fahrettinf/4-1-yapay-zeka-algoritmalar%C4%B1-fd64b8080748

http://firatdemirel.com/makine-ogrenmesi/

https://medium.com/deep-learning-turkiye/makine-%C3%B6%C4%9Frenmesi-e%C4%9Flencelidir-b9d50aad3a62

https://medium.com/@wintermute_/reinforcement-learning-peki%C5%9Ftirmeli-%C3%B6%C4%9Frenme-i%CC%87nsan-beyniyle-aradaki-fark-kapan%C4%B1rken-c0d0a6f7c2e8

https://d3c33hcgiwev3.cloudfront.net/_ec21cea314b2ac7d9e627706501b5baa_Lecture2.pdf?Expires=1564444800&Signature=U7Ox8KnX1CveFHH9bUgnMVT4WfyA7-1K7aP3WdbP9iJaf8fj8tT3L3iL84gnnf~5CGy0z5cfxgvLyoK5HZb0tuzledoIuavNsto3A8mINU-6eqvIhIDv0cEeFnvXpv~sj~jFXCQoG9och0d8YTbjl0DLNuOJwp~Lr6NOVSLk66M_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A



