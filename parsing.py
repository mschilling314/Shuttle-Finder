from edit_dist import most_likely_match
from substring import find_possible_meaning


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


if __name__ == "__main__":
    s = ["Depart Ward", "Sheridan/Loyola", "Chicago/Kedzie", "Chicago/Greenleaf (northbound)", "Chicago/Davis", "Weber Arch", "Jacobs Center", "Tech Institute", "Patten Gym", "Central L Station (westbound)", "Central/Jackson (westbound)", "Arrive Ryan Field"]
    print(parse_v1("Wad", s))