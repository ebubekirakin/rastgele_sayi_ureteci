import datetime

class SaniyeBazliRNG:
    def __init__(self):
        zaman = datetime.datetime.now()
        self.mevcut_sayi = zaman.second
        if self.mevcut_sayi == 0: self.mevcut_sayi = 1
        print(f"Sistem Başlatıldı. Tohum (Saniye): {self.mevcut_sayi}")

    def collatz_adim(self, sayi):
        if sayi % 2 == 0:
            return sayi // 2
        else:
            return 3 * sayi + 1

    def uret(self, min_deger, max_deger):
        olusan_sayi = 0
        analiz_metni = "   --- İŞLEM ADIMLARI ---\n"
        
        for i in range(10):
            eski_hal = self.mevcut_sayi 
            
            # 1. Collatz Motoru
            self.mevcut_sayi = self.collatz_adim(self.mevcut_sayi)
            
            # 2. Döngü Kırıcı (+13 Eklemesi)
            if self.mevcut_sayi <= 4:
                analiz_metni += f"      * (Sayı {self.mevcut_sayi} oldu, döngüden kurtarmak için +13 eklendi)\n"
                self.mevcut_sayi += 13 
            
            # 3. Basamak Koparma
            son_basamak = self.mevcut_sayi % 10
            
            # 4. Yapıştırma
            olusan_sayi = (olusan_sayi * 10) + son_basamak
            
            analiz_metni += f"      {i+1}. Adım: {eski_hal} -> Collatz -> {self.mevcut_sayi} oldu. (Alınan Rakam: {son_basamak})\n"

        # SONUÇ HESAPLAMA
        aralik = max_deger - min_deger + 1
        kalan = olusan_sayi % aralik
        sonuc = kalan + min_deger
        
        analiz_metni += f"   ----------------------\n"
        analiz_metni += f"   Oluşan Büyük Sayı: {olusan_sayi}\n"
        analiz_metni += f"   Aralığa Sığdırma : {olusan_sayi} % {aralik} (mod) = {kalan}\n"
        analiz_metni += f"   Sonuç ({kalan} + {min_deger}): {sonuc}"
        
        # --- DÜZELTİLEN KISIM BURASI ---
        # Artık sabit 55 eklemiyoruz!
        # Ürettiğimiz o büyük sayının (olusan_sayi) son iki rakamını alıp ekliyoruz.
        # "olusan_sayi" her tur değiştiği için eklenen sayı da hep değişecek.
        degisken_tekme = (olusan_sayi % 60) + 7 
        self.mevcut_sayi += degisken_tekme
        # -------------------------------
        
        return sonuc, analiz_metni

# --- KULLANIM ---
print("--- DETAYLI COLLATZ ÜRETECİ (FİNAL VERSİYON) ---")

try:
    alt = int(input("En küçük sayı: "))
    ust = int(input("En büyük sayı: "))
    adet = int(input("Kaç adet üretilsin: "))

    rng = SaniyeBazliRNG()
    
    print(f"\nSonuçlar:")
    for i in range(adet):
        sayi, detay = rng.uret(alt, ust)
        print(f"\n>>> {i+1}. ÜRETİLEN SAYI: {sayi}")
        print(detay)
        print("="*40)

except ValueError:
    print("Sadece sayı giriniz.")