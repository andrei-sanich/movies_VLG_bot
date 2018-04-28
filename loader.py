import time
from datetime import datetime
import logging

import config
from source import WebSource
from storer import Storer


def url_premieres():
    
    url = 'https://www.kinopoisk.ru/premiere/ru/'
    month = int(datetime.now().strftime("%m"))
    year = datetime.now().strftime("%Y")
    url_premieres = url + "{}/month/{}/".format(year, month)
    return url_premieres


def main():

    try:
        links_afisha = WebSource(config.URL_AFISHA_VLG).get_links_afisha()
		
        afisha_movies = [WebSource(link).get_info_about_movie() for link in links_afisha]
        
        Storer('database.txt').save('afisha', afisha_movies)
		
        links_temp = WebSource(url_premieres()).get_links_premieres()
        
        links_premieres = [link for link in links_temp if link not in links_afisha]
        
        premieres_movies = [WebSource(link).get_info_about_movie() for link in links_premieres]
        
        Storer('database.txt').save('premieres', premieres_movies)
    except Exception as err:
        logging.error(err)
        time.sleep(5)
        print("Error!")


if __name__  == '__main__':
    main()
