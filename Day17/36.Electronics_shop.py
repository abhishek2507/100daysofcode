'''
The question can be found out at:
https://www.hackerrank.com/challenges/electronics-shop/problem
'''

def getMoneySpent(keyboards, drives, b):
    bestchoice=-1
    keyboards.sort(reverse=True)
    drives.sort()
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            if (keyboards[i]+drives[j]>b):
                break
            else:
                bestchoice=max(bestchoice,keyboards[i]+drives[j])
    return bestchoice