# =============================================================================
# Chrome Dino bot using Selenium+PIL
# Author: Michael Sumaya
# =============================================================================
import threading
from io import BytesIO
from selenium import webdriver
from selenium.webdriver import ActionChains as ac, Keys
from PIL import Image

GAME_URL = "chrome://dino/"

# Check position
X, Y = 200, 300
# Size
W, H = 100, 25


def jump_and_duck(driver):
    ac(driver).reset_actions()
    ac(driver).send_keys(Keys.SPACE).perform()


chrome = webdriver.Chrome()
try:
    chrome.get(GAME_URL)
except:
    # This is expected
    pass

ac(chrome).send_keys(Keys.SPACE).perform()

while True:
    try:
        ss = chrome.get_screenshot_as_png()
        with Image.open(BytesIO(ss)) as img:
            roi = img.crop((X, Y, X+W, Y+H))

        if roi.getcolors(1) == None:
            threading.Thread(target=jump_and_duck, args=[chrome]).start()
    except:
        break
