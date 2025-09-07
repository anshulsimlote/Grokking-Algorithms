def findSmallest(dataList):
    smallest = dataList[0]
    smallest_index = 0
    for index in range(1,len(dataList)):
        data = dataList[index]
        if(data < smallest):
            smallest = data
            smallest_index = index
    return smallest_index

dataList = [5,2,99,0,3]
result = []
for index in range(0,len(dataList)):
    smallest_index = findSmallest(dataList)
    result.append(dataList.pop(smallest_index))
print(f"Result: {result}")