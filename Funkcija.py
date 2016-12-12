def pocisti_podatke(podatki):
    s = podatki.groupdict()
    s["Zaporedna_številka"] = int(s["Zaporedna_številka"].replace(",", ""))
    s["Ime"] = s["Ime"]
    s["Socialblade_rang"] = int(s["Socialblade_rang"].replace(",", ""))
    s["Ocena"] = s["Ocena"]
    s["Število_naročnikov"] = int(s["Število_naročnikov"].replace(",", ""))
    s["Število_ogledov"] = int(s["Število_ogledov"].replace(",", ""))
    return s


import orodja
import re
import csv

def funkcija():
    orodja.shrani("http://socialblade.com/youtube/top/5000/mostsubscribed", "podatki.txt")
    vsebina = orodja.vsebina_datoteke("podatki.txt")
    slovarji = []
    stolpci = ["Zaporedna_številka", "Ime", "Socialblade_rang", "Ocena", "Število_naročnikov", "Število_ogledov"]
    vzorec = re.compile("style.*?=.width: \d*?px; background: #f.f.f.*? border-bottom: 1px solid #eee.*?>(?P<Zaporedna_številka>.*?)</div>.*?"
    "style.*?>(?P<Socialblade_rang>.*?)</div>.*?"
    "<span style.*?>(?P<Ocena>.*?)</span>.*?"
    "<a href.*?>(?P<Ime>.*?)</a>.*?"
    "style.*?><.*?>(?P<Število_naročnikov>.*?)</span>.*?"
    "style.*?><.*?>(?P<Število_ogledov>.*?)</span>", flags=re.DOTALL)
    for yt in re.finditer(vzorec, vsebina):
        slovarji.append(pocisti_podatke(yt))
    orodja.zapisi_tabelo(slovarji, stolpci, "csv_datoteka.txt")
