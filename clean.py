import re
import html

pat = re.compile('&#X[0-9a-fA-F]{2,4};')

def clean(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            m = pat.search(line)
            while m:
                a, b = m.span()
                head, sep, tail = line.partition(line[a:b])
                line = head + html.unescape(sep) + tail
                m = pat.search(line)
            lines.append(line)
    with open(filename, 'w') as f:
        f.writelines(lines)

if __name__ == '__main__':
    import sys
    import os.path

    if len(sys.argv) <= 1:
        print("usage: clean <files>", file=sys.stderr)
        exit(1)

    files = []
    for arg in sys.argv[1:]:
        if os.path.isfile(arg):
            files.append(arg)
        else:
            print(arg, 'is not a file', file=sys.stderr)
            exit(2)

    for f in files:
        clean(f)

