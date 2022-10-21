from collections import Counter
from lib2to3.pygram import Symbols

def main(filname):
    symbols = list('.,-\\/"\'![]()“”')
    with open(filname, 'r') as f:
        context = f.read().lower()
        for s in symbols:
            context = context.replace(s,' ')
        lines = context.count('\n')
        words = []
        for line in context.strip().split('\n'):
            words.extend([w for w in line.strip().split(' ') if w.isalpha()])

        counter = Counter(words)
        for k, v in counter.items():
            print('%s : %s' % (k, v))

        print('lines : %d' % lines)
        print('words : %d' % len(counter))

if __name__=='__main__':
    main('little_python\car-child-soldiers.txt')