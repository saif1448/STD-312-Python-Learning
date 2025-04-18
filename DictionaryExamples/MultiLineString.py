
string = '''
        asda
        asd
        asd
        asd
        azds
        asd
        asd 
         '''

#multiline string ----> store multi line string
# ----> doc string

string = 'I am a person'

word_list = string.split()
print(word_list)


string = 'I,am,a,person'

word_list = string.split(',')
print(word_list)


word_list = ['I', 'am', 'a', 'person']

d = {
}

print(d.get('c', 0))