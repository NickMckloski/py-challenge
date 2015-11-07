import sys

def main(args):
    n = int(input("Enter a number to begin: "))
    if 0 in balances(n):
        show_path(n)
    else:
        print("Impossible")

def balances(n, cache={}):
    if n not in cache:
        cache[n] = find_balances(n)
    return cache[n]

def find_balances(n):
    if n <= 1:
        return {0: 1} if n == 1 else {}
    return {dir + bal: (n + dir) / 3
            for dir in next_dirs(n)
            for bal in balances((n + dir) / 3)}

def next_dirs(n):
    return (d for d in [-2, -1, 0, 1, 2] if (n + d) % 3 == 0)

def show_path(n):
    bal = 0
    while n > 1:
        m = balances(n)[-bal]
        dir = m*3 - n
        print(n, dir)
        bal += dir
        n = m
    print(1)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))