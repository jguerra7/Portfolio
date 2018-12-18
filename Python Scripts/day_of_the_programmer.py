'''
Day of the programmer
Given a year,y, find the date of the 256th day of that year according to the official Russian calendar during that year. Then print it in the format dd.mm.yyyy, where dd is the two-digit day, mm is the two-digit month, and yyyy is y.
'''

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if year <= 1918 and year %4 == 0:
        print('12.09.{0:}'.format(year))
    elif year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print('12.09.{0:}'.format(year))
    else:
        print('13.09.{0:}'.format(year))

if __name__ == '__main__':

    year = int(input().strip())

    result = dayOfProgrammer(year)

'''
Sample input:
1800

Sample output:
12.09.1800
'''
