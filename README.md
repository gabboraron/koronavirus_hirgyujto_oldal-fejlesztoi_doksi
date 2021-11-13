# Koronavírus hírgyűjtő oldal fejlesztői dokumentáció az API-hoz
*Az oldal a magyarokkal kapcsolatos koronavírus híreket gyűjti, nem csak Magyarországról!*

*Az oldal a hivatalos koronavirus oldal működésbe helyezése előtt kb egy héttel már működött, azóta gyűjti a híreket*

***Felhasználásához minden esetben a forrás megjelölése szükséges, pl: `Készült az http://awxyhe.web.elte.hu/koronavirus segítségével.` vagy a [logo](https://github.com/gabboraron/koronavirus_hirgyujto_oldal-fejlesztoi_doksi/tree/master/logo) és a weboldalra muató link haználatával!***

pl:
```html
<a href="https://awxyhe.web.elte.hu/koronavirus/index.php">
  <img src="css/pictures/koronavirushu.png" alt="Készült az http://awxyhe.web.elte.hu/koronavirus segítségével." style="max-height:SZOVEGKORNYEZETMERETE vh" >
</a>
```
vagy
```html
<a href="https://awxyhe.web.elte.hu/koronavirus/index.php">Készült az http://awxyhe.web.elte.hu/koronavirus segítségével.</a>
```

* Weboldal: https://awxyhe.web.elte.hu/koronavirus/index.php
* Mozilla Firefox böngésző kiegészítő: https://addons.mozilla.org/en-US/firefox/addon/magyar-koronav%C3%ADrus-info/

****

>
> Az elmúlt 24 óra hírei JSON formátumban az alábbi linken kérhetőek le: https://awxyhe.web.elte.hu/koronavirus/fetchlast24hnews.php
> 
> Az összes összegyűjtött hír JSON formátumban az alábbi linken érhető el: https://awxyhe.web.elte.hu/koronavirus/fetchallnews.php
>

Minden esetben egy `news` tömbben vannak a hírek, objektumonként HTMLencodolva, pl:
```
"{\"newssource\":\"hvg\",\"timestamp\":\"Sun, 09 Aug 2020 18:32:00 GMT\",\"image\":\"https:\\/\\/images.hvg.hu\\/image.as\",\"title\":\"Array\",\"description\":\"Nem csak az allergi&#225;sok vannak nagyobb vesz&#233;lyben.\",\"link\":\"http:\\/\\/hvg.hu\\/itthon\\/20200809_A_parlagfu_miatt_lehet_tobb_koronavirusos_beteg#rss\"}"
```

> Ahol a :
> * **`newssource`** - a hírforrás, lehet: `indexhu` - index.hu `foter` - foter.ro `hirado` - hirado.hu `hn` - 24.hu `hvg` - hvg.hu `vadak` - vadhajtasok.hu `felvidekma` - felvidek.ma `erdelyma` - erdely.ma `negynegynegy` - 444.hu `karpathir` - karpathir.com, hogy miért ezek a hírforrások vannak arról tudj meg többet, itt: https://awxyhe.web.elte.hu/koronavirus/howitworks.html
> * **`timestampofnews`** - időbélyeg a hírhez, az rssbe beküldés vagy az onnan beyüjtés dátuma, hírforrás függő
> * **`image`** - kép a hírhez, ha elérhető, ha nem akkor [`koronavirushu.png`](https://awxyhe.web.elte.hu/koronavirus/koronavirushu.png)
> * **`title`** - cím, amennyiben az RSS-hez hozzá volt adva
> * **`description`** - leírás, amennyiben az RSS-hez hozzá volt adva
> * **`link`** - a  hír linkje, elérhetősége

Python példa: [get_koronvirusinfoDATA.py](https://github.com/gabboraron/koronavirus_hirgyujto_oldal-fejlesztoi_doksi/blob/master/get_koronvirusinfoDATA.py)
```python
#!/usr/bin/python
import requests
import json 
import html
import sys

requestpost = requests.post('https://awxyhe.web.elte.hu/koronavirus/fetchallnews.php')
response_data = requestpost.json()
print(html.unescape(response_data["news"][0]))
currentNews = json.loads(response_data["news"][0])
print(html.unescape(currentNews["title"]))
print(html.unescape(currentNews["description"]))
print(html.unescape(currentNews["link"]))
print(requestpost.status_code)
```
