# 💽 DiskArchive Pro

> **Python, PySide6 ve SQLite ile geliştirilmiş profesyonel disk envanter, analiz ve raporlama yazılımı.**

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![PySide6](https://img.shields.io/badge/PySide6-Qt6-green)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Sürüm](https://img.shields.io/badge/Sürüm-v2.0.0-success)

---

# 📖 Proje Hakkında

**DiskArchive Pro**, bilgisayardaki diskleri, klasörleri ve dosyaları tarayarak detaylı analiz yapan profesyonel bir masaüstü uygulamasıdır.

Tarama sonuçları SQLite veritabanında saklanır ve kullanıcıya;

- Disk analizi
- Dosya analizi
- Klasör analizi
- İstatistikler
- Grafikler
- Arama
- Raporlama

gibi gelişmiş özellikler sunar.

---

# ✨ Özellikler

## 💽 Disk Tarama

- Hızlı tarama motoru
- Çok iş parçacıklı (Multi Thread)
- Büyük klasör desteği
- Gerçek zamanlı ilerleme takibi

---

## 📁 Klasör Analizi

- Klasör boyutları
- Alt klasör sayıları
- Dosya sayıları
- Boş klasör analizi

---

## 📄 Dosya Analizi

- Dosya uzantıları
- Dosya boyutları
- Oluşturulma tarihi
- Değiştirilme tarihi

---

## 🔍 Gelişmiş Arama

- Dosya adına göre arama
- Uzantıya göre filtreleme
- Boyuta göre filtreleme
- Tarihe göre filtreleme

---

## 📊 Dashboard

Dashboard ekranında;

- Toplam Disk
- Toplam Klasör
- Toplam Dosya
- Toplam Boyut
- En Büyük Dosyalar
- En Büyük Klasörler
- Dosya Türleri Grafiği

anlık olarak görüntülenebilir.

---

## 📈 Raporlama

- İstatistikler
- Grafikler
- Analiz ekranı
- Rapor altyapısı

---

# 🖼️ Ekran Görüntüleri

## Dashboard

![Dashboard](screenshots/dashboard.png)

## Dosya Arama

![Search](screenshots/search.png)

## İstatistikler

![Statistics](screenshots/statistics.png)

---

# ⚙️ Kurulum

Projeyi indiriniz.

```bash
git clone https://github.com/yusufyakici/DiskArchivePro.git
```

Gerekli kütüphaneleri yükleyiniz.

```bash
pip install -r requirements.txt
```

Programı çalıştırınız.

```bash
python main.py
```

---

# 📁 Proje Yapısı

```
DiskArchivePro
│
├── app
│   ├── config
│   ├── database
│   ├── gui
│   ├── models
│   ├── repository
│   ├── scanner
│   ├── services
│   ├── workers
│   └── utils
│
├── assets
├── screenshots
├── README.md
├── requirements.txt
└── main.py
```

---

# 🚀 Yol Haritası

## ✅ Tamamlanan

- Dashboard
- Disk Tarama
- SQLite Veritabanı
- Repository Pattern
- Multi Thread Tarama
- Dosya Arama
- İstatistikler
- Grafikler
- Rapor Altyapısı

---

## 🚧 Geliştiriliyor

- Tarama Geçmişi (Scan History)
- Yinelenen Dosya Bulucu
- SHA256 / MD5 Hash
- HTML Rapor
- PDF Rapor
- Excel Aktarma
- Tarama Karşılaştırma
- Karanlık Tema
- Eklenti (Plugin) Sistemi

---

# 🛠 Kullanılan Teknolojiler

- Python
- PySide6
- SQLite
- Qt Charts
- ReportLab
- OpenPyXL

---

# 📌 Sürüm Bilgisi

**Mevcut Sürüm**

```
v2.0.0
```

---

# 👨‍💻 Geliştirici

**Yusuf YAKICI**

Sistem Uzmanı

GitHub

https://github.com/yusufyakici

---

# ⭐ Destek

Projeyi beğendiyseniz GitHub üzerinde ⭐ vererek destek olabilirsiniz.

Her türlü öneri ve geri bildiriminiz benim için değerlidir.
