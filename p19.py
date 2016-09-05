# Funksjon som sjekker om året er et skuddår
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True

    return False


# Funksjon som returnerer hvilken ukedag året starter på.
# (fungerer bare fra og med 1900)
def weekday_newyear(year):
    if year == 1900:
        return 0

    else:
        ukedag = 1
        i = 1901
        while i < year:
            if is_leap_year(i) == True:
                ukedag += 2
            else:
                ukedag += 1
            i += 1
        return ukedag%7


# Teller hvor mange søndager som er den 1 i hver mnd. fra 1901 til og med 2013
sundays = 0
for year in range(1901, 2001):
    ukedag_nummer = weekday_newyear(year)
    if ukedag_nummer == 6:
        sundays += 1

    dagerPrMnd = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30] #januar til om med november

    for dager in dagerPrMnd:
        if dager == 28 and is_leap_year(year):
            ukedag_nummer += dager + 1
        else:
            ukedag_nummer += dager

        if ukedag_nummer%7 == 6:
            sundays += 1

print(sundays)















            
    
