class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        my_dic={
            "(":")", "[":"]","{":"}"
        }
        
        stack=[]
        for i in range(len(s)):
            if s[i] in my_dic.keys():
                stack.append(s[i])
            else:
                if not stack:
                    return False
                else:
                    a=stack.pop()
                    if s[i]!=my_dic[a]:
                        return False
                         
        return stack==[]
                   