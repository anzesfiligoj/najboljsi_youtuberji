def pocisti_podatke(podatki):
    s = podatki.groupdict()
    for i in ["st", "nd", "th", "rd"]:
        if i in s["Zaporedna_številka"]:
            s["Zaporedna_številka"] = s["Zaporedna_številka"].replace(i, "")
    s["Zaporedna_številka"] = int(s["Zaporedna_številka"].replace(",", ""))
    s["Ime"] = s["Ime"]
    s["Število_posnetkov"] = int(s["Število_posnetkov"].replace(",", ""))
    s["Ocena"] = s["Ocena"]
    s["Število_naročnikov"] = int(s["Število_naročnikov"].replace(",", ""))
    s["Število_ogledov"] = int(s["Število_ogledov"].replace(",", ""))
    return s


import orodja
import re
import csv

def funkcija():
    orodja.shrani("https://socialblade.com/youtube/top/5000", "podatki.txt")
    vsebina = orodja.vsebina_datoteke("podatki.txt")
    podatki = []
    stolpci = ["Zaporedna_številka", "Ime", "Ocena", "Število_posnetkov", "Število_naročnikov", "Število_ogledov"]
    vzorec = re.compile(
    r'<div style="float: left; width: 50px; color:#888;">(?P<Zaporedna_številka>.*?)</div>.*?'
    r'<span style="font-weight: bold; color:#.*?;">(?P<Ocena>.*?)</span> </div>.*?'
    r'<a href=".*?">(?P<Ime>.*?)</a>.*?'
    r'<div style="float: left; width: 100px;"><span style="color:#555;">(?P<Število_posnetkov>.*?)</span></div>.*?'
    r'<span style="color:#555;">(?P<Število_naročnikov>.*?)</span>.*?<div style="float: left; width: 150px;">.*?<span style=.color:#555;">(?P<Število_ogledov>.*?)</span>',
    flags=re.DOTALL)
    for yt in re.finditer(vzorec, vsebina):
        podatki.append(pocisti_podatke(yt))
    orodja.zapisi_tabelo(podatki, stolpci, "csv_datoteka.txt")
