from selenium import webdriver
from bs4 import BeautifulSoup
import json
from time import sleep
import os


DATA_FILE = 'pixiv_data.json'


def load_saved_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data.get('users', []), data.get('last_page', 1)
    return [], 1


def save_data(users, last_page):
    data = {
        'users': users,
        'last_page': last_page
    }
    with open(DATA_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def post():
    user_id = input("Enter user ID: ")

    users, last_page = load_saved_data()

    browser = webdriver.Chrome()
    browser.get(f'https://accounts.pixiv.net/login?return_to=https%3A%2F%2Fwww.pixiv.net%2Fen%2Fusers%2F{user_id}%2Ffollowing%3Fp%3D1&lang=en&source=pc&view_type=page')
    '''
    I'm too lazy to do normal authorization (I honestly did it, but...), as there are problems in the form of captcha, so write your data with your hands 👍
    '''
    sleep(60)
    print('End login...')
    sleep(10)
    print('Begin parse')

    current_page = last_page
    while True:
        print(f'Page number: {current_page}')
        main_url = f'https://www.pixiv.net/en/users/{user_id}/following?p={current_page}'
        browser.get(main_url)
        sleep(5)

        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')

        titles = soup.find_all('a', class_='sc-d98f2c-0 sc-19z9m4s-2 QHGGh')
        if not titles:
            print("You have reached the end of the page list.")
            break

        for title in titles:
            name = title.text.strip()
            link = 'https://www.pixiv.net' + title['href']
            users.append({'name': name, 'link': link})
            print(f"Name: {name}, Link: {link}")

        save_data(users, current_page)
        print(f'Page {current_page} saved.')

        current_page += 1

    browser.quit()
    print('Parsing completed.')


if __name__ == '__main__':
    post()
