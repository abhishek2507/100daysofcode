'''
The question can be found out at:
https://www.hackerrank.com/challenges/counting-valleys/problem
'''
def countingValleys(n, s):
    step=[]
    count=0
    for i in range(n):
        if s[i]=="U":
            if i==0:
                step.append(1)
            else:
                step.append(step[i-1]+1)
        if s[i]=="D":
            if i==0:
                step.append(-1)
            else:
                step.append(step[i-1]-1)
        if ((step[i] == 0) and (step[i-1]<0)):
            count+=1
    return count