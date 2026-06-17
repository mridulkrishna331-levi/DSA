# # FOR LOOP

# for i in range(5):
#     print(i)
# # range 0 se start hogi and then aakhri tak chalegi jaise yha 5 h toh 4 tak means total 5 honge 0,1,2,3,4 bas 5 print ni hoga

# for o in range(1, 9):
#     print(o)
# # yha par jo range h vo 1 se tart hogi and 6 tak chalegi means 5 tak number print honge

# for j in range(1, 9, 2):
#     print(j)
# # yha jaise chalga vse hi chalega par 2 step ki deri se means 2 ke gap se chalega

# for k in range(10, 0, -1):
#     print(k)
# # yha jaise ki loop reverse chalega then 10 se chalke 0 par chalega andd -1 measn 1-1 step kam hota jayega


# WHILE LOOP
# jab tak condition true h tab tak loop chalega

# i = 1
# while i <= 5:
#     print(i)
#     i += 1


# baki BREAK use hota h loop ko turat break karne k liye
# for i in range(10):
#     # print(i) condition bahar hi likhni hoti h ander nhi loop ke

#     if i == 7:
#         break
#     print(i)

# baki aise hi CONTINUE use hota h jo ki iteration ko skip kar deta h
# for i in range(6):
#     if i == 4:
#         continue

#     print(i)

# NESTED LOOP
# pattern printing
# for i in range (5):
#     print("*"*5)

# for i in range(1,5):
#     print("*" * i)

# FUNCTION
# def greet():
#    print("Namaste")
# greet()

# function m kuch PARAMETERS hote h jo ki aage help karte h

# without parameter
# def greet():
#     print("Hello Mridul")


# greet()

# with parameter
# def greet(name):
#     print("Hello", name)


# greet("manu")
# jo pass kiya h vo argument h or jo function m dala h vo h parameter


# RETURN statement use hoti h jab hume value wapas chahie hoti h
def add(a, b):
    return a+b


# list is mutable
fruits = ["apple", "mango", "banana"]
fruits.insert(1, "kela")
fruits.remove("kela")
# pop is used to delete an elemment on the basis of the indexing
fruits.pop(2)
# similarly sort is used for ascending order and unsort is foor the descending order
print(fruits[0,2])
print(fruits)
