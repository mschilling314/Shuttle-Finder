import pandas as pd
import constants as c
import os
import bisect


def grab_data(direction: int):
    return pd.read_csv(os.path.join("data", c.shuttle_csvs[direction] + ".csv"))


def make_query(df: pd.DataFrame, stop: str, time: int):
    times = df[stop].tolist()
    time_index = bisect.bisect_right(times, time)
    return time_index


def find_next_shuttle(df: pd.DataFrame, stop: str, time: int):
    times = df[stop].tolist()
    return times[make_query(df=df, stop=stop, time=time)]


def find_departure_time_to_arrive_by(df: pd.DataFrame, source: str, dest: str, arr_time: int):
    time_index = make_query(df=df, stop=dest, time=arr_time)
    src = df[source].tolist()
    if time_index > 0:
        time_index -= 1
    return src[time_index]


def find_arrival_time_if_leaving_at(df: pd.DataFrame, source: str, dest: str, depart_time: int):
    time_index = make_query(df=df, stop=source, time=depart_time)
    dst = df[dest].tolist()
    return dst[time_index]


def find_first(df: pd.DataFrame, stop: str):
    return df[stop].tolist()[0]


def find_last(df: pd.DataFrame, stop: str):
    return df[stop].tolist()[-1]


if __name__=="__main__":
    sched = grab_data(direction=0)
    print(find_next_shuttle(sched, "Chicago/Sheridan", 1520))
    print(find_departure_time_to_arrive_by(sched, "Chicago/Sheridan", "Arrive Ward", 1700))
    print(find_arrival_time_if_leaving_at(sched, "Chicago/Sheridan", "Arrive Ward", 1520))
    print(find_first(sched, "Arrive Ward"))
    print(find_last(sched, "Arrive Ward"))