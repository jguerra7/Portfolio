'''
Given the names and grades for each student in a Physics class of students N, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
'''


#Empty list to play with
name_input = []
score_input = []

# Basic input to get all of the information needed
for _ in range(int(input())):
    name = input()
    name_input.append(''.join(name))
    score = input()
    score_input.append(float(score))

# This is where the name is associated with the score
def nested_list(n,s):
    sorted_zip_list = []
    zip_list = zip(n,s)
    sorted_zip = sorted(zip_list, key=lambda x: x[1])
    for i in sorted_zip:
        sorted_zip_list.append(list(i))
    return sorted_zip_list

# Holy CRAP!!! I'm pretty sure I over complicated the second lowest score generator
def second_lowest_generator(sl):
    bottom_names = []
    temp_list = []
    second_lowest_list = []
    for i in sl:
        if i > min(sl):
            temp_list.append(i)
    for i in temp_list:
        if i == min(temp_list):
            second_lowest_list.append(i)
    for j, k in enumerate(nl):
        if k[1] in second_lowest_list:
            bottom_names.append(''.join(k[0]))
    return sorted(bottom_names)

#Let's make those functions work!
n = name_input
s = score_input
nl = nested_list(n,s)   # Establishing variable to call on second lowest score generator
nl
sl = score_input
slg = second_lowest_generator(sl)

# This is where the magic happens! 
for i in slg:
    print(i)


'''
Sample Input:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output:
Berry
Harry
'''
