import sys

fileName = sys.argv[1]
ks = map(int, sys.argv[2:])

n = 0
buckets = []

def add(pos):
    buckets.append([pos, 1])

    resid = []
    while True:
        if len(buckets) < 3:
            break

        last1 = buckets[-1]
        last2 = buckets[-2]
        last3 = buckets[-3]

        if last1[1] == last2[1] and last2[1] == last3[1]:
            resid.append(last1)
            last2[1] += last3[1]
            buckets.pop()
            buckets.pop()
            buckets.pop()
            buckets.append(last2)
        else:
            break
    resid.reverse()
    buckets.extend(resid)

def query(k):
    tot = 0
    for b in reversed(buckets):
        if n - b[0] >= k:
            return b[1]/2.0 + tot
        tot += b[1]
    return tot

def main():
    with open(fileName) as f:
        lines = f.readlines()

    pos = 0
    for line in lines:
        for ch in line:
            if ch == '1':
                add(pos)
            pos += 1
    global n
    n = pos

    for k in ks:
        print(query(k))


if __name__ == '__main__':
    main()

