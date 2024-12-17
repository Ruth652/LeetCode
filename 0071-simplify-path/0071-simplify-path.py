class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack=[]
        path = path.split('/')
        for char in path:
            if char == "..":
                if stack:
                    stack.pop()
                else:
                    continue
            elif char == "" or char == ".":
                continue
            else:
                stack.append(char)
        
        return "/" + ("/").join(stack)
                
            