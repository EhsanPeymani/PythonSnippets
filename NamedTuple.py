# idea from talkpython.fm
import collections

Rating = collections.namedtuple("Rating", "id, x, y, rating")


def main():
    list_rating = []

    for data in get_data():
        print("Id:{}, rating={}, position=({}, {})".format(
              data.id, data.rating, data.x, data.y))

        list_rating.append(data.rating)

    print('List of rating is: {}'.format(list_rating))

    print('This is the namedtuple: {}'.format(get_data()))


def get_data():
    data = [Rating(1, 2.3, 3.4, 90),
            Rating(2, 5.6, 8.1, 70),
            Rating(3, 5.5, 1.2, 85)]

    return data


if __name__ == "__main__":
    main()

