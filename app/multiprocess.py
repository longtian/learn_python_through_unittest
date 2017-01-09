from multiprocessing import Process
from os import getpid
from time import sleep


def child(name, index):
    print('child %s(%s)' % (name, getpid()))
    sleep(index)


for x in range(5):
    p = Process(target=child, args=('test-' + str(x), x))
    p.start()

    # parent will not wait for each child
    # p.join()
