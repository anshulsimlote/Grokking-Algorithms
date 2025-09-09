# Original data
data = [2, 4, 1, 6, 9, 7, 5, 8]

def merge(arr, left, mid, right):
    l = arr[left:mid]
    r = arr[mid:right]

    i = j = 0
    k = left
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1

    while i < len(l):
        arr[k] = l[i]
        i += 1
        k += 1
    while j < len(r):
        arr[k] = r[j]
        j += 1
        k += 1

def merge_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr)
    if left < right - 1:  # at least 2 elements
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid, right)
        merge(arr, left, mid, right)

print(f"Original data: {data}")
merge_sort(data)
print(f"Sorted data: {data}")
