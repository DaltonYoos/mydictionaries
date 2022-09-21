
infile = open('sometext.txt', 'r')

dictionary = {}

for words in infile:

    words = words.lower()
    words = words.replace(',', '')
    words = words.replace('.','')

    characters = words.split(' ')

    for character in characters:
        if character in dictionary:
            
            dictionary[character] += 1
        
        else:

            dictionary[character] = 1


print(dictionary)

infile.close()
