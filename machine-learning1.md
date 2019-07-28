**Makine Öğrenmesi Nedir ?**

  Matematiksel ve istatistikler yöntemler kullanarak mevcut verilerden çıkarım yapan bilinmeyene dair tahminlerde bulunan yöntem 
paradigmasıdır.

- **Supervised Learning(Gözetimli Öğrenme)**

Problemdeki her bir datanın kendine ait özelliklerini biliyoruz ve buradan yola çıkarak geriye doğru bir mantık oluşturmaya 
çalışıyoruz. Her bir dataya ait veriler ile öğrenme algoritmamız besliyoruz ve algoritma bu veriler arasında nasıl 
bir matematik gerektiğini çözmeye çalışıyor.

    Örnek: 2  4  5 = 3
           5  2  8 = 2 aralarındaki matematik sembollerini bulmaya çalışmak
        
`Supervised Learning de regression algoritmaları kullanılır.`

- **Unsupervised Learning**

Elimizde özellik dataları var fakat bu özellik datalarının neye ait olduğu belli değil.

    Örnek: Biri size bir kağıtta sayı listesi veriyor ve bu sayıların ne ifade ettiğini bilmiyorum ama belki 
    sen burada bir düzen veya grup bulabilirsin.
    
Unsupervised Learningde classification algoritmaları kullanılır.


- **Reinforcement Learning**

    - Makine Öğrenmesi’nde genellikle Markov Karar Süreci adı verilen bir model kullanılıyor. 
  Bu model yapay zekânın önceden bilgilendirilmesine ve yönlendirilmesine dayalı. 
  Kesin bir neden sonuç ilişkisi var. 
    - Pekiştirmeli Öğrenme süreciyse ön bilgi yerine gözlem ve seçimde bulunmak üzerine kurulu. 
  Neden sonuç ilişkisinin nasıl kurulduğu bilgisi yapay zekâya verilmiyor (ya da çok az veriliyor), 
  yapay zekâ kendisi öğreniyor.


![Alt text](https://github.com/Ferihann/Intern-Notes/blob/master/Screenshot%20from%202019-07-28%2014-16-04.png)

**Makine Öğrenmesi Algoritmaları**

![Alt text](https://github.com/Ferihann/Intern-Notes/blob/master/Screenshot%20from%202019-07-28%2016-43-24.png)

- **Lineer Regression**

   ![Alt text](https://github.com/Ferihann/Intern-Notes/blob/master/Screenshot%20from%202019-07-28%2019-14-34.png)

  - **Regression line :** Noktaların tamamına en yakın geçen doğru

  Regression ile gerçek değere yakın output tahmin edilmeye çalışılır.

  - **Regression function :**   
     ![Alt text](https://github.com/Ferihann/Intern-Notes/blob/master/Screenshot%20from%202019-07-28%2016-56-11.png)

  - **Loss Function(Cost Function , Objective Function) :**

    - ![Alt text](https://github.com/Ferihann/Intern-Notes/blob/master/Screenshot%20from%202019-07-28%2018-08-32.png)

    - Hypothesis : Bizim regresyon fonksiyonumuz
    - Cost Function : Hipotezimizin ne kadar doğru sonuç verdiğini hesaplar.

    - Amacımız cost fonksiyonunun değerini en aza indirgemek bunun için de gradient descend algoritmasını kullanacağız.

 












Kaynakça : 

https://medium.com/@fahrettinf/4-1-yapay-zeka-algoritmalar%C4%B1-fd64b8080748

http://firatdemirel.com/makine-ogrenmesi/

https://medium.com/deep-learning-turkiye/makine-%C3%B6%C4%9Frenmesi-e%C4%9Flencelidir-b9d50aad3a62

https://medium.com/@wintermute_/reinforcement-learning-peki%C5%9Ftirmeli-%C3%B6%C4%9Frenme-i%CC%87nsan-beyniyle-aradaki-fark-kapan%C4%B1rken-c0d0a6f7c2e8

https://d3c33hcgiwev3.cloudfront.net/_ec21cea314b2ac7d9e627706501b5baa_Lecture2.pdf?Expires=1564444800&Signature=U7Ox8KnX1CveFHH9bUgnMVT4WfyA7-1K7aP3WdbP9iJaf8fj8tT3L3iL84gnnf~5CGy0z5cfxgvLyoK5HZb0tuzledoIuavNsto3A8mINU-6eqvIhIDv0cEeFnvXpv~sj~jFXCQoG9och0d8YTbjl0DLNuOJwp~Lr6NOVSLk66M_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A



