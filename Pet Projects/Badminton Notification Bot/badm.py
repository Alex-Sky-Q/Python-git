import configparser
import logging
import os
import requests
import sys
import time
from datetime import datetime
from lxml import html
from requests.adapters import HTTPAdapter
from urllib3 import Retry

CONN_ERR = 'Cannot connect to the site'
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
STATUS_FILE = os.path.join(DIR_PATH, 'status.txt')

logging.basicConfig(filename=os.path.join(DIR_PATH, 'logfile.log'), encoding='utf-8',
                    level=logging.INFO)  # default level WARNING

config = configparser.ConfigParser()
path_to_config = os.path.join(DIR_PATH, 'config.ini')
config.read(path_to_config)

bot_baseURL = 'https://api.telegram.org/bot'
bot_token = config['bot']['token']
bot_method = 'sendMessage'
bot_chat = config['bot']['user']


# Identify URL to check
def identify_url():
    url = None
    curr_weekday = datetime.utcnow().weekday()
    if curr_weekday == 0 or (curr_weekday == 1 and datetime.utcnow().hour < 17):  # 22-3 - UTC
        url = config['target_url']['check_url_monday']
    elif curr_weekday == 1 or (curr_weekday == 2 and datetime.utcnow().hour < 17):
        url = config['target_url']['check_url_tuesday']
    elif curr_weekday == 3 or (curr_weekday == 4 and datetime.utcnow().hour < 17):
        url = config['target_url']['check_url_thursday']
    # print(f'{datetime.utcnow()} - URL to check: {url}')
    logging.info(f'{datetime.utcnow()} - URL to check: {url}')
    return url


def send_message(text):
    s = requests.Session()
    retries = Retry(total=5, backoff_factor=0.3, status_forcelist=[502, 503, 504])
    s.mount('https://', HTTPAdapter(max_retries=retries))
    bot_url = f'{bot_baseURL}{bot_token}/{bot_method}?chat_id={bot_chat}&text={text}'
    try:
        # resp = requests.post(bot_url).json()
        s.post(bot_url)
    except requests.exceptions.RequestException as e:
        # print(f'{datetime.utcnow()} - {CONN_ERR} \n\n {str(e)}')
        logging.error(f'{datetime.utcnow()} - {CONN_ERR} \n\n {str(e)}')
        sys.exit()
    else:
        # print(f'{datetime.utcnow()} - Message was successfully sent')
        logging.info(f'{datetime.utcnow()} - Message was successfully sent\n')


def check_topic(url):
    s = requests.Session()
    retries = Retry(total=5, backoff_factor=0.3, status_forcelist=[502, 503, 504])
    s.mount('https://', HTTPAdapter(max_retries=retries))
    # Identify date to check for
    curr_day = datetime.utcnow().strftime('%d.%m.%Y')  # dd.mm.yyyy
    # print(f'{datetime.utcnow()} - Current date identified: {curr_day}')
    logging.info(f'{datetime.utcnow()} - Current date identified: {curr_day}')
    while True:
        try:
            # resp = requests.get(url).content
            resp = s.get(url).content
        except requests.exceptions.RequestException as e:
            message_text = f'{datetime.utcnow()} - {CONN_ERR} \n\n {str(e)}'
            # print(message_text)
            logging.error(message_text)
            send_message(message_text)
            break
        else:
            title_text = html.fromstring(resp).find('.//title').text
            # print(f'{datetime.utcnow()} - Title tag is found: "{title_text}"')
            logging.info(f'{datetime.utcnow()} - Title tag is found: "{title_text}"')
            if curr_day not in title_text:
                s.close()
                # print(f'{datetime.utcnow()} - Title is changed. Preparing message to send')
                logging.info(f'{datetime.utcnow()} - Title is changed. Preparing message to send')
                text_to_send = f'Привет! Запись открыта!\n\n {title_text} \n \n {url}'
                send_message(text_to_send)
                with open(STATUS_FILE, 'w') as f:
                    f.write("OK")
                sys.exit()
            else:
                if datetime.utcnow().hour < 23:
                    # print(f'{datetime.utcnow()} - Title is not changed. Waiting 45 s for the next check')
                    logging.info(f'{datetime.utcnow()} - Title is not changed. Waiting 45 s for the next check')
                    time.sleep(45)
                else:
                    # print(f'{datetime.utcnow()} - Title is not changed. Going to exit until the next check')
                    logging.info(f'{datetime.utcnow()} - Title is not changed. Going to exit until the next check')
                    with open(STATUS_FILE, 'w') as f:
                        f.write("")
                    sys.exit()  # time.sleep() is not available since there is 10 hrs limit for execution


check_url = identify_url()
if check_url:
    if 5 < datetime.utcnow().hour < 17:
        with open(STATUS_FILE) as f:
            last_status = f.readline()
        if last_status != "OK":
            logging.info(f'{datetime.utcnow()} - Morning check. Last run was not OK. Going to start a new check')
            check_topic(check_url)
        else:
            logging.info(f'{datetime.utcnow()} - Morning check. Last run was OK. Going to exit')
            sys.exit()
    else:
        check_topic(check_url)
else:
    # print(f'{datetime.utcnow()} - URL is not identified. System exit')
    logging.error(f'{datetime.utcnow()} - URL is not identified. System exit\n')
    sys.exit()
