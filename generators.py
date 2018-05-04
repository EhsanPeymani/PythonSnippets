# talkpython.fm
# create a generator for fibionachi series\
# later we create another generator which returns even numbers
# using these 2 generators we create a pipeline
import time
import sys

def fibionachi():
    current, nxt = 0, 1
    yield current

    while True:
        current, nxt = nxt, nxt + current
        yield current


def even_numbers(input):
    for item in input:
        if item%2 == 0:
            yield item


def even_fib():
    for item in even_numbers(fibionachi()):
        yield item


for item in even_fib():
    print(item, end=', ')
    time.sleep(0.5)
    sys.stdout.flush()

    if item > 20000:
        break