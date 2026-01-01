# 💊 İlaç Tanıma Sistemi

Flutter mobil uygulama + YOLO11 + Gemini AI OCR ile gerçek zamanlı ilaç tanıma sistemi.

---

## 🏗️ SİSTEM MİMARİSİ

- 📱 **Mobil Uygulama**: Flutter (Android/iOS)
- 🔧 **Backend API**: Flask + Python
- 🤖 **AI Modelleri**: YOLO11 + Gemini 2.5 Flash
- 💾 **Veritabanı**: JSON tabanlı ilaç veritabanı (13 ilaç)

---

## 🚀 BAŞLANGIÇ KILAVUZU

### ✅ 1. Backend API'yi Başlat

```bash
# Proje klasörüne gir
cd C:\Users\Ahmet\Desktop\ilac_tanima_sistemi2

# Sanal ortamı aktif et
.venv\Scripts\activate

# Backend'i başlat
python ilac_mobil/backend_api.py
```

**Backend çalışıyor ✅:**
- 🟢 Yerel: `http://127.0.0.1:5000`
- 🟡 Network: `http://10.199.183.6:5000`

### ✅ 2. Flutter Mobil Uygulamayı Başlat

```bash
# Mobil uygulama klasörüne gir
cd ilac_mobil

# Bağımlılıkları yükle (ilk kez)
flutter pub get

# Uygulamayı çalıştır
flutter run
```

### ✅ 3. API Key'i Kontrol Et

1. `.env` dosyasını aç
2. Gemini API key'ini kontrol et:
   ```
   GEMINI_API_KEY=<GEMINI_API_KEY_BURAYA>
   ```
3. **Kaydet** (Ctrl+S)

