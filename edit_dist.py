import numpy as np


def del_cost():
    return 1

def ins_cost():
    return 1

def sub_cost(c1, c2):
    if c1 == c2: 
        return 0
    else:
        return 2


def min_edit_distance(source: str, target: str) -> int:
    """Compare `source` and `target` strings and return their edit distance with
    Levenshtein costs, according to the algorithm given in SLP Ch. 2, Figure 2.17.

    Parameters
    ----------
    source : str
        The source string.
    target : str
        The target string.

    Returns
    -------
    int
        The edit distance between the two strings.
    """
    n = len(source)
    m = len(target)
    dist = np.zeros((n+1, m+1))
    
    for i in range(1, n+1):
        dist[i, 0] = dist[i-1, 0] + del_cost()
    for j in range(1, m+1):
        dist[0, j] = dist[0, j-1] + ins_cost()

    for i in range(1, n+1):
        for j in range(1, m+1):
            dist[i, j] = min(dist[i-1, j] + del_cost(),
                             dist[i-1, j-1] + sub_cost(source[i-1], target[j-1]),
                             dist[i, j-1] + ins_cost())
    return int(dist[n, m])


def most_likely_match(user_word: str, possibilities: list) -> str:
    best_match = possibilities[0]
    dist = min_edit_distance(user_word.upper(), possibilities[0].upper())
    for possibility in possibilities:
        p = possibility.upper()
        u = user_word.upper()
        d = min_edit_distance(p, u)
        # print(f"{p} {d}")
        if d < dist:
            dist = d
            best_match = possibility
    return best_match

  


if __name__ == "__main__":
    s = ["Depart Ward", "Sheridan/Loyola", "Chicago/Kedzie", "Chicago/Greenleaf (northbound)", "Chicago/Davis", "Weber Arch", "Jacobs Center", "Tech Institute", "Patten Gym", "Central L Station (westbound)", "Central/Jackson (westbound)", "Arrive Ryan Field"]
    print(most_likely_match("Central", s))
