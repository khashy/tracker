import requests


def get_global_data():
    url = "https://corona.lmao.ninja/v2/continents?yesterday&sort"
    response = requests.get(url)
    res = response.json()
    return res


def each_country_data(location):
    url = "https://corona.lmao.ninja/v2/countries/"
    url += location + '?/yesterday'
    response = requests.get(url)
    res = response.json()
    return res


def countries_data():
    url = 'https://corona.lmao.ninja/v2/countries/'
    response = requests.get(url)
    res = response.json()
    return res
