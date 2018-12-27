from collections import deque, defaultdict


def solver(max_players: int, max_marble: int):
    result_board = deque([0])
    players_score = defaultdict(int)

    for marble in range(1, max_marble + 1):
        if marble % 23 == 0:
            result_board.rotate(7)
            players_score[marble % max_players] += marble + result_board.pop()
            result_board.rotate(-1)
        else:
            result_board.rotate(-1)
            result_board.append(marble)
    print("Winnig score: {}".format(players_score.get(max(players_score.keys(), key = lambda k: players_score[k]))))


if __name__ == "__main__":
    solver(9, 25)
    solver(10, 1618)
    solver(13, 7999)
    solver(17, 1104)
    solver(21, 6111)
    solver(30, 5807)
    solver(458, 71307)
    solver(458, 7130700)