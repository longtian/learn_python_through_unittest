chunk_size = 1024 * 5


def copy_big(src, target):
    src_file = open(src, 'rb')
    target_file = open(target, 'wb')
    while True:
        data = src_file.read(chunk_size)

        if not data:
            break

        target_file.write(data)

# time python3 copy_big.py
#
# real    0m1.023s
# user    0m0.080s
# sys     0m0.224s
