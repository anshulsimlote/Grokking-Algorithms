data = [2,4,1,6,9,7,5,8]


def  quickSort(data):
    res = []
    if(len(data) <= 1):
        return data
    if(len(data) == 2):
        if data[0] > data[1]:
            res.append(data[1])
            res.append(data[0])
        else:
            res.append(data[0])
            res.append(data[1])
        return res
    pivot = data[0]
    l = []
    r = []
    for index in range(1,len(data)):
        val = data[index]
        if(val < pivot):
            l.append(val)
        else:
            r.append(val)
    res.extend(quickSort(l))
    res.append(pivot)
    res.extend(quickSort(r))
    return res

print(f"data : {data}")

print(f"Sorted : {quickSort(data)}")
