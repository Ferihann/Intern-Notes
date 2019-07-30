  
**K-Nearest Neighbour Algorithm** 

KNN algoritmasının adımları:
- İlk olarak k parametresi belirlenir. Bu parametre verilen bir noktaya en yakın komşuların sayısıdır.
- Örneğin: k=2 olsun. Bu durumda en yakın 2 komşuya göre sınıflandırma yapılacaktır.
- Örnek veri setine katılacak olan yeni verinin, mevcut verilere göre uzaklığı tek tek hesaplanır.
- İlgili uzaklılardan en yakın k komşu ele alınır. Öznitelik değerlerine göre k komşu veya komşuların sınıfına atanır.
- Seçilen sınıf, tahmin edilmesi beklenen gözlem değerinin sınıfı olarak kabul edilir. Yani yeni veri etiketlenmiş (label) olur.
- Hem sınıflandırma hem de regresyon için kullanılabilir.
![](https://github.com/Ferihann/Intern-Notes/blob/master/screenshots/Screenshot%20from%202019-07-29%2010-37-09.png)

**Decision Tree**

![](https://github.com/Ferihann/Intern-Notes/blob/master/screenshots/Screenshot%20from%202019-07-29%2010-09-10.png)

- Bir karar ağacı, çok sayıda kayıt içeren bir veri kümesini, bir dizi karar kuralları uygulayarak daha küçük kümelere bölmek için kullanılan bir yapıdır. Yani basit karar verme adımları uygulanarak, 
büyük miktarlardaki kayıtları, çok küçük kayıt gruplarına bölerek kullanılan bir yapıdır.

- **Karar ağacı tipleri**
  - Entropiye dayalı sınıflandırma ağaçları (ID3,
C4.5) 
  - Regresyon ağaçları (CART) olmak üzere iki kategoride birçok algoritma önerilmiştir. 
- **ID3**
  - Entropiden yararlanır .Entropi düzensizliği ifade eder.
  - ![](https://github.com/Ferihann/Intern-Notes/blob/master/Screenshot%20from%202019-07-29%2011-18-16.png)
  - ID3 algoritmasında sistemin genel entropisinin hesaplanmasının ardından her bir özniteliğin entropisi de ayrı ayrı hesaplanır. Hesaplanan entropi değerleri, genel entropiden çıkartılarak; hangi özniteliğin entropi değerini en çok azalttığı tespit edilir.
  - ![](https://github.com/Ferihann/Intern-Notes/blob/master/screenshots/Screenshot%20from%202019-07-29%2011-23-17.png)
  - En fazla kazanç getiren kök düğüm olmaya hak kazanır.
- CART Karar Ağacı :Ağacın temel prensibi herbir düğümde ağacı iki dala ayırmasıdır. 


       OVERFITTING(high variance) : Overfitting probleminde model çalıştığımız veri seti üzerinde harika sonuçlar verir 
       (training error düşük) fakat hiç görmediği yeni veri setleri üzerinde başarısız 
       tahminler yapar. (test error yüksek)
       
       
       UNDERFITTING(high bias) : Diğer bir deyişle eğer modelimizi eğitim (training) veri seti üzerinde çok basit olarak
       kurguladıysak hiç görmediğimiz test verisi üzerinde başarısız tahminler (sallama) 
       yaparız ve gerçek değerle tahmin ettiğimiz değer arasındaki fark çok olur.
       
       
 Bu problemleri nasıl çözebiliriz ?
    
 **Validasyon** : Sınava girmeden önce arşiv sorularının (training data) bir kısmına diyelim ki %20'sine hiç bakmayıp (validation data) sanki gerçekten sınava giriyormuş gibi kendimizi denemeye validasyon metodu diyoruz. Bu methodun 2 sakıncası var.
Bütün veri eğitim sürecinden geçmiyor bir kısmı validasyona ayrılıyor bu senaryoda eksik veri underfitting problemine sebep olabilir.(verideki bazı patternler trendler gözden kaçabilir.)
Eğitimden geçen veri iyi bir örneklem olmayabilir.

  - 2.deney için veri setinin farklı bir yüzde 20'lik kısmını test için yüzde 80'lik kısmını eğitim için ayırıyoruz ve bu prosedürü 3. 4. 5. deneyler için de gerçekleştiriyoruz. Günün sonunda modellerin başarı oranlarının ortalamasını alıyoruz.
  - ![](https://github.com/Ferihann/Intern-Notes/blob/master/screenshots/Screenshot%20from%202019-07-29%2017-00-06.png)
  
**Naïve Bayes**

![](https://github.com/Ferihann/Intern-Notes/blob/master/screenshots/Screenshot%20from%202019-07-29%2010-10-02.png)

![](https://github.com/Ferihann/Intern-Notes/blob/master/screenshots/Screenshot%20from%202019-07-29%2014-49-16.png)

- Yeni gelen verinin hangi gruba dahil olacağını belirlemek için bayes teoremi ile verimizin herbir grup ile ayrı ayrı benzerlik 
olasılığı hesaplanır ve benzerlik oranı en büyük çıkan gruba dahil edilir.
- Sınıflandırmada kullanılır.

**Support Vector Machines**

- Temel olarak iki sınıfa ait verileri birbirinden en uygun şekilde ayırmak için kullanılır. 
Bunun için karar sınırları yada diğer bir ifadeyle hiper düzlemler belirlenir.
      
      1)Support Vector Machine Logistic Regression ile benzer bir sınıflandırma algoritmasıdır.
      Her ikisi de iki sınıfı ayıran en iyi çizgiyi bulmaya çalışırlar.
      2)Algoritma çizilecek doğrunun iki sınıfında elemanlarına en uzak yerden geçicek şekilde
      ayarlanmasını sağlar. 
      3)Hiçbir parametre almayan ( nonparametric ) bir sınıflayıcıdır. 
      4)SVM aynı zamanda doğrusal ve doğrusal olmayan verileride sınıflandırabilir ancak 
      genellikle verileri doğrusal olarak sınıflandırmaya çalışır.



- ![](https://github.com/Ferihann/Intern-Notes/blob/master/screenshots/Screenshot%20from%202019-07-29%2010-10-20.png)
- SVM günümüzde yüz tanıma sistemlerinden, ses analizine kadar birçok sınıflandırma probleminde kullanılmaktadırlar.
- ![](https://github.com/Ferihann/Intern-Notes/blob/master/screenshots/Screenshot%20from%202019-07-29%2015-00-47.png)

Confusion Matris :
  - Karmaşıklık matrisi test verisi ile tahmin değerlerinin karşılaştırmamızı ve yaptığımız modelimizin 
  performansını ölçmemizi sağlar.Başarı oranını ölçmeyi sağlar.
- True Positive (Doğru Pozitif ) : Olumlu tahmin ettiniz ve bu doğru .
- True Negative (Doğru Negatif ): Olumsuz tahmin ettiniz ve bu doğru.
- False Positive (Yanlış Olumlu) : Olumlu tahmin ettiniz ve bu yanlış.
- False Negative ( Yanlış Olumsuz ) : Olumsuz tahmin ettiniz ve bu yanlış.

      Accuracy : ( TP + FN )/toplam
      Error Rate : (FN + FP)/tplam
      True pozitive rate(Sensivity) :  TP/(FN + TP)
      True negative rate(Specifity) : TN/(TN + FP)
      Precision : TP / (FP + TP)
      Prevalance : (FN + TP)/ Toplam

**Random Forest Algorithm**

![](https://github.com/Ferihann/Intern-Notes/blob/master/screenshots/Screenshot%20from%202019-07-30%2011-21-39.png)

-  Karar ağaçlarının en büyük problemlerinden biri aşırı öğrenme-veriyi ezberlemedir (overfitting). Rassal orman modeli bu problemi çözmek için hem veri setinden hem de öznitelik setinden rassal olarak 10'larca 100'lerce farklı alt-setler seçiyor ve bunları eğitiyor. 

-  Bu yöntemle 100'lerce karar ağacı oluşturuluyor ve her bir karar ağacı bireysel olarak tahminde bulunuyor. Günün sonunda problemimiz regresyonsa karar ağaçlarının tahminlerinin ortalamasını problemimiz sınıflandırmaysa tahminler arasında en çok oy alanı seçiyoruz.

- Rassal orman modelinde farklı veri setleri üzerinde eğitim gerçekleştiği için varyans, diğer bir deyişle karar ağaçlarının en büyük problemlerinden olan overfitting azalır. Ayrıca bootstrap yöntemiyle oluşturduğumuz alt-veri kümelerinde outlier bulunma şansını da düşürmüş oluruz.

- k tane örnek eğitim setinden rasgele seçilir.

- k tane Decision Tree oluşturulur ve her node için:

- Rasgele d tane özellik  yenisiyle değiştirilmeden seçilir.
 En iyi bölünmeyi sağlayan özelliği kullanarak düğüm bölünür. Örneğin, bilgi kazancını en üst düzeye çıkararak.(information gain)
- 1.ve 2. adımlar k defa tekrar edilir.

- Elde edilen sonuçlar birleştirerek, çoğunlukta olan tahmin kazanır.












Kaynakça : 

https://medium.com/data-science-tr/overfitting-underfitting-cross-validation-b47dfda0cf4e

https://medium.com/@ekrem.hatipoglu/machine-learning-classification-logistic-regression-part-8-b77d2a61aae1

https://medium.com/@k.ulgen90/makine-%C3%B6%C4%9Frenimi-b%C3%B6l%C3%BCm-4-destek-vekt%C3%B6r-makineleri-2f8010824054

https://medium.com/deep-learning-turkiye/makine-%C3%B6%C4%9Frenmesi-algoritmalar%C4%B1-id3-algoritmas%C4%B1-71983b3e3b77

http://bmb.cu.edu.tr/uorhan/DersNotu/Ders03.pdf

https://medium.com/@k.ulgen90/makine-%C3%B6%C4%9Frenimi-b%C3%B6l%C3%BCm-2-6d6d120a18e1

https://medium.com/@k.ulgen90/makine-%C3%B6%C4%9Frenimi-b%C3%B6l%C3%BCm-5-karar-a%C4%9Fa%C3%A7lar%C4%B1-c90bd7593010

https://medium.com/data-science-tr/overfitting-underfitting-cross-validation-b47dfda0cf4e
