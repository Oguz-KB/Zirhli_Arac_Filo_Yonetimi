class ZirhliArac:
    def __init__(self, arac_id, model, yakit_seviyesi=100, muhimmat_seviyesi=100):

        self.arac_id = arac_id
        self.model = model
        self.yakit_seviyesi = yakit_seviyesi
        self.muhimmat_seviyesi = muhimmat_seviyesi
        self.bakim_gerekli_mi = False
        self.gorevde_mi = False

    def yakit_ikmali_yap(self):
        self.yakit_seviyesi = self.yakit_seviyesi = 100
        print(f"{self.arac_id} kodlu aracın yakıtı ikmal edildi. Yeni durum: %100")

    def muhimmat_yukle(self,miktar):
        self.muhimmat_seviyesi += miktar
        if self.muhimmat_seviyesi > 100:
            print(f"{self.arac_id} depolama kapasitesi doldu! Mühimmat %100 olarak sabitlendi.")
        else:
            print(f"{self.arac_id} aracına {miktar} birim mühimmat yüklendi. Yeni seviye: %{self.muhimmat_seviyesi}")

class Tank(ZirhliArac):
    def __init__(self, arac_id, model, top_kalibresi, yakit_seviyesi=100, muhimmat_seviyesi=100):
        super().__init__(arac_id,model,yakit_seviyesi,muhimmat_seviyesi)
        self.top_kalibresi = top_kalibresi

    def agirtop_atisi_yap(self):

        if self.muhimmat_seviyesi >= 20:
            self.muhimmat_seviyesi -= 20
            print(f"{self.arac_id} ({self.model}) {self.top_kalibresi}mm topuyla ateş etti! Kalan Mühimmat: %{self.muhimmat_seviyesi}")
        else:
            print(f"UYARI: {self.arac_id} atış yapamaz! Yetersiz mühimmat (%{self.muhimmat_seviyesi})")

class ZPT(ZirhliArac):
    def __init__(self, arac_id, model, yakit_seviyesi =100, muhimmat_seviyesi=100, personel_kapasitesi=12, mevcut_personel=0):
        super().__init__(arac_id,model,yakit_seviyesi,muhimmat_seviyesi)
        self.personel_kapasitesi = personel_kapasitesi
        self.mevcut_personel = mevcut_personel

    def personel_bindir(self,kisi_sayisi):
        self.mevcut_personel += kisi_sayisi
        if self.mevcut_personel > self.personel_kapasitesi:
            self.mevcut_personel = self.personel_kapasitesi
            print(f"{self.arac_id} kapasitesi aşıldı! Araç en fazla {self.personel_kapasitesi} kişi taşıyabilir. Mevcut personel {self.mevcut_personel} olarak sabitlendi.")
        else:
            print(f"{self.arac_id} aracına {kisi_sayisi} personel bindirildi. Araçtaki toplam personel: {self.mevcut_personel}")


class FiloKarargahi:
    def __init__(self, karargah_adi):
        self.karargah_adi = karargah_adi
        self.envanter = []

    def filoya_arac_ekle(self, arac):
        self.envanter.append(arac)
        print(
            f"{self.karargah_adi} envanterine {arac.arac_id} ({arac.model}) katıldı. Toplam araç sayısı: {len(self.envanter)}")

    def filo_durum_raporu_ver(self):
        print(f"\n==========================================")
        print(f"--- {self.karargah_adi} ANLIK DURUM RAPORU ---")
        print(f"==========================================")

        for arac in self.envanter:
            durum = "Görevde!" if arac.gorevde_mi else "Karargahta!"
            print(
                f"ID: {arac.arac_id} | Model: {arac.model:<15} | Yakıt: %{arac.yakit_seviyesi:<3} | Mühimmat: %{arac.muhimmat_seviyesi:<3} | Durum: {durum}")
            print("==========================================\n")

    def goreve_arac_ata(self, gorev_tipi, min_yakit=50, min_muhimmat=50):
        print(
            f"--- YENİ GÖREV EMRİ: {gorev_tipi} (İstenen Min. Yakıt: %{min_yakit}, Min. Mühimmat: %{min_muhimmat}) ---")

        for arac in self.envanter:
            if not arac.gorevde_mi and arac.yakit_seviyesi >= min_yakit and arac.muhimmat_seviyesi >= min_muhimmat:

                if gorev_tipi == "Taarruz" and isinstance(arac, Tank):
                    arac.gorevde_mi = True
                    print(
                        f"BAŞARILI: {arac.arac_id} ({arac.model}) 'Taarruz' görevine atandı! Operasyon başlıyor...\n")
                    return

                elif gorev_tipi == "Sevkiyat" and isinstance(arac, ZPT):
                    arac.gorevde_mi = True
                    print(
                        f"BAŞARILI: {arac.arac_id} ({arac.model}) 'Sevkiyat' görevine atandı! Personel taşınıyor...\n")
                    return

                elif gorev_tipi == "Devriye" and isinstance(arac, ZirhliArac):
                    arac.gorevde_mi = True
                    print(f"BAŞARILI: {arac.arac_id} ({arac.model}) 'Devriye' görevine çıktı.\n")
                    return

        print(f"BAŞARISIZ: '{gorev_tipi}' görevi için şartları sağlayan uygun veya boşta araç bulunamadı!\n")

arac1 = Tank(arac_id="ALT-001", model="Altay Tankı", top_kalibresi=120)
arac2 = ZirhliArac(arac_id="PARS-002", model="Pars 6x6", yakit_seviyesi=80, muhimmat_seviyesi=50)
zpt1 = ZPT(arac_id="KIRPI-001", model="Kirpi II", personel_kapasitesi=12)

karargah = FiloKarargahi(karargah_adi="5. Zırhlı Tugay Karargahı")
karargah.filoya_arac_ekle(arac1)
karargah.filoya_arac_ekle(arac2)
karargah.filoya_arac_ekle(zpt1)

karargah.filo_durum_raporu_ver()

karargah.goreve_arac_ata(gorev_tipi="Taarruz", min_yakit=70, min_muhimmat=60)

karargah.goreve_arac_ata(gorev_tipi="Taarruz", min_yakit=50, min_muhimmat=50)

karargah.goreve_arac_ata(gorev_tipi="Sevkiyat", min_yakit=40, min_muhimmat=10)

karargah.filo_durum_raporu_ver()