from selenium import webdriver
# from selenium.webdriver.common.proxy import Proxy, ProxyType
import os, io
# from config import basedir
import time
from flask import Flask
from flask import render_template, redirect, request, url_for, session, send_file, Response
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
        # options.binary_location = '/app/.apt/usr/bin/google-chrome-stable'
        options.binary_location = '/app/.apt/usr/bin/google-chrome'

        print(GOOGLE_CHROME_SHIM)
        print(GOOGLE_CHROME_SHIM)
        options.add_argument("--headless")
        #options.add_argument("--disable-gpu")


    if ua:
        # ua_string = '--user-agent=' + '"' + ua + '"'
        # ua_string = 'user-agent=' + ua
        # options.add_argument(ua_string)
        # mobile_emulation = {"deviceName": "Nexus 7"}
        #mobile_emulation =  {"deviceName": "Nexus 5"}
        #mobile_emulation =  {"deviceName": "LG Optimus One", "width": 213, "height": 320, "deviceScaleFactor": 1.5, "userAgent": "Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; LG-MS690 Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1", "touch": "true", "mobile": "true"}
        mobile_emulation = {"deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 }, "pixelRatio":3.0, "mobileEmulationEnabled":True, "userAgent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) " +
                                                                                                                                                              "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Mobile Safari/537.36"}
        options.add_experimental_option("mobileEmulation", mobile_emulation)

    return webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options, service_args=["--verbose", "--log-path=%s/chromedriver.log" %(basedir)])


def some_long_calculation():
    driver = create_chromedriver(True)
    #driver = create_chromedriver()
    print(driver.capabilities['version'])
    # driver.get("https://www.foxnews.com/")
    # driver.get("https://www.yahoo.com/news/")
    driver.get("https://boston.craigslist.org/")
    # driver.find_element_by_id("yui_3_18_0_4_1519680410096_1347").click()
    # driver.find_element_by_id("yui_3_18_0_4_1519680410096_1347").click()

    # print(1)
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
