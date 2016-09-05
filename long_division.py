def long_division(n, d):    
    v = n//d
    n = 10*(n - v*d)
    answer = str(v)

    if n == 0:
        return answer

    answer += '.'

    intermediate_n = {}
    while n != 0:

        repeat_index = intermediate_n.get(n, None)
        if repeat_index != None:
            non_repeating = answer[:repeat_index]
            repeating = answer[repeat_index:]
            return non_repeating + '(' + repeating + ')'
        intermediate_n[n] = len(answer)

        v = n//d
        answer += str(v)
        n -= v*d
        n *= 10

    return answer
