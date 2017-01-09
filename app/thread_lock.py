from threading import Thread, Lock

num = 0
lock = Lock()


def calc():
    global num
    for _ in range(1000):
        lock.acquire()
        num += 1
        lock.release()


threads = [];

for i in range(5):
    threads.append(Thread(target=calc))

list(map(lambda s: s.start(), threads))

list(map(lambda s: s.join(), threads))

print(num)
