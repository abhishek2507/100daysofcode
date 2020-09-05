'''
The question can be found out at:
https://www.hackerrank.com/challenges/kangaroo
'''
def kangaroo(x1, v1, x2, v2):
    while True:
        if (x1>x2 and v1>v2) or (x1>x2 and v1==v2):
            return "NO"
        elif (x2>x1 and v2>v1) or (x2>x1 and v2==v1):
            return "NO"
        elif x1==x2:
            return "YES"
        else:
            x1+=v1
            x2+=v2