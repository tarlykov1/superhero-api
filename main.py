import requests


def main():
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'
    heroes = requests.get(url=url + '/all.json', headers={'Content-Type': 'application/json; charset=utf-8'})
    my_heroes = ['Hulk', 'Captain America', 'Thanos']
    intelligence = {}
    for hero in heroes.json():
        if hero['name'] in my_heroes:
            intelligence[hero['name']] = hero['powerstats']['intelligence']
    intelligence_heroes = dict([max(intelligence.items(), key=lambda k_v: k_v[1])])
    print(intelligence_heroes)

main()