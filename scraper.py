import time
from selenium import webdriver
from threading import Timer
from selenium.webdriver.chrome.options import Options

# Stock Prices Alert List Setup
watch_list = {
    "INTC" : {          # The Stock symbol e.g INTC = Intel Corporation
        "low" : 45,     # Alert when LIVE prices goes BELOW this value
        "high" : 90     # Alert when LIVE prices goes ABOVE this value
    },
    "TSLA" : {
        "low" : 400,
        "high" : 900
    },
    "FB" : {
        "low" : 160,
        "high" : 400
    },
    "BYND" : {
        "low" : 53,
        "high" : 200
    },
    "LON:AZN" : {
        "low" : 6700,
        "high" : 9500
    },
    "EBAY" : {
        "low" : 40,
        "high" : 70
    },
    "LON:AV" : {
        "low" : 210,
        "high" : 390
    },
    "SDRY" : {
        "low" : 89,
        "high" : 180
    },
    "LSE:GYM" : {
        "low" : 100,
        "high" : 300
    },
    "LLOY" : {
        "low" : 23,
        "high" : 60
    },
    "NEX" : {
        "low" : 100,
        "high" : 300
    }
}

# print(watch_list)

def checkPrice(symbol, low, high, live_data):
    if live_data < float(low):
        print(symbol +" @ "+ str(live_data) +"\nGood time to BUY \n**")

    if live_data > float(high):
        print(symbol +" @ "+ str(live_data) +"\nGood time to SELL \n**")


def live_price_check():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print('---------------- > PRICE CHECK START :' + current_time)

    for symbols in watch_list.items():
        symbolkey = symbols[0]

        # print('-')
        # print(watch_list[symbols[0]]['low'])
        # print(watch_list[symbols[0]]['high'])

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument("--disable-extensions")

        driver = webdriver.Chrome("./chromedriver", options=chrome_options)
        start_url = "https://www.google.com/search?q="+symbolkey+"+stocks"
        driver.get(start_url)

        live_data = float(driver.find_element_by_class_name("NprOob").text.replace(',',''))

        print(symbolkey + ' @ ' + str(live_data))
        driver.close()
        driver.quit()

        checkPrice(symbols[0], watch_list[symbols[0]]['low'], watch_list[symbols[0]]['high'], live_data)
        print("----------------")

    print('---------------- > PRICE CHECK COMPLETE')

    Timer(10*60,live_price_check).start()

live_price_check() # Execute the code


## Other Methods
# -----------------------------------------------------------------------------
# print(driver.title)
# print(driver.page_source.encode("utf-8"))
# search_bar = driver.find_element_by_name("q")
# search_bar.clear()
# search_bar.send_keys("getting started with python")
# search_bar.send_keys(Keys.RETURN)
# print(driver.find_element_by_class_name("NprOob")).text
# print(driver.current_url)

## Killing a script that is in progress
# -----------------------------------------------------------------------------
# pkill -9 -f scraper.py #macOs only
