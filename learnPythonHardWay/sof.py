from collections import OrderedDict

data = {
    1: [
        "data",
        "data"
    ],
    2: [
        "data",
        "data"
    ],
    3: [
        "data",
        "data"
    ],
    5: [
        "data",
        "data"
    ]
}

nums = [1,2,3,4,5]
listofi = []
for i in data:
    listofi.append(i)

for x in range(len(nums)):
    try:
        if listofi[x] == nums[x]:
            print 'e'
        else:
           data[nums[x]] = data[listofi[x]]
           del data[listofi[x]]
    except IndexError:
        listofi = 'null'

print data


