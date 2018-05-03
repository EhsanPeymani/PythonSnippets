# talkpython.fm
from enum import Enum


def less_pythonic_approach(move: str):
    if move == Move.East or move == Move.West or move == Move.North or move == Move.South:
        print('This is a direct move.')
    else:
        print('This is diagonal move.')


def more_pythonic_approach(move: str):
    direct_moves = {Move.South, Move.North, Move.East, Move.West}

    if move in direct_moves:
        print('This is a direct move.')
    else:
        print('This is diagonal move.')


def main():
    user_text = input('what direction [n,e,w,s, ne, nw, se, sw] ? ')

    move = Move.parse(user_text)

    if not move: # if move is None:
        print('It is not a move!!!')
        return

    # less_pythonic_approach(move)
    more_pythonic_approach(move)


class Move(Enum):
    West = 1
    North = 2
    East = 3
    South = 4
    NorthEast = 5
    SouthEast = 6
    NorthWest = 7
    SouthWest = 8

    @staticmethod
    def parse(text: str):
        if not text:
            return None

        text = text.strip().lower()

        if text == 'w':
            return Move.West
        if text == 'e':
            return Move.East
        if text == 'n':
            return Move.North
        if text == 's':
            return Move.South

        if text == 'nw':
            return Move.NorthWest
        if text == 'ne':
            return Move.NorthEast
        if text == 'sw':
            return Move.SouthWest
        if text == 'se':
            return Move.SouthEast

        return None


if __name__ == '__main__':
    main()
