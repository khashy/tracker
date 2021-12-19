# tracker
Covid-19 tracker app for terminal.

for installation type :

```bash 
sudo python3 setup.py install
```
---
After installation :

```bash
tracker --help
```
### Usage: tracker [OPTIONS] COMMAND [ARGS]...

  This is Tracker!

  This console application helps you track down the latest covid-19
  statistics around the world

  All data is provided by https://corona.lmao.ninja/

  For more information --help.

Options:

--help  Show this message and exit.

Commands:

all-countries  Shows all countries
  
  continents     For global statics
  
  countries      Enter the name of countries you want
  
  ### Using tracker for a single country :
  
  ```bash
  tracker countries italy
  ```
  ### For multiple countries put \, and do not use space\!
  
  ```bash
  tracker countries italy,germany,uk
  ```
  ---
  
  ### I will be happy if anyone wants to improve the functionality of this app so feel free to do it.
  ### Its free and open source.
