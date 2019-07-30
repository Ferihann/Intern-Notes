**UNSUPERVISED LEARNING ALGORITHMS**

**CLUSTERING** 

  Clustering ( Kümeleme ) bir veri setinde benzer özellikler gösteren verilerin gruplara ayrılmasına denir. Aynı küme içinde   benzerlikler fazla, kümeler arası benzerlikler azdır. 
  
Kümeleme algoritmaları temelde ikiye ayrılır:
    - Hiyerarşik 
    - Hiyerarşik Olmayan

Euclid, Manhattan, ve Minkowski algoritmaları Uzaklığı hesaplamalarda kullanılır.


**Non Hiyerarchical Clustering**

- **Centroid-based Clustering:**

   - ![](https://github.com/Ferihann/Intern-Notes/blob/master/screenshots/Screenshot%20from%202019-07-30%2015-41-47.png)

   - K-means algoritması sıkça kullanılan centroid-based algoritmasıdır.Centroid-based algoritmalar effektiftir , etkilidir      ve temel kümeleme algoritmasıdır.Fakat outliers ve initial condition(ilk başlangıç noktasını seçme) konusunda hassastır.

- **Density-based Clustering**

  - ![](https://github.com/Ferihann/Intern-Notes/blob/master/screenshots/Screenshot%20from%202019-07-30%2015-52-00.png)
  
  - Verilerin yoğunlaştığı bölgere göre kümeleme yapar.
  - Fakat outlierları kümeye dahil edemedi.
  - Bu kümeleme , çok boyutlarda ve küme çeşitliliğinin fazla olduğu durumlarda efficient çalışmayabilir.

- **Distribution-based Clustering**

  -![](https://github.com/Ferihann/Intern-Notes/blob/master/screenshots/Screenshot%20from%202019-07-30%2016-11-41.png)
  - Bu kümeleme algoritması Gaussian distribution 'dan faydalanır. Figürde kümeler 3 gauss distributiona ayrılmıştır.
  
**K-Means Algorithm**

- K sayısı küme sayısını belirtir.K değerini kendi hepsalayan X-Means adında başka bir algoritmada vardır.
- k parametresi seçilir.
- Küme merkezi seçilir.
- Verilen küme merkezlerine olan uzaklıkları hesaplanır. İncelenen veri en yakın kümeye dahil edilir.
- İncelenen verilerin dahil edilmesiyle yeni küme merkezleri hesaplanır.
- Yapılan analizler sonucunda küme merkezlerinde herhangi bir değişiklik olmuyor ise işlem sonlandırılır.

       K-Means algoritmasındaki başlangıç merkez noktalarının rastgele atanması sorunlara yol açabilmektedir. 
       Başlangıç noktalarını daha iyi seçebilmek için 2007 yılında David Arthur ve Sergei Vassilvitskii K-Means
       algoritmasının bir varyasyonu olan K-Means++ algoritmasını geliştirilmiştir.
       K-Means++’a göre rastgele başlangıç noktası seçildikten sonra diğer tüm veriler ile arasındaki mesafe 
       hesaplanır. Bu mesafenin karesi alınıp belli hesaplamalar yaparak yeni başlangıç noktaları seçilir. 
       Bu işlemin kamaşıklık analizi O(log k)’dır.
 **k-medoids:** 
K-means algoritması gürültülü verilere duyarlıdır. Yani gürültüde kümelere dahil olmaktadır. Bu dez avantajı gidermek için k-medoids algoritması 1987 yılında Kaufman ve Rousseeuw tarafından geliştirilmiştir. k-medoids algoritması kümenin merkez noktasındaki elemanı yeni küme merkezi olarak belirlemektedir.

**Hiyerarchical Clustering**

![](https://github.com/Ferihann/Intern-Notes/blob/master/screenshots/Screenshot%20from%202019-07-30%2015-37-56.png)

- Agglomerative ( Parçadan bütüne ) ve Divisive ( Bütünden parçaya ) olarak iki farklı varyasyonu vardır.
Temelde iki yaklaşıma sahiptir: birleştirici (agglomerative) ve ayrıştırıcı / bölücü (divisive) (Rafsanjani ve diğ., 2012). Birleştirici hiyerarşik kümelemede, her bir örnek başlangıçta ayrı bir küme olarak kabul edilir, her adımda kümelerin
birbirlerine uzaklıkları hesaplanır ve en yakın iki küme birleştirilerek bir üst küme oluşturulur. Böylece, 
her adımda küme sayısı bir azaltılır ve işlem bütün örneklerin dahil olduğu tek bir büyük küme
oluşuncaya kadar devam ettirilir. 

- Bu süreç, dendogram olarak adlandırılan hiyerarşik bir ağaç
diyagramı ile görselleştirilebilmektedir. Ayrıştırıcı hiyerarşik kümelemede ise, tam tersi bir biçimde, tüm
örnekler başlangıçta tek bir küme olarak kabul edilir ve her aşamada benzer olmayan gözlemler
belirlenerek daha küçük kümeler oluşturulur. Bu süreç, her gözlem tek başına küme oluşturuncaya
kadar sürdürülür. 
- Dendogram :Öbek ağacı

![](https://github.com/Ferihann/Intern-Notes/blob/master/screenshots/Screenshot%20from%202019-07-30%2015-33-33.png)


















Kaynak :

https://developers.google.com/machine-learning/clustering/clustering-algorithms

https://medium.com/@k.ulgen90/python-ile-k%C3%BCmeleme-algoritmalar%C4%B1-makine-%C3%B6%C4%9Frenimi-b%C3%B6l%C3%BCm-8-8204ffa702f2

https://dergipark.org.tr/download/article-file/664873
