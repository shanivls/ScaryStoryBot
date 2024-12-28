import os
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

USER = {'username': 'truman.up123@gmail.com', 'password': 'MyloGoldi0112!'}
ELEVENLABS_URL = 'https://elevenlabs.io/app/sign-in?redirect=/app/speech-synthesis/text-to-speech'
DOWNLOAD_DIR = os.path.abspath('../story_voices')

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'download.default_directory': DOWNLOAD_DIR,  # Set default download directory
    'download.prompt_for_download': False,  # Do not prompt for download
    'download.directory_upgrade': True,
    'safebrowsing.enabled': True
})
browser = webdriver.Chrome(options=chrome_options)


def login():
    form = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'sign-in-form'))
    )
    inputs = form.find_elements(By.TAG_NAME, 'input')

    inputs[0].send_keys(USER['username'])
    inputs[1].send_keys(USER['password'])
    form.submit()
    print("submitted")


def enter_text_to_read(text: str):
    text_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'textarea'))
    )
    text_input.send_keys(text)
    print("entered text")


def select_voice(voice: str):
    select_voice_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Select voice"]'))
    )
    select_voice_button.click()

    search_bar = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Search for a voice..."]'))
    )
    search_bar.send_keys(voice)
    time.sleep(0.2)
    search_bar.send_keys(Keys.ENTER)
    print("voice selected")


def click_on_generate():
    generate_btn = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="Generate speech"]'))
    )
    generate_btn.click()
    print("generate")


def download_file():
    download_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Download Audio"]'))
    )
    download_button.click()
    print("download")


def generate_voice(text: str):
    browser.get(ELEVENLABS_URL)
    login()
    enter_text_to_read(text)
    select_voice("John Doe")
    click_on_generate()
    download_file()

    file_downloaded = False
    while not file_downloaded:
        time.sleep(1)
        files = os.listdir(DOWNLOAD_DIR)
        if any(file.endswith('.mp3') for file in files):
            file_downloaded = True
    browser.quit()


generate_voice('1')
