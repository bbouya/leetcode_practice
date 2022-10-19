'''

'''
class Solution:
    def isValid(self, s: str) -> bool:
        result = False
        count = -1
        for i in range(len(s)):
            if(s[i]=='(' and count ==-1):
                count = 1
            elif(s[i]==')' and count == 1):
                count = 2
                return True
            else: continue

        return False


if __name__=='__main__':
    print('ay')
    r = '()'
    res = Solution()
    ress = res.isValid(r)
    print(ress)