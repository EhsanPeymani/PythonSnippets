# talkpython.fm

# the idea is to rewrite the static class parse(text) form Move using dictionary
# from multiple_tests_against_one_variable import Move

# we can do this approach for calling functions or callables

from enum import Enum


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

        # dictionary as switch case
        parse_dict = {
            'w': Move.West, 'e': Move.East, 'n': Move.North, 's': Move.South,
            'nw': Move.NorthWest, 'ne': Move.NorthEast, 'sw': Move.SouthWest, 'se': Move.SouthEast
        }

        return parse_dict.get(text, None)

    @staticmethod
    def careful_selection(text: str):
        if not text:
            return None

        text = text.strip().lower()

        # dictionary as switch case
        # use functions for values
        care_dict = {
            'n': lambda: print('North. Very Dangerous'),
            's': lambda: print('South. Make sure this is the right direction')
        }

        action = care_dict.get(text, lambda: print('Fine to go.'))
        return action()


print('n:', Move.parse('n'))
print('ns:', Move.parse('ns'))


Move.careful_selection('n')
Move.careful_selection('s')
Move.careful_selection('nz')
