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


def query_for_time(**kwargs) -> int:
    """
    Using properly structured input, returns an integer corresponding to the time resulting from the query.

    Input:
    fun (required): holds an integer from 0-4 inclusive, corresponding to a query
    dir (required): holds either 0 or 1 as an integer, corresponds to the direction we're going in
    src: str for a stop, corresponds to departure and arrival time queries
    dst: str for a stop, corresponds to departure and arrival time queries
    time: formatted int (hmm or hhmm) required for next, departure, arrival time queries
    stop: str for a stop, corresponds to next, first, last queries

    Output:
    time: an int formatted as hmm or hhmm
    """
    if "fun" not in kwargs.keys() or "dir" not in kwargs.keys():
        raise ValueError("Function or direction missing from query.")
    sched = grab_data(direction=kwargs["dir"])
    fun = kwargs["fun"]
    try:
        if fun == 0:
            time = find_next_shuttle(sched, kwargs["stop"], kwargs["time"])
        elif fun == 1:
            time = find_departure_time_to_arrive_by(sched, kwargs["src"], kwargs["dst"], kwargs["time"])
        elif fun == 2:
            time = find_arrival_time_if_leaving_at(sched, kwargs["src"], kwargs["dst"], kwargs["time"])
        elif fun == 3:
            time = find_first(sched, kwargs["stop"])
        elif fun == 4:
            time = find_last(sched, kwargs["stop"])
        else:
            raise ValueError("Invalid function argument given.")
    except:
        raise ValueError("Invalid arguments given.")
    return time

