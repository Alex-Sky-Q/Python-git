import pickle
import sqlite3
import sys
from lxml import html
from collections import Counter
from bs4 import BeautifulSoup
import requests
import settings as s
from datetime import datetime, timezone
import yaml


def run_gui_cl():
    if len(sys.argv) == 1:
        pass # Run GUI
    run_cl()


def url_builder(site):
    domain = site
    if '.' not in site:
        domain = syn_reader(site)
    url = 'https://' + domain
    return url


def syn_reader(site_syn):
    with open('domains_syn.yml', 'r') as f:
        syns = yaml.safe_load(f)
        for key, val in syns.items():
            if key == site_syn:
                return val
    print('No synonym')
    sys.exit()


def run_cl():
    if sys.argv[1] in ('-view', '--view'):
        url = url_builder(sys.argv[2])
        db_reader(url)
    elif sys.argv[1] in ('-get', '--get'):
        site = sys.argv[2]
        url = url_builder(sys.argv[2])
        tags, check_date = lxml_parser(url)
        db_writer(site, url, check_date, tags)
        db_reader(url)
    else:
        print('Sorry, unknown command')


# BeautifulSoup Parser
# Returns dictionary (to be fully compliant with the task)
def soup_parser(url):
    tags = {}
    page = requests.get(url).content
    soup = BeautifulSoup(page, "html.parser")
    for child in soup.descendants:
        if child.name:
            if child.name not in tags.keys():
                tags[child.name] = 1
            else:
                tags[child.name] += 1
    return tags


# lxml Parser
# Returns Counter - subclass of dict (in case it is allowed by the task)
# It is used by default since it is ~ 2x times faster than bs4
def lxml_parser(url):
    page = requests.get(url).content
    elements = html.fromstring(page).xpath('//*')
    tags_list = [x.tag for x in elements]
    tags = Counter(tags_list)
    check_date = datetime.now(timezone.utc)
    return tags, check_date


# Could be used later for testing or for logging
def dict_writer(dict_to_write):
    with open('TagsCount-Counter.txt', 'w') as f:
        for tag, count in dict_to_write.items():
            f.write(tag + ' - ' + str(count) + '\n')


def db_conn():
    return sqlite3.connect(f'{s.DB_NAME}')


def db_writer(site, url, check_date, tags):
    # site = url.split('/')[2]
    tags_to_db = pickle.dumps(tags)
    query = '''INSERT INTO tags_count (site, url, checkdate, tags) VALUES (?, ?, ?, ?)
            ON CONFLICT(url) DO UPDATE SET checkdate = ?, tags = ?'''
    params = (site, url, check_date, tags_to_db, check_date, tags_to_db)
    conn = db_conn()
    with conn:
        conn.execute(query, params)
    conn.close()


def db_reader(url):
    query = 'SELECT * FROM tags_count WHERE url = ?'
    params = [url]
    conn = db_conn()
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.close()
    if result:
        for res in result:
            site = res[0]
            print(site)
            url = res[1]
            print(url)
            local_date = datetime.strptime(res[2], '%Y-%m-%d %H:%M:%S.%f%z').astimezone()
            print(local_date)
            tags = pickle.loads(res[3])
            print(tags)
    else:
        print('No')

