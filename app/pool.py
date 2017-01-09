from multiprocessing import Pool
from os import getpid, cpu_count


def count_number(file_name, number):
    """
    统计一个大文件里指定 byte 的个数，为了跑在不同进程上所以没有优化
    """

    print('searching %s:(%s)' % (number, getpid()))
    with open(file_name, 'rb') as f:
        count = 0
        while True:
            data = f.read(1024)
            if not data:
                break
            for d in data:
                if d == number:
                    count += 1

    print('found %s=%s (%s)' % (number, count, getpid()))


pool = Pool(cpu_count())

for i in range(0, 6):
    pool.apply_async(count_number, args=('/tmp/out', i))

print('waiting')
pool.close()
pool.join()
print('done')
