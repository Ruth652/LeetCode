class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack=[]
        path = path.split('/')
        for char in path:
            if char=="" or char== ".":
                continue
            elif char=="..":
                if stack:
                    stack.pop()
                else:
                    continue
            else :
                stack.append(char)
                
            
        
        return "/"+"/".join(stack)
                
            