def shaker(arr):
    swapped = True
    start = 0
    ed = len(arr) - 1

    while swapped:
        swapped = False

        for i in range(start, ed):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if not swapped:
            break
        ed -= 1

        swapped = False

        for i in range(ed - 1, start - 1, -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

        start += 1
    return arr

A = list(map(int, input().split()))
print(*shaker(A))
