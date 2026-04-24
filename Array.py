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
# arr = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
# toh uske liye  koi variiable bna lenge let say i name se usme apne array ka name (arr.index) or jis bhi element ko hume find karna h vo element likh denge
# i = arr.index(7)
# print(i)
# for x in arr:
#     print(x, end="   ")


# NUMPY MODULE
# NUMPY MODULE
# NUMPY MODULE
# NUMPY MODULE
# NUMPY MODULE
# NUMPY MODULE
# NUMPY MODULE

# import numpy likhnenge toh hume baar baar numpy.array wagerah likhna hoga toh us chiz ko hatane ke liye hume whi doosra wala tarika aapnana hoga from numpy karke ya fir uska alias bna kar kar sakte h toh aise na kare guru

from numpy import *
# yha par typecode bhi batane ki zarurat nhi h
# val = array([1, 2, 3, 4, 5.9])
# for x in val:
#     print(x, end="   ")

# numpy se hum hetrogenous array bhi bna sakte h

# hum type code bhi daal sakte h or phir vo usko usi ke hisab se set kar dega
# val = array([1, 2, 3, 4, 5],float)
# for x in val:
#     print(x, end="   ")

# hum ek array banayenge jisme sare element Arthematic Progression m ho vo hum bna sakte h directly with the help of line space
# val = linspace(10, 20, 5)
# ISME LAST WALA NUMBER INCLUDED RAHEGA
# y isme hum teen parameter denge jisme plhe wale m hum batayenge ki number kha se shuru ho rha h and doosre wale m batayenge ki number kha par khatam ho rha h and teesre wale m batayenge ki number ke hume kitne parts karne h


# dooosa tarika h jo ki h arrange ka
# val = arange(10,20,3)
# isme bhi jo hum teeen parameter denge usme plhe hum denge ki number ko start kh se karna h or doosre wale m batayenge ki end kha par karna h or teesre wale m batayenge ki humko kitna common diffrence chahie
# OR ISME JO BHI LAST NUMBER RAHEGA VO EXCLUDED RAHEGA


# EK HUM BNA SAKTE H 1-D ARAY JISME HUME SARE ELEMENT ZEROES M HO
# val = zeros(10)
# or bracket ke ander wali chiz batayegi ki kitne size ka hume banana h


# agar aa jaye ki hume 0 or 1 ke alawa kisi or elemnet ka array banana h toh uske liye hum use karenge "full" name ka kuch toh
# or iske ander do parameter pass karenge plha hum batayneg ki kitne size ka hume aray banana h or doosrew wale m bta denge ki uske ander kya value fill karni h

# val = full(10,5)
# for x in val:
#     print(x, end=",")


# array ko revverse bhi kar sakte h .reverse name ke function se


# MULTI DIMENSIONAL ARRAY
# means numpy me hum multiimensional array kaise bna sakte h

# Zero dimensional array
# zero = array(10)

# One dimensional array
# isme bus ek extra square bracket lagayenge or jtne bhi element dakne daa sakte h or seedha print kara denge
# one = array([1, 2, 3, 4, 5])
# print(one)

# Two dimensional array
# isko bananae ke liye hum sabse plhe squar bracket ko lagayenhge
# or two dimensional array ka matlab hota h ki collection of one dimensional array
# two = array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(two)

# Three dimensional array
three = array([[[1, 2], [3, 4]],  [[5, 6], [7, 8]]])
print(three)

# this is the end 