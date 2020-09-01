'''
The question can be found out at :
https://www.hackerrank.com/challenges/mars-exploration

'''

def marsExploration(s):
    sos = "SOS"
    count=0
    for i in range(len(s)):
        if(s[i] != sos[i%3]):
            count+=1
    return count