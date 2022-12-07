def speed_sort(s):
    if len(s) <= 1:
        return s

    elem = s[0]
    left = list(filter(lambda x: x < elem, s))
    middle = [i for i in s if i == elem]
    right = list(filter(lambda x: x > elem, s))

    return speed_sort(left) + middle + speed_sort(right)

A = list(map(int, input().split()))
print(speed_sort(A))