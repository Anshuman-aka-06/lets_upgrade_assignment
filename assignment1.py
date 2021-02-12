#assignment 1
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


