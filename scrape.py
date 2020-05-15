'''
Scraping the latest news from Australia CNN
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Scraper:
    """Class to scrape CNN latest news """

    def __init__(self):
        self.headline = set()

    def scraper(self):
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
            return

        #find the latest news by find_elements_by_xpath
        headline_element = browser.find_elements_by_xpath("//h3[@data-analytics='Australia latest_list-xs_article_']")
        self.headline = {x.text for x in headline_element}

    def print_headline(self):
        """Print the headline"""
        if len(self.headline) == 0:
            print("None")
        else:
            print("Headlines:")
            for title in self.headline:
                print(title)

if __name__ == "__main__":
    cnn_headline = Scraper()
    cnn_headline.scraper()
    cnn_headline.print_headline()
