
infile = open('sometext.txt', 'r')
sometext = infile.read()


dictionary = {}

text = sometext.split(' ')

for words in text:

    words = words.lower()
    words = words.replace(',', '')
    words = words.replace('.','')

    counter = text.count(words)

    dictionary[words] = counter


print(dictionary)

infile.close()
