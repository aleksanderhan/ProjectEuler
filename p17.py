numberwords = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven',
               8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen',
               15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',
               20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy',
               80:'eighty', 90:'ninety', 100:'hundred', 1000:'thousand'}




# converts integers less than 10k to their corresponding "wordnumber"
def number_to_word(number):
    wordnumber = '' 
    tusen = int(number/1000)    
    if tusen != 0:
        wordnumber += numberwords[tusen] + numberwords[1000]
    number = number - tusen*1000 
    hundre = int(number/100)
    if hundre != 0:
        wordnumber += numberwords[hundre] + numberwords[100] 
    number = number - hundre*100
    if (hundre != 0 or tusen != 0) and number != 0:
        wordnumber += 'and'
    if number > 20:
        tier = int(number/10)
        wordnumber += numberwords[tier*10]
        number = number - tier*10
        if number != 0:
            wordnumber += numberwords[number]
    elif number != 0:
        wordnumber += numberwords[number]
        
    return wordnumber



antall_bokstaver = 0
for i in range(1, 1001):
    antall_bokstaver += len(number_to_word(i))
print(antall_bokstaver)

