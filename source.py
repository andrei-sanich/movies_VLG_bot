from bs4 import BeautifulSoup
from lxml import etree
from selenium import webdriver
import time


class WebSource():
    
   
    def __init__(self, url):

        self.url = url
        self.driver = webdriver.PhantomJS()
        
    
    def get_html(url):
    
        self.driver.get(self.url)
        html = driver.page_source
        return html
        

    def get_links_afisha(self):

        self.driver.get(self.url)
        try:
            button = self.driver.find_element_by_xpath("//input[@class='nice_button'][@type='button']")
            while button:
                button.click()
                time.sleep(1)
                button = self.driver.find_element_by_xpath("//input[@class='nice_button'][@type='button']")
        except:
            pass
        time.sleep(1)
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        movies = soup.find_all('div', {'class': 'name'})
        links = ["https://www.kinopoisk.ru" + movie.find('a').get('href') for movie in movies]
        return links
       
        
    def get_links_premieres(self):
        
        self.driver.get(self.url)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        movies = soup.find_all('span', {'class': 'name', 'itemprop': 'name'})
        links = ["https://www.kinopoisk.ru" + movie.find('a').get('href') for movie in movies]
        return links

    
    def get_info_about_movie(self):

        self.driver.get(self.url)
        time.sleep(10)
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        items = soup.find_all('div', {'id': 'content_block'})
        for item in items:
            name_rus = item.find('h1', {'class': 'moviename-big'}).text
            name_eng = item.find('span', {'itemprop': 'alternativeHeadline'}).text
        table = soup.find('table', {'class': 'info'})
        genres = [x.text for x in table.find('span', {'itemprop': 'genre'}).find_all('a')]
        countries = [x.text for x in table.find('td', {'class': 'type'}, text = u'страна').nextSibling.nextSibling.find_all('a')]
        directors = [x.text for x in table.find('td', {'itemprop': 'director'}).find_all('a')]
        writers = [x.text for x in table.find('td', {'class': 'type'}, text = u'сценарий').nextSibling.find_all('a')]
        rus_prem = table.find('td', {'id': 'div_rus_prem_td2'}).find('a').text
        info = {
                'name_rus': name_rus,
                'name_eng': name_eng,
                'genres': genres,
                'countries': countries,
                'directors': directors,
                'writers': writers,
                'rus_prem': rus_prem
                }
        return info