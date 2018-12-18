'''
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left. 
'''

def count_substring(string, sub_string):
    ls = []
    o = 0
    count = 0
    l = len(sub_string)
    sub_ls = [sub_string]
    while l <= len(string):
        ls.append(string[o:l])
        o += 1
        l += 1
    for _ in ls:
        if _ in sub_ls:
            count += 1
    return count 


'''
Sample input:
ABCDCDC
CDC

Sample output:
2
'''
