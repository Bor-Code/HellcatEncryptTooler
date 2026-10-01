<div align="center">

# HashTool v2.0

### Profesyonel Hash Kırma ve Dönüştürme Aracı

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](https://github.com)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com)

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="100"/>

[İndir](#-kurulum) • [Dokümantasyon](#-temel-kavramlar) • [Hızlı Başlangıç](#-kullanım) • [Yardım](#-sorun-giderme)

</div>

---

## İçindekiler

```
Temel Kavramlar → Hash, MD5, SHA, Wordlist, Brute Force
Özellikler       → Hash Cracker, Hash Converter
Kurulum          → Windows, Linux, macOS
Kullanım         → Adım adım rehber
Sorun Giderme    → Yaygın hatalar ve çözümler
Yasal Uyarı      → Etik kullanım kuralları
```

---

<div align="center">

## Temel Kavramlar

</div>

### Hash Nedir?

> Hash, veriyi **tek yönlü** matematiksel fonksiyonla sabit uzunlukta karakter dizisine dönüştürme işlemidir.

```diff
+ Girdi: "merhaba"
+ MD5:    5d41402abc4b2a76b9719d911017c592

+ Girdi: "merhaba!" (1 karakter fark)
+ MD5:    ff856acd7b494773dbfb0f3ff8e2b2cd (tamamen farklı)
```

| Özellik | Açıklama |
|---------|----------|
| **Deterministik** | Aynı girdi → Aynı hash |
| **Hızlı** | Milisaniyeler içinde hesaplama |
| **Sabit Uzunluk** | Her zaman aynı boyut |
| **Tek Yönlü** | Hash'ten geri dönülemez |

**Kullanım Alanları:**
```
 Şifre Saklama    │ Veritabanlarında güvenli depolama
 Veri Doğrulama   │ Dosya bütünlüğü kontrolü
 Dijital İmza     │ Belge onaylama
 Deduplikasyon    │ Tekrar eden verileri bulma
```

---

### Hash Türleri

<table>
<tr>
<td width="33%">

#### MD5
```
128 bit (32 hex)
Çok hızlı
Artık güvenli değil
Test için uygun
```

</td>
<td width="33%">

#### SHA-1
```
160 bit (40 hex)
Hızlı
2017'de kırıldı
Git'te kullanılıyor
```

</td>
<td width="33%">

#### SHA-256
```
256 bit (64 hex)
Güvenli
Bitcoin, SSL/TLS
Önerilen algoritma
```

</td>
</tr>
</table>

**Hash Uzunluk Tablosu:**
```
32 karakter  →  MD5
40 karakter  →  SHA-1
56 karakter  →  SHA-224
64 karakter  →  SHA-256
128 karakter →  SHA-512
```

---

### Wordlist (Sözlük)

> Her satırda bir şifre adayı olan metin dosyası

```bash
# wordlist.txt örneği
password
123456
admin
letmein
qwerty
```

| Wordlist | Boyut | Kullanım |
|----------|-------|----------|
| **Küçük** | 10K-100K | Hızlı testler |
| **Orta** | 100K-1M | Genel amaçlı |
| **RockYou** | 14M+ | Kapsamlı kırma |

**Popüler Kaynaklar:**
- [SecLists](https://github.com/danielmiessler/SecLists)
- [RockYou.txt](https://github.com/brannondorsey/naive-hashcat/releases)

---

### Brute Force (Kaba Kuvvet)

> Tüm olası kombinasyonları sistematik olarak deneme

```python
# Örnek: a-z + 0-9 (36 karakter)
1 karakter: 36           kombinasyon (~0.001 sn)
2 karakter: 1,296        kombinasyon (~0.01 sn)
3 karakter: 46,656       kombinasyon (~0.5 sn)
4 karakter: 1,679,616    kombinasyon (~2 sn)
5 karakter: 60,466,176   kombinasyon (~1 dk)
6 karakter: 2,176,782,336 kombinasyon (~40 dk)
```

<div align="center">

**7+ karakter için saatler/günler sürer!**

</div>

---

<div align="center">

## Özellikler

</div>

<table>
<tr>
<td width="50%">

### Hash Cracker
```
 MD5, SHA-1, SHA-256
 Wordlist Attack
 Brute Force (1-8 karakter)
 Gerçek zamanlı ilerleme
 Durdur/Devam
 Detaylı log
```

</td>
<td width="50%">

### Hash Converter
```
MD5, SHA-1, SHA-256
SHA-224, SHA-384, SHA-512
SHA3-256, SHA3-512
BLAKE2b, BLAKE2s
Tek tıkla tüm formatlar
Kopyalama özelliği
```

</td>
</tr>
</table>

---

<div align="center">

## Kurulum

</div>

### <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/windows8/windows8-original.svg" width="20"/> Windows

```batch
# 1. Python Kurulumu
https://python.org/downloads → İndir → "Add Python to PATH"

# 2. Proje İndirme
git clone https://github.com/kullaniciadi/hashtool.git
cd hashtool

# 3. Çalıştırma
python hashTool.py
```

**EXE Oluşturma:**
```batch
build.bat
# Çıktı: dist\HashTool.exe
```

---

### <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" width="20"/> Linux

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-tk git

# Proje
git clone https://github.com/kullaniciadi/hashtool.git
cd hashtool
python3 hashTool.py

# Executable Oluşturma
chmod +x build.sh
./build.sh
# Çıktı: dist/HashTool
```

---

### <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/apple/apple-original.svg" width="20"/> macOS

```bash
# Homebrew + Python
brew install python3 python-tk

# Proje
git clone https://github.com/kullaniciadi/hashtool.git
cd hashtool
python3 hashTool.py
```

---

<div align="center">

## Kullanım

</div>

### Wordlist Attack

```diff
1. Hash gir:    5f4dcc3b5aa765d61d8327deb882cf99
2. Hash türü:   MD5
3. Yöntem:      Wordlist
4. Dosya seç:   wordlist.txt
5. BAŞLAT!

+ BAŞARILI! Şifre: password
+ Süre: 0.03 saniye
```

---

### Brute Force Attack

```diff
1. Hash gir:    098f6bcd4621d373cade4e832627b4f6
2. Hash türü:   MD5
3. Yöntem:      Brute Force
4. Max uzunluk: 4
5. BAŞLAT!

+ 1,679,616 kombinasyon denendi
+ BAŞARILI! Şifre: test
+ Süre: 45.23 saniye
```

---

### Hash Converter

```diff
1. Metin yaz:   BenimŞifrem123
2. "TÜM FORMATLARA DÖNÜŞTÜR" tıkla

+ MD5:     e10adc3949ba59abbe56e057f20f883e
+ SHA-1:   5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8
+ SHA-256: 5e884898da28047151d0e56f8dc6292773603d0d...
+ ... 7 format daha
```

---

<div align="center">

## Sorun Giderme

</div>

<details>
<summary><b> python: command not found</b></summary>

```bash
# Çözüm
Windows: Python'u PATH'e ekle (kurulumda )
Linux:   sudo apt install python3
macOS:   brew install python3
```
</details>

<details>
<summary><b> ModuleNotFoundError: tkinter</b></summary>

```bash
# Ubuntu/Debian
sudo apt install python3-tk

# Fedora
sudo dnf install python3-tkinter

# macOS
brew install python-tk
```
</details>

<details>
<summary><b> MemoryError / Program Donuyor</b></summary>

```bash
# Çözüm 1: Küçük wordlist kullan
head -n 100000 rockyou.txt > wordlist_small.txt

# Çözüm 2: RAM yükselt (min 8 GB)
```
</details>

<details>
<summary><b> Hash Bulunamadı</b></summary>

```bash
# Kontrol 1: Hash uzunluğu doğru mu?
MD5=32, SHA1=40, SHA256=64

# Kontrol 2: Hash türü doğru mu?

# Kontrol 3: Wordlist'te var mı?
# → Daha büyük wordlist dene (rockyou.txt)
```
</details>

<details>
<summary><b> UnicodeDecodeError</b></summary>

```bash
# Linux
iconv -f ISO-8859-1 -t UTF-8 wordlist.txt > wordlist_utf8.txt

# Windows
Notepad++ → Encoding → Convert to UTF-8
```
</details>

<details>
<summary><b> EXE Çalışmıyor</b></summary>

```bash
# Antivirüs kontrolü
Windows Defender → Virus settings → Add exclusion

# Terminal'den test
cd dist
HashTool.exe
```
</details>

---

<div align="center">

## Performans Tablosu

</div>

| Uzunluk | Kombinasyon | MD5 Süresi* |
|---------|-------------|-------------|
| 3 karakter | 46K |  ~1 sn |
| 4 karakter | 1.6M |  ~30 sn |
| 5 karakter | 60M |  ~20 dk |
| 6 karakter | 2.1B |  ~12 saat |
| 7 karakter | 78B |  ~18 gün |
| 8 karakter | 2.8T |  ~2 yıl |

<sub>*Ortalama laptop (i5, 2.5GHz) üzerinde tahmini süre</sub>

---

<div align="center">

## Sık Sorulan Sorular

</div>

<details>
<summary><b>Program yasal mı?</b></summary>

Kendi şifreleriniz için → Yasal
Başkalarının şifreleri için → Yasadışı

Sadece **eğitim** ve **yetkili test** amaçlı kullanın!
</details>

<details>
<summary><b>Salt'lı hash kırılabilir mi?</b></summary>

Hayır, salt eklenen hash'ler wordlist/rainbow table saldırılarına dayanıklıdır.
</details>

<details>
<summary><b>GPU desteği var mı?</b></summary>

Bu araç CPU tabanlıdır. GPU için:
- Hashcat (100x daha hızlı)
- John the Ripper
kullanmanız önerilir.
</details>

<details>
<summary><b>RockYou.txt nedir?</b></summary>

14 milyon gerçek kullanıcı şifresini içeren en kapsamlı wordlist.

İndirme: [GitHub](https://github.com/brannondorsey/naive-hashcat/releases)
</details>

---

<div align="center">

## Yasal Uyarı

</div>

```diff
! BU ARAÇ YALNIZCA EĞİTİM AMAÇLIDIR

+ Kendi şifrelerinizi test edin
+ Eğitim ortamlarında kullanın
+ İzinli penetrasyon testlerinde kullanın

- Başkalarının şifrelerini kırmayın
- Yetkisiz erişim sağlamayın
- Kötü amaçlı kullanmayın
```

**Yasal Sonuçlar:**
- 🇹🇷 TCK Madde 243: Bilişim sistemine yetkisiz giriş → 2-4 yıl hapis
- 🇺🇸 Computer Fraud and Abuse Act (CFAA)
- 🇪🇺 GDPR ihlalleri

<div align="center">

** Etik ve Sorumlu Kullanım Dileğiyle!**

</div>

---

<div align="center">

## İletişim ve Destek

[![GitHub Issues](https://img.shields.io/badge/Issues-Report%20Bug-red.svg)](https://github.com/kullaniciadi/hashtool/issues)
[![GitHub PRs](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)](https://github.com/kullaniciadi/hashtool/pulls)
[![Documentation](https://img.shields.io/badge/Docs-Read%20More-blue.svg)](https://github.com/kullaniciadi/hashtool/wiki)

### Katkıda Bulun

```bash
git clone https://github.com/kullaniciadi/hashtool.git
git checkout -b yeni-ozellik
git commit -m "Yeni özellik eklendi"
git push origin yeni-ozellik
```

### Yıldız Vermek Unutmayın! 

<img src="https://img.shields.io/github/stars/kullaniciadi/hashtool?style=social"/>

</div>

---

<div align="center">

### Geliştirilen Teknolojiler

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="40"/> &nbsp;
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg" width="40"/> &nbsp;
<img src="https://upload.wikimedia.org/wikipedia/commons/3/37/Hashicorp_logo.svg" width="40"/>

**Made with ❤️ for Cybersecurity Education**

---

**Lisans:** MIT &nbsp; | &nbsp; **2025** &nbsp; | &nbsp; **v2.0**

</div>
