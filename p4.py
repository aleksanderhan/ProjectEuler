def is_same_string(string1, string2):
    if len(string1) != len(string2):
        return False
    else:
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                return False
    return True


def reverse_string(string):
    gnirts = ''
    for i in range(len(string)):
        gnirts += string[-1-i]
    return gnirts


def is_palindrome(string):
    gnirts = reverse_string(string)
    return(is_same_string(string, gnirts))



n = 0
for i in range(100, 1000):
    for j in range(i, 1000):
        if is_palindrome(str(i*j)) and i*j > n:
            n = i*j

print(n)
            

