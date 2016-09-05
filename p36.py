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


DP = []
for i in range(1000001):
    if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
        DP.append(i)

print(sum(DP))

