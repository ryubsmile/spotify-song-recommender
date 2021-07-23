from django.test import TestCase

import json
import re
# Create your tests here.

arr = '{"songId":"4iJyoBOLtHqaGxP12qzhQI","artistId":"1uNFoZAHBGtllmzznpCI3s"},{"songId":"6uDBSDI9pDM7C4Gm0hc2hI","artistId":"0NFlmEJpgyF2sO4mtlwFfl"},{"songId":"43PGPuHIlVOc04jrZVh9L6","artistId":"6AgTAQt8XS6jRWi4sX7w49"}'
# arr2 = re.sub("},{", "}~{", arr)
# print(arr2)

# arr3 = arr2.split("~")
# #print(arr3)

# for a in arr3:
#     a = json.loads(a)

arr = re.sub("},{", "}~{", arr).split("~")

for i in range(len(arr)):
    arr[i] = json.loads(arr[i])

print(arr)
print(type(arr))
print(type(arr[0]))
print(arr[0]["songId"])