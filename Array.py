# import array as array

from array import *
# from array import * isme do baar array.array ya array.arr likhene ki bhi zarurat nhi h !!!               direclty aray bna sakte h or y sabse accha tarika h

# val = array('i', [1, 2, 3, 4, 5, 6])
# print(val)

# for i in range(0, len(val)):
#     print(val[i], end=" ")

# agar yha par array ke ander jo element h vo drastically change hote h toh uske liye neeche wala jo enhanced loop h na usko use kar sakte h or ya toh phir                                                                 for i in range(0, len(val))        bhi likh sakte h
# print('/n')

# for x in val:
#     print(x, end=' , ')

# print('/n')
# print(val.typecode)

# print('/n')

# val.reverse()

# for i in range(0, len(val)):
# #     print(val[i], end=" ")
# val = array('i', [1, 2, 3, 4, 5, 6])
# print(val)

# val.append(23)
# val.insert(1, 26)

# lets say ki ek nya array bnana h or jitne bhi purane aray ke elemets the unko nye array me copy karna h
# copyArray = array(val.typecode, (x*2 for x in val))
# isme jo x for c in range likha hua  h usme jo plhe wala jo x h na vo liist bna dega  or doosra wala for loop chala dega toh ek tarike se sare ke sare element jo h vo itereate hoke isme aate jayenge


#  like agar array ke koi ek lement ko delete karna h or isme popo name ka function ka use hota h or bracket ke ander hum likenge index ki kon se element kko hume delete karna h
# or agar humne bracket ke ander kuch nhi likha hua na toh phir vo apne aap last wala jo element usko delete kar dega
# copyArray.pop(3)

# isme ek or function h remove name ka isme jo bracket me jo element h vo likhenge toh direct element hi delete h jeyega hume index likhne ki zarurat nhi h
# copyArray.remove(4)

# for i in range(0, len(copyArray)):
#     print(copyArray[i], end=" ")


# SLICING
# val = array('i', [1, 2, 3, 4, 5, 6,7,8,9,10])
# copyArray = array(val.typecode, (x for x in val))
# copyArray.remove(2)

# isme do parametere denge hum square bracket m colon se seperate karke
# a = val[1:-2]
# agar hum starting index bhi na lagaye or ending index bhi na lageye toh or do colon lga de or last m ek parameter or jo ki h ki -1 likh do  toh jo humare new array ban kar aayega vo humara reverse ho jayega
# a = val[::-1]

# AGAR USER SE INPUT LENA H OR ARRAY BANATA JANA H
# arr = array('i', [])
# n = int(input('enter a number'))

# for i in range(0, n):
#     arr.append(int(input("enter next number")))

# ARRAY M KOI ELEMNT KO SERCH KARNA H
arr = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

for x in arr:
    print(x, end="   ")
