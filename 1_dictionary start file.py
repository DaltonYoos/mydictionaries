import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}



print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(type(phonebook))
phone = (phonebook['Chris'])

print(phone)

mydictionary = {}
print(mydictionary)

mydictionary = dict(m=8, n=9)
print(mydictionary)


print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********')
print()

name = 'Chri'

if name in phonebook:
    print(phonebook[name])
else:
    print(name, "Not In Phonebook")




print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)
phonebook['Chris'] = '555-0123'
phonebook['Joe'] = '555-4444'
print(phonebook)

#Keys cannot be changed, only the information/values can be updated.
#For instance, in the terminal, Chirs's phone number changed.

print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()


#del phonebook['Chris']
#This will give you an error if the key cannot be found
#print(phonebook)


print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for key in phonebook:
    print(key)
    print(phonebook[key])


for value in phonebook.values():
    print(value)

for keys,v in phonebook.items():
    print("Key: ", key, "Value: ", v)

print()
print('*****  end section 5 ********')
print()

for tuple in phonebook.items():
    print(tuple)

\


print()
print('*****  start section 6 - using get and clear ********')
print()

phone = phonebook.get("Chri", "key not found")
print(phone) #phone variable acts as a key for the dictionary

#phonebook.clear()
#print(phonebook)




print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()


#pop method. Gives you key value pair and deltes from dictionary
#a = phonebook.pop('Chris', 'not found')
#print(a)

print(phonebook)


print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()

#pop item is not random, it gives you the last element in your dictionary

#a = phonebook.popitem()

#print(a)

print(phonebook)




print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()

list_of_keys = list(phonebook)
print(list_of_keys)
random_key = random.choice(list_of_keys)
print(random_key)
random_value = phonebook[random_key]
print(random_value)

# Alternatively
random_value = phonebook[random.choice(list(phonebook))] #faster and more efficient than the afforementioned code
print(random_value)


print()
print('*****  end section 9 ********')
print()


#random.choice will give you a random element in list.
#If you use the list function, you can get a list of all the keys in the dictionary





