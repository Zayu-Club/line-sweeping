import random
import math
# import matplotlib.pyplot as plt

# N = 4
# MAX_NUMBERS = 50
N = 32
MAX_NUMBERS = 62500000

MAX_EDGE = 2 ** N
MAX_SIZE = MAX_EDGE ** 2
BLOCK_SIZE = math.ceil(MAX_NUMBERS ** (1/2))

if MAX_NUMBERS > MAX_SIZE:
    print("MAX_NUMBER[{}] > MAX_SIZE[{}]: OVERFLOW".format(
        MAX_NUMBERS, MAX_SIZE
    ))
    exit()


doneFrame = '█'
fgFrame = '▒'
bgFrame = '░'


def bar(now, all, lenght=30):
    process = now/all
    done1 = math.floor(process*lenght)
    done2 = math.ceil(process*lenght)-done1
    wait = lenght - done1 - done2
    return '{}{}{}  {:.2f}% {}/{}'.format(doneFrame*done1, fgFrame*done2,
                                          bgFrame*wait, process*100, now, all)


print("Creating indexs...")
INDEX = set()
while len(INDEX) < BLOCK_SIZE:
    INDEX.add(random.randint(0, MAX_EDGE-1))

points = dict()
for i in INDEX:
    points[i] = set()
print("Created indexs...")


count = set()
print('\x1b[?25l', end='', sep='')
print("Creating points...")
while len(count) < MAX_NUMBERS:
    x = random.sample(INDEX, 1)[0]
    y = random.randint(0, MAX_EDGE-1)
    points[x].add(y)
    count.add((x, y))
    print('\r', bar(len(count), MAX_NUMBERS), end='', sep='')
print('\x1b[?25h\x1b[1B', sep='')
print("Created points...")

print("Sorting indexs...")
index = list(points.keys())
index.sort()
print("Sorted indexs...")


print("Sorting points...")


def d(x, y):
    return (
        (y[0]-x[0])**2 + (y[1]-x[1])**2
    )


for key in index:
    points[key] = list(points[key])
    points[key].sort()

for i in range(len(index)):
    if i == len(index)-1:
        break
    if d((index[i], points[index[i]][-1]),
         (index[i+1], points[index[i+1]][-1])) < \
        d((index[i], points[index[i]][-1]),
          (index[i+1], points[index[i+1]][0])):
        points[index[i+1]].sort(reverse=True)
print("Sorted points...")

print("Saving...")
with open("./line-sweeping", "w", encoding="utf-8") as f:
    for i, key in enumerate(index):
        for j, value in enumerate(points[key]):
            if not (i == 0 and j == 0):
                f.write('\n')
            f.write('{} {}'.format(str(key), str(value)))
print("Saved...")

# res = list()
# for key in index:
#     for value in points[key]:
#         res.append((key, value))
# plt.plot(
#     [r[0] for r in res],
#     [r[1] for r in res],
#     '-r'
# )
# plt.show()
