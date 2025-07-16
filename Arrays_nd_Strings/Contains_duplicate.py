a = [1, 2,2, 3, 4, 5, 6, 7, 8, 9]
hashmap = {}
for i in a:
    if i not in hashmap:
        hashmap[i] = 1
    else:
        print(i , " is a duplicate")
