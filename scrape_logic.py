from bs4 import BeautifulSoup
from scrape import soupify

url = "https://letterboxd.com/lucas_sequeira/watchlist/page/2/"

def list_movies(url):
    
    soup = soupify(url)
    parent_list = soup.find(class_="grid -p125 -scaled128")

    movies = parent_list.find_all("div", class_="react-component")

    for movie in movies:
        print(movie.get('data-item-full-display-name'))
    #print(type(parent_list.find_all("div")))


list_movies(url)