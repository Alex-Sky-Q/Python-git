import os

# Can be improved by storing DB and SYN files in the user local folder
# so that admin rights will not be required if program is installed in Program Files directory

file_path = os.path.dirname(__file__)

DB_NAME = f'{file_path}/tags_count.db'
SYN_FILE = f'{file_path}/domains_syn.yml'
ICO_FILE = f'{file_path}/TC_36896_32.ico'
