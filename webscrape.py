import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_schedule(url: str) -> pd.DataFrame:
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
    
    stop_names = []
    stop_times = []
    for index in range(len(articles)):
        row = articles.find_all('td')
        stop_names.append(row[0].text.strip())
        row.pop(0)
        times = []
        for item in row:
            times.append(item.text.strip())
        stop_times.append(times)
    df = pd.DataFrame({"Stop": stop_names, "Time": stop_times})
    df.set_index("Stop", inplace=True)
    return df



if __name__ == '__main__':
    print(get_schedule("https://www.northwestern.edu/transportation-parking/shuttles/routes/schedules/intercampus-evanston-to-chicago.html"))