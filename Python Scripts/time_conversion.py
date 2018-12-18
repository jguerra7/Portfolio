#This will convert to military time

def timeConversion(s):
    hr = (s.split(':'))
    clock_convert = []
    for _ in hr:
        clock_convert.append(_[0:2])
    if 'PM' in hr[-1] and '12' not in clock_convert[0]:
        clock_convert[0] = str(int(clock_convert[0])+12)
    if 'AM' in hr[-1] and '12' in clock_convert[0]:
        clock_convert[0] = '00'
    print(':'.join(clock_convert))

s = input()

timeConversion(s)

'''
Sample input:
07:05:45PM

Sample output:
19:05:45
'''
