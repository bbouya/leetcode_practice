'''

'''
class Solution:
    def isValid(self, s: str) -> bool:
        # Create a pair of opening and closing parrenthesis
        opcl = dict(('()', '[]', '{}'))
        #Create stack data structure
        stack = []

        for idx in s :
            if idx in '([{':
                stack.append(idx)
            elif len(stack) == 0 or idx


if __name__=='__main__':
    print('ay')
    r = '()'
    res = Solution()
    ress = res.isValid(r)
    print(ress)