def sequentialSearch(a, n, key):
    i = 0
    while i < n and a[i] != key:
        i = i + 1

    if i < n: return 1
    else: return -1

data = [4, 9, 11, 23, 2, 19, 7]
key = 7
print(sequentialSearch(data, len(data), key))