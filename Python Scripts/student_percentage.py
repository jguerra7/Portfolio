'''
You have a record of students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer followed by the names and marks for students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.
'''

def student_avg(n):
    n = int(n)
    query = []
    student_info = {}
    for _ in range(n):
        name, *raw_score = input().split()
        scores = list(map(float, raw_score))
        student_info[name] = scores
    query_name = query.append(input())
    for i in query:
        if i in student_info:
            result = (sum(student_info[i]))/len(student_info[i])
            return '{0:.2f}'.format(result)

student = input()
print(student_avg(student))

'''
Sample input:
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh

Sample output:
26.50
'''
