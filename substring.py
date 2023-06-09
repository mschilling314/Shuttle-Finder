def find_possible_meaning(user_string: str, stops: list[str]):
    res = []
    user_string_cleaned = user_string.upper()
    for stop in stops:
        s = stop.upper()
        if user_string_cleaned in s:
            res.append(stop)
    return res


if __name__ == "__main__":
    s = ["Depart Ward", "Sheridan/Loyola", "Chicago/Kedzie", "Chicago/Greenleaf (northbound)", "Chicago/Davis", "Weber Arch", "Jacobs Center", "Tech Institute", "Patten Gym", "Central L Station (westbound)", "Central/Jackson (westbound)", "Arrive Ryan Field"]
    print(find_possible_meaning("chi", s))
