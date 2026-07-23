# 🛡️ Zırhlı Araç Filo ve Görev Yönetim Modülü

Bu proje, **Python** ve **Nesne Tabanlı Programlama (OOP)** prensipleri kullanılarak geliştirilen simülasyon tabanlı bir savunma sanayii filo yönetim sistemidir. Proje, yazılım mimarisini adım adım inşa ederek OOP kavramlarını (Kalıtım, Kapsülleme, Çok Biçimlilik) pratik etmek amacıyla geliştirilmektedir.

## 🏗️ Sistem Mimarisi ve Katmanlar

Proje 3 ana katmandan oluşmaktadır. Mimari, modülerlik ve kolay genişletilebilirlik esas alınarak tasarlanmıştır:

### 1. Katman: Temel Sınıf (Tamamlandı ✅)
* **`ZirhliArac` (Base Class):** Filodaki tüm araçların ortak fiziksel özelliklerini (ID, Model, Yakıt, Mühimmat, Bakım Durumu) ve temel davranışlarını (`yakit_ikmali_yap`, `muhimmat_yukle`) barındıran ana şablondur.

### 2. Katman: Özelleşmiş Alt Sınıflar (Tamamlandı ✅)
* **`Tank` (Subclass):** `ZirhliArac` sınıfından **Kalıtım (Inheritance)** yoluyla türetilmiştir. Ana top kalibresi niteliğine ve `agirtop_atisi_yap()` davranışına sahiptir.
* **`ZPT` (Zırhlı Personel Taşıyıcı):** Personel taşıma kapasitesi niteliğine ve kapasite kontrolü yapan `personel_bindir()` metoduna sahiptir.

### 3. Katman: Filo Karargahı (Geliştirme Aşamasında ⏳)
* **`FiloKarargahi` (Manager Class):** Envanterdeki araçları koleksiyonlar halinde yönetecek, araç operasyonel durumlarını denetleyecek ve zorluk derecesine göre göreve araç atayacak merkezi yönetim modülüdür.

## 💻 Çalıştırma
Projenin ana derleyicisini çalıştırmak için terminalde şu komutu kullanabilirsiniz:
```bash
python main.py