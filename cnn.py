'''
Scraping the latest news from Australia CNN
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def get_australia_latest():
    """Scraping CNN Australia latest news"""
    option = webdriver.ChromeOptions()
    option.add_argument("--incognito")

    browser = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver', options=option)

    browser.get("https://www.cnn.com/australia")

    #Wait 20 seconds for page to load
    time_out = 20

    try:
        #wait until the photo appear
        WebDriverWait(browser, time_out).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='media__image media__image--responsive']")))

    except TimeoutException:
        print("Time out for page to load")
        browser.quit()
        return []

    #find the latest news by find_elements_by_xpath
    headline_element = browser.find_elements_by_xpath("//h3[@data-analytics='Australia latest_list-xs_article_']")
    headline = [x.text for x in headline_element]

    browser.quit()
    return headline

def print_australia_latest(original_headline):
    """Remove the duplicated headlines and print the headlines"""
    #remove dublicated headline
    headline = set([x for x in original_headline])

    #print out the headline
    if len(headline) == 0:
        print("None")
        return 'None'

    print("Headlines:")
    for title in headline:
        print(title, '\n')
    return headline

headlines = get_australia_latest()
print_australia_latest(headlines)
