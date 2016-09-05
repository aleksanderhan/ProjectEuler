with open('names.txt', 'r') as file:
    text = file.read()
    
text = text.split(',')
names = []
for name in text:
    names.append(name[1:-1])

names.sort()
del(name)

def  alphabetical_value(name):
    alphabeth = 'abcdefghijklmnopqrstuvwxyz'
    score = 0
    for letter in name.lower():
        score += alphabeth.index(letter) + 1
    return score


totalNameScore = 0
for i in range(len(names)):
    totalNameScore += (i + 1)*alphabetical_value(names[i])

print(totalNameScore)





'''
# start of a alphabetical sorting algorithm

test = ['aabc', 'bc', 'a', 'abc', 'ba']
def alphabeticalSort(inList):
    tempListe = []
    for word in inList:
        if
'''
