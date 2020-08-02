class Solution(object):
    def findComplement(self, num):
        return num ^ int(bin(num)[2:].replace("0","1"),2)
val=Solution()
n=int(input())
print(val.findComplement(n))
