'''
The question can be found here:
https://www.hackerrank.com/challenges/tree-huffman-decoding
'''

"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    ans=""
    current=root
    for i in range(len(s)):
        if s[i]=='0':
            current=current.left
        else:
            current=current.right
        if (current.left==None and current.right==None):
            ans=ans+current.data
            current=root
    print(ans)

	#Enter Your Code Here