import requests
from bs4 import BeautifulSoup

#url = "https://letterboxd.com/lucas_sequeira/watchlist/page/1/"

headers = {

    'User-Agent': 'Mozilla/5.0',
    'Accept-Language': 'en-US,en;q=0.5'
}


def soupify(url):

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            html_content = response.content
            soup = BeautifulSoup(html_content, "html.parser")
            return soup

        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}") 
   
