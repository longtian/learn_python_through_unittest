import os
import time

pid = os.fork()


def start_server():
    time.sleep(1)


if pid < 0:
    print('fail')
elif pid == 0:
    print('child')
    start_server()
else:
    print('parent')
    time.sleep(1)
