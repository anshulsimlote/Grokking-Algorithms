def binarySearch(dataList, searchItem, debug=False):
    low = 0
    high = len(dataList) - 1

    while low <= high:
        mid = (low + high) // 2

        if debug:
            print(f"low={low}, high={high}, mid={mid}, value={dataList[mid]}")

        if dataList[mid] == searchItem:
            return mid
        elif dataList[mid] > searchItem:
            high = mid - 1
        else:
            low = mid + 1

    return -1


# Example usage
dataList = [2, 4, 3, 1, 2, 5, 9]
dataList.sort()
print("Sorted list:", dataList)

searchItems = [1, 2, 4, 6, 9, 10]
for item in searchItems:
    result = binarySearch(dataList, item, debug=True)
    print(f"Search {item}: Result index {result}")
    print("-" * 30)
