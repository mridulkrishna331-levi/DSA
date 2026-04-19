# import array as array
import array as arr
# from array import * isme do baar array.array ya array.arr likhene ki bhi zarurat nhi h !!!               direclty aray bna sakte h or y sabse accha tarika h

val = arr.array('i', [1, 2, 3, 4, 5, 6])
print(val)

# for i in range(0, len(val)):
#     print(val[i], end=" ")

# agar yha par array ke ander jo element h vo drastically change hote h toh uske liye neeche wala jo enhanced loop h na usko use kar sakte h or ya toh phir                                                                 for i in range(0, len(val))        bhi likh sakte h
print('/n')

# for x in val:
#     print(x, end=' , ')

# print('/n')
# print(val.typecode)

# print('/n')

# val.reverse()

# for i in range(0, len(val)):
#     print(val[i], end=" ")
val.append(23)
val.insert(1, 26)
for i in range(0, len(val)):
    print(val[i], end=" ")
