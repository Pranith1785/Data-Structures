

def arrManipulation(arr, queries):

    for x, y, v in queries:
        arr[x-1] = arr[x-1] + v
        arr[y] = arr[y] - v

    max = 0
    val = 0
    for pos in arr:
        val += pos
        if val > max:
            max = val
    return max


if __name__ == '__main__':

    n, m = map(int, input().rstrip().split())
    arr = [0] * (n+1)
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    print("max value is: ", arrManipulation(arr, queries))
