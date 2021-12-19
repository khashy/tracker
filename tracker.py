import click
import tables


@click.group()
def cli():
   '''
   This is Tracker!\n
   This console application helps you track down the latest covid-19 statistics around the world\n
   All data is provided by https://corona.lmao.ninja/\n
   For more information use --help.
   '''


@cli.command(help='Enter the name of countries you want')
@click.argument('location')
def countries(location):
    tables.each_country_table(location)


@cli.command(help='For global statics')
def continents():
    tables.continent_table()


@cli.command(help='Shows all countries')
def all_countries():
    tables.country_table()


if __name__ == '__main__':
    cli()
