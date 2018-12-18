'''
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
'''


def swap_case(s):
    lower_c = list('abcdefghijklmnopqrstuvwxyz')
    upper_c = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    zip_ls = zip(lower_c,upper_c)
    mixed_ls = []

    for _ in s:
        if _ in lower_c:
            mixed_ls.append(_.upper())
        elif _ in upper_c:
            mixed_ls.append(_.lower())
        else:
            mixed_ls.append(_)

    return ''.join(mixed_ls)


'''
Sample input:
HackerRank.com presents "Pythonist 2".

Sample output:
hACKERrANK.COM PRESENTS "pYTHONIST 2".
'''
