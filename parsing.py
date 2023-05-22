from edit_dist import most_likely_match
from substring import find_possible_meaning


def parse_v1(user_string, possibilities):
    poss = find_possible_meaning(user_string=user_string, stops=possibilities)
    # print(poss)
    return most_likely_match(user_word=user_string, possibilities=poss)


if __name__ == "__main__":
    s = ["Depart Ward", "Sheridan/Loyola", "Chicago/Kedzie", "Chicago/Greenleaf (northbound)", "Chicago/Davis", "Weber Arch", "Jacobs Center", "Tech Institute", "Patten Gym", "Central L Station (westbound)", "Central/Jackson (westbound)", "Arrive Ryan Field"]
    print(parse_v1("Ch", s))