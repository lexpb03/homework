a = list(map(int, input().split()))
for bul in range(len(a) - 1):
    for i in range(len(a) - 1 - bul):
        print(a[i], " and ", a[i+1])
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
print(a)