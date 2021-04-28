import argparse
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--range', dest='accumulate', action='store_const',
                    const=range, default=100000000,
                    help='range of the loop (default: 10 000 000)')
parser.add_argument('--lengh', dest='accumulate', action='store_const',
                    const=sum, default=4,
                    help='lengh of the matrix (default: 4)')
args = parser.parse_args()
print(args.accumulate(args.integers))
#print(lengh, ranges)