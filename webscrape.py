import requests
from bs4 import BeautifulSoup


def get_schedule(url: str, deposit: str) -> None:
    """
    Gets an up-to-date schedule assuming no changes in service, writes it to a 2D CSV.

    Inputs:
    url:  Must point to a valid Northwestern-style shuttle schedule.
    deposit:  Path to where you want to write the file, may need to change to os.path?

    Outputs:
    A CSV file, but as a side-effect, not a return.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('tr')
    print(articles)



if __name__ == '__main__':
    get_schedule