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
import tkinter as tk
from tkinter import ttk

NO_REC_DB = 'No data for this URL in DB'
NO_SYN = 'No synonym in the file'
READ_DB_OK = 'Read from DB successfully'


def url_builder(site):
    # Can be improved with regexp
    if '.' not in site:
        domain = syn_reader(site)
    else:
        domain = site
    if domain:
        url = 'https://' + domain
        return url


def syn_reader(site_syn):
    with open('domains_syn.yml', 'r') as f:
        syns = yaml.safe_load(f)
        for key, val in syns.items():
            if key == site_syn:
                return val
    if len(sys.argv) == 1:
        stat_screen.set(NO_SYN)
    else:
        print(NO_SYN)
        sys.exit()


def run_command(comm, site):
    if comm in ('-view', '--view'):
        url = url_builder(site)
        db_reader(url)
    elif comm in ('-get', '--get'):
        url = url_builder(site)
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


def db_reader(input_url):
    query = 'SELECT * FROM tags_count WHERE url = ?'
    params = [input_url]
    conn = db_conn()
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchone()
    conn.close()
    if result:
        local_date = datetime.strptime(result[2], '%Y-%m-%d %H:%M:%S.%f%z').astimezone().strftime('%d-%m-%Y, %H:%M:%S')
        tags_db = pickle.loads(result[3])
        tags_str = ''
        for key, val in tags_db.items():
            item = key + ' - ' + str(val) + '\n'
            tags_str += item
        if len(sys.argv) == 1:
            site_screen.set(result[0])
            url_screen.set(result[1])
            date_screen.set(local_date)
            tags_screen.set(tags_str)
            stat_screen.set(READ_DB_OK)
        else:
            print('Site: ' + result[0])
            print('URL: ' + result[1])
            print('Check Date: ' + local_date)
            print('Tags:\n' + tags_str)
    elif len(sys.argv) == 1:
        stat_screen.set(NO_REC_DB)
        site_screen.set('')
        date_screen.set('')
        url_screen.set('')
        tags_screen.set('')
    else:
        print(NO_REC_DB)


def run_gui():
    global site_screen, url_screen, date_screen, tags_screen, stat_screen
    root = tk.Tk()
    frm1 = ttk.Frame(root)
    frm1.pack()
    ttk.Label(frm1, text="Hello World!").pack(pady=5)

    frm2 = ttk.Frame(root)
    frm2.pack(padx=30)
    ttk.Label(frm2, text='Site (synonym):').pack(side='left')
    inp_url = tk.StringVar()
    ttk.Entry(frm2, textvariable=inp_url).pack(side='left')

    ttk.Button(frm2, text='View', command=lambda: run_command('-view', inp_url.get())).pack(side='left', padx=3)
    ttk.Button(frm2, text='Get', command=lambda: run_command('-get', inp_url.get())).pack(side='left')

    ttk.Separator(root, orient='horizontal').pack(fill='x', pady=10)

    frm3 = ttk.Frame(root)
    frm3.pack(padx=15, side='top', anchor='w')
    ttk.Label(frm3, text='Site:').pack(side='left')
    site_screen = tk.StringVar()
    ttk.Label(frm3, textvariable=site_screen, font=('Consolas', '11')).pack(padx=5)

    frm4 = ttk.Frame(root)
    frm4.pack(padx=15, side='top', anchor='w')
    ttk.Label(frm4, text='URL:').pack(side='left')
    url_screen = tk.StringVar()
    ttk.Label(frm4, textvariable=url_screen, font=('Consolas', '11')).pack(padx=5)

    frm5 = ttk.Frame(root)
    frm5.pack(padx=15, side='top', anchor='w')
    ttk.Label(frm5, text='Check Date:').pack(side='left')
    date_screen = tk.StringVar()
    ttk.Label(frm5, textvariable=date_screen, font=('Consolas', '11')).pack(padx=5)

    frm6 = ttk.LabelFrame(root, text='Tags')
    frm6.pack(padx=15, pady=5, ipadx=5, side='top', anchor='w')
    tags_screen = tk.StringVar()
    ttk.Label(frm6, textvariable=tags_screen, width=15, font=('Consolas', '10')).pack()

    ttk.Separator(root, orient='horizontal').pack(fill='x', pady=3)

    frm7 = ttk.Frame(root)
    frm7.pack(side='left')
    stat_screen = tk.StringVar()
    stat_screen.set(' Ready')
    ttk.Label(frm7, textvariable=stat_screen, font=('Consolas', '9')).pack(padx=3)

    frm8 = ttk.Frame(root)
    frm8.pack(padx=3, pady=3, side='bottom', anchor='se')
    # ttk.Button(frm7, text='Quit', command=root.destroy).pack()
    ttk.Label(frm8, text='Alex Sky, 2022', foreground='grey').pack()


    root.mainloop()
