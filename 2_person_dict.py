person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

print((person['children'][1]))

print(person['pets']['cat'])

i = 0

for child in person['children']:

    print(child)

for pet in person['pets']:

    print(person['pets'][pet])

    #print(person[p]) will not print because 'pets' is its own dictionary, it is not in the person dictionary. 
    # It and has keys of its own outside of just the person dictionary
    
    