import time
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from loguru import logger
import threading
import random

url = "http://energydragondrink.com/"
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

i = 0


def nakrutka():
    while True:
        try:
            with open("proxies.txt") as f:
                p = f.read()

            p = p.split("\n")
            p = random.choice(p)
            print(p)
            proxies = {
                'http': f'http://{p}',
                'https': f'http://{p}'
            }
            r = requests.get(url, proxies=proxies)
            headers = {
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'http://energydragondrink.com',
                'Referer': 'http://energydragondrink.com/',
                'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            }

            data = {
                'dem_pid': '1',
                'dem_act': 'vote',
                'action': 'dem_ajax',
                'answer_ids': '27'
            }
            time.sleep(2)
            response = requests.post(
                'http://energydragondrink.com/wp-admin/admin-ajax.php', headers=headers, data=data, verify=False, proxies=proxies)
            time.sleep(2)
            logger.success("Успешно проголосовал")
        except:
            pass


def main():

    thread_numbers = 150
    for _ in range(1, thread_numbers):
        thread = threading.Thread(target=nakrutka)
        thread.start()


if __name__ == "__main__":
    main()

# 5375
