# https://schedule.readthedocs.io/en/stable/?__s=pmg5mgpk3vbznnh9d3t1
import time
import datetime
import schedule


def task1():
    s = 'Working, {}'.format(datetime.datetime.now())
    print(s)


def task_run_once():
    task1()
    return schedule.CancelJob


# schedule.every(1).seconds.do(task1)
# schedule.every().day.at('15:25').do(task_run_once)
schedule.every(2).seconds.do(task_run_once)

while True:
    schedule.run_pending()
    time.sleep(1)

