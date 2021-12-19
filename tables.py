from prettytable import PrettyTable
import colored
import req


def continent_table():
    table = PrettyTable()
    res = req.get_global_data()
    table.field_names = ['Continent', 'Cases', 'Today Cases', 'Deaths', 'Today Deaths', 'Recovered', 'Active',
                         'Critical']
    for index in range(0, len(res)):
        table.add_row(
            [
                res[index].get('continent'),
                res[index].get('cases'),
                res[index].get('todayCases'),
                res[index].get('deaths'),
                res[index].get('todayDeaths'),
                res[index].get('recovered'),
                res[index].get('active'),
                res[index].get('critical')
            ]
        )
    print(colored.stylize('\nContinental Statistics', colored.bg(56)))
    print(colored.stylize(table, colored.fg(104)))


def country_table():
    table = PrettyTable()
    res = req.countries_data()
    table.field_names = [
        'Country',
        'Cases',
        'Today Cases',
        'Deaths',
        'Today Deaths',
        'Recovered',
        'Today Recovered',
        'Active',
        'Population',
        'Critical'
    ]
    for index in range(0, len(res)):
        table.add_row(
            [
                res[index].get('country'),
                res[index].get('cases'),
                res[index].get('todayCases'),
                res[index].get('deaths'),
                res[index].get('todayDeaths'),
                res[index].get('recovered'),
                res[index].get('todayRecovered'),
                res[index].get('active'),
                res[index].get('population'),
                res[index].get('critical')
            ]
        )
    print(colored.stylize('\nGlobal Statistics', colored.bg(56)))
    print(colored.stylize(table, colored.fg(104)))


def each_country_table(location):
    table = PrettyTable()
    res = req.each_country_data(location)
    table.field_names = [
        'Country',
        'Cases',
        'Today Cases',
        'Deaths',
        'Today Deaths',
        'Recovered',
        'Today Recovered',
        'Active',
        'Population',
        'Critical'
    ]
    if type(res) is list:
        for index in range(0, len(res)):
            table.add_row(
                [
                    res[index].get('country'),
                    res[index].get('cases'),
                    res[index].get('todayCases'),
                    res[index].get('deaths'),
                    res[index].get('todayDeaths'),
                    res[index].get('recovered'),
                    res[index].get('todayRecovered'),
                    res[index].get('active'),
                    res[index].get('population'),
                    res[index].get('critical')
                ]
            )
    else:
        table.add_row([
            res.get('country'),
            res.get('cases'),
            res.get('todayCases'),
            res.get('deaths'),
            res.get('todayDeaths'),
            res.get('recovered'),
            res.get('todayRecovered'),
            res.get('active'),
            res.get('population'),
            res.get('critical')
        ])
    print(colored.stylize('\n Statistics', colored.bg(56)))
    print(colored.stylize(table, colored.fg(104)))
