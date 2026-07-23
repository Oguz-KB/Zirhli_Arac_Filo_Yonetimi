from traceback import print_tb


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
            print(f"BUM! {self.arac_id} ({self.model}) {self.top_kalibresi}mm topuyla ateş etti! Kalan Mühimmat: %{self.muhimmat_seviyesi}")
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



arac1 = ZirhliArac(arac_id="ALT-001", model="Altay Tankı")
arac2 = ZirhliArac(arac_id="PARS-002", model="Pars 6x6", yakit_seviyesi=80, muhimmat_seviyesi=50)
zpt1 = ZPT(arac_id="KIRPI-001", model="Kirpi II", personel_kapasitesi=12)
