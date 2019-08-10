from bs4 import BeautifulSoup
from selenium import webdriver

class NaverMovie:
    def __init__(self,url):
        driver=webdriver.Chrome('data/chromedriver')
        self.driver.get(url)
        self.soup=BeautifulSoup(driver.page_source,'html.parser')

    def scrap(self):
        html=self.soup.prettify()
        #print(html)
        all_divs=self.soup.find_all('div',attrs={'class':'tit3'})
        arr=[div.a.span.string for div in all_divs]
        for i in arr:
            print(i)
        self.driver.close()



