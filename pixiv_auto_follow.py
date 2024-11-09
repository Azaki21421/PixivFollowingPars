from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import json
from time import sleep, time


DATA_FILE = 'pixiv_data.json'


def load_links():
    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data.get('users', []), data.get('last_index', 0)


def save_progress(users, last_index):
    data = {
        'users': users,
        'last_index': last_index
    }
    with open(DATA_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def follow_users():
    users, last_index = load_links()
    links = [user['link'] for user in users]
    total_links = len(links)

    browser = webdriver.Chrome()
    browser.get('https://accounts.pixiv.net/login?return_to=https%3A%2F%2Fwww.pixiv.net%2F&lang=en&source=pc&view_type=page')
    sleep(60)

    print('End login...')
    sleep(10)

    start_time = time()

    for index, link in enumerate(links[last_index:], start=last_index):
        print(f'Following the link {index + 1}/{total_links}: {link}')
        browser.get(link)
        sleep(3)

        try:
            buttons = browser.find_elements(By.XPATH, '//*[@id="root"]/div[2]/div/div[3]/div/div/div[1]/div[2]/div/div[2]/div/div[1]/div[2]/button')

            for button in buttons:
                button_text = button.text.strip()
                if button_text in ["Follow", "Following"]:
                    if button_text == "Follow":
                        button.click()
                        print("Button pressed 'Follow'")
                    else:
                        print("Already subscribed (Following)")
                    break
                else:
                    print(f"Skip text button: '{button_text}'")

        except NoSuchElementException:
            print("Follow button not found")

        save_progress(users, index + 1)

        elapsed_time = time() - start_time
        avg_time_per_follow = elapsed_time / (index - last_index + 1)
        remaining_follows = total_links - (index + 1)
        estimated_remaining_time = avg_time_per_follow * remaining_follows
        print(f"Progress: {index + 1}/{total_links}")
        print(f"Remaining time: {int(estimated_remaining_time // 60)} min {int(estimated_remaining_time % 60)} sec")

        sleep(2)

    browser.quit()
    print('Following completed.')


if __name__ == '__main__':
    follow_users()
