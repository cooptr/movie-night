from bs4 import BeautifulSoup
from scrape import soupify
import math
import asyncio
from scrape import grab
url = "https://letterboxd.com/bwbrewster/watchlist/page/"

def list_page_movies(html):

    soup = BeautifulSoup(html, 'html.parser')
    
    parent_list = soup.find(class_="grid -p125 -scaled128")
    movies = parent_list.find_all("div", class_="react-component")
    for movie in movies:
        print(movie.get('data-item-full-display-name'))

async def generate_watchlist_links(url):

    sem = asyncio.Semaphore(10)

    first_url = url + '1/'
    html = await grab(first_url, sem)
    soup = BeautifulSoup(html, "html.parser")

    page_count_string = soup.find(class_="js-watchlist-count").text
    page_count = math.ceil(int(page_count_string.split('f')[0][:-1].replace(",",""))/28)
    links = []
    i = 0
    while i < page_count:
        i += 1
        current_page_number = str(i)
        current_page = url + current_page_number + '/'
        links.append(current_page)
    return(links)

async def main(url):

    sem = asyncio.Semaphore(10)

    links = await generate_watchlist_links(url)
    coros = [grab(url, sem) for url in links]
    results = await asyncio.gather(*coros)
    for result in results:
        list_page_movies(result)

asyncio.run(main(url))



