# 🎉 Çekiliş Uygulaması

Kullanıcı listesi yönetimi ve rastgele çekiliş yapabilen, terminal tabanlı bir Python uygulaması.

---

## 📋 Özellikler

- ✅ Kullanıcı ekleme, silme ve listeleme
- 🔀 Listeyi rastgele karıştırma
- 🎲 İstenen sayıda katılımcıyı animasyonlu çekiliş ile seçme
- 💾 Kullanıcı listesini dosyaya kaydetme (kalıcı veri)
---

## 🚀 Kurulum ve Çalıştırma

Python 3 yüklü olması yeterlidir. Herhangi bir ek kütüphane gerekmez.

```bash
# Projeyi klonla
git clone https://github.com/FehmiNahcivanFn/cekilish-uygulamasi.git

# Klasöre gir
cd cekilish-uygulamasi

# Uygulamayı çalıştır
python cekilish.py
```

---

## 🎮 Kullanım

Uygulama başlatıldığında aşağıdaki menü karşılar:

```
  ╔══════════════════════════════════════╗
  ║        ÇEKİLİŞ UYGULAMASI           ║
  ║     Kayıtlı kullanıcı: 0            ║
  ╚══════════════════════════════════════╝

     1  →  Kullanıcı Ekle
     2  →  Kullanıcıları Göster
     3  →  Kullanıcı Sil
     4  →  Listeyi Temizle
     5  →  Listeyi Karıştır
     6  →  Rastgele Çekiliş Yap
     0  →  Çıkış
```

### Çekiliş nasıl yapılır?
1. Önce **1** ile katılımcıları ekle
2. **6** ile çekilişi başlat
3. Kaç kişi seçileceğini gir — kazananlar animasyonlu şekilde açıklanır 🎉

---

## 📁 Dosya Yapısı

```
cekilish-uygulamasi/
│
├── cekilish.py        # Ana uygulama dosyası
├── kullanicilar.txt   # Kullanıcı listesi (otomatik oluşturulur)
└── README.md
```

> ⚠️ `kullanicilar.txt` dosyası uygulama tarafından otomatik oluşturulur.

---

## 🛠️ Kullanılan Teknolojiler

| Teknoloji | Açıklama |
|-----------|----------|
| Python 3  | Ana programlama dili |
| `random`  | Rastgele seçim ve karıştırma |
| `time`    | Çekiliş animasyonu |
| `os`      | Dosya işlemleri ve ekran temizleme |

---
