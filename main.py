import requests

heroes_list = []
class SuperHero:
    def __init__(self, name, API):
        self.name = name
        self.api = API

    def unloading(self):
        response = requests.get('https://superheroapi.com/api/' + str(API) + '/search/' + str(self.name))
        data = response.json()
        res = data['results']
        for elem in res:
            сharacter = elem['powerstats']['intelligence']
            dict_heroes = {self.name: сharacter}
            heroes_list.append(dict_heroes)
            return heroes_list

API = "2619421814940190"
hulk = SuperHero("Hulk", API)
captain_america = SuperHero("Captain America", API)
thanos = SuperHero("Thanos", API)

hulk.unloading()
captain_america.unloading()
thanos.unloading()

super_dict = {}

for d in heroes_list:
    for k, v in d.items():
        super_dict[k] = int(v)

def get_key(val):
    for key, value in super_dict.items():
         if val == value:
             return key

def max_intelligence():
    max_val = max(super_dict.values())
    return f'Умнейший из героев {get_key(max_val)}, с интеллектом {max_val}'

print(max_intelligence())




