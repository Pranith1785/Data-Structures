

def truck_tour(arr):

    rem = 0
    start_point = 0
    for i in range(len(arr)):
        rem += arr[i][0] - arr[i][1]

        if rem < 0:
            start_point = i+1
            rem = 0

    return start_point



pt = []
for _ in range(3):
    pt.append(list(map(int,input().split())))

print(truck_tour(pt))