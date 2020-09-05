'''
The question can be found out at:
https://www.hackerrank.com/challenges/sock-merchant
'''
def sockMerchant(n, ar):
    freq={}
    count=0
    for socks in ar:
        if socks in freq:
            freq[socks]+=1
        else:
            freq[socks]=1
    
    for socks in freq:
            count+=(freq[socks]//2)
    return count