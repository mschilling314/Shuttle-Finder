from query import query_for_time


def cli_input() -> dict:
    """
    Prompts a user for various inputs in order to make a structured query.

    Output is structured as a dictionary with the following str keys:
    fun (required): holds an integer from 0-4 inclusive, corresponding to a query
    dir (required): holds either 0 or 1 as an integer, corresponds to the direction we're going in
    src: str for a stop, corresponds to departure and arrival time queries
    dst: str for a stop, corresponds to departure and arrival time queries
    time: formatted int (hmm or hhmm) required for next, departure, arrival time queries
    stop: str for a stop, corresponds to next, first, last queries
    """
    res = {}
    res["dir"] = int(input("\nPlease enter 0 if going to Chicago, 1 if going to Evanston.\n"))
    res["fun"] = int(input("\nPlease input:\n0 for next shuttle \n1 for Depart to Arrive by \n2 for Arrive Leaving at \n3 for First\n4 for last\n"))
    if res["fun"] in {0, 3, 4}:
        res["stop"] = input("\nWhat stop did you want to inquire about? ")
    else:
        res["src"] = input("\nWhat stop will you leave from?\n")
        res["dst"] = input("\nWhat stop are you going to?\n")
    if res["fun"] in {0, 1, 2}:
        res["time"] = input("\nWhat time did you have in mind?\n")
    return res


def format_time(t: int) -> str:
    minu = t % 100
    hour = t // 100
    indicator = False
    if hour > 12:
        indicator = True
        hour -= 12
    res = f"{hour}:{minu} "
    if indicator:
        res += "PM"
    else: 
        res += "AM"
    return res


def run_cli() -> None:
    """
    Runs the CLI, performing a query on the Intercampus database as per user inputs, looping until the user wants to stop.
    """
    cont = True
    while cont:
        structured_input = cli_input()
        time = query_for_time(**structured_input)
        f_time = format_time(t=time)
        print(f"\nThe time that results from your query is {f_time}.\n")
        contin = input("Input 0 to quit, or any other key to continue. ")
        if contin == "0":
            cont = False


if __name__=="__main__":
    run_cli()

