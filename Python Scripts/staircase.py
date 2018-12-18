'''
     #
    ##
   ###
  ####
 #####
######
'''

def staircase(n):
    range_n = range(n)
    m = n-1

    for j,k in enumerate(range_n):
        print ((' '*m)+('#'*(j+1)))
        m -= 1

if __name__ == '__main__':
    n = int(input())

    staircase(n)

'''
Sample input:
6

Sample output:
     #
    ##
   ###
  ####
 #####
######
'''
