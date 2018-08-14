from selenium import webdriver
# from selenium.webdriver.common.proxy import Proxy, ProxyType
import os, io
# from config import basedir
import time
from flask import Flask
from flask import render_template, redirect, request, url_for, session, send_file, Response
# from glob import glob
# from random import shuffle
# import xml.etree.ElementTree as ET
# import spintax
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# from PIL import Image
import json


basedir = os.path.abspath(os.path.dirname(__file__))

def create_chromedriver(ua=False):
    options = webdriver.ChromeOptions()
    CHROMEDRIVER_PATH = os.getenv('$HOME') or basedir+'/chromedriver.exe'
    FLASK_CONFIG = os.getenv('FLASK_CONFIG')



    if FLASK_CONFIG and FLASK_CONFIG == "production":
        # CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
        CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
        GOOGLE_CHROME_SHIM = os.getenv('$GOOGLE_CHROME_SHIM') or 'no path found'
        options.binary_location = '/app/.apt/usr/bin/google-chrome-stable'
        # options.binary_location = '/app/.apt/usr/bin/google-chrome'/
        # options.binary_location = '/app/.apt/opt/google/chrome/chrome'
        # options.binary_location = '/app/.apt/opt/google/chrome/'
        # options.binary_location = GOOGLE_CHROME_SHIM

        print(GOOGLE_CHROME_SHIM)
        print(GOOGLE_CHROME_SHIM)
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")

        # options.add_argument("--start-maximized")
        # options.add_argument("--disable-infobars")
        # options.add_argument("--disable-extensions")
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-dev-shm-usage")

    if ua:
        print('ua block33')
        # ua_string = '--user-agent=' + '"' + ua + '"'
        # ua_string = 'user-agent=' + ua
        # options.add_argument(ua_string)
        # mobile_emulation = {"deviceName": "Nexus 7"}
        mobile_emulation =  {"deviceName": "iPad Mini"}
        # mobile_emulation =  {"deviceName": "LG Optimus One"}
        # mobile_emulation =  {"deviceName": "LG Optimus One", "width": 213, "height": 320, "deviceScaleFactor": 1.5, "userAgent": "Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; LG-MS690 Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1", "touch": "true", "mobile": "true"}
        options.add_experimental_option("mobileEmulation", mobile_emulation)

        # options = webdriver.ChromeOptions()

        capabilities = options.to_capabilities()

        # driver = webdriver.Remote( command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=capabilities)

        # from selenium import webdriver
        # mobile_emulation = {"deviceName": "Nexus 5"}
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        # driver = webdriver.Remote(executable_path=CHROMEDRIVER_PATH,command_executor='http://127.0.0.1:4444/wd/hub',
        #                           desired_capabilities=options.to_capabilities())


        # return webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,desired_capabilities=capabilities, options=options)
    return webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)
    # return webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,goog:chromeOptions=options )


    # return webdriver.Remote(executable_path=CHROMEDRIVER_PATH, command_executor='http://127.0.0.1:4444/wd/hub',
    #                       desired_capabilities=options.to_capabilities())





def some_long_calculation():
    driver = create_chromedriver(True)
    # driver = create_chromedriver()
    print(driver.capabilities['version'])
    print(driver.capabilities['version'])

    driver.get("https://www.yahoo.com/")
    # driver.get("https://www.yahoo.com/news/")
    # driver.find_element_by_id("yui_3_18_0_4_1519680410096_1347").click()
    # driver.find_element_by_id("yui_3_18_0_4_1519680410096_1347").click()

    print(1)
    # yield "<br/>"

    # https: // www.yahoo.com / news /
    # time.sleep(5)
    png = driver.get_screenshot_as_png()
    driver.close()

    # return 'a'
    return png

test_app = Flask(__name__)


@test_app.route('/')
def sanity_check():
    png = some_long_calculation()

    return send_file(io.BytesIO(png),mimetype='image/png')


if __name__ == '__main__':
    test_app.run(debug=True)