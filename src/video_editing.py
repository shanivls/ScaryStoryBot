import os
import time

from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

USER = {"username": "truman.up123@gmail.com", "password": "MyloGoldi0112!"}
CAPCUT_URL = (
    "https://www.capcut.com/editor?start_tab=video&__action_from=my_draft&position=my_draft&from_page"
    "=work_space&enter_from=create_new&scenario=tiktok&scale=9%3A16"
)
VIDEO_PATH = "C:/Users/shani/Work2/scarystory/ScaryStoryVideoBot/resources/cut_videos"
VOICE_PATH = (
    "C:/Users/shani/Work2/scarystory/ScaryStoryVideoBot/resources/stories_voices"
)

DOWNLOAD_DIR = os.path.abspath("../final_videos")

chrome_options = Options()
chrome_options.add_experimental_option(
    "prefs",
    {
        "download.default_directory": DOWNLOAD_DIR,  # Set default download directory
        "download.prompt_for_download": False,  # Do not prompt for download
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    },
)
browser = webdriver.Chrome(options=chrome_options)

browser.get(CAPCUT_URL)


def login():
    mail_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "signUsername"))
    )
    mail_input.send_keys(USER["username"] + Keys.ENTER)

    password_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))
    )
    password_input.send_keys(USER["password"] + Keys.ENTER)


def guide_buttons():
    run = True
    while run:
        try:
            guide_button = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "guide-confirm-button"))
            )
            guide_button.click()
        except TimeoutException:
            run = False


def upload_video():
    upload_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="file"]'))
    )
    upload_input.send_keys(VIDEO_PATH + "/vid1.2.mp4")


def close_shortcut():
    try:
        guide_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "lv-modal-close-icon"))
        )
        guide_button.click()
    except TimeoutException:
        pass


def fill_video():
    canvas_cover = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div#canvas-cover"))
    )
    time.sleep(2)
    second_div = canvas_cover.find_element(
        By.CSS_SELECTOR, "div.segment-widget-menu-PAPmpQ"
    )

    # Get all child div elements inside second_div
    child_divs = second_div.find_elements(By.TAG_NAME, "div")

    # Click on the second div
    if len(child_divs) >= 2:
        child_divs[1].click()


def upload_voice():
    upload_media_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "upload-menus-UMIhl_"))
    )
    upload_media_button.click()

    upload_file_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "upload-file-top-button-M9BnEd"))
    )
    file_input = upload_file_button.find_element(By.XPATH, '//input[@type="file"]')
    file_input.send_keys(VOICE_PATH + "/voice1.mp3")

    # delete unwanted video
    time.sleep(1)

    canvas_cover = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div#canvas-cover"))
    )
    canvas_cover.click()
    canvas_cover.send_keys(Keys.DELETE)


def mute_video():
    volume_div = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="track-operation"]/div[1]'))
    )
    volume_div.click()


def export_video():
    export_btn = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "export-video-btn"))
    )
    export_btn.click()
    download_btn = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "download-more-video-yZDg8N"))
    )
    download_btn.click()
    export_finish = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "export-confirm-button"))
    )
    export_finish.click()
    download_btn = WebDriverWait(browser, 180).until(
        EC.presence_of_element_located((By.CLASS_NAME, "downloadButton"))
    )
    download_btn.click()
    time.sleep(10)


def create_video():
    browser.maximize_window()
    login()
    print("(done) login")
    time.sleep(3)
    guide_buttons()
    print("(done) guide buttons")
    upload_video()
    print("(done) upload video")
    time.sleep(2)
    fill_video()
    print("(done) fill video")
    time.sleep(2)
    mute_video()
    print("(done) mute")
    time.sleep(2)
    upload_voice()
    print("(done) upload voice")
    time.sleep(2)
    export_video()
    time.sleep(2)
    print("FINISH")


create_video()
