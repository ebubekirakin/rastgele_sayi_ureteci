import time  # Sadece başlangıç "tohumunu" (seed) zamanla almak için kullanacağız.

class BenimRastgeleUretecim:
    def __init__(self, tohum=None):
        """
        Üreteci başlatan fonksiyon.
        Eğer bir 'tohum' (seed) verilmezse, o anki zamanı kullanırız.
        Böylece program her çalıştığında farklı sayılar üretir.
        """
        if tohum is None:
            # Şu anki zamanı milisaniye cinsinden alıp tam sayı yapıyoruz
            self.durum = int(time.time() * 1000)
        else:
            self.durum = tohum
            
        # --- ALGORİTMA SABİTLERİ ---
        self.a = 1664525      # Çarpan
        self.c = 1013904223   # Artış
        self.m = 2**32        # Modül

    def rastgele_sayi_uret(self):
        """
        0 ile 1 arasında (0.0 - 1.0) ondalıklı sayı üretir.
        """
        self.durum = (self.a * self.durum + self.c) % self.m
        return self.durum / self.m

    def aralikta_uret(self, min_deger, max_deger):
        """
        İstediğimiz iki sayı arasında rastgele tam sayı üretir.
        """
        ham_oran = self.rastgele_sayi_uret()
        hedef_aralik = max_deger - min_deger + 1
        sonuc = min_deger + int(ham_oran * hedef_aralik)
        return sonuc

# --- KULLANIM TESTİ ---

# 1. Sınıfımızı başlatalım
uretec = BenimRastgeleUretecim() 

print("--- Otomatik Test (Sistem 0-1 arası üretiyor) ---")
for i in range(3):
    print(f"{i+1}. Sayı: {uretec.rastgele_sayi_uret()}")

# --- YENİ EKLENEN KISIM: KULLANICI GİRİŞİ ---
print("\n" + "="*40)
print("   KULLANICI KONTROLLÜ ÜRETİM MODU")
print("="*40)

try:
    # Kullanıcıdan verileri alıyoruz (input string döndürür, int ile sayıya çeviriyoruz)
    k_min = int(input("1. Alt sınırı giriniz (Örn: 50): "))
    k_max = int(input("2. Üst sınırı giriniz (Örn: 100): "))
    k_adet = int(input("3. Kaç adet sayı üretilsin?: "))

    print(f"\n>> {k_min} ile {k_max} arasında {k_adet} adet sayı üretiliyor:\n")

    for i in range(k_adet):
        # Kullanıcının girdiği değişkenleri fonksiyona yolluyoruz
        sansli_sayi = uretec.aralikta_uret(k_min, k_max)
        print(f"{i+1}. Sonuç: {sansli_sayi}")

except ValueError:
    # Eğer kullanıcı sayı yerine harf girerse program çökmesin diye bu uyarıyı verir.
    print("\nHATA: Lütfen sadece sayısal değerler giriniz!")