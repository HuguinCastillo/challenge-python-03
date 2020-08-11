# Resolve the problem!!
import re

def run():
    # Start coding here
    f = open('encoded.txt', 'r', encoding='utf-8').read()
    x = re.findall("[\127-\255]", f)
    print(x)

if __name__ == '__main__':
    run()