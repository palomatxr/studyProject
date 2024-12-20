#exemplo [[1,0,0,1], [0,1,1,0]] output True
#exemplo [[1,0,0,0,1], [1,0,1,0,0]] output False
def checkMagazine(magazine, note):
    # Write your code here
    hashNote = {}

    word = ''
    for element in note:
        if element == " " and word != '':
            hashNote[word] = None
            word = ''
        word += element

    secondWord = ''
    for element in magazine:
        if element == " " and secondWord != '':
            if secondWord in hashNote:
                hashNote[secondWord] = element
            secondWord = ''
        secondWord += element

    noteTrue = False
    for element in hashNote.values():
        if element == None:
            noteTrue = True
    if noteTrue:
        print('No')
    else:
        print('Yes')

test = {'1': 1, '2' : 1}

test['1'] = 2

print(test['1'])