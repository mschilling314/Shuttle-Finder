import requests
from bs4 import BeautifulSoup
import pandas as pd
import constants as c
import os


def get_schedule(url: str) -> pd.DataFrame:
    """
    Gets an up-to-date schedule assuming no changes in service, writes it to a 2D CSV.

    Inputs:
    url:  Must point to a valid Northwestern-style shuttle schedule.
    
    Outputs:
    A CSV file, but as a side-effect, not a return.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('tr')
    stops = {}
    articles.pop(0)
    for article in articles:
        row = article.find_all('td')
        name = row[0].text.strip().replace(" / ", "/")
        row.pop(0)
        times = []
        for item in row:
            time = item.text.strip()
            if time[-4] == "p" and time[0:2] != "12":
                hour = int(time.split(":")[0])
                hour += 12
                time = str(hour) + time[2:]
            time = time[0:-5]
            time = time.replace(":", "")
            # if len(time) < 4:
            #     time = '0' + time
            times.append(time)
        stops[name] = times
    df = pd.DataFrame.from_dict(stops)
    return df


def get_the_schedules():
    for index in range(len(c.shuttle_urls)):
        df = get_schedule(c.shuttle_urls[index])
        filename = os.path.join("./data", c.shuttle_csvs[index] + ".csv")
        df.to_csv(filename)





if __name__ == '__main__':
    # print(get_schedule("https://www.northwestern.edu/transportation-parking/shuttles/routes/schedules/intercampus-evanston-to-chicago.html"))
    get_the_schedules()
