import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-x', type=int, help='input x', default=0)
parser.add_argument('-y', type=int, help='input y', default=0)

args = parser.parse_args()

print('x + y = ' + str(args.x + args.y))
