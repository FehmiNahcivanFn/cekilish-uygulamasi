"""
╔══════════════════════════════════════════╗
║         ÇEKİLİŞ UYGULAMASI              ║
║  Kullanıcı listesi yönetimi ve rastgele  ║
║  çekiliş yapabilen konsol uygulaması.    ║
║  Geliştirici: Fehmi Nahcivan             ║
╚══════════════════════════════════════════╝
"""

import random   # Rastgele seçim ve karıştırma işlemleri için
import time     # Çekiliş animasyonunda bekleme süresi için
import os       # Ekran temizleme ve dosya varlığı kontrolü için

# Kullanıcı verilerinin kaydedileceği dosya adı
DOSYA_ADI = "kullanicilar.txt"

# ──────────────────────────────────────────
# Yardımcı Fonksiyonlar
# ──────────────────────────────────────────

def ekranı_temizle():
    """İşletim sistemine göre terminali temizler (Windows: cls, Linux/Mac: clear)."""
    os.system("cls" if os.name == "nt" else "clear")

def başlık_yaz(metin):
    """Verilen metni dekoratif bir başlık çerçevesi içinde ekrana yazdırır."""
    print("\n" + "═" * 40)
    print(f"  {metin}")
    print("═" * 40)

def devam_et():
    """Kullanıcının Enter'a basmasını bekleyerek akışı duraklatır."""
    input("\n  ↵  Devam etmek için Enter'a basınız...")

def kaydet(kullanıcılar):
    """Kullanıcı listesini dosyaya yazar. Her kullanıcı ayrı bir satıra kaydedilir."""
    with open(DOSYA_ADI, "w", encoding="utf-8") as f:
        for k in kullanıcılar:
            f.write(k + "\n")

def yükle():
    """
    Program açılışında kullanıcı listesini dosyadan okur.
    Dosya yoksa boş liste döner.
    """
    if not os.path.exists(DOSYA_ADI):
        return []
    with open(DOSYA_ADI, "r", encoding="utf-8") as f:
        # Boş satırları filtreler, baştaki/sondaki boşlukları temizler
        return [satır.strip() for satır in f if satır.strip()]

# ──────────────────────────────────────────
# Ana Fonksiyonlar
# ──────────────────────────────────────────

def kullanıcı_ekle(kullanıcılar):
    """
    Yeni bir kullanıcı adı alır ve listeye ekler.
    - Boş isim girilirse uyarı verir.
    - Listede zaten varsa tekrar eklemez (duplicate kontrolü).
    """
    başlık_yaz("Kullanıcı Ekle")
    ekle = input("  Eklenecek kullanıcı adı: ").strip()

    if not ekle:
        print("  ⚠  Kullanıcı adı boş olamaz.")
    elif ekle in kullanıcılar:
        print(f"  ⚠  '{ekle}' zaten listede mevcut.")
    else:
        kullanıcılar.append(ekle)
        kaydet(kullanıcılar)   # Değişikliği hemen dosyaya yaz
        print(f"  ✓  '{ekle}' başarıyla eklendi.")

    devam_et()


def kullanıcı_gör(kullanıcılar):
    """Mevcut kullanıcı listesini numaralı şekilde ekrana yazdırır."""
    başlık_yaz(f"Kullanıcı Listesi  ({len(kullanıcılar)} kişi)")

    if not kullanıcılar:
        print("  Henüz kullanıcı eklenmedi.")
    else:
        for i, k in enumerate(kullanıcılar, 1):
            print(f"  {i:>3}. {k}")

    devam_et()


def kullanıcı_sil(kullanıcılar):
    """
    Listeden seçilen kullanıcıyı siler.
    Kullanıcı numarasıyla seçim yapılır; 0 girilerek iptal edilebilir.
    """
    başlık_yaz("Kullanıcı Sil")

    if not kullanıcılar:
        print("  Liste zaten boş.")
        devam_et()
        return

    # Mevcut listeyi göster
    for i, k in enumerate(kullanıcılar, 1):
        print(f"  {i:>3}. {k}")

    print()
    try:
        seçim = int(input("  Silinecek kullanıcı numarası (0 = iptal): "))
        if seçim == 0:
            return
        if 1 <= seçim <= len(kullanıcılar):
            silinen = kullanıcılar.pop(seçim - 1)   # Listeden çıkar
            kaydet(kullanıcılar)                      # Dosyayı güncelle
            print(f"  ✓  '{silinen}' silindi.")
        else:
            print("  ⚠  Geçersiz numara.")
    except ValueError:
        print("  ⚠  Lütfen bir sayı giriniz.")

    devam_et()


