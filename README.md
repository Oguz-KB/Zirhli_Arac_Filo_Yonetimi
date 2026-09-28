# 🛡️ Zırhlı Araç Filo ve Görev Yönetim Modülü

Bu proje, **Python** ve **Nesne Tabanlı Programlama (OOP)** prensipleri kullanılarak geliştirilen simülasyon tabanlı bir savunma sanayii filo yönetim sistemidir. Yazılım mimarisi sıfırdan adım adım kurgulanarak OOP'nin temel taşları uygulamalı olarak entegre edilmiştir.

## 🏗️ Sistem Mimarisi ve Katmanlar

Proje, modülerlik ve kolay genişletilebilirlik esas alınarak 3 ana katmanda kurgulanmıştır:

### 1. Katman: Temel Sınıf (Tamamlandı ✅)
* **`ZirhliArac` (Base Class):** Filodaki tüm araçların ortak fiziksel niteliklerini (`arac_id`, `model`, `yakit_seviyesi`, `muhimmat_seviyesi`, `gorevde_mi`) ve temel ikmal davranışlarını (`yakit_ikmali_yap`, `muhimmat_yukle`) tanımlayan ana şablondur.

### 2. Katman: Özelleşmiş Alt Sınıflar (Tamamlandı ✅)
* **`Tank` (Subclass):** `ZirhliArac` sınıfından **Kalıtım (Inheritance)** yoluyla türetilmiştir. Ana top kalibresi niteliğine ve mühimmat tüketim kontrolü yapan `agirtop_atisi_yap()` metoduna sahiptir.
* **`ZPT` (Zırhlı Personel Taşıyıcı):** Personel taşıma kapasitesi niteliğine ve kapasite sınırı denetimiyle çalışan `personel_bindir()` metoduna sahiptir.

### 3. Katman: Filo Karargahı (Tamamlandı ✅)
* **`FiloKarargahi` (Manager Class):** Envanterdeki araçları **Bileşiklik (Composition / Has-A)** prensibiyle kendi içindeki bir listede yöneten komuta merkezidir.
* **Yetkinlikleri:**
  * **`filoya_arac_ekle(arac)`:** Üretilen araç nesnelerini envantere kaydeder.
  * **`filo_durum_raporu_ver()`:** Envanterdeki tüm araçların yakıt, mühimmat ve görev durumlarını formatlı bir rapor olarak sunar.
  * **`goreve_arac_ata(gorev_tipi, min_yakit, min_muhimmat)`:** İstenen operasyonun türüne (Taarruz, Sevkiyat, Devriye) ve zorluk derecesine göre envanteri tarar; şartları sağlayan en uygun aracı otomatik olarak göreve kilitler.

## 🧠 Kullanılan Temel OOP Concepts
* **Inheritance (Kalıtım):** Alt sınıfların ana araç şablonundan özellik miras alması.
* **Composition (Bileşiklik):** Karargah sınıfının araç nesnelerini bir koleksiyon olarak barındırması.
* **Encapsulation & Validation (Doğrulama):** Mühimmat ve personel yüklemelerinde kapasite sınırlarının korunması.

## 💻 Çalıştırma
Projenin ana simülasyonunu çalıştırmak için terminalde şu komutu kullanabilirsiniz:
```bash
python main.py
```

## 📋 Gereksinimler
* Python 3.x ve üzeri (Ekstra bir kütüphane gerektirmez)

## 🤝 Katkıda Bulunma
Projeyi public'e aldıktan sonra, geliştirmelere katkı sağlamak isterseniz `Pull Request` (PR) gönderebilirsiniz. 

## 📄 Lisans
Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır. Dilediğiniz gibi kullanabilir ve geliştirebilirsiniz.