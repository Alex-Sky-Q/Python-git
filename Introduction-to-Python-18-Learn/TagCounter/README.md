# Tag Counter
Tag Counter is a program to query a website, count the tags and store it in a local DB

## Portable version
Portable version is located here: `/dist/tagcounter.exe`
## Installation
1. If the package is installed in the system directory (e.g., "Program Files") - then program should also be run as admin 
2. If the package is installed in the user directory - please ensure that this directory is added to user or system `Path` (in `Environment Variables`)

Package can be installed using [pip](https://pip.pypa.io/en/stable/)
```cmd
pip install TagCounter-0.1.tar.gz
```

## Usage
Tag Counter can be run via CLI or GUI

CLI interface: `tagcounter -command site`

Possible commands: `-get`, `-view`

`-get` command/button is used to connect to the website, read the content and save it in DB.
All get requests are logged in `get.log`

`-view` command/button is used to read data from DB

Site can be entered as a URL or as a synonym

### Synonyms
Synonyms for the frequently used URLs can be specified in the `domains_syn.yml` (please do not use dots `.` for the synonyms).
For example: `ggl: google.com`
### New DB
In case you would like to use a new DB, please specify its name in `settings.py` and run `db_init.py` once

## Roadmap
The program can be improved in several ways:
1. Change storage of DB and Synonym files to the user local folder so that admin rights will not be required if program is installed in system directory
2. Improve design

## Authors
Alex Sky - [GitHub](https://github.com/Alex-Sky-Q/Python-git/tree/master/Introduction-to-Python-18-Learn/TagCounter)