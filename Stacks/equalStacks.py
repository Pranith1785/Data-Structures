import numpy as np


def equalStacks(s1, s2, s3):
    h1 = sum(s1)
    h2 = sum(s2)
    h3 = sum(s3)

    while(h1 != h2 or h2 != h3 or h3 != h1):
        if h1 >= h2 and h1 >= h3:
            h1 = h1-s1.pop()
        elif h2 >= h1 and h2 >= h3:
            h2 = h2-s2.pop()
        elif h3 >= h1 and h3 >= h2:
            h3 = h3-s3.pop()
    print("done")
    return(h1)


def equalStacks1(s1, s2, s3):

    h1 = [0] + np.cumsum(s1).tolist()
    h2 = [0] + np.cumsum(s2).tolist()
    h3 = [0] + np.cumsum(s3).tolist()
    print(h1)
    print(h2)
    print(h3)

    while(h1[-1] != h2[-1] or h2[-1] != h3[-1] or h3[-1] != h1[-1]):
        if h1[-1] >= h2[-1] and h1[-1] >= h3[-1]:
            h1.pop()
        elif h2[-1] >= h1[-1] and h2[-1] >= h3[-1]:
            h2.pop()
        elif h3[-1] >= h1[-1] and h3[-1] >= h2[-1]:
            h3.pop()

    return (h1[-1])


s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
s3 = list(map(int, input().split()))

print(equalStacks1(s1[::-1], s2[::-1], s3[::-1]))
