def solution(n):
    # this code will convert conventional numbers into roman numerals
    roman_num = []
    while n/1000 >= 1:                  # find roman numeral for 1000 place                     
        roman_num.append('M')
        n = n - 1000
    while n/500 >= 1:                   # find roman numeral for number between 500-1000
        if n/100 >= 9:
            roman_num.append('CM')
        else:
            roman_num.append('D'+'C'*((n-500)//100))    
        n = n-(n//100)*100
    while n/100 >= 1:                   # find roman numeral for number between 100-500
        if n/100 >= 4:
            roman_num.append('CD')
        else:
            roman_num.append('C'*(n//100))
        n = n-(n//100)*100
    while n/50 >= 1:                    # find roman numeral for number between 50-100
        if n/90 >= 1:
            roman_num.append('XC')
        else:
            roman_num.append('L'+'X'*((n-50)//10))
        n = n-(n//10)*10
    while n/10 >= 1:                    # find roman numeral for number between 10-50
        if n/10 >= 4:
            roman_num.append('XL')
        else:
            roman_num.append('X'*(n//10))
        n = n-(n//10)*10
    while n/5 >= 1:                     # find roman numeral for number between 5-10
        if n >= 9:
            roman_num.append('IX')
        else:
            roman_num.append('V'+'I'*(n-5))
        n = 0
    while n >= 1:                       # find roman numeral for number between 1-5
        if n == 5:
            roman_num.append('V')
        elif n == 4:
            roman_num.append('IV')
        else:
            roman_num.append('I'*n)
        n = 0
    return "".join(roman_num)




