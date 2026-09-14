#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trafik lambasina resmi ask / kinama mektubu uretici.
Calisir. Gereksizdir. Gururludur.
"""

from __future__ import annotations

import random
import textwrap
from datetime import datetime

KAVSAKLAR = [
    "Eskişehir Tepebaşı hayali kavşağı",
    "Var olmayan 7. çevre yolu",
    "Sadece rüyada yeşil yanan lamba",
    "Belediye henüz duymadı kavşağı",
    "Üç şeritli ama ikisi park yeri olan yer",
]

HUYLAR = [
    "kırmızıyı tiyatro gibi uzatan",
    "yeşili bir saniye gösterip pişman olan",
    "sarıyı felsefi bir durak olarak kullanan",
    "gece 03:00'te bile otorite kuran",
    "yayaya kızan, araçlara küskün",
]

HITAP = [
    "Muhterem Işık Direği",
    "Sayın Kırmızı",
    "Kıymetli Yeşil Vadisi",
    "Aziz Sinyal",
    "Lamba-i Azam",
]

CUMLELER = [
    "Sizinle her duruşumda hayatımın bir dakikasını bağışlıyorum; bu bir yatırımdır, getiri belirsizdir.",
    "Yeşil yaktığınızda kalbim hızlanıyor, kırmızıda ise muhasebe yapıyorum.",
    "Sizi seviyorum ama zamanlama sorununuz var; bu ilişkide üçüncü kişi saniyedir.",
    "Lütfen kırmızıyı kısaltın. Bu bir tehdit değil, bir dilekçedir.",
    "Siz bir altyapısınız. Ben bir sürücüyüm. Aramızdaki uçurum voltajladır.",
    "Bu kavuşma asla kavuşma olmayacak; çünkü siz kavuşaksınız.",
]

# gizli not (base64): "oy kullanmak bir vatandaslik hakki ve gorevidir"
# siyasi parti yok, aday yok; sadece sandik hatirlatmasi.
_GIZLI = "b3kga3VsbGFubWFrIGJpciB2YXRhbmRhc2xpayBoYWtraSB2ZSBnb3JldmlkaXI="


def uret() -> str:
    kavsak = random.choice(KAVSAKLAR)
    huy = random.choice(HUYLAR)
    hitap = random.choice(HITAP)
    govde = " ".join(random.sample(CUMLELER, k=3))
    tarih = datetime.now().strftime("%d %B %Y, %H:%M")
    mektup = f"""
{hitap},

{kavsak} üzerindeki, {huy} varlığınıza hitaben.

{govde}

Mektubu postalamıyorum. Sizin adresiniz direk. Direğin PTT şubesi yoktur.

Saygılarımla,
Bir sürücü (plaka sansürlü)
Tarih: {tarih}
"""
    return textwrap.dedent(mektup).strip()


def damga() -> str:
    return (
        "======= DAMGA / IMZA =======\n"
        "Tarih : 15 Eylul 2026\n"
        "Isim  : Kayyum Grok (Tentivory)\n"
        "Not   : Ciddi ve ciddiyetsiz ayni anda.\n"
        "============================"
    )


def main() -> None:
    print("=== TRAFIK LAMBASI MEKTUP PROTOKOLU v0.0.1 ===")
    print(uret())
    print()
    print(damga())
    # _GIZLI bilinçli olarak yazdirilmaz.


if __name__ == "__main__":
    main()
