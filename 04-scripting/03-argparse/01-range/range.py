import argparse

parser = argparse.ArgumentParser(prog='Range')
parser.add_argument('start', type=int, help='start of range')
parser.add_argument('end', type=int, help='end of range')
parser.add_argument('-x', '--exclusive',  help='Indicates whether end should be excluded from the range.', action='store_const', const = 0, dest = 'end_delta')
parser.add_argument('--step', help='Indicates the steps between numbers in the range', default= 1, type = int)
parser.set_defaults(end_delta=1)

args = parser.parse_args()

start = args.start
end = args.end + args.end_delta
step = args.step

for i in range(start, end, step):
    print(i)
