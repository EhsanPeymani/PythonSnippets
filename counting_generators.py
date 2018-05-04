from generators import fibionachi


def fib_less_than(limit: int):
    for n in fibionachi():
        if n > limit:
            break
        yield n


# we want to count the number of items in fib_less_than(20000)
count = sum(1 for _ in fib_less_than(20000))
print('count is ', count)