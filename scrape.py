import requests
from bs4 import BeautifulSoup
import asyncio
import aiohttp
import random


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
            return None

    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}") 
        return None

async def grab(url, sem):

    random_time = random.uniform(1.0, 3.0)
    await asyncio.sleep(random_time)

    async with sem:

        async with aiohttp.ClientSession() as session:

            try:
                async with session.get(url, headers=headers) as response:
                    if response.status == 200:
                        html = await response.text()
                        return html
                    else:
                        print(f"failed to fetch {url}, status: {response.status}")

            except aiohttp.ClientError as e:
                print(f"network error: {e}")


    
