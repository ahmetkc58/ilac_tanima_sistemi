"""İlaç kutusu fotoğrafından ilaç tespiti ve bilgi gösterimi (YOLO11 + veri.json).

Kullanım:
    python tahmin_ornek.py kutu.jpg
    python tahmin_ornek.py kutu.jpg --conf 0.4
"""
import argparse
import json
from pathlib import Path

from ultralytics import YOLO

KLASOR = Path(__file__).parent


def ilac_bilgisi_bul(veritabani, sinif_adi):
    """Model sınıf adını (küçük harfli olabilir) veri.json kaydıyla eşleştirir."""
    for kayit in veritabani:
        if kayit["isim"].strip().lower() == sinif_adi.strip().lower():
            return kayit
    return None


def main():
    ap = argparse.ArgumentParser(description="İlaç kutusu tespiti")
    ap.add_argument("goruntu", help="İlaç kutusu fotoğrafı")
    ap.add_argument("--conf", type=float, default=0.25, help="Güven eşiği (varsayılan 0.25)")
    args = ap.parse_args()

    model = YOLO(str(KLASOR / "yolo11_ilac_best.pt"))
    veritabani = json.loads((KLASOR / "veri.json").read_text(encoding="utf-8"))

    sonuc = model.predict(args.goruntu, conf=args.conf, verbose=False)[0]
    if len(sonuc.boxes) == 0:
        print("İlaç tespit edilemedi. Kutuyu daha net ve iyi ışıkta çekmeyi dene.")
        return

    # En yüksek güvenli tespiti al
    en_iyi = max(sonuc.boxes, key=lambda b: float(b.conf))
    ad = sonuc.names[int(en_iyi.cls)]
    print(f"Tespit: {ad}  (güven: {float(en_iyi.conf):.2f})")

    bilgi = ilac_bilgisi_bul(veritabani, ad)
    if bilgi is None:
        print("Bu ilaç veri.json içinde bulunamadı.")
        return

    print(f"Sınıf        : {bilgi['sinif']}")
    print(f"Kullanım     : {bilgi['kullanim']}")
    print(f"Doz          : {bilgi['dozu']}")
    print(f"Yan etkiler  : {', '.join(bilgi['yan_etkiler'])}")
    print(f"Uyarılar     : {'; '.join(bilgi['uyarilar'])}")
    print("\nBu bilgiler yalnızca bilgilendirme amaçlıdır, tıbbi tavsiye değildir.")


if __name__ == "__main__":
    main()
