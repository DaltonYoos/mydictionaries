
infile = open('sometext.txt', 'r')

dictionary = {}

for words in infile:

    words = words.lower()
    words = words.replace(',', '')
    words = words.replace('.','')

    text = words.split(' ')

    for word in text:

        if word in dictionary:

            dictionary[word] += 1
        
        else:

            dictionary[word] = 1


print(dictionary)

infile.close()
