
infile = open('info_security.txt', 'r')
text = infile.readline()
outfile = open('encrypted.txt', 'w')

encryption_code = { 'A': '!', 'B':'@', 'C':'#', 'D':'$', 'E':'%', 'F':'^', 'G':'&', 
                'H':'*', 'I':'(', 'J':')', 'K':'-', 'L':'=', 'M':'~', 'N':'[', 'O':']',
                    'P': ',', 'Q':'.','R':'/', 'S':'?','T':'|', 'U':'<', 'V':'>', 'W':'_', 'X':'{',
                        'Y':'}', 'Z':';', 'a':'!1', 'b': '#2', 'c':'@3', 'd':'$4', 'e':'%5', 'f':'06', 'h':'07', 'i':'08',
                            'j':'09', 'k':'10', 'l':'11', 'm':'12','n':'13', 'o':'14', 'p':'15', 'q':'16', 'r':'17', 's': '18',
                                't':'19', 'u':'20', 'w':'21', 'x':'22', 'y':'23', 'z':'24', '.':'+', ':':'??', ' ':''}



for character in text:
    
    if character in encryption_code:
        outfile.write(encryption_code[character])

    else:
        outfile.write(character)

    
infile.close()
outfile.close()

