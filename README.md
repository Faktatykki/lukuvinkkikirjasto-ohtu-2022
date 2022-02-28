![Github Actions](https://github.com/Faktatykki/lukuvinkkikirjasto-ohtu-2022/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/Faktatykki/lukuvinkkikirjasto-ohtu-2022/branch/main/graph/badge.svg?token=65YU2VW5CH)](https://codecov.io/gh/Faktatykki/lukuvinkkikirjasto-ohtu-2022)

# lukuvinkkikirjasto-ohtu-2022
Miniprojekti OhTu kevät 2022

## Linkkejä

Sovellus löytyy osoitteesta:
https://lit-brushlands-38911.herokuapp.com/

[Product backlog ja Sprint backlog](https://ronindashboards.herokuapp.com/jira/shared/dashboard?boardToken=VTJGc2RHVmtYMS9TMWNIeXRZYmhFQmJCTHdkWGxxazJNUWNiNmxMNlMwK011U2ZoK0RyNkpMM2YrNG8wWGk4aEoyUmx0NEkyUC9TcEhNZ0xZWkowK1pXYUhVbHU5aHJNS3BUamFLSWI0SUhjZFdEZEwwNmVhck5RNVdBWjJzSmhhY05pZ3MvbGZSY2F4YTY2T1h6dTV3NFFxYXYrVTcvZVpicitmbEdCSld2WDhKWmFIMjlWeXFkMGRPbzhZamJOWUNvU2tPTkZMRzFlQktJWXJEQnJCNVVSaENxa1lQUlQvUUI0d3RPRm1PVXNpaHg2Zk1RMUlZZ0pTbjBwZ1plOExIblBXTDVhSmp4VHJwZUxYdVUwK1E9PQ%3D%3D)

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

Robot Framework testien suorittaminen:
```
robot src/tests
```
## Definition of Done

- Testikattavuus >75%
- Kaikki testit menevät läpi
- Koodin staattinen analyysi on kunnossa (pylint >8 pistettä)
- Koodi on dokumentoitu suomeksi docstringia noudattaen
- Koodi on puskettu tuotantoympäristöön
