from edit_dist import most_likely_match
from substring import find_possible_meaning
import re


def parse_v1(user_string, possibilities):
    """
    Issues to fix in v2:
    - Noiyes -> gives an error higher up bc this says there are no matches since we filter for substring first
      - Possible solution is to do a try/except style logic?
      - In general prone to spelling errors I think, for example what would happpen if I tried "Wad"
    - Weird returned result
    """
    poss = find_possible_meaning(user_string=user_string, stops=possibilities)
    # print(f"Parsing poss: {poss}")
    return most_likely_match(user_word=user_string, possibilities=poss)


def parse_v2(user_string: str, possibilities: list) -> str:
    """
    Essentially, this first tries to narrow the scope of possible stops by seeing if the user's input is a substring, before identifying the most likely match based on pure edit distance.

    Inputs:
    user_string:  The user's input for a stop.
    possibilities:  The list of possible stops.

    Output:
    A string corresponding to a stop from the possibilities list, which will allow for querying.
    """
    poss = find_possible_meaning(user_string=user_string, stops=possibilities)
    if len(poss) == 0:
        poss = possibilities
    print(most_likely_match(user_word=user_string, possibilities=poss))
    return most_likely_match(user_word=user_string, possibilities=poss)


def parse_time(t: str) -> int:
    """
    Uses a singular regex expression derived through some trial and error to return time in the proper format of hhmm.

    Input:
    t:  A user input that can have any format like h:mm, hh.mm, hh:mm a.m etc.

    Output:
    An integer in 24 hour hhmm format
    """
    pattern = r"(\d{1,2})[.:](\d{2})(\s?)(?:([ap])(?:\.\s?)(?:m)?)?"
    match = re.search(pattern, t, re.IGNORECASE)
    if match:
        hour = int(match.group(1))
        minu = int(match.group(2))
        indicator = match.group(4)
        if indicator:
            if indicator[0].lower() == "p":
                hour += 12
        return (hour * 100) + minu
    raise ValueError("Invalid time input.")


if __name__ == "__main__":
    s = ["Depart Ward", "Sheridan/Loyola", "Chicago/Kedzie", "Chicago/Greenleaf (northbound)", "Chicago/Davis", "Weber Arch", "Jacobs Center", "Tech Institute", "Patten Gym", "Central L Station (westbound)", "Central/Jackson (westbound)", "Arrive Ryan Field"]
    print(parse_v1("Wad", s))