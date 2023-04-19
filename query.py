import pandas as pd
import constants as c
import os


def grab_data(direction: int):
    return pd.read_csv(os.path.join("data", c.shuttle_csvs[direction] + ".csv"))


def make_query(df: pd.DataFrame, stop: str, time: int):
    time_index = df[stop].searchsorted(time, side='right')
    return time_index


def find_next_shuttle(df: pd.DataFrame, stop: str, time: int):
    time_index = make_query(df, stop, time)
    return df[stop][time_index]


def find_departure_time_to_arrive_by(df: pd.DataFrame, source: str, dest: str, arr_time: int):
    time_index = make_query(df=df, stop=dest, time=arr_time)
    if time_index > 0:
        time_index -= 1
    return df[source][time_index]


def find_arrival_time_if_leaving_at(df: pd.DataFrame, source: str, dest: str, depart_time: int):
    time_index = make_query(df=df, stop=source, time=depart_time)
    return df[dest][time_index]


def find_first(df: pd.DataFrame, stop: str):
    return df[stop][0]


def find_last(df: pd.DataFrame, stop: str):
    return df[stop][len(df[stop])-1]


if __name__=="__main__":
    dir = int(input("\nPlease enter 0 if going to Chicago, 1 if going to Evanston.\n"))
    sched = grab_data(direction=dir)
    fun = int(input("\nPlease input:\n0 for next shuttle \n1 for Depart to Arrive by \n2 for Arrive Leaving at \n3 for First\n4 for last\n"))
    if fun in {0, 3, 4}:
        stop = input("\nWhat stop did you want to inquire about? ")
    else:
        source = input("\nWhat stop will you leave from?\n")
        dest = input("\nWhat stop are you going to?\n")
    if fun in {0, 1, 2}:
        time = int(input("\nWhat time did you have in mind?\n"))
    print("\nTime: ")
    
    if fun == 0:
        print(find_next_shuttle(sched, stop, time))
    elif fun == 1:
        print(find_departure_time_to_arrive_by(sched, source, dest, time))
    elif fun == 2:
        print(find_arrival_time_if_leaving_at(sched, source, dest, time))
    elif fun == 3:
        print(find_first(sched, stop))
    elif fun == 4:
        print(find_last(sched, stop))
    

    # print(find_next_shuttle(sched, "Chicago/Sheridan", 1520))
    # print(find_departure_time_to_arrive_by(sched, "Chicago/Sheridan", "Arrive Ward", 1700))
    # print(find_arrival_time_if_leaving_at(sched, "Chicago/Sheridan", "Arrive Ward", 1520))
    # print(find_first(sched, "Arrive Ward"))
    # print(find_last(sched, "Arrive Ward"))