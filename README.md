![Github Actions](https://github.com/Faktatykki/lukuvinkkikirjasto-ohtu-2022/workflows/CI/badge.svg)
# lukuvinkkikirjasto-ohtu-2022
Miniprojekti OhTu kevät 2022

Sovellus löytyy osoitteesta:
https://lit-brushlands-38911.herokuapp.com/

## Virtual environmentin pikaohjeet:
Virtuaaliympäristön luominen hakemistoon 'venv':
```
python3 -m venv venv
```

Virtuaaliympäristön käynnistäminen:
```
source venv/bin/activate
```

Riippuvuuksien asentaminen:
```
pip install -r requirements.txt
```

Virtuaaliympäristöstä poistuminen:
```
deactivate
```

Riippuvuuksien päivittäminen requirements.txt-tiedostoon:
```
pip freeze > requirements.txt
```

## Definition of Done

- Testikattavuus >75%
- Kaikki testit menevät läpi
- Koodin staattinen analyysi on kunnossa (pylint >8 pistettä)
- Koodi on dokumentoitu suomeksi docstringia noudattaen
- Koodi on puskettu tuotantoympäristöön
