'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up. 
'''


def runner_up(n):
    runner_up_list = []
    for i in n:
        if i < max(n):
            runner_up_list.append(i)
    return max(runner_up_list)

def integer_converter(n):
    int_list = []
    for i in n:
        int_list.append(int(i))
    return int_list

empty = input()
n = input()
n = list(n.split(' '))
m = integer_converter(n)
print(runner_up(m))


'''
Sample Input:
5
2 3 6 6 5

Sample Output:
5
'''
