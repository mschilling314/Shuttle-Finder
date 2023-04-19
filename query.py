import pandas as pd
import constants as c
import os


def grab_data(direction: int) -> pd.DataFrame:
    """
    Gets the data and puts it into Pandas DataFrame format.

    Input:
    direction:  0 if going to Chicago, 1 if going to Evanston.

    Outputs:
    The Pandas DataFrame corresponding to the correct schedule.
    """
    return pd.read_csv(os.path.join("data", c.shuttle_csvs[direction] + ".csv"))


def make_query(df: pd.DataFrame, stop: str, time: int) -> int:
    """
    Makes a query to find the index that a time would be inserted into the schedule, useful for figuring out when the next time the shuttle will be at the given stop is.

    Inputs:
    df:  The schedule, formatted with the headers being stop names, the entries being stop times in hhmm or hmm format.
    stop:  The stop you're interested in.
    time:  What time you're interested in.

    Outputs:
    time_index:  The index of the first time strictly after time.
    """
    time_index = df[stop].searchsorted(time, side='right')
    return time_index


def find_next_shuttle(df: pd.DataFrame, stop: str, time: int) -> int:
    """
    Gives the time of the next shuttle given a stop and time you want to leave.

    Inputs:
    df:  The schedule, formatted with the headers being stop names, the entries being stop times in hhmm or hmm format.
    stop: The stop.
    time:  The time you want to inquire about.

    Outputs:
    The first time the shuttle will be at the stop strictly after the time you inquire about.
    """
    time_index = make_query(df, stop, time)
    return df[stop][time_index]


def find_departure_time_to_arrive_by(df: pd.DataFrame, source: str, dest: str, arr_time: int) -> int:
    """
    Finds the time you'll need to depart by to get to a stop by a given time

    Inputs:
    df:  The schedule of the shuttle.
    source:  The stop you leave from.
    dest:  The stop you're going to.
    depart_time:  The time you want to arrive.

    Outputs:
    Your departure time.
    """
    time_index = make_query(df=df, stop=dest, time=arr_time)
    if time_index > 0:
        time_index -= 1
    return df[source][time_index]


def find_arrival_time_if_leaving_at(df: pd.DataFrame, source: str, dest: str, depart_time: int) -> int:
    """
    Finds the time you'll arrive at a stop if you leave another stop at a given time.

    Inputs:
    df:  The schedule of the shuttle.
    source:  The stop you leave from.
    dest:  The stop you're going to.
    depart_time:  The time you leave source.

    Outputs:
    Your arrival time.
    """
    time_index = make_query(df=df, stop=source, time=depart_time)
    return df[dest][time_index]


def find_first(df: pd.DataFrame, stop: str) -> int:
    """
    Given a schedule and stop, returns the first time the shuttle is at that stop.

    Inputs:
    df: The schedule, formatted with the headers being stop names, the entries being stop times in hhmm or hmm format.
    stop:  The name of the stop.

    Outputs:
    An int that is the fist time the stop is visited.
    """
    return df[stop][0]


def find_last(df: pd.DataFrame, stop: str) -> int:
    """
    Given a schedule and stop, returns the last time the shuttle is at that stop.

    Inputs:
    df: The schedule, formatted with the headers being stop names, the entries being stop times in hhmm or hmm format.
    stop:  The name of the stop.

    Outputs:
    An int that is the last time the stop is visited.
    """
    return df[stop][len(df[stop])-1]


def query_from_structured_input() -> None:
    """
    Meant to make a query based on a series of answers to questions.  Need to fix to fail gracefully.
    """
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
    

if __name__=="__main__":
    query_from_structured_input()