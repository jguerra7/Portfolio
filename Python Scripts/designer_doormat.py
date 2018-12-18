'''
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
'''


def designer_door_mat(h,w):
    h2 = h//2
    w2 = w//2
    rh = range(h2)
    w_var = w2-1
    w_var2 = w2-3
    count = 1
    for x,y in enumerate(rh):
        print(('-'*w_var)+('.|.'*count)+('-'*w_var))
        if x != h2-1:
            w_var -= 3
            count += 2
    print(('-'*w_var2)+'WELCOME'+('-'*w_var2))
    for x,y in enumerate(rh):
        print(('-'*w_var)+('.|.'*count)+('-'*w_var))
        w_var += 3
        count -= 2

hw = []
height_width = input().split()
for _ in height_width:
    hw.append(int(_))
height = hw[0]
width = hw[-1]
designer_door_mat(height,width)

'''
Sample input:
9 27

Sample output:
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
'''
