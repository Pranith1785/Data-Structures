from collections import deque

stack = deque()
max_val = [0]
for _ in range(int(input())):
    t = list(map(int, input().rstrip().split()))
    if t[0] == 1:
        stack.append(t[1])
        if max_val[-1] <= t[1]:
            max_val.append(t[1])

    elif t[0] == 2:
        if stack[-1] == max_val[-1]:
            max_val.pop()
        stack.pop()

    else:
        print(max_val[-1])

print(max(stack))
