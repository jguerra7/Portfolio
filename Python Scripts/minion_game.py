'''
Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings. 
'''

def minion_game(string):
    vowel = list('aAeEiIoOuU')
    s_points = 0
    k_points = 0
    ln = len(string)
    for j,k in enumerate(string):
       if k not in vowel:
           s_points += ln-j
       elif k in vowel:
           k_points += ln-j
    if s_points > k_points:
        print('Stuart {}'.format(s_points))
    elif k_points > s_points:
        print('Kevin {}'.format(k_points))
    else:
        print('Draw')

'''
Sample input: BANANA

Sample output: Stuart 12
'''