**Yeni key almak için:** [Google AI Studio](https://aistudio.google.com/app/apikey)

---

## 💻 KULLANIM

### 📱 Mobil Uygulamada

1. **Kamera ile fotoğraf çek** veya **galeriden seç**
2. İlaç kutusunu net bir şekilde göster
3. **Analiz** butonuna bas
4. **Sonuçları görüntüle:**
   - ✅ Tespit Edilen İlaç Adı
   - 🎯 YOLO Güven Skoru
   - 📝 OCR Metni
   - 💊 İlaç Kullanım Bilgileri
   - ⚠️ Yan Etkiler
   - ⚕️ Dozaj Bilgisi

### 🔧 Backend API Endpoints

- `GET /health` - Sistem sağlık kontrolü
- `POST /analyze` - Tam analiz (YOLO + OCR + DB)
- `POST /yolo-detect` - Sadece YOLO tespiti
- `POST /ocr` - Sadece OCR işlemi
- `GET /medicine/<name>` - İlaç detayları

---

## 📊 TESPİT EDİLEN 13 İLAÇ

| # | İlaç Adı | Kullanım |
|---|----------|----------|
| 1 | **Dolorex** | Ağrı kesici, ateş düşürücü |
| 2 | **Deloday** | Alerjik rinit |
| 3 | **Parol** | Ağrı kesici |
| 4 | **Coldaway C** | Soğuk algınlığı |
| 5 | **Narisat** | Alerjik rinit sprey |
| 6 | **Majezik** | İltihap, ağrı |
| 7 | **Azenose** | Alerjik rinit |
| 8 | **Beklomil** | Astım inhaler |
| 9 | **Tantum Verde** | Boğaz iltihapı |
| 10 | **Fardoben** | Boğaz enfeksiyonu |
| 11 | **Aksef** | Antibiyotik |
| 12 | **Buscopan** | Mide kramp |
| 13 | **Erdobil** | Anti-konvülsan |

---

## 🔧 SORUN GIDERME

### ❌ Backend Başlamıyor

**Çözüm:**
```bash
# Sanal ortamı aktif et
.venv\Scripts\activate

# Backend'i başlat
python ilac_mobil/backend_api.py
```

### ❌ Flutter Bağlanamıyor

**Çözüm:**
1. Backend'in çalıştığını kontrol et (`http://10.199.183.6:5000/health`)
2. `ilac_mobil/lib/services/api_service.dart` dosyasında IP adresini kontrol et
3. Bilgisayar ve telefon **aynı Wi-Fi**'de olmalı
4. Firewall'u kontrol et (port 5000 açık olmalı)

### ❌ Gemini OCR Hatası (404 model not found)

**Çözüm:**
- Backend otomatik olarak uygun Gemini modelini seçer
- API key'in geçerli olduğundan emin ol
- İnternet bağlantını kontrol et

### ❌ YOLO Tespit Edemiyor

**Sebepleri:**
- Resim çok karanlık/aydınlık
- İlaç kutusu açı yapıyor
- Resim kalitesi düşük
- İlaç veritabanında değil (sadece 13 ilaç tanır)

---

## ⚡ HIZLI KOMUTLAR

```bash
# Backend'i Başlat
python ilac_mobil/backend_api.py

# Flutter Uygulamayı Başlat
cd ilac_mobil
flutter run

# Flutter Temizle ve Yeniden Yükle
flutter clean
flutter pub get
flutter run

# Sanal Ortamı Aktif Et
.venv\Scripts\activate

# Çıkış
CTRL+C  (Terminal'de)
```

---

## 📁 DOSYA YAPISI

```
ilac_tanima_sistemi2/
├── ilac_mobil/                   ← 📱 Flutter Mobil Uygulama
│   ├── lib/
│   │   ├── screens/              ← Ekranlar
│   │   ├── services/             ← API servisleri
│   │   ├── models/               ← Veri modelleri
│   │   └── widgets/              ← UI bileşenleri
│   ├── backend_api.py            ← 🔧 Flask Backend API
│   └── assets/data/
│       └── veri.json             ← İlaç veritabanı (kopyası)
├── .env                          ← 🔑 API Anahtarları
├── veri.json                     ← 💊 Ana İlaç Veritabanı
├── yolo11_ilac_best.pt           ← 🤖 YOLO Modeli
├── requirements.txt              ← Python bağımlılıkları
├── dataset/                      ← Eğitim verileri
└── README.md
```

---

## 🌐 NETWORK YAPISI

### Backend API
```
Yerel:   http://127.0.0.1:5000
Network: http://10.199.183.6:5000
```

### Mobil Uygulama
- Android cihaz **aynı Wi-Fi**'de olmalı
- `api_service.dart` içinde backend URL: `http://10.199.183.6:5000`

### IP Adresini Değiştirmek
Eğer bilgisayarın IP'si değişirse:

1. PowerShell'de IP'ni öğren:
   ```bash
   ipconfig
   ```

2. `ilac_mobil/lib/services/api_service.dart` dosyasını aç:
   ```dart
   static const String baseUrl = 'http://SENIN_IP:5000';
   ```

3. Flutter'ı yeniden başlat

---

## 🎯 ÖZELLİKLER

### Tamamlananlar ✅
- ✅ YOLO11 ile ilaç kutusu tespiti
- ✅ Gemini 2.5 Flash OCR ile metin okuma
- ✅ 13 ilaçlık veritabanı
- ✅ Flutter mobil uygulama (Android/iOS)
- ✅ REST API backend
- ✅ Gerçek zamanlı kamera entegrasyonu
- ✅ Türkçe karakter desteği
- ✅ Detaylı ilaç bilgileri (kullanım, yan etkiler, dozaj)

### Planlar 🚧
- 🔄 Daha fazla ilaç ekleme
- 🔄 Offline mod (yerel OCR)
- 🔄 Geçmiş taramalar listesi

---

## 📞 DESTEK

**Sorun yaşıyorsan:**

1. Backend terminalindeki çıktıyı kontrol et
2. `.env` API key'ini kontrol et
3. Flutter terminalindeki hata mesajlarını oku
4. Backend health endpoint'ini test et: `http://10.199.183.6:5000/health`
5. İnternet bağlantısını kontrol et
6. Firewall ayarlarını kontrol et (port 5000)

---

## ⚠️ ÖNEMLİ NOTLAR

- ⚕️ **Bu sistem medikal tavsiye vermez** - Sadece bilgilendirme amaçlıdır
- 🔐 `.env` dosyasını kimseyle paylaşma
- 🌐 İnternet bağlantısı gerekli (Gemini OCR için)
- 📱 Mobil kullanımda bilgisayar ve telefon **aynı Wi-Fi**'de olmalı
- 🔥 Firewall port 5000'i engellememeli
- 💊 Sistem sadece **13 ilaç** tanıyabilir

---

## 📱 MOBİL UYGULAMA TESTİ

Backend çalışıyor mu kontrol et:
```bash
# Tarayıcıda aç
http://10.199.183.6:5000/health
```

Sonuç şöyle olmalı:
```json
{
  "status": "healthy",
  "yolo_loaded": true,
  "gemini_loaded": true,
  "database_loaded": true,
  "medicine_count": 13
}
```

---

**✅ Sistemi başlatmaya hazır mısın?**

```bash
# Terminal 1: Backend
python ilac_mobil/backend_api.py

# Terminal 2: Flutter
cd ilac_mobil
flutter run
```

🎉 İyi çalışmalar!
