travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

def n_country(pais,visitas,cidades):
  novo={}
novo['country']=pais
novo['visits']=visitas
novo['cities']=cidades
travel_log.append(novo)

#

n_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
print(travel_log['cities'])