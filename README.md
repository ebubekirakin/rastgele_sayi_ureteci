# Collatz Tabanlı Sözde Rastgele Sayı Üreteci (PRNG)

Bu proje, ünlü bir matematik problemi olan Collatz Sanısı (3x+1 Problemi) üzerine kurgulanmış özgün bir Sözde Rastgele Sayı Üretim algoritmasıdır.

Standart `random` kütüphanelerinin arkasındaki karmaşık bit işlemlerini kullanmak yerine; matematiksel kaos, basamak analizi ve dinamik mutasyon yöntemlerini harmanlayarak tahmin edilmesi zor sayı dizileri üretmeyi hedefler.

##  Projenin Amacı

Bilgisayar bilimlerinde rastgelelik genellikle deterministik algoritmalarla (PRNG) sağlanır. Bu projede amacım, bit tabanlı (XOR/Shift) klasik yöntemler yerine, sayısal tabanlı (Number Theoretic) bir yaklaşımla rastgelelik elde etmektir. Algoritma, Collatz dizilerinin kaotik yapısını bir "karıştırıcı" (mixer) olarak kullanır.

##  Algoritma Mantığı (Nasıl Çalışıyor?)

Algoritma 5 temel aşamadan oluşur:

### 1. Zaman Tabanlı Tohumlama 

Sistemin başlangıç noktası (`seed`), bilgisayarın o anki saniyesinden alınır. Bu, her çalışma anında farklı bir başlangıç noktası (Initial State) sağlar.

### 2. Collatz Motoru 

Sayılara klasik Collatz kuralları uygulanır:

* Sayı Çift ise: x/2
* Sayı Tek ise: 3x+1

### 3. Döngü Kırıcı 

Collatz dizileri doğası gereği 4-2-1 döngüsüne girer. Algoritmam, sayı 4 veya altına düştüğünde sisteme **Asal Sayı (13)** ekleyerek döngüyü kırar ve üretimin devamlılığını sağlar.

### 4. Basamak Yapıştırma 

Standart yöntemlerin aksine, bu algoritma sayının tamamını değil, her işlem adımında oluşan sayının birler basamağını (`mod 10`) alır. Bu basamaklar ardışık olarak birleştirilerek (Concatenation) devasa bir ham sayı inşa edilir.

### 5. Dinamik Mutasyon 

Peş peşe sayı üretiminde aynı tohumun tekrarlanmaması için, üretilen son sayının yapısına göre belirlenen değişken bir değer (`offset`), bir sonraki turun başlangıç tohumuna eklenir. Bu, "Kapalı Yörünge" (Closed Orbit) sorununu kesin olarak çözer.

## 🛠️ Kurulum ve Kullanım

Proje saf Python ile yazılmıştır, herhangi bir harici kütüphane gerektirmez.

1. Repoyu klonlayın veya dosyayı indirin.
2. Terminali açın ve kodu çalıştırın:

```bash
python main.py

```

3. Program sizden 3 parametre isteyecektir:
* **Alt Sınır:** (Örn: 1)
* **Üst Sınır:** (Örn: 100)
* **Adet:** (Kaç sayı üretileceği)



## Örnek Çıktı

Program çalıştığında, her sayının nasıl türetildiğini gösteren şeffaf bir "İşlem Adımları" raporu sunar:

```text
>>> 1. ÜRETİLEN SAYI: 87
   --- İŞLEM ADIMLARI ---
      1. Adım: 42 -> Collatz -> 21 oldu. (Alınan Rakam: 1)
      2. Adım: 21 -> Collatz -> 64 oldu. (Alınan Rakam: 4)
      ...
      * (Sayı 2 oldu, döngüden kurtarmak için +13 eklendi)
      ...
   ----------------------
   Oluşan Büyük Sayı: 1426845630
   Aralığa Sığdırma : 1426845630 % 100 (mod) = 86
   Sonuç (86 + 1): 87

```

## Akış Diyagramı
<img width="448" height="1000" alt="image" src="https://github.com/user-attachments/assets/cf41afab-718b-45cd-884e-c9dabc4698ce" />




Geliştirici: Ebubekir AKIN   (230541132)
