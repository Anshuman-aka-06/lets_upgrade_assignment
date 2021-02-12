#assignment 2

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

