#question 1
#five list method

#step 1- declare a list

lst = [1,2,4,"Hello world",[1,3],5]

#method no. 1- to count no. of occurence of particular item in list we use count method

print(lst.count(2))

#method no. 2 - to enter a element at the end of list we use append method

lst.append("anshuman singh")

print(lst)

#method no. 3 - to insert a elements at a particular index we use insert method

lst.insert(5,"methods")

print(lst)

#method no. 4 - to delete an elements from a list we use pop

lst.pop()

print(lst)

#if we provide index to pop it will delete the elements of that index else it will delete the last element

#method no- 5 - index method is used to find the index of a paritcular character

char_index = lst.index(4)

print(char_index)

#question 2

# five mehtods of dictionary

dit = {"Name":"Anshuman Singh",
       "year":"second",
       "College":"sinhgad college of engineering",
       "location":"Pune"
       }

#method 1 - to get the keys we use key method

print(dit.keys())

#methods 2 - to get the values we use values()

print(dit.values())

#method 3 - to get the value of paritcular key there are two ways

print(dit.get("year"))

print(dit["year"])

#method 4 - to get key value pair

pair = list(dit.items())
for key,value in pair:
    print(key,value)


#method 5 - to delete key of dictionary we use pop    dict.pop(key to be deleted)

dit.pop("location")

print(dit)