def listeyi_temizle(kullanıcılar):
    """
    Tüm kullanıcıları listeden ve dosyadan siler.
    İşlem öncesi onay alınır.
    """
    başlık_yaz("Listeyi Temizle")
    onay = input("  Tüm kullanıcılar silinecek. Emin misiniz? (e/h): ").strip().lower()
    if onay == "e":
        kullanıcılar.clear()   # Listeyi bellekte temizle
        kaydet(kullanıcılar)   # Boş listeyi dosyaya yaz
        print("  ✓  Liste temizlendi.")
    else:
        print("  ✗  İptal edildi.")
    devam_et()


def salla(kullanıcılar):
    """
    Kullanıcı listesini rastgele karıştırır ve yeni sıralamayı dosyaya kaydeder.
    Özellikle sıra belirlemek için kullanışlıdır.
    """
    başlık_yaz("Listeyi Karıştır")

    if not kullanıcılar:
        print("  ⚠  Listede kullanıcı yok.")
        devam_et()
        return

    random.shuffle(kullanıcılar)   # Yerinde karıştırma (in-place)
    kaydet(kullanıcılar)

    print("  Liste karıştırıldı:\n")
    for i, k in enumerate(kullanıcılar, 1):
        print(f"  {i:>3}. {k}")

    devam_et()


def rastgele_seç(kullanıcılar):
    """
    Listeden istenen sayıda rastgele kullanıcı seçer.
    Her seçilen isim animasyonlu olarak (nokta nokta) ekrana yazdırılır.
    Aynı kişi iki kez seçilmez (random.sample kullanılır).
    """
    başlık_yaz("Rastgele Çekiliş")

    if not kullanıcılar:
        print("  ⚠  Listede kullanıcı yok.")
        devam_et()
        return

    try:
        kaç = int(input(f"  Kaç kişi seçilsin? (max {len(kullanıcılar)}): "))
        if kaç <= 0:
            print("  ⚠  En az 1 kişi seçilmelidir.")
            devam_et()
            return
        if kaç > len(kullanıcılar):
            print(f"  ⚠  Listede yalnızca {len(kullanıcılar)} kişi var.")
            devam_et()
            return
    except ValueError:
        print("  ⚠  Lütfen geçerli bir sayı giriniz.")
        devam_et()
        return

    # Tekrarsız rastgele seçim
    seçilenler = random.sample(kullanıcılar, kaç)

    print()
    for i, kişi in enumerate(seçilenler, 1):
        # Animasyon: "Çekiliyor..." yazısı noktalarla büyür
        print(f"  Çekiliyor", end="", flush=True)
        for _ in range(3):
            time.sleep(0.4)
            print(".", end="", flush=True)
        # \r ile satır başına dönüp kazananı yazar
        print(f"\r  {i:>3}. 🎉  {kişi}          ")
        time.sleep(0.3)

    print("\n  ✓  Çekiliş tamamlandı.")
    devam_et()


# ──────────────────────────────────────────
# Ana Döngü
# ──────────────────────────────────────────

def main():
    """
    Uygulamanın giriş noktası.
    Program başlarken mevcut kullanıcıları dosyadan yükler,
    ardından kullanıcı çıkana kadar menüyü döngüsel gösterir.
    """
    kullanıcılar = yükle()   # Uygulama başlarken kayıtlı verileri yükle

    while True:
        ekranı_temizle()

        # Ana menü arayüzü
        print("\n  ╔══════════════════════════════════════╗")
        print("  ║        ÇEKİLİŞ UYGULAMASI           ║")
        print(f"  ║     Kayıtlı kullanıcı: {len(kullanıcılar):<13}║")
        print("  ╚══════════════════════════════════════╝\n")
        print("     1  →  Kullanıcı Ekle")
        print("     2  →  Kullanıcıları Göster")
        print("     3  →  Kullanıcı Sil")
        print("     4  →  Listeyi Temizle")
        print("     5  →  Listeyi Karıştır")
        print("     6  →  Rastgele Çekiliş Yap")
        print("     0  →  Çıkış\n")

        try:
            seçim = int(input("  Seçiminiz: "))
        except ValueError:
            # Sayı dışı bir şey girilirse menüye dön
            continue

        ekranı_temizle()

        # Seçime göre ilgili fonksiyonu çağır
        if seçim == 1:
            kullanıcı_ekle(kullanıcılar)
        elif seçim == 2:
            kullanıcı_gör(kullanıcılar)
        elif seçim == 3:
            kullanıcı_sil(kullanıcılar)
        elif seçim == 4:
            listeyi_temizle(kullanıcılar)
        elif seçim == 5:
            salla(kullanıcılar)
        elif seçim == 6:
            rastgele_seç(kullanıcılar)
        elif seçim == 0:
            print("\n  İyi günler! Görüşmek üzere.\n")
            break
        else:
            print("  ⚠  Lütfen geçerli bir seçim yapınız.")
            time.sleep(1)


# Doğrudan çalıştırıldığında main() fonksiyonunu başlat
if __name__ == "__main__":
    main()