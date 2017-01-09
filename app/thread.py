from threading import Thread, current_thread


def count_number(file_name, number):
    """
    统计一个大文件里指定 byte 的个数

    在一个进程的不同线程里访问文件感觉很慢啊

    估计是因为 GIL 锁的问题
    """

    name = current_thread().name

    print('searching %s:(%s)' % (number, name))
    with open(file_name, 'rb') as f:
        count = 0
        while True:
            data = f.read(1024)
            if not data:
                break
            for d in data:
                if d == number:
                    count += 1

    print('found %s=%s (%s)' % (number, count, name))


def create_thread(i):
    return Thread(target=count_number, args=('/tmp/out', i), name="SearchThread#" + str(i))


threads = [create_thread(i) for i in range(5)]

list(map(lambda s: s.start(), threads))

print('ok')

list(map(lambda s: s.join(), threads))

print('done')
